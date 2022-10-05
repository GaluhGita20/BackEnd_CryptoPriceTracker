import requests
import time
import webbrowser
from flask import Flask,jsonify, render_template, request
import json


app = Flask(__name__)


def get_price():
  url= "http://api.coincap.io/v2/assets?"
  response = requests.request("GET", url, headers={}, data={})
  if response.status_code ==200:
    for x in range (0,5):
      with open("result.json", "r+") as jsonFile:
        data = json.load(jsonFile)
        temp = data

        # inisialisasi data update
        data["data"][x]['name'] = data_hasil = response.json()['data'][x]['name']
        data["data"][x]['symbol'] = data_hasil = response.json()['data'][x]['symbol']
        data["data"][x]['supply'] = data_hasil = response.json()['data'][x]['supply']
        data["data"][x]['priceUsd'] = data_hasil = response.json()['data'][x]['priceUsd']
        data["data"][x]['marketCapUsd'] = data_hasil = response.json()['data'][x]['marketCapUsd']

        jsonFile.seek(0)  # rewind
        json.dump(data, jsonFile)
        jsonFile.truncate()
      print(data_hasil)
    return temp
  else:
    print("Error")
    return 0

price = get_price()
@app.route('/crypto_price', methods=['GET'])
def stuff():
  global price
  price= get_price()
  return jsonify(result=price)

if __name__ == '__main__':
  app.run(debug=True, host='localhost', port=4444)