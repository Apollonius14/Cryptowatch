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
#
#for pair in ["BCHEUR","BCHUSD"]:
#    print (pair, ":", response3.json()["result"][pair]["fees_maker"])


startime = time.clock()

#while time.clock() < startime + 15:
#    response4 = requests.post("https://api.kraken.com/0/public/Ticker",data = {'pair':['ETHUSD','ETHEUR']})
#    print(time.clock())
#    print(response4.json())
#    time.sleep(3)

print (time.time())
time.sleep(3)
print (time.time())


# Looks like Kraken only serves one currency pair at a time...
