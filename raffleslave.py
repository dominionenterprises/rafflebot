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

        auth = tweepy.OAuthHandler( '5Xr8HX71XetZYmGV86AmcEgVo', '85ql1GsrOLTRre0AqqprX9Xtm5SkMOWzJk9OVJPRiLM8bm72JA' )
        auth.set_access_token( '832250876551110658-MLGfJUjJH6Ktwlf51AQQlSO9QPcp3ew', 'UvCcyNqwH3X7u2KfRWeYvlOWxN2k1ONfjrlpxRK1Shj33' )

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
