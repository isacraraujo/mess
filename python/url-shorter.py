#pip install bitly_api

import bitly_api
API_USER = "username"
API_KEY  = "API_Key"

bitly    = bitly_api.Connection(API_USER, API_KEY)
response = bitly.shorten("https://copyassignment.com/")
print(response)