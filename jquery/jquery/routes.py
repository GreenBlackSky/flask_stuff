from flask import current_app as app, render_template, request


@app.route('/', methods=['GET'])
def get_site():
    return render_template('add.html')


@app.route('/', methods=['POST'])
def process_request():
    pass