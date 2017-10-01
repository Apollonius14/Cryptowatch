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

# Session lenght in minutes
session_length = 2

# Creates a client API instance

S = KAPI.pubAPI()

# Gets valid trading pairs for user to chose from

valid_pairs = S.getpairs()

# Hard-coding display to 5 pairs per line
def display_pairs(list,line):
    length = len(list)
    lastline = divmod(length,line)[0]
    print (line,lastline)
    i=0
    while i < length:
        if length - i >= lastline:
            print (" | ".join(list[i:i+line]))
            i+=line
        else:
            print (" | ".join(list[i:i+lastline]))
            i+=lastline

display_pairs(valid_pairs,6)

# User Interface Loop
# (for now only one option, single pair, runs once)
# 1. Requests pair and session length from user

pair = input("Please select currency pair to view:")


while pair not in valid_pairs:

    pair = input("Please select currency pair to view:")

S.getrates(pair)

# Creates a live plotter instance

P = Plotter.Plotter(pair, session_length)

# Invokes a public session between client API and
# Kraken's API for the duration of session_length
# to get rates for the pair in question and live
# plots

tstart = time.time()

# Main output routine

def update(frame):

    # Get pair data from API
    S.getrates(pair)

    # Add pair to Plotter array
    P.convert(S.pricepoints)

    # Return line object to animation
    return P.ln,


while time.time() < tstart + session_length:

    # Keep the graph animation going for session length
    ani = FuncAnimation(P.fig, update, blit=True)
    plt.show()

