import tweepy
from pymongo import MongoClient

class RaffleSlave:
    "The class responsbile for a single raffle, a new instance for each individual raffle"

    Params = None

    api = None

    alive = True

    def __init__(self, hashtag, max, id, owner ):
        self.Params = {}
        self.Params['max'] = max
        self.Params['hashtag'] = hashtag
        self.Params[ '_id' ] = id
        self.Params[ 'owner' ] = owner

        auth = tweepy.OAuthHandler( '5Xr8HX71XetZYmGV86AmcEgVo', '85ql1GsrOLTRre0AqqprX9Xtm5SkMOWzJk9OVJPRiLM8bm72JA' )
        auth.set_access_token( '832250876551110658-MLGfJUjJH6Ktwlf51AQQlSO9QPcp3ew', 'UvCcyNqwH3X7u2KfRWeYvlOWxN2k1ONfjrlpxRK1Shj33' )

        self.api = tweepy.API( auth )

    def update(self):
        public_tweets = self.api.search( '@'+self.Params['owner']+' #'+self.Params['hashtag'] )
        client = MongoClient()
        db = client.raftl

        tweetcollection = db.tweets
        followers = self.api.followers_ids(self.Params['owner'])

        existingTweets = tweetcollection.find()

        for tweet in public_tweets:

            val = 0
            for checker in tweetcollection.find():
                if( tweet.author.id == checker['user_id'] ):
                    val+=1
                    if( val >= self.Params['max'] ):
                        break

            if( val < self.Params['max'] and tweet.author.screen_name != self.Params['owner'] ):
                tweetcollection.update_one( {'_id':tweet.id}, {'$set': {'_id':tweet.id, 'user_id':tweet.author.id, 'following':tweet.author.id in followers,'raffle_id':self.Params['_id'], 'body':tweet.text, 'username':tweet.author.screen_name, 'profile_img':tweet.author.profile_image_url_https } }, True )

    def getParams(self):
        return self.Params

    def checkAlive(self):
        return self.alive
