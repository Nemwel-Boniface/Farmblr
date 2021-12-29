from django.shortcuts import render
from datetime import datetime
from base64 import b64encode

import requests
from requests.auth import HTTPBasicAuth
from decouple import config


# Create your views here.
def generate_timestamp():
    time = datetime.now()
    return time.strftime('%Y%m%d%H%M%S')


def generate_password():
    timestamp = generate_timestamp()
    data_to_encode = config('BUSINESS_SHORTCODE') + config('LIPA_NA_MPESA_ONLINE_PASSKEY') + timestamp
    encoded_string = b64encode(data_to_encode.encode())
    password = encoded_string.decode('utf-8')
    return password


def generate_access_token():
    api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    consumer_key = config('CONSUMER_KEY')
    consumer_secret = config('CONSUMER_SECRET')
    r = requests.get(api_url, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    json_response = r.json()
    access_token = json_response['access_token']
    return access_token
