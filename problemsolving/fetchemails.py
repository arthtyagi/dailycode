"""
Python application to fetch emails using the GITHUB api for Github users I provide the 
application with. Outputting them in a csv file. 
Why?
I input a csv file full of github usernames from DomeCode. The output --> email addresses.
How? 
Github API
c240de65e0ea9f6a754af45516c7be30883184bf
https://api.github.com/users/username/events/public
"""
"""
from github import Github
import requests
from pprint import pprint

# github username
username = "arthtyagi"
g = Github()
# url to request
url = f"https://api.github.com/users/{username}"
# make the request and return the json
user = g.get_user(username)
email = user.email

pprint(email)
"""


# Getting user input
import urllib.request
import json
import os
username = 'arthtyagi'
query_url = f"https://api.github.com/users/{username}/events/public"
r = urllib.request.urlopen(query_url).read()
data = json.loads(r)
cleandata = json.dumps(data)
finaldata = json.loads(cleandata)
print(finaldata['payload']['author']['email'])