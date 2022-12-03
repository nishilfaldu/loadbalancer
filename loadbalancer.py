# loadbalancer.py

import random

import requests
from flask import Flask, request

loadbalancer = Flask(__name__)

servers = ['localhost:8081', 'localhost:8082',
           'localhost:9081', 'localhost:9082']

# @loadbalancer.route('/')
# def router():
#     host_header = request.headers['Host']
#     if host_header == 'www.mango.com':
#         response = requests.get(f'http://{random.choice(MANGO_BACKENDS)}')
#         return response.content, response.status_code
#     elif host_header == 'www.apple.com':
#         response = requests.get(f'http://{random.choice(APPLE_BACKENDS)}')
#         return response.content, response.status_code
#     else:
#         return 'Not Found', 404


# @loadbalancer.route('/mango')
# def mango_path():
#     response = requests.get(f'http://{random.choice(MANGO_BACKENDS)}')
#     return response.content, response.status_code


# @loadbalancer.route('/apple')
# def apple_path():
#     response = requests.get(f'http://{random.choice(APPLE_BACKENDS)}')
#     return response.content, response.status_code


@loadbalancer.route('/')
def home():
    return "<p>Hello, World! Welcome to loadbalancer!</p>"


@loadbalancer.route('/first')
def firstPage():
    request_headers = request.headers
    # print(request.headers['Host'])
    response = requests.get(f'http://{random.choice(servers)}')
    print(response.content)
    return "<p>this is first page</p>"


if __name__ == '__main__':
    loadbalancer.run()
