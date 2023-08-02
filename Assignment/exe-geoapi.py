# required libraries/modules
from urllib.request import urlopen
from urllib.parse import urlencode
import urllib.error
import json

# initializing a dictionary with a 'key' parameter
param = {'key' : 42}

# requesting for an address
url = input("Enter location: ")

# initializing the first half of the URL
serviceurl = "http://py4e-data.dr-chuck.net/json?"

# adding 'address' parameter to dictionary
param['address'] = url

# default address used for testing/debugging
if len(url) < 1:
    param['address'] = "University of Malaya"

# combining two halves to create the whole URL
url = serviceurl + urlencode(param)

# printing 'Retrieving' message to match sample execution
print(f"Retrieving {url}")

# opening the URL, reading it into 'jsn' and converting to str type
jsn = urlopen(url).read().decode()

# printing 'Retrieved' message to match sample execution
print(f"Retrieved {len(jsn)} characters")

# loading in str data and parsing it in JSON structure
data = json.loads(jsn)

# dumping the data to see its structure
# print(json.dumps(data, indent=2))

# locating 'place_id' and storing the value
placeID = data["results"][0]["place_id"]

# formatted output
print(f"Place id {placeID}")