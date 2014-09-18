import logging
import os
import shutil
from cliff.command import Command

class Create(Command):
    "The basic command to create a ginger site"

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        self.app.stdout.write('Creating ginger site...')
        current_directory = os.getcwd()
        src_directory = 'lib/site_template/'
        shutil.copytree(src=src_directory, dst=current_directory)
