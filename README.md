# Project Setup
## Install dependency and setup virtualenv
    pip install virtualenv
    
    cd <kahadata>
    virtualenv pyenv
    pyenv/bin/pip install -r requirements.txt 


## Setup db

    APP_SETTINGS="config.DevelopmentConfig" KAYA_SECRET='xx' KAHA_DSN='sqlite:///kaha.sdb' pyenv/bin/python manager.py db  upgrade


# Importing data
## Get Data

   curl <kaha-api-data>  > data.json


## Import the data in sqlite
    
    APP_SETTINGS="config.DevelopmentConfig" KAYA_SECRET='xx' KAHA_DSN='sqlite:///kaha.sdb' pyenv/bin/python dataimport.py


## Running the api server

    APP_SETTINGS="config.DevelopmentConfig" KAYA_SECRET='xx' KAHA_DSN='sqlite:///kaha.sdb' pyenv/bin/python app.py


# Using the API 

    <server>/resources/<district>
*NOTE* Return list of resources for matching district.


    <server>/resources/<district>?for=need
*NOTE* Return list of resources matching the district and of type 'Need'

    <server>/resources/<district>/<resource_type>
    <server>/resources/<district>/<resource_type>,<resource_type>
*NOTE* Return list of resources for matching district and resource types

    <server>/resource/<uuid>
*NOTE* Return a resource for the uuid

More to come..
