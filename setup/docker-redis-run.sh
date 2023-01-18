#!/bin/bash

docker pull redis

docker run --name redis-server -d redis