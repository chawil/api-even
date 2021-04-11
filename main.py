from flask import Flask
from flask import request

import functions

app = Flask(__name__)


@app.route('/call/<function_name>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def call_function(function_name: str):
    function_to_call = getattr(functions, function_name)
    body = request.json
    return function_to_call(body)


app.run(host="0.0.0.0")