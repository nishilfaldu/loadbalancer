# loadbalancer


# To test the load balancer, follow the steps:

## Clone the repository
```
git clone https://github.com/nishilfaldu/loadbalancer.git
```

## Create and activate virtual environment
```
python3 -m venv env
source env/bin/activate
```

## Installing dependencies
```
pip install -r requirements.txt
```

## Create an image for spinning multiple servers
```
docker build -t server .
```

## Starting docker containers
```
docker-compose up -d
```

## Starting the web application which will make requests to servers
```
python loadbalancer.py
CMD+Click 127.0.0.1 -> to see the web page
navigate to 127.0.0.1/first
```
