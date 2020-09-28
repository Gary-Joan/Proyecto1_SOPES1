#! /bin/bash

mongoimport --host mongodb --db dbsa --collection listado --type json --file /mongo-seed/census.json --jsonArray