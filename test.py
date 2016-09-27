
# get response json:
import requests
data = requests.post(url='http://localhost:8080/test', data={'id': 99})
print data.content
