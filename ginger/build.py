import logging
import os
import shutil
import yaml
import re
import pickle
import sass
import json

from cliff.command import Command
from jinja2 import Environment, FileSystemLoader

class Build(Command):
	"Generates html"

	log = logging.getLogger(__name__)

	def take_action(self, parsed_args):
		self.app.stdout.write('Building ginger site...\n')

		current_directory = os.getcwd()

		views_directory = current_directory + '/_views'
		layouts_directory = current_directory + '/_layouts'

		env = Environment(loader=FileSystemLoader(layouts_directory), autoescape=False)

		stream = open(current_directory+'/_config.yaml', 'r')
		_config = yaml.load(stream)

		site_data = {
			'title': _config['title'],
			'author': _config['author'],
			'description': _config['description'],
			'style': _config['style'],
			'views': []
		}

		for filename in os.listdir(views_directory):
			if filename != ".DS_Store":
				filepath = views_directory+"/"+filename
				print filepath
				this_view = open(filepath, 'r').read()

				#print this_view

				exp = r'^(-{3}(?:\n|\r)([\w\W]+?)-{3})?([\w\W]*)'
				parsed_page = re.search(exp, this_view)
				view_data = yaml.load(parsed_page.group(2))
				view_data['template'] = parsed_page.group(3).strip()
				site_data['views'].append(view_data)

				self.app.stdout.write(' - Parsing %s\n' % view_data['title'])

			
		template = env.get_template( '%s.html' % _config['style'] )

		json_data = json.dumps(site_data)
		rendered_layout = template.render(site_data=site_data, json_data=json_data)


		with open('index.html', 'wb') as html_output:
			html_output.write(rendered_layout)

		rendered_css = sass.compile_file('_scss/main.scss')
		with open('css/main.css', 'wb') as css_output:
			css_output.write(rendered_css)