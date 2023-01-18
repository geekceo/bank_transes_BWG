# Bank Transactions For BWG


[![Python 3.10](https://img.shields.io/badge/python-3.6+-green.svg)](https://www.python.org/downloads/release/python-360/)\
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)



### Getting Started

##### Firstly open setup folder via terminal
##### In this folder executing several files to setup project

```bash
$ bash docker-pg-run.sh #started docker container with postgresql db
$ bash docker-redis-run.sh #started docker container with redis
$ bash autocreate-tables-pg.sh #created tables with field to work with project via postgresql
```

##### Installing all requirements:
```bash
$ cd .. # to leave setup folder
$ pip3 install -r freeze.txt
```

##### Start the project:
```bash
$ uvicorn main:app --reload --port 8000
```


### Using

##### We have several API URN to make transactions and get/set user info:

```URL
/api/v1/getUser?uname=<username> - get info about user
/api/v1/setUser - with response body. To create new user
/api/v1/send - with response body. To exchange money between users
/api/v1/withdrawal - with response body. To withdrawal money from ATC
```

##### Examples on ```http://127.0.0.1/docs```

##### In withdrawal time task to withdrawal pushing in redis queue then picked up by worker to handling.

##### Transactions has several statuses, like 'New' when tranasction was started, 'Successed' when users balance greater or equal then amount sum, and 'Declined' when not enough money
