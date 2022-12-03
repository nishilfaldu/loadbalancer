# loadbalancer.py

import random

import requests
from flask import Flask, request, session

loadbalancer = Flask(__name__)

loadbalancer.secret_key = 'BAD_SECRET_KEY'

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
    response = requests.get(f'http://{servers[0]}')
    if (response.status_code != 200):
        return_string = "server 1 is down"
    else:
        return_string = response.content
        servers.append(servers.pop(0))

    print(return_string)
    return return_string


if __name__ == '__main__':
    loadbalancer.run()
