from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/api')
def testing():
    return {'message': "halo success"}