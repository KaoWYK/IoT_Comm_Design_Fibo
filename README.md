# IoT_Comm_Design_Fibo

## Introduction
Mixture of Communication Pattern: a system with a simple ﬁbonacci caculator capability and a logging feature as following:

![圖片](https://user-images.githubusercontent.com/16716620/144636360-3ca74bad-d408-4af0-ab5b-9d695933ecfc.png)


## Environment
- For Eclispse Mosquitto MQTT Broker
```
- Linux thinkpad-t480 5.4.0-81-generic #91~18.04.1-Ubuntu SMP Fri Jul 23 13:36:29 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
- Docker version 20.10.8, build 3967b7d
- Python 3.7.1
```

## How to run
#### Install project dependencies
- Install protobuf compiler
```bash
$ sudo apt-get install protobuf-compiler
```
- Install buildtools
```bash
$ sudo apt-get install build-essential make
```
- Install packages
```bash
$ pip3 install -r requirements.txt
```
#### Compile protobuf schema to python wrapper
```bash
$ cd src/fibonacci/gRPC && make
$ cd ../../logs/gRPC && make
```
#### Run the eclipse mosquitto docker container
```bash
$ cd MQTT && sudo docker run -d -it -p 1883:1883 -v $(pwd)/mosquitto.conf:/mosquitto/config/mosquitto.conf eclipse-mosquitto
```
#### Run the backend server
- Django-rest interface (at port:8000)
```bash
$ cd ../../..
# under /src directory
$ python3 manage.py migrate
$ python3 manage.py runserver 0.0.0.0:8000
```
- gRPC service for fibonacci calculation (at port:8080)
```bash
# Open another terminal
$ cd src/fibonacci/gRPC
$ python3 server.py --ip 0.0.0.0 --port 8080
```
- gRPC service for history logging (at port:8800)
```bash
# Open another terminal
$ cd src/logs/gRPC
$ python3 server.py --ip 0.0.0.0 --port 8800
```

## Testing
- Open another terminal
####  Using `curl` to perform client request
- Calculate fibonacci: enter # for order
```bash
# curl -X POST -d '{"order": <number>}' http://localhost:8000/rest/fibonacci
$ curl -X POST -d '{"order": 10}' http://localhost:8000/rest/fibonacci
# Will receive {"order":10,"answer":55}
$ curl -X POST -d '{"order": 5}' http://localhost:8000/rest/fibonacci
# Will receive {"order":5,"answer":5}
```
- Get history input
```bash
$ curl http://localhost:8000/rest/logs
# Will receive {"history":[10,5]}
```

