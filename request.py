import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'qtitle': "htlml css", 'qbody':"Javscript"})

print(r)