import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#
#fig, ax = plt.subplots()
#xdata, ydata = [], []
#ln, = plt.plot([], [], 'ro', animated=True)
#
#def init():
#    ax.set_xlim(0, 0.5*np.pi)
#    ax.set_ylim(0.05, 0.05)
#    return ln,
#
#def update(frame):
#    xdata.append(frame)
#    ydata.append(np.sin(frame))
#    ax.set_xlim(min(xdata), max(xdata))
#    ax.set_ylim(min(ydata), max(ydata))
#    ln.set_data(xdata, ydata)
#    return ln,
#
#ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
#                    init_func=init, blit=True)
#plt.show()

#my_fig = plt.figure()
#my_second = plt.figure()
#print (type(my_fig))
#
#import time
#i = 10
#
#while i > 0:
#    my_second.show()
#    time.sleep(1)
#    i-=1

#fig, ax = plt.subplots()

#import random
#
#fig, ax = plt.subplots()
#xdata, ydata = [], []
#ln, = plt.plot([], [], 'ro', animated=True)
#
#def init():
#    ax.set_xlim(-1, 15)
#    ax.set_ylim(-1, 15)
#    return ln,
#
#def conv(frame):
#    xdata.append(random.randint(1,10))
#    ydata.append(random.randint(1,10))
#    ln.set_data(xdata, ydata)
#    return ln,
#
#while True:
#
#    ani = FuncAnimation(fig, conv,
#                        init_func=init, blit=True)
#
#    plt.show()

#import datetime
#import time
#
#times = []
#for i in range(3):
#    times.append(datetime.datetime.now())
#    time.sleep(2)
#
#print (times)
#print (min(times))

#import requests
#
#pairs_resp = requests.get("https://api.kraken.com/0/public/AssetPairs")
#
#print (pairs_resp.json()['result']['BCHEUR'])
#
#pairs = [key for key in pairs_resp.json()['result'].keys()]
#
#print(pairs)

import base64

import requests
import time
import urllib.parse
import hashlib
import hmac
import base64

TFA = input("Enter 2FA")
TFA = int(TFA)
secret = input("Enter Password")
secret = bytes(secret,'utf-8')
secret = base64.b64encode(secret)

urlpath = "https://api.kraken.com/0/private/TradeBalance"

data = {
    'nonce': int(1000 * time.time()),
    'otp': TFA,
}

def sign(data, urlpath):
    """ Sign request data according to Kraken's scheme.
    :param data: API request parameters
    :type data: dict
    :param urlpath: API URL path sans host
    :type urlpath: str
    :returns: signature digest
    """
    postdata = urllib.parse.urlencode(data)

    # Unicode-objects must be encoded before hashing
    encoded = (str(data['nonce']) + postdata).encode()
    message = urlpath.encode() + hashlib.sha256(encoded).digest()

    signature = hmac.new(base64.b64decode(secret),
                         message, hashlib.sha512)
    sigdigest = base64.b64encode(signature.digest())

    return sigdigest.decode()

signature = sign(data,"https://api.kraken.com/0/private/TradeBalance")

my_key = 'okadhim'

headers = {
    'API-Key': my_key,
    'API-Sign': signature,
}

balance = requests.post(urlpath, data = [], headers = [])

print(balance.json())






