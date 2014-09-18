import logging
import os
import shutil
from cliff.command import Command
import SimpleHTTPServer
import SocketServer

PORT = 4000

class Serve(Command):
	"Build the site and create a server to serve it"

	log = logging.getLogger(__name__)

	def take_action(self, parsed_args):
		self.app.run(['build'])

		Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

		httpd = SocketServer.TCPServer(("", PORT), Handler)

		print "Serving at 0.0.0.0:%s" % PORT
		httpd.serve_forever()