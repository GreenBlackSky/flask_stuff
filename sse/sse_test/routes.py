from flask import current_app as app, render_template
from flask_sse import sse


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send')
def stream():
    sse.publish({"message": "Hello"}, type='greeting')
    return "message sent"