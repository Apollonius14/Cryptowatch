"""Simple live plotter for use in conjunction with KAPI"""

# Import numpy and plotters
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Plotter(object):

    def __init__(self, name):

        self.data_series = np.array([[], []])
        self.title = name
        self.fig = plt.figure()

# Covert tuples from KAPI into numpy array

    def convert(self, pricepoints):
        """takes API price points and appends to the data
        series held in this instance of Plotter

            :params: KAPI pricepoints
            :returns: plotting series as numpy array

            """

        # Need correct datatypes for time and price to
        # enable plotting. Note both NUMPY and Matplotlib
        # happily accept python datetime objects

        tseries = []
        pseries = []

        for time, price in pricepoints[self.title]:
            tseries.append(time)
            pseries.append(float(price))

        self.data_series = [[tseries],[pseries]]

        # Note that Numpy arrays can be extended "inplace" so each time I want to
        # add a point to a Numpy array I must in one way another copy my data into
        # a new fixed-length container. Issue for liveplotting - see below.

        return self.data_series

        # Live plot numpy array using pair as title

    def show(self):


        self.fig.show()
        return


