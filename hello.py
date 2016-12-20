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
        return r.text
    except:
        return False

#def hello_world():
#    return 'Hello World! I am running on port ' + str(port)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
