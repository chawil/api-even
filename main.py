from flask import Flask

import functions

app = Flask(__name__)


@app.route('/even/<number>', methods=['GET'])
def call_even(number: int):
    result = {"number": number}

    try:
        number = int(number)
    except ValueError:
        result["error"] = "A number is expected"
        return result, 500

    is_even = functions.is_even(number)
    result["isEven"] = is_even
    return result


app.run(host="0.0.0.0")
