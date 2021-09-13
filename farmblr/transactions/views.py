from django.shortcuts import render
from datetime import datetime
from base64 import b64encode

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
