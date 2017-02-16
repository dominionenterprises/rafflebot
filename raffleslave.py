import tweepy
from pymongo import MongoClient

class RaffleSlave:
    "The class responsbile for a single raffle, a new instance for each individual raffle"

    Params = { 'max':-1, 'hashtag':' ', '_id':-1 }

    api = None

    alive = True

    def __init__(self, hashtag, max, id ):

        self.Params['max'] = max
        self.Params['hashtag'] = hashtag
        self.Params[ '_id' ] = id

        auth = tweepy.OAuthHandler( 'Vj5hr2GqqgmyU1d3uo4C2JU63', 'amknuv5eFOFjgUPb9u6BdYywz3wV2fQfMuK9ApAwRWfMqaR3No' )
        auth.set_access_token( '2859266634-9EQRinUa8HoghhW7MQEMfnWycvLv9ameuhOKhFG', 'gSaPkTCjQGX9sTnTFTKS0GDRFmfrjxuVvFG4odKl5WzQ1' )

        self.api = tweepy.API( auth )

    def update(self):
        public_tweets = self.api.search( '@hackuraffl #'+self.Params['hashtag'] )

        client = MongoClient()
        db = client.raftl

        tweetcollection = db.tweets
        followers = self.api.followers_ids('hackuraffl')

        for tweet in public_tweets:
            tweetcollection.replace_one( {'_id':tweet.id}, {'_id':tweet.id, 'user_id':tweet.author.id, 'following':tweet.author.id in followers,'raffle_id':self.Params['_id'], 'body':tweet.text }, True )


    def getParams(self):
        return self.Params

    def checkAlive(self):
        return self.alive
