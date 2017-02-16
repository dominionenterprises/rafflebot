from SimpleHTTPServer import SimpleHTTPRequestHandler
import SimpleHTTPServer
from BaseHTTPServer import HTTPServer

PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser
class myHandler(SimpleHTTPRequestHandler):
    #Handler for the GET requests
    def do_GET(self):
        if self.path != "/getRaffles":
            self.path = '/public/'+ self.path
            return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET( self )

        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write("Hello World!")
        return

    def do_POST(self):
        content_len = int(self.headers.getheader('content-length', 0))
        post_body = self.rfile.read(content_len)

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER

	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()
