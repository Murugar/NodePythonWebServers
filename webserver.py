import BaseHTTPServer

HOST_NAME = 'localhost'
PORT_NUMBER = 5000
TEMPLATE = '<h1>Hello, world from Python Http Server.</h1>'

class App(BaseHTTPServer.BaseHTTPRequestHandler):
	def _set_headers(self, key, value):
		self.send_header(key, value)

	def do_GET(self):
		self.send_response(200)
		self._set_headers('Content-Type', 'text/html')
		self.end_headers()
		self.wfile.write(TEMPLATE)

if __name__ == '__main__':
	server = BaseHTTPServer.HTTPServer
	httpd = server((HOST_NAME, PORT_NUMBER), App)
	try:
		print 'Server starting at port 5000'
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
		print 'Server stopping'
		httpd.server_close()
