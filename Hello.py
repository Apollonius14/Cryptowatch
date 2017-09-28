import requests
import time

"""Testing out all the small elements so that we can 
build something tomorrow"""

"""
Response1 is a response object resulting from sending the HTTP
message using the requests.get method.
"""

#response1 = requests.get("https://api.kraken.com/0/public/Time")

"""
If the response is a json object (which it always is in
Kraken API the below gets unixtime on the server
"""

#print (response1.json()['result']['unixtime'])
#print (response1.content["result"]["unixtime"])

"""
Below gets asset
"""

payl = {'asset': ['BCH','REP','DASH']}

#response2 = requests.post("https://api.kraken.com/0/public/Assets",data = payl)

#print (response2.status_code)
#print (response2.json())

"""
Asset Pairs
"""

# have not (yet) figured out how to specify parameters in requests HTTP
# method - can only filter one item
# need to figure out how Kraken API interprets lists
# instead requesting all data and filtering it for now (probably slow).

#response3 = requests.get("https://api.kraken.com/0/public/AssetPairs")
#print (response3.json())

#keys_avail = [item for item in dict(response3.json()['result']).keys()]

#print (keys_avail)


#for pair in ["BCHEUR","BCHUSD"]:
#    print (pair, ":", response3.json()["result"][pair]["fees_maker"])


#startime = time.clock()

#while time.clock() < startime + 15:
#response4 = requests.post("https://api.kraken.com/0/public/Ticker",data = {'pair':['XBTUSD']})
#print (response4.json())
#print(time.strftime("%H:%M:%S",time.localtime()))
#price = float(response4.json()['result']['XETHZEUR']['a'][0])
#print (price)
##print (type(price))
#time.sleep(3)

#print (time.time())
#time.sleep(3)
#print (time.time())


# Looks like Kraken only serves one currency pair at a time...

import numpy as np
timestamp = time.strftime("%H:%M:%S",time.localtime())

#new_arr = np.array([[0,1,2],[0,1,2]])
#new_arr[0].append[1]
#print (new_arr)

a = [(0,1),(2,3),(4,5)]

list1 = []
list2 = []

for x,y in a:
    list1.append(x)
    list2.append(y)

print (list1)
print (list2)

array1 = ["omar","frank","tim"]
array2 = [1,2,3]

new_arr = np.array([array1,array2],dtype=[("a1", object),("a2",float)])
print (new_arr)