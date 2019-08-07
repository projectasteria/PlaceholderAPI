import time
import json
import urllib
import requests
from flask import Flask
from flask_testing import TestCase

url = 'http://localhost:5001'

time.sleep(5)

class MyTest(TestCase):

    def create_app(self): 
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def test_server_is_up_and_running(self):
        response = (urllib.request.urlopen(url))
        self.assertEqual(response.code, 200)
    
    def test_server_correct(self):
        response = urllib.request.urlopen(url)
        source = str(response.read())
        self.assertEqual(source[2:][:-1], "Application Alive")
    
    def test_user_protocol(self):
        response = requests.get(url+'/api/v1.0/register/testnew').json()
        self.assertEqual(response["response"], "User Successfully Created")
        response = requests.get(url+'/api/v1.0/register/testnew/testexp').json()
        self.assertEqual(response["response"], "Experiment Successfully Created")
        response = requests.get(url+'/api/v1.0/remove/testnew/testexp').json()
        self.assertEqual(response["response"], "Experiment Successfully Removed")
        response = requests.get(url+'/api/v1.0/remove/testnew').json()
        self.assertEqual(response["response"], "User Successfully Removed")
