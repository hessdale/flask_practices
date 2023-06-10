import json
import mariadb
import dbcreds
import dbhelper
from flask import Flask, request, make_response, jsonify
app = Flask(__name__)


@app.post('/api/client')
def new_client():
    error = dbhelper.check_endpoint_info(request.json,['username','password','premium'])
    if(error != None):
        return make_response(jsonify(error),400)
    username = request.json.get('username')
    password = request.json.get('password')
    premium = request.json.get('premium')
    results =  dbhelper.run_procedure('call new_client(?,?,?)'[username,password,premium])
    if(type(results) == list):
        return make_response(jsonify(results),200)
    else:
        return make_response('sorry something went wrong',500)

@app.patch('/api/client')
def update_password():
    valid_info = dbhelper.check_endpoint_info(request.json,['username','old_password','new_password'])
    if(type(valid_info) == str):
        return valid_info
    username = request.json.get('username')
    old_password = request.json.get('old_password')
    new_password = request.json.get('new_password')
    results =  dbhelper.run_procedure('call update_password(?,?,?)'[username,old_password,new_password])
    if(type(results) == list):
        return json.dumps(results,default=str)
    else:
        return 'sorry something went wrong'



@app.get('/api/client')
def get_all():
    try:
        results = dbhelper.run_procedure('call get_all()',[])
        if(type(results) == list):
            return json.dumps(results,default=str)
        else:
            return 'sorry something went wrong'
    except TypeError:
        print('invalid input type, try again.')
    except UnboundLocalError:
        print('coding error')
    except ValueError:
        print('value error, try again') 



app.run(debug=True)
