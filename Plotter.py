"""Simple live plotter for use in conjunction with KAPI"""

# Import numpy and plotters
import matplotlib.pyplot as plt
import datetime
import numpy as np

class Plotter(object):

    def __init__(self, name, session_length):

        # Future can select multiple pair names and get multiple subplots sharing time

        self.data_series = [[], []]
        self.title = name #Pair name
        self.fig, self.ax = plt.subplots()
        self.ln, = self.ax.plot([], [], '-', animated=True)
        self.startime = datetime.datetime.now()
        self.session_length = session_length
        self.ax.set_title(self.title)
        self.ax.set_ylim(-100,100)
        self.ax.set_xlim(self.startime - datetime.timedelta(seconds=self.startime.second),
                         self.startime - datetime.timedelta(seconds=self.startime.second) +
                         datetime.timedelta(minutes=self.session_length+1))

    def convert(self, pricepoints):
        """takes API price points and appends to the data
        series held in this instance of Plotter

            :params: KAPI pricepoints
            :returns: plotting series as numpy array with tseries as a
            list of datetime objects and pseries a list of floats

            """

        # Note both NUMPY and Matplotlib
        # happily accept python datetime objects

        # Append latest timestamp
        self.data_series[0].append(pricepoints[self.title][-1][0])

        # Append latest price
        self.data_series[1].append(pricepoints[self.title][-1][1])
	
        self.ax.set_ylim(np.min(self.data_series[1])-1, np.max(self.data_series[1])+1)

        self.ln.set_data(self.data_series[0],
                         self.data_series[1])

        # Note that Numpy arrays can be extended "inplace" so each time I want to
        # add a point to a Numpy array I must in one way another copy my data into
        # a new fixed-length container. Issue for liveplotting - see below.

        return

        # Live plot numpy array using pair as title

    #def show(self):

    #    def update(frame):
    #        self.ax.set_xlim(min(self.data_series[0]), max(self.data_series[0]))
    #        self.ax.set_ylim(min(self.data_series[1]) - 100, max(self.data_series[1]) + 100)
    #        self.ln.set_data(self.data_series[0], self.data_series[1])
    #        return self.ln,

    #    self.ani = FuncAnimation(self.fig, update, blit=True)

    #    self.fig.show()


