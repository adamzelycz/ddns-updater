#!/bin/bash

# You can choose from available providers in `providers/` folder
IP_PROVIDER="static" # Default "static"
DYN_NAME="custom-domain"
SECRET="custom-secret"
# You can use "%<ip>%" as placeholder for provided IP
UPDATE_URL="https://example.com/update?secret=${SECRET}&domain=${DYN_NAME}&addr=%<ip>%"
# Custom arguments for given ip provider (e.g. password to an administration or static IP for "static" provider)
CUSTOM_ARGS="1.2.3.4"

# 0 = OFF, 1 = ON
DEBUG=0

# EXECUTION
DIR=$(dirname $0)
python3 $DIR/ddns-updater.py "$IP_PROVIDER" "$UPDATE_URL" "$DEBUG" $CUSTOM_ARGS
