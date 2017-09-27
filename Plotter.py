"""Simple live plotter for use in conjunction with KAPI"""

# Import numpy and plotters
import numpy as np
from matplotlib import animation

class Plotter(object):

    def __init__(self):

        self.data_series = []

# Covert tuples from KAPI into numpy array

    def convert(self,pricepoints):
        """takes API price points and converts to dict containing
            numpy array and series name

            :params: KAPI pricepoints
            :returns: plotting series in form {"pair": np.array(([times....][prices...])))

            """
        # First convert times into numpy times




# Live plot numpy array using pair as title

