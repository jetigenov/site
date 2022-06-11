import json
import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_data():
    url = 'http://127.0.0.1:5000/data'  # можно добавить в окружение
    response = requests.get(url, verify=False)
    response = json.loads(response.text)['list']
    return render_template("index.html", value=response)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
