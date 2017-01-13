import requests

url = 'https://api.darksky.net/forecast/[key]/[latitude],[longitude],[time]'
base_url = 'https://api.darksky.net/forecast'
key = '9e58d64a94172a32306acb0580d747e0'

lat = '40.640040'
lng = '-74.369018'
time = '1984-01-09T12:00:00'

url = base_url + key + '/' + str(lat) + ',' + str(lng) + ',' + str(time)

r = requests.get(url)


weather = r.json()
