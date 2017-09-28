"""Apollonius14 Live Cryptocurrency Price Plotter Rev.0
September 27 2017"""

# A single-purpose prototype which uses Kraken cryptocurrency
# exchange as a live data source, obtains rates for currency
# pairs and plots them live for a particular session
# Future: enables order placement

# Cryptotalk Libraries
import KAPI
import Plotter

# Import Time
import time

valid_pairs = []
session_length = 15

# Creates a client API instance

S = KAPI.pubAPI()

# Gets valid pairs for user to chose from


# User Interface Loop
# (for now only one option, single pair, runs once)
# 1. Requests pair and session length from user

pair = 'XBTUSD'

# Creates a live plotter instance

P = Plotter.Plotter(pair)

# Invokes a public session between client API and
# Kraken's API for the duration of session_length
# to get rates for the pair in question and live
# plots

timestart = time.time()

while time.time() < timestart + session_length:

    S.getrates(pair)

    # TODO: currently creating a new numpy array in Plotter each time a new pair is retreived,
    # rather than appending the new data

    P.convert(S.pricepoints)

    time.sleep(3)

    print("Loop")

    P.show()

print(S.pricepoints)
print(P.data_series)