import bus
import os
import sys

try:
    config_file = sys.argv[1]
except:
    print("Config file not specified")
    sys.exit(1)

settings = bus.open_settings(config_file)

data_path = settings['data']
html_path = settings['html']
output_html_filename = os.path.join(html_path, settings['output_html_file'])

# Get all departures
all_departures = []

stops = settings['stops']
num_deps = settings['num_departures']
for stop in stops:

    filename = os.path.join(data_path, stop['stop_id']) + ".latest.xml"
    departures = bus.convert_xmlfile_to_array(filename, stop['stop_name'])[:num_deps]

    all_departures.extend(departures)

page_template = """
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>%s</title>
  </head>
  <body>
    <h1>%s</h1>

    %s

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  </body>
</html>
"""

page_title = settings['output_html_title']

row_wrapper = "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td class='%s'>%s</td></tr>"

content = "<table class='table table-striped'>"
content = content + "<thead class='thead-dark'>"
content = content + "<tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr>" % ("Date", "Bus Stop", "Line", "Direction", "Scheduled Departure Time",  "Expected Departure Time")
content = content + "</thead>"

for d in all_departures:
    status = ""
    content = content + row_wrapper % (d['date'].astimezone().strftime("%Y-%m-%d"), d['bus_stop'], d['line_name'], d['direction'], d['scheduled_departure'].astimezone().strftime("%H:%M"), status, d['expected_departure'].astimezone().strftime("%H:%M"))

content = content + "</table>"

with open(output_html_filename, "w") as f:
    f.write(page_template % (page_title, page_title, content))
