from flask import Flask
from flask import *
import requests
import amazon_api

app = Flask(__name__)


@app.route('/get')
def send_data():
    amazon = amazon_api.AmazonApi()
    details = amazon.read_file()
    img_link = amazon.get_link()
    data = {"data": details,"links":img_link}
    json_dump = json.dumps(data)
    return json_dump


if __name__ == '__main__':
    app.run(port=7777)