import logging
import os
import sys
import yaml
import re
import sass
import json

from cliff.command import Command
from jinja2 import Environment, FileSystemLoader

class Build(Command):
	"Generates html"

	log = logging.getLogger(__name__)

	def get_parser(self, prog_name):
		parser = super(Build, self).get_parser(prog_name)
		parser.add_argument('-w', '--watch', dest='watch', action='store_true')
		return parser


	def take_action(self, parsed_args):
		self.app.stdout.write('Building ginger site...\n')

		print "Watch for changes? %s" % parsed_args.watch 

		current_directory = os.getcwd()

		views_directory = current_directory + '/_views'
		layouts_directory = current_directory + '/_layouts'

		env = Environment(loader=FileSystemLoader(layouts_directory), autoescape=False)


		try:
                    stream = open(current_directory+'/_config.yaml', 'r')
		    _config = yaml.load(stream)
                except IOError:
                    self.app.stdout.write('No _config.yaml file found. Unable'
                                          ' to build site.\n Please run ginger'
                                          ' new in order to create site.\n')
                    sys.exit(1)

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
