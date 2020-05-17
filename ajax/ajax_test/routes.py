from flask import current_app as app, render_template, request, make_response, jsonify
from .logic import add_nums


@app.route('/', methods=['GET'])
def get_site():
    return render_template('add.html')


@app.route('/', methods=['POST'])
def process_request():
    values = request.get_json()
    val1, val2 = int(values['num1']), int(values['num2'])
    result = add_nums(val1, val2)
    return make_response(jsonify({'result': result}), 200)
