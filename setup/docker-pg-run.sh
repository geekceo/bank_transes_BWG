#!/bin/bash

docker run --name pg -p 6233:5432 -e POSTGRES_PASSWORD=pgidgaf -d postgres