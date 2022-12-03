# loadbalancer.py

import random

import requests
from flask import Flask, request, session, redirect
from requests.exceptions import ConnectionError

loadbalancer = Flask(__name__)

loadbalancer.secret_key = 'BAD_SECRET_KEY'

servers = ['localhost:8081', 'localhost:8082',
           'localhost:9081', 'localhost:9082']

nameServers = {
    'localhost:8081': 'server1',
    'localhost:8082': 'server2',
    'localhost:9081': 'server3',
    'localhost:9082': 'server4'
}


@loadbalancer.route('/')
def home():
    return "<p>Hello, World! Welcome to loadbalancer!</p>"


@loadbalancer.route('/first')
def firstPage():
    try:
        response = requests.get(f'http://{servers[0]}')
        return_string = response.content
        servers.append(servers.pop(0))
    except ConnectionError as e:
        print(e)
        return_string = f"{nameServers[servers[0]]} is down"
        servers.append(servers.pop(0))
        return redirect("/first")
    return return_string


if __name__ == '__main__':
    loadbalancer.run()
