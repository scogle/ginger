import logging
import os
import distutils.core
from cliff.command import Command

class Create(Command):
    "The basic command to create a ginger site"

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        if is_created():
            self.app.stdout.write('Error: It appears there is already '
                                  'a ginger site in this directory.\n'
                                  'To create a new site, delete '
                                  '_config.yaml and rerun ginger new\n')
        else:
            self.app.stdout.write('Creating ginger site...\n')
            curr_dir = os.getcwd()
            src_dir = get_pkg_path()+'../data/site_template/'
            distutils.dir_util.copy_tree(src=src_dir, dst=curr_dir)

def get_pkg_path():

    """ Gets path of this packages init file and returns it """
    pkg = os.path.realpath(__file__)
    last_slash = pkg.rfind('/')
    return pkg[:last_slash+1]

def is_created():

    """ Checks to see if ginger new command has already been run on dir """
    return os.path.isfile(os.getcwd()+'/_config.yaml')
