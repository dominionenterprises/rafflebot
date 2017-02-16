from SimpleHTTPServer import SimpleHTTPRequestHandler
import SimpleHTTPServer
from pymongo import MongoClient
import json
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

        client = MongoClient()

        db = client.raftl
        raffle_collection = db.raffles
        tweet_collection = db.tweets

        returnjson = []
        for raffle in raffle_collection.find():
            tweetjson = []
            tweets = tweet_collection.find( {'raffle_id':raffle['_id']} )
            for tweet in tweets:
                tweetjson.append( {'_id':tweet['_id'], 'user_id':tweet['user_id'], 'following':tweet['following'], 'body':tweet['body'] })

            returnjson.append( {'id': str(raffle['_id']), 'max': raffle['max'], 'hashtag':raffle['hashtag'], 'tweets':tweetjson } )

        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write(json.dumps( returnjson ) )
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
