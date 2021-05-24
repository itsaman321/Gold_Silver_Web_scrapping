from bs4 import BeautifulSoup
import requests
import json

def rate():
	HTMLtext =  requests.get('https://m.moneycontrol.com/commodity/gold-price.html').text
	soup = BeautifulSoup(HTMLtext, 'lxml')
	dataBoard = soup.find_all('div',class_='databrd')
	title= ''
	value = ''
	dataGold = {}
	for i in range(0,4) :
		for j in dataBoard[i] :
			heading =  dataBoard[i].find_all('div',class_='datafl')
			for k in heading:
				title = k.find('p').text
				subhead = k.find('p',class_='datacol')
				value = k.find('strong').text
				dataGold[title] = value
			break
	jsondata = json.dumps(dataGold)
	print(jsondata)
	return jsondata

########################################

from flask import Flask, jsonify, request
app = Flask(__name__)

#commands to run flask app
# export FLASK_APP=hello.py
# flask run


# @app.route("/")
# def index():
# 	return "<p>Hello, World!</p>"

@app.route("/rate/", methods=['GET'])
def Rate():
	if request.method == 'GET':
		data = rate()
		return data

