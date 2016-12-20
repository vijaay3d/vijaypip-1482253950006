# Using the IBM Bluemix Weather Company API
# Bruce Elgort
# July 9, 2016
# Version 1.0
# IBM Weather Company Docs: https://console.ng.bluemix.net/docs/services/Weather/weather_rest_apis.html#rest_apis
 
import requests
import json
 
def get_weather(zip):
    username = 'your username'
    password = 'your password'
 
    watsonUrl = 'https://twcservice.mybluemix.net/api/weather/v1/location/' + zip + ':4:US' + '/observations.json?language=en-US'
 
    try:
        r = requests.get(watsonUrl,auth=(username,password))
        return r.text
    except:
        return False
 
def display_weather(results):
    print()
    print('Here is the weather for {0}'.format(results['observation']['obs_name']))
    print('{0:20} {1:&lt;10}'.format('Current Temperature:',str(results['observation']['temp']) + '° and ' + results['observation']['wx_phrase']))
    print('{0:20} {1:&lt;10}'.format('Feels Like: ',str(results['observation']['feels_like']) + '°'))
    print('{0:20} {1:&lt;10}'.format('Low Temp: ',str(results['observation']['min_temp']) + '°'))
    print('{0:20} {1:&lt;10}'.format('High Temp: ',str(results['observation']['max_temp']) + '°'))
    print('{0:20} {1:&lt;10}'.format('Winds:',str(results['observation']['wspd']) + ' mph coming from the ' + results['observation']['wdir_cardinal']))
 
def get_weather():
    zip = input('Enter US ZIP code to get weather for:\n')
    results = get_weather(zip)
    if results != False:
        results = json.loads(str(results))
        display_weather(results)
    else:
        print('Something went wrong<img draggable="false" class="emoji" alt="😦" src="https://s0.wp.com/wp-content/mu-plugins/wpcom-smileys/twemoji/2/svg/1f626.svg">')
 
if __name__ == '__main__':
    get_weather()