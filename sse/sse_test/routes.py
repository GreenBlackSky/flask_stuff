from flask import current_app as app, render_template, request, make_response, jsonify
from flask_sse import sse


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/input', methods=['POST'])
def input():
    message = request.get_json()['message']
    sse.publish({'message': message}, type='message')
    return make_response(jsonify({"status": "success"}), 200)
