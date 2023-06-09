import json
import mariadb
import dbcreds
import dbhelper
from flask import Flask, request
app = Flask(__name__)

@app.post('/api/new_client')
def new_client():
    valid_info = dbhelper.check_endpoint_info(request.json,['username','password','premium'])
    if(type(valid_info) == str):
        return valid_info




app.run(debug=True)
