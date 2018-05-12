#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 13:11:28 2017 while at the lihue airport
@author: jeffreyfong

installing on c9: 
    sudo pip3 install flask==0.10.1
    sudo pip3 install datedelta==1.2
"""

from flask import Flask
from flask import request
from flask import send_from_directory

import json
import numpy
import math
import datetime
import datedelta



# crossdomain function needs all of these imports
from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper

def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, list):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator





    
    
    
 
#app = Flask(__name__)
app = Flask(__name__, static_url_path='', static_folder='web/static/')

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['TESTING'] = True


    


print('i am here') 
@app.route('/')
@crossdomain(origin='*')  # needed to allow domains  ,methods=['POST', 'OPTIONS']
def home():
     
  
    # https://gist.github.com/nhmc/0537027242dd66e47002
    
    print('hello maui')
    
    return send_from_directory('', 'index.html')
    
    #return 'Hello Maui !!!!!!!!!!!'
    
      
    
    
'''    
from urllib.request import urlopen
import urllib.parse

#from lxml import html

import requests

@app.route('/API/v1/SCRAPE')
@crossdomain(origin='*')  # needed to allow domains  ,methods=['POST', 'OPTIONS']
def scrape():
    
    
    #url = 'http://www.zillow.com/webservice/GetDeepSearchResults.htm?zws-id=X1-ZWz1g528m5rsaz_76gmj&address=2114+Bigelow+Ave&citystatezip=Seattle%2C+WA'
    url = 'http://www.zillow.com/webservice/GetUpdatedPropertyDetails.htm?zws-id=X1-ZWz1g528m5rsaz_76gmj&zpid=80333139'
    #url = 'http://www.zillow.com/webservice/GetSearchResults.htm?zws-id=X1-ZWz1g528m5rsaz_76gmj&address=475+Front+St+unit+208&citystatezip=96761'
    
    response = urlopen(url)
    string = response.read().decode('utf-8')
    print(string)
    #json_obj = json.loads(string)
    
    return 'test'
'''
    

from funcs import *
from crypto import *

@app.route('/crypto')
@crossdomain(origin='*')  # needed to allow domains  ,methods=['POST', 'OPTIONS']
def crypto():
    
    portfolio = getPortfolio()
    #portfolio = json.dumps(portfolio)
    
    html = "<html><body><div>BTC: $"+str(round(portfolio['value']['BTC'],2))+"</div>"
    html += "<div>BTG: $"+str(round(portfolio['value']['BTG'],2))+"</div>"
    html += "<div>XEM: $"+str(round(portfolio['value']['XEM'],2))+"</div>"
    html += "<div>XRP: $"+str(round(portfolio['value']['XRP'],2))+"</div>"
    html += "<div>ETH: $"+str(round(portfolio['value']['ETH'],2))+"</div>"
    html += "<div>Total: $"+str(round(portfolio['value']['Total'],2))+"</div>"
    html += "<div>Total Return: "+str(round(100*((portfolio['value']['Total'] / 500)-1),2))+"%</div></body></html>"
    
    return html
    
    

@app.route('/dev')
@crossdomain(origin='*')  # needed to allow domains  ,methods=['POST', 'OPTIONS']
def dev():
    
    
    # length of the loan in years
    Nyear = 29
    
    # the yearly percentage interest rate 
    rate = 6 
    
    # the amount borrowed
    principle = 300000.0
    
    # The amount in a 100% offset account
    offset = 0.0
    
    # Start end years that the offset amount is present in the account
    start, end = 0, None

    monthly_payment = calc_monthly_payment(principle, Nyear, rate)
    
    
    #mp = 1821.013838679435
    #monthly_payment = mp
    M = calc_amort(principle, rate, monthly_payment, offset, offset_start_year=start, offset_end_year=end)
    
    
    
    print('monthly_payment:', monthly_payment)
    print('amort:', M)
    print('len:', (len(M['P'])-1)/12)
    print('Hello Maui Dev')
    
    return 'Hello Maui Dev'
    
    
    
    
    
    
@app.route('/API/v1/calc', methods=['GET', 'POST'])
@crossdomain(origin='*')  # needed to allow domains  ,methods=['POST', 'OPTIONS']
def calc():
    
    # http://localhost:8888/API/v1/calc?params={"principle":500000,"interest":0.035}
    # http://www.hawaiigaga.com/hawaii-vacation-rental-statistics.aspx
    # https://dbedt.hawaii.gov/hhfdc/files/2015/02/RENTAL-HOUSING-STUDY-2014-UPDATE-COUNTY-OF-MAUI.pdf
    
    
    print('Mortgage calculation\n')
    
    def formatDD(dd):
        ret = str(dd.year) + '-' + str(dd.month) + '-' + str(dd.day)
        return ret
        
    now = datetime.datetime.now()
    firstDateNextMonth = datetime.date(now.year, now.month, 1) + datedelta.MONTH
    print('Starting Mortagage Date:', firstDateNextMonth)
    
     
              
    
    print('---------------------------------')
    price = float(request.args.get('price'))
    downpayment = float(request.args.get('downpayment'))
    years = float(request.args.get('years'))
    rate = float(request.args.get('rate'))
    principle = price-downpayment
    monthly_payment = calc_monthly_payment(principle, years, rate)
    monthlyRates = request.args.get('monthlyRates')
    print(monthlyRates)
    
    print('Price:', price)
    print('downpayment:', downpayment)
    print('principle:', principle)
    print('monthly_payment:', monthly_payment)
    print('years:', years)
    print('rate:', rate)
    
   
    params = {'price':price,
              'appreciationRate':0.04,
              'downpayment':downpayment, 
              'interest':(rate/100)/12,
              'payment':monthly_payment,
              'condoFees':784,
              'propertyTaxRate':0.00456,
              'managementTake':0.5}
    params['monthlyRates'] = json.loads(monthlyRates)
   # params['monthlyRates'] = monthlyRates
              
    totalMonthly_payment = monthly_payment + params['condoFees'] + (params['propertyTaxRate']*params['price'])/12
        
    #https://maui-api-riskmanagerjeff.c9users.io/API/v1/calc?

   
              
    '''
    params['monthlyRates'] = [
        {'month':'Jan', 'nightly':200, 'occupancy':0.0},
        {'month':'Feb', 'nightly':200, 'occupancy':0.90},
        {'month':'Mar', 'nightly':185, 'occupancy':0.90},
        {'month':'Apr', 'nightly':185, 'occupancy':0.80},
        {'month':'May', 'nightly':170, 'occupancy':0.80},
        {'month':'Jun', 'nightly':170, 'occupancy':0.70},
        {'month':'Jul', 'nightly':170, 'occupancy':0.70},
        {'month':'Aug', 'nightly':170, 'occupancy':0.70},
        {'month':'Sep', 'nightly':170, 'occupancy':0.80},
        {'month':'Oct', 'nightly':170, 'occupancy':0.80},
        {'month':'Nov', 'nightly':185, 'occupancy':0.90},
        {'month':'Dec', 'nightly':200, 'occupancy':0.90}
    ]          
    '''  
    
    #params['rental'] = (365/12)*params['nightlyRate']*(1-params['managementTake'])*params['occupancyRate']
    
    params['rentalIncome'] = []
    daysInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
    avgRentalIncome = 0
    for MM in range(0,12):
        v = (daysInMonth[MM])*params['monthlyRates'][MM]['nightly']*params['monthlyRates'][MM]['occupancy']*(1/100)*(1-params['managementTake'])
        params['rentalIncome'].append( v )
        avgRentalIncome += v/12
    
    
        
    #print(params)
    
    #schedule = {'interest':[], 'principle_pmts':[]}
    
    ret1 = {'schedule':[]}
    ret2 = {'schedule':[]}
    
    DD = firstDateNextMonth
    
    ret1['schedule'].append({
        'i':0,
        'date':formatDD(DD),
        'principle_pmt':-params['downpayment'],
        'principle_only':0,
        'interest':0,
        'cashflow':-params['downpayment'],
        'remaining':params['price']-params['downpayment']
    })
    
    ret2['schedule'].append({
        'i':0,
        'date':formatDD(DD),
        'principle_pmt':-params['downpayment'],
        'principle_only':0,
        'interest':0,
        'cashflow':-params['downpayment'],
        'remaining':params['price']-params['downpayment']
    })
    
    DD = DD + datedelta.MONTH
 
    remaining1 = params['price']-params['downpayment']
    remaining2 = params['price']-params['downpayment']
    
    i = 1
    ii = 1
    MM = 1
    while remaining2>0:
        
        
        condoFees = params['condoFees']
        propertyTax = (params['propertyTaxRate']*params['price'])/12
        
        
        interest1 = params['interest']*remaining1
        interest2 = params['interest']*remaining2
        
        
        # CF = -principle_only - interest_only - condoFees - propertyTax + rentalIncome
        # cummCF = cummCF + CF
        
        
        principle_pmt1 = (params['payment']+params['rentalIncome'][MM-1]) - interest1 # - condoFees - propertyTax
        principle_only = (params['payment']) - interest1 # - condoFees - propertyTax
        
        principle_pmt2 = (params['payment']+0) - interest2 # - condoFees - propertyTax
        principle_only2 = (params['payment']) - interest2 # - condoFees - propertyTax
                          
        if remaining1 - principle_only < 0:
            principle_only = remaining1
            
        if remaining2 - principle_pmt2 < 0:
            principle_pmt2 = remaining2
            
        remaining1 = remaining1 - principle_only
        remaining2 = remaining2 - principle_pmt2
        
        if principle_pmt1 > 0:
            ret1['schedule'].append({
                'i':i,
                'date':formatDD(DD),
                'principle_pmt':principle_pmt1,
                'principle_only':principle_only,
                'interest':interest1,
                'cashflow':params['rentalIncome'][MM-1] - principle_only - interest1 - condoFees - propertyTax,
                'remaining':remaining1
            })
            ii = ii+1
        
        if principle_pmt2 > 0:
            ret2['schedule'].append({
                'i':i,
                'date':formatDD(DD),
                'principle_pmt':principle_pmt2,
                'principle_only':principle_only2,
                'interest':interest2,
                'cashflow':0 - principle_pmt2 - interest2 - condoFees - propertyTax,
                'remaining':remaining2
            })
        
        
        #print('Month', i, DD, remaining2)
        i = i+1
        DD = DD + datedelta.MONTH
        MM = MM+1
        if MM==13:
            MM = 1
            
    nMonths_without_rental = i-1-1       
    nMonths_with_rental = ii-1-1
    
    
    
            
    if False:
        ret1['schedule'].append({
            'i':i,
            'date':formatDD(DD),
            'principle_pmt':0,
            'principle_only':0,
            'interest':0,
            'cashflow':params['price']*math.exp(params['appreciationRate']*(i/12)),
            'remaining':0
        })
        
        ret2['schedule'].append({
            'i':i,
            'date':formatDD(DD),
            'principle_pmt':0,
            'principle_only':0,
            'interest':0,
            'cashflow':params['price']*math.exp(params['appreciationRate']*(i/12)),
            'remaining':0
        })
    
    #totalInterest = sum(schedule['interest'])
    #print('total interest paid:', totalInterest)
    
    futureValue = params['price']*math.exp(params['appreciationRate']*(i/12))
    presentValue = futureValue / math.pow( 1+rate/100, (i/12) )
   
    CFarray = [cf['cashflow'] for cf in ret1['schedule']]
    
    
    #rate = numpy.irr(CFarray) * 1
    
    #CFarray[0] = 0
    
    #RemainingArray = [c['remaining'] for c in ret1['schedule']]
    #print(RemainingArray)
    
    
    
    npv_cashflow = numpy.npv(params['interest']/12,CFarray)
    
    
    #PnL = npv - params['downpayment']
    #print('capital required:', params['downpayment'])
    print('npv_cashflow:', npv_cashflow)
    print('futureValue:', futureValue)
    print('presentValue:', presentValue)
    
    CFarray_full = CFarray
    CFarray_full[0] = -downpayment
    CFarray_full.append(futureValue)
    print(CFarray_full)
    rate = numpy.irr(CFarray_full) * 1
    irr = math.exp(rate*12)-1
    print('IRR:', str(irr) )
    
    
    
    #print("P&L:", PnL)
    
    #print('IRR:', str(math.exp(rate*12)-1) )
    #print(str(i/12), 'years')
    
    
    #print( ret['schedule'] )
    
    data = {
        'monthly_payment': monthly_payment,
        'nMonths_with_rental': nMonths_with_rental,
        'nMonths_without_rental': nMonths_without_rental,
        'npv_cashflow':npv_cashflow,
        'futureValue':futureValue,
        'presentValue':presentValue,
        'IRR': irr,
        'avgRentalIncome': avgRentalIncome,
        'totalMonthly_payment': totalMonthly_payment
    }
    
    
    obj = [
        {
        'key': 'With Rental Income',
        'values': ret1['schedule']
        },
        {
        'key': 'Without',
        'values': ret2['schedule']
        }
    ]
    
  
   
    
    data['schedules'] = obj
    
    
    jsonData = json.dumps(data)
    
    #print(obj)
    print(years)
    print(rate)
    print(principle)
    
    return jsonData




  
if __name__ == '__main__':
    

    #calc()
    
    # for c9, this setting is recommended and ports open:  app.run(host='0.0.0.0', port=8080, debug=True)  
    app.run(host='0.0.0.0', port=8080, debug=True)  
