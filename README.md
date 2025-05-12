# An improved Python NextBuses API Parser

This is a fork of the GitLab project below:

https://gitlab.developers.cam.ac.uk/cscs/nextbuses-api-python-parser

## What does this project do?

As per the original GitLab project, this is a Python parser for the NextBus API. It will send a request, do some magic behind the scene and output a human-readable HTML file with the next buses departures from the bus stops of your choice:

![immagine](https://github.com/user-attachments/assets/1242a7b3-fbe8-4e46-87f5-50c87919f625)

This should work for any bus authority within England, Wales and Scotland. I couldn't find the ATCO codes for bus stops in Northern Ireland, so unfortunately this is untested for NI.

## Summary of changes from the original project:

* In bus.py, made it so the expected and scheduled departure times are shown in the local timezone, rather than in UTC
* In config.json, added the parameter *"num_departures": 6,* so that you can choose how many arrivals to show for each bus stop. Of course, change 6 to whatever value you need.

## NextBus API

To be able to use this parser, you will need to request a NextBus API account. As of writing this, they provide 180,000 free hits every 6 months. To request access to the API, please follow this link:

https://www.travelinedata.org.uk/traveline-open-data/nextbuses-api/

Once you are given access to the API, you will be given a set of username and password which will be used by the API parser, and stored in *config.json* file.

## Bus stop ATCO code

The parser expects the ATCO code for the bus stop, while Google Maps shows the Naptan code for it. You can download the list of ATCO codes for your local transport authority from here:

https://beta-naptan.dft.gov.uk/download/la

I have included the bus stop code list for Cardiff in file *bus stop codes.xlsx*, but you will need to find the list for your local authority.

## Usage:
* Install python3 and pip
* Install pip requirements in requirements.txt (Flask, flask-cors, requests)
* *Optional:* set up python environment with python -m venv /path/to/your/environment
* Search bus stop in google maps and copy bus stop ID
* Open spreadsheet file from https://beta-naptan.dft.gov.uk/download/la, search for bus stop ID and copy matching ATCOcode
* Edit config.json with desired bus stop code and number of departures to show, plus your NextBus API username and password
* Run the parser and HTML page builder with:
  ```python sync.py config.json && python generate.py config.json```
* The resulting page will be in html/buses.html

## A word about Python <3.11 and datetime

According to https://note.nkmk.me/en/python-datetime-isoformat-fromisoformat/#isoformat-string-with-z Python versions below 3.11 do not handle the trailing Z from UTC timezone correctly. The best way to avoid issues would be installing Python version 3.11 and above, otherwise the code from this project would need modifying so that it transforms ```2023-04-01T05:00:30.001000Z``` into ```2023-04-01 05:00:30.001000+00:00```. This is beyond my Python abilities unfortunately.
A symptom of this happening would be an error message similar to the one below:

![immagine](https://github.com/user-attachments/assets/c1ce1221-7843-4221-9c2a-f73cc7645767)

The running python version can be checked by running the command ```python --version``` or ```/path/to/your/environment/python --version```

# *Original project description from GitLab:*

# Simple Python NextBuses API Parser and HTML Display

This project is a very simple implementation of the NextBuses API (https://www.travelinedata.org.uk/traveline-open-data/nextbuses-api/).

This allows you to easily get live bus timetable information from the UK's live bus data network.

TODO: Finish documentation beyond simple overview.

## Setup

```
pip3 install -r requirements.txt
```

### config.json

Copy config.json.template to config.json and update with your API credentials.

You can customize the data and html paths in here as well.

### Static Page Generator - Installation

There are two calls needed to generate a HTML display page:

```
python3 sync.py /path/to/config.json
python3 generate.py /path/to/config.json
```

sync.py should be schedule to download an updated set of files on a regualar schedule.
generate.py will operate from this cached data file.

