import tweepy

class RaffleSlave:
    "The class responsbile for a single raffle, a new instance for each individual raffle"

    Params = { 'MAX_ENTRIES':-1, 'HASHTAG':' ' }

    def __init__(self, hashtag, max ):

        self.Params['MAX_ENTRIES'] = max
        self.Params['HASHTAG'] = hashtag

        auth = tweepy.OAuthHandler( 'Vj5hr2GqqgmyU1d3uo4C2JU63', 'amknuv5eFOFjgUPb9u6BdYywz3wV2fQfMuK9ApAwRWfMqaR3No' )
        auth.set_access_token( '2859266634-9EQRinUa8HoghhW7MQEMfnWycvLv9ameuhOKhFG', 'gSaPkTCjQGX9sTnTFTKS0GDRFmfrjxuVvFG4odKl5WzQ1' )

        api = tweepy.API( auth )

        public_tweets = api.search( '@hackuraffl #'+self.Params['HASHTAG'] )
        for tweet in public_tweets:
            print tweet.text
