# Simple program to auto update DNS information

## When would you need this utility?
- Your public ip address is dynamic
- You want to use self hosted DDNS service (such as
[dprandzioch/docker-ddns](https://github.com/dprandzioch/docker-ddns))
- Your router is worth a piece of shit
    - There is no functionality for custom DDNS update url
    - CLI interface does not provide information about public IP address
    - The only possible way is through crappy web management

If you meet all these conditions above, congratulations!
You are the second one on this planet who could appreciate this simple program.

## Available IP providers
- Static (pre-defined IP address)
- Router TP-LINK Archer MR200

## Basic info

- Author: Adam Zelycz
- Created: 2019-06-17

## Requirements

- Docker  
or
- Linux (tested on Debian)
- Python 3
- Make

## Installation (if you do not use Docker)

`make install`

## Usage

1. Open [ddns-updater.sh](ddns-updater.py) and set your router model (ip provider). You can choose
from available types in [model](providers) folder
2. Also do not forget to fill _update url_ with custom variables (secret, domain etc.) and
possible custom configuration of selected provider
3. Make sure that script has correct permissions to be
executed - `chmod +x ddns-udater.sh`
4. Run [ddns-updater.sh](ddns-updater.py)
5. Configure your cron to run this script repetetively.
You can be inspired by [crontab.docker.txt](crontab.docker.txt).

## Debugging

[Configuration](ddns-updater.sh) allows you to turn on generating debug information
during running the script. log files and screenshots are located in [log](log) folder. 
