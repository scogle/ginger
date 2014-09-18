import logging
import os

from cliff.command import Command


class Create(Command):
    "The basic command to create a ginger site"

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        self.app.stdout.write('Creating ginger site...')
        
        path = os.path