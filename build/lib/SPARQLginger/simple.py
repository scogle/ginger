import logging
import os

from cliff.command import Command


class Create(Command):
    "The basic command to create a SPARQLginger project"

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        self.log.info('sending greeting')
        self.log.debug('debugging')
        self.app.stdout.write('hi!\n')





class Build(Command):
    "Generate HTML for project"


class Serve(Command):
    "Generates the HTML and serves it from a simple HTTP server"

