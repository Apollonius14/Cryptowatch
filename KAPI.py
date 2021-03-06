"""Cleint API dedicated to Kraken API"""

# Creates a client API which can hold
# either a public or private session
# with Kraken API. Public sessions are
# able to query currency pairs available
# and currency pair rates Private sessions
# (future) enable order placement

"""Begin Script"""

# Timestamp
import datetime
import time

# HTTP communications
import requests


class pubAPI(object):

    def __init__(self):
        self.pricepoints = {}
        self.feedata = {}
        self.pairs = []

    def getpairs(self):
        """ queries Kraken for currency pairs available for information
        : params: none
        : returns: list self.pairs

        """

        pairs_resp = requests.get("https://api.kraken.com/0/public/AssetPairs")

        self.pairs = [key for key in pairs_resp.json()['result'].keys()]

        return self.pairs

    def getrates(self, pair):
        """
        Takes the pair in question, creates a dictionary entry
        for it (if not already existing), then appends to
        it a tuples of datetime objects (hh:mm:ss) and rate (float)
        : params: pair (string)
        : returns: dict pricepoints {"PAIR": [(time1,rate1),(time2,rate2)...]

        .Note: pairs are referenced ETHUSD in the call but their key in the
               Kraken API ticker call is XETHZUSD. Need to verify but it
               appears that cryptos are suffixed with an "X" and fiats with
               a "Z".

        """

        if pair not in list(self.pricepoints.keys()):

            self.pricepoints[pair] = []



        rates_resp = requests.post("https://api.kraken.com/0/public/Ticker", data={'pair': [pair]})

        timestamp = datetime.datetime.now()

        price = float(rates_resp.json()['result'][pair]['a'][0])

        self.pricepoints[pair].append((timestamp, float(price)))

        time.sleep(3)

        return self.pricepoints

    def getfees(self, pair):
        """Returns the fee schedule for the currency pair passed in pair

        """
        return

    def getbalance(self):


        return
