from flask import Flask
from flask_restful import Api
import os
from services import decode
import logging


logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
LOGGER = logging.getLogger(__name__)
LOGGER.root.setLevel(logging.NOTSET)


APP_HOST = os.environ.get('APP_HOST', '0.0.0.0')
APP_PORT = int(os.environ.get('APP_PORT', '5000'))
APP_RELOAD = os.environ.get('APP_RELOAD', True)
AUTH_AD_HOST = os.environ.get('AUTH_AD_HOST')
AUTH_AD_PORT = os.environ.get('AUTH_AD_PORT')
AUTH_AD_DOMAIN = os.environ.get('AUTH_AD_DOMAIN')
AUTH_AD_DN = os.environ.get('AUTH_AD_DN')
AUTH_AD_USERNAME = os.environ.get('AUTH_AD_USERNAME')
AUTH_AD_PASSWORD = decode(os.environ.get('AUTH_AD_PASSWORD'))


app = Flask(__name__)
api = Api(app)


@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', "*")
    response.headers.add('Access-Control-Allow-Methods', 'DELETE')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type, Authorization, X-Access-Token, data')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Content-Type', 'application/json')
    return response
