# IoT_Comm_Design_Fibo

## Introduction
Mixture of Communication Pattern: a system with a simple ﬁbonacci caculator capability and a logging feature as following:

![圖片](https://user-images.githubusercontent.com/16716620/144636360-3ca74bad-d408-4af0-ab5b-9d695933ecfc.png)


## Environment
```
- Linux thinkpad-t480 5.4.0-81-generic #91~18.04.1-Ubuntu SMP Fri Jul 23 13:36:29 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
- Docker version 20.10.8, build 3967b7d
- Python 3.7.1
```

## How to run
- Install project dependencies
```bash
$ pip3 install -r requirements.txt
```
- Migrate database tables
```bash
$ cd mysite/
$ python3 manage.py migrate
```
- Run the backend server
```bash
$ python3 manage.py runserver 0.0.0.0:8000
```

## Using `curl` to perform client request
```bash
$ curl http://localhost:8000/rest/tutorial
$ curl -X POST -d '{"order": 10}' http://localhost:8000/rest/fibonacci
$ curl http://localhost:8000/rest/logs
```

