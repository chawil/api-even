from flask import Flask

from core import is_even
from core import is_odd

app = Flask(__name__)


@app.route('/even/<input>', methods=['GET'])
def call_even(input: int):
    result = {"input": input}

    try:
        number = int(input)
    except ValueError:
        result["error"] = "A number is expected"
        return result, 500

    even = is_even(number)
    result["isEven"] = even
    return result

@app.route('/odd/<input>', methods=['GET'])
def call_odd(input: int):
    result = {"input":input}
    try :
        number = int(input)
    except ValueError:
        result["error"] = "A number is expected"
        return result, 500
    odd = is_odd(number)
    result["isOdd"] = odd
    return result


if __name__ == '__main__':
    app.run(host="0.0.0.0")
