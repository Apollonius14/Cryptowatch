___

### Cryptotalk

Author: Omar Kadhim - Fall 2017

Python script to connect to Kraken cryptocurrency API. Public sessions can be used to
get currency pair rates and Private sessions can be used to place orders.
___

### Update Log:

Rev0: September 2017. Basic working version connects with public Kraken API, prompts
user to select currency/cryptocurrency pair and live-plots the rate.
____

### Getting Started:

Ensure the below files are in the same directory. Run Cryptotalk.py and follow prompts.

Files:

** KAPI.py
API class that performs queries on Krakens's
public API. Returns the price of a currency pair
as a price-point object in a named series in a library 
{Pair: [(Time,Kraken sell price),(T2,P2)...]}

** Plotter.py
Creates MATPLOTLIB plot instance which takes price-point-objects
and returns a live plot 

** Cryptotalk.py
Calls KAPI and Plotter with user-determined parameters
Currency-Pair
Time to keep running
Runs an animation of the live price
_____

