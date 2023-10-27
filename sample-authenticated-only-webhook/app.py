import os
from flask import Flask, render_template, request
import flask
# import json
# import logging

# logging.basicConfig()
# logger=logging.getLogger(level=logging.DEBUG)
app = Flask(__name__)
print("test")

@app.route('/', methods=['GET'])
def index():
    print("test")
    results = ["test"]
    return results
    # request_json = request.get_json()
    # results = []
    # results.extend(["some text"])
    # service = os.environ.get('K_SERVICE', 'Unknown service')
    # revision = os.environ.get('K_REVISION', 'Unknown revision')

    # logger.info(f"service: {service}")
    # logger.info(f"revision: {revision}")

    # return flask.jsonify({"results":results})

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
