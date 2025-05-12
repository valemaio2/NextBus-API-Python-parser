# An improved Python NextBuses API Parser

This is a fork of the GitLab project below:

https://gitlab.developers.cam.ac.uk/cscs/nextbuses-api-python-parser

## Summary of changes from the original project:

* In bus.py, made it so the expected and scheduled departure times are shown in the local timezone, rather than in UTC

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

