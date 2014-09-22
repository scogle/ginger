import os
import logging
from cliff.command import Command
import SimpleHTTPServer
import SocketServer
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

PORT = 4000

class EventHandler(FileSystemEventHandler):
	"""Extending the watchdog FileSystemEventHandler class to  rebuild on watch
	"""

	def on_any_event(event, app):
		print "firing event handler"

class Serve(Command):
	"""Build the site and create a server to serve it
	"""

	log = logging.getLogger(__name__)

	def get_parser(self, prog_name):
		parser = super(Serve, self).get_parser(prog_name)
		parser.add_argument('-w', '--watch', dest='watch', action='store_true')
		return parser

	def take_action(self, parsed_args):
		self.app.run(['build'])

		Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
		httpd = SocketServer.TCPServer(("", PORT), Handler)

		print "Serving at 0.0.0.0:%s" % PORT
		httpd.serve_forever()

		if parsed_args.watch is True:

			event_handler = EventHandler
			path = os.getcwd()

			observer = Observer()
			observer.schedule(event_handler, path, recursive=True)
			observer.start()
			try:
				while True:
					time.sleep(1)
			except KeyboardInterrupt:
				observer.stop()
			observer.join()


