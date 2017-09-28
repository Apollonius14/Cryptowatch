"""Apollonius14 Live Cryptocurrency Price Plotter Rev.0
September 27 2017"""

# A single-purpose prototype which uses Kraken cryptocurrency
# exchange as a live data source, obtains rates for currency
# pairs and plots them live for a particular session
# Future: enables order placement

# Cryptotalk Libraries
import KAPI
import Plotter
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import datetime

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
timedatestart = datetime.datetime.now()

def update(frame):

    # TODO: Put all plotter related activities in plotter instance. 

    S.getrates(pair)
    P.convert(S.pricepoints)
    P.ax.set_xlim(timedatestart, datetime.datetime.now())
    P.ax.set_ylim(3000, 5000)
    P.ln.set_data(P.data_series[0], P.data_series[1])
    print (P.data_series)
    return P.ln,

while time.time() < timestart + session_length:

    # TODO: currently creating a new numpy array in Plotter
    # TODO: each time a new pair is retreived,
    # TODO: -rather than appending the new data

    # TODO: below should be console and graph outpu

    time.sleep(2)

    print("Loop")

    ani = FuncAnimation(P.fig, update, blit=True)

    plt.show()
