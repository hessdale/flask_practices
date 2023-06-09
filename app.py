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
    username = request.json.get('username')
    password = request.json.get('password')
    premium = request.json.get('premium')
    results =  dbhelper.run_procedure('call new_client(?,?,?)'[username,password,premium])
    if(type(results) == list):
        return json.dumps(results,default=str)
    else:
        return 'sorry something went wrong'



app.run(debug=True)
