from rafflemaster import RaffleMaster
from raffleslave import RaffleSlave
from pymongo import MongoClient

master = RaffleMaster()
client = MongoClient()

db = client.raftl
raffle_collection = db.raffles
"raffle_collection.insert_one( {'hashtag':'raffle1', 'max':3} )"
" raffle_id tweet_id user_id "

for raffle in raffle_collection.find():
    master.addRaffle( RaffleSlave( raffle['hashtag'], raffle['max'], raffle['_id'] ) )

master.checkAlive()
master.runUpdates()
