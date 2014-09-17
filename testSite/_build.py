import logging
import os
import shutil
import yaml
import re
import pickle
import sass
import json

from jinja2 import Environment, FileSystemLoader


print "Building..."

current_directory = os.getcwd()

views_directory = current_directory + '/_views/'
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
	print filename
	filepath = views_directory+"/"+filename
	this_view = open(filepath, 'r').read()

	#print this_view

	exp = r'^(-{3}(?:\n|\r)([\w\W]+?)-{3})?([\w\W]*)'
	parsed_page = re.search(exp, this_view)
	view_data = yaml.load(parsed_page.group(2))
	view_data['template'] = parsed_page.group(3).strip()
	site_data['views'].append(view_data)

	
if site_data['style'] == 'two-col':
	template = env.get_template('two-col.html')

json_data = json.dumps(site_data)
rendered_layout = template.render(site_data=site_data, json_data=json_data)


with open('index.html', 'wb') as html_output:
	html_output.write(rendered_layout)

#print sass.compile(dirname='_scss')




