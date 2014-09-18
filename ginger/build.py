import logging
import os
import shutil
import yaml
import re

from cliff.command import Command

class Build(Command):
	"Generates html"

	log = logging.getLogger(__name__)

	def take_action(self, parsed_args):
		self.app.stdout.write('Building ginger site...')
		current_directory = os.getcwd()

		views_directory = current_directory + '/_views/'

		stream = open(current_directory+'/_config.yaml', 'r')
		_config = yaml.load(stream)

		print _config

		site_data = {
			'title': _config['title'],
			'author': _config['author'],
			'description': _config['description']
		}
		print site_data

		for filename in os.listdir(views_directory):
			print filename
			filepath = views_directory+"/"+filename
			this_view = open(filepath, 'r').read()

			print this_view

			front_matter = re.search( r'^\s*---(.*)---\s*$', this_view, re.MULTILINE)

			print front_matter



