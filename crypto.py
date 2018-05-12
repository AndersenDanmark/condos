from urllib.request import urlopen
import json

import requests
import re



def getPortfolio():


    
    #url = "https://api.coinbase.com/v2/prices/BTC-CAD/spot"
    #url = "https://api.coinbase.com/v2/prices/XEM-BTC/spot"
    #url = "https://api.gdax.com/GET/products/BTC-USD/stats&start=2017-01-01&end=2017-09-14"
    
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,CAD"
    response = urlopen(url)
    string = response.read().decode('utf-8')
    json_BTC = json.loads(string)
    
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTG&tsyms=USD,CAD"
    response = urlopen(url)
    string = response.read().decode('utf-8')
    json_BTG = json.loads(string)
    #print('BTC in CAD is',json_BTC['CAD'])

    url = "https://min-api.cryptocompare.com/data/price?fsym=XEM&tsyms=USD,CAD"
    response = urlopen(url)
    string = response.read().decode('utf-8')
    json_XEM = json.loads(string)
    #print('XEM in CAD is',json_XEM['CAD'])
    
    url = "https://min-api.cryptocompare.com/data/price?fsym=XRP&tsyms=USD,CAD"
    response = urlopen(url)
    string = response.read().decode('utf-8')
    json_XRP = json.loads(string)
    
    url = "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,CAD"
    response = urlopen(url)
    string = response.read().decode('utf-8')
    json_ETH = json.loads(string)
    
    portfolio_old = {
        "BTC": {"Position":0.04510166, "Price":{"CAD":json_BTC['CAD'], "USD":json_BTC['USD']}},
        "BTG": {"Position":0.04510166, "Price":{"CAD":json_BTG['CAD'], "USD":json_BTG['USD']}},
        "XEM": {"Position":398, "Price":{"CAD":json_XEM['CAD'], "USD":json_XEM['USD']}},
        "ETH": {"Position": 0.48998544, "Price":{"CAD":json_ETH['CAD'], "USD":json_ETH['USD']}} 
    } 
    
    portfolio = {
        "BTC": {"Position":0.03683, "Price":{"CAD":json_BTC['CAD'], "USD":json_BTC['USD']}},
        "BTG": {"Position":0.04510166, "Price":{"CAD":json_BTG['CAD'], "USD":json_BTG['USD']}},
        "XEM": {"Position":398, "Price":{"CAD":json_XEM['CAD'], "USD":json_XEM['USD']}},
        "XRP": {"Position":50, "Price":{"CAD":json_XRP['CAD'], "USD":json_XRP['USD']}},
        "ETH": {"Position": 0.48998544, "Price":{"CAD":json_ETH['CAD'], "USD":json_ETH['USD']}} 
    }    
    
    print(portfolio)
    print('BTC:', portfolio["BTC"]["Position"]*portfolio["BTC"]["Price"]["CAD"])
    print('BTG:', portfolio["BTG"]["Position"]*portfolio["BTG"]["Price"]["CAD"])
    print('XEM:', portfolio["XEM"]["Position"]*portfolio["XEM"]["Price"]["CAD"])
    print('XRP:', portfolio["XRP"]["Position"]*portfolio["XRP"]["Price"]["CAD"])
    print('ETH:', portfolio["ETH"]["Position"]*portfolio["ETH"]["Price"]["CAD"])
    ss = portfolio["BTC"]["Position"]*portfolio["BTC"]["Price"]["CAD"] + portfolio["BTG"]["Position"]*portfolio["BTG"]["Price"]["CAD"] + portfolio["XEM"]["Position"]*portfolio["XEM"]["Price"]["CAD"] + portfolio["XRP"]["Position"]*portfolio["XRP"]["Price"]["CAD"] + portfolio["ETH"]["Position"]*portfolio["ETH"]["Price"]["CAD"]
    print('Total:', ss)
    
    portfolio['value'] = {
        'BTC': portfolio["BTC"]["Position"]*portfolio["BTC"]["Price"]["CAD"],
        'BTG': portfolio["BTG"]["Position"]*portfolio["BTG"]["Price"]["CAD"],
        'XEM': portfolio["XEM"]["Position"]*portfolio["XEM"]["Price"]["CAD"],
        'XRP': portfolio["XRP"]["Position"]*portfolio["XRP"]["Price"]["CAD"],
        'ETH': portfolio["ETH"]["Position"]*portfolio["ETH"]["Price"]["CAD"],
        'Total': portfolio["BTC"]["Position"]*portfolio["BTC"]["Price"]["CAD"] + portfolio["BTG"]["Position"]*portfolio["BTG"]["Price"]["CAD"] + portfolio["XEM"]["Position"]*portfolio["XEM"]["Price"]["CAD"] + portfolio["XRP"]["Position"]*portfolio["XRP"]["Price"]["CAD"] + portfolio["ETH"]["Position"]*portfolio["ETH"]["Price"]["CAD"]
    }
    
    #url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,CAD"
    #https://www.quadrigacx.com/api_info
    #resp = requests.get(url)
    
    #print(resp.content)
    
    #Kraken Coinbase
    url = "https://min-api.cryptocompare.com/data/histoday?fsym=ETH&tsym=USD&limit=60&aggregate=3&e=Coinbase&extraParams=your_app_name"
    response = urlopen(url)
    string = response.read().decode('utf-8')
    data = json.loads(string)
    #print(data)

    return portfolio
    
    
getPortfolio()