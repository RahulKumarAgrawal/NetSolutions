import requests
URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)
print(r.content)
