# Using the IBM Bluemix Weather Company API
# Bruce Elgort
# July 9, 2016
# Version 1.0
# IBM Weather Company Docs: https://console.ng.bluemix.net/docs/services/Weather/weather_rest_apis.html#rest_apis

import requests 
import json

def get_weather(zip):
    username = '909eebc9-780a-4af9-bd5c-44baaa854d50'
    password = '200T8xvi5B'
    
    watsonUrl = 'https://twcservice.mybluemix.net/api/weather/v1/location/' + zip + ':4:US' + '/observations.json?language=en-US'

    try:
        r = requests.get(watsonUrl,auth=(username,password))
        return r.text
    except:
        return False

def display_weather(results):
    print()
    print('Here is the weather for {0}'.format(results['observation']['obs_name']))
    print('{0:20} {1:<10}'.format('Current Temperature:',str(results['observation']['temp']) + '° and ' + results['observation']['wx_phrase']))
    print('{0:20} {1:<10}'.format('Feels Like: ',str(results['observation']['feels_like']) + '°'))
    print('{0:20} {1:<10}'.format('Low Temp: ',str(results['observation']['min_temp']) + '°'))
    print('{0:20} {1:<10}'.format('High Temp: ',str(results['observation']['max_temp']) + '°'))
    print('{0:20} {1:<10}'.format('Winds:',str(results['observation']['wspd']) + ' mph coming from the ' + results['observation']['wdir_cardinal']))
 
def get_weather():
    zip = input('Enter US ZIP code to get weather for:\n')
    results = get_weather(zip)
    if results != False:
        results = json.loads(str(results))
        display_weather(results)
    else:
        print('Something went wrong :-(')
 
if __name__ == '__main__':
    get_weather()
