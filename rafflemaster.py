from raffleslave import RaffleSlave
from pymongo import MongoClient
import time

class RaffleMaster:
    "Raffle master that maintains every individual raffle"

    raffles = []

    def addRaffle( self, RaffleSlave ):
        self.raffles.append( RaffleSlave )

    def checkAlive(self):
        alive = False

        for raffle in self.raffles:
            if not raffle.checkAlive():
                self.raffles.remove( raffle )
            else:
                alive = True

        return alive

    def runUpdates(self):
        for raffle in self.raffles:
            raffle.update()

    def insertRaffle( self, raffle, raffle_collection ):
        raffle_collection.insert_one( raffle.getParams() )
