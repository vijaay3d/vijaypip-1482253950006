"""Cloud Foundry test"""
from flask import Flask
import cf_deployment_tracker
import os
import requests 
import json

# Emit Bluemix deployment event
cf_deployment_tracker.track()

app = Flask(__name__)

# On Bluemix, get the port number from the environment variable VCAP_APP_PORT
# When running this app on the local machine, default the port to 8080
port = int(os.getenv('VCAP_APP_PORT', 8080))


@app.route('/')
def hello_world():
    username = '909eebc9-780a-4af9-bd5c-44baaa854d50'
    password = '200T8xvi5B'
    zip = '75034'
    watsonUrl = 'https://twcservice.mybluemix.net/api/weather/v1/location/' + zip + ':4:US' + '/observations.json?language=en-US'
    try:
        r = requests.get(watsonUrl,auth=(username,password))
        results = r.text
        if results != False:
            results_json = json.loads(str(results))
            print()
            print('Here is the weather for {0}'.format(results_json['observation']['obs_name']))
            print('{0:20} {1:<10}'.format('Current Temperature:',str(results_json['observation']['temp']) + '° and ' + results_json['observation']['wx_phrase']))
            print('{0:20} {1:<10}'.format('Feels Like: ',str(results_json['observation']['feels_like']) + '°'))
            print('{0:20} {1:<10}'.format('Low Temp: ',str(results_json['observation']['min_temp']) + '°'))
            print('{0:20} {1:<10}'.format('High Temp: ',str(results_json['observation']['max_temp']) + '°'))
            print('{0:20} {1:<10}'.format('Winds:',str(results_json['observation']['wspd']) + ' mph coming from the ' + results_json['observation']['wdir_cardinal']))
        else:
            print('Something went wrong :-(')
    except:
        return False

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
