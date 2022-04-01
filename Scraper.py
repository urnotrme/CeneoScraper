import requests

url="https://www.ceneo.pl/113706425#tab=reviews"
response=requests.get(url)
print(response.text)

