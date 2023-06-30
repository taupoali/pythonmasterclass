import requests

chimeUrl = input("Enter the chime webhook url: ")
chimeMessagePayload = {'Content': 'The new chime message'}
requests.post(url=chimeUrl, json=chimeMessagePayload)

