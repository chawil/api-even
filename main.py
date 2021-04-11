from flask import Flask

from core import is_even

app = Flask(__name__)


@app.route('/even/<number>', methods=['GET'])
def call_even(number: int):
    result = {"number": number}

    try:
        number = int(number)
    except ValueError:
        result["error"] = "A number is expected"
        return result, 500

    even = is_even(number)
    result["isEven"] = even
    return result


if __name__ == '__main__':
    app.run(host="0.0.0.0")
