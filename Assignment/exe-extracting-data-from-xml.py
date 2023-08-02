# Importing necessary libraries/modules
from urllib.request import urlopen
import urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# Requesting user input for a URL
url = input("Enter location: ")

# Setting a default URL for testing/debugging if user input is empty
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_1856259.xml"

# Printing a message to indicate that data retrieval is in progress
print(f"Retrieving: {url}")

# Opening the URL, reading its contents, and converting it from bytes to a string
xml = urlopen(url).read().decode()

# Printing the number of characters retrieved
print(f"Retrieved {len(xml)} characters")

# Converting the XML string into a tree representation using ElementTree
tree = ET.fromstring(xml)

# Initializing variables to count and sum the contents of 'count' tags within 'comment' tags
sum = 0
count = 0

# Looping through each 'comment' tag within the 'comments' tag and counting the total number of comments and summing up their 'count' values
for comment in tree.findall('comments/comment'):
    count += 1
    sum += int(comment.find('count').text)

# Printing the count of comments and their total sum
print(f"Count: {count}\nSum: {sum}")