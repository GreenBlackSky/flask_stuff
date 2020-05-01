from flask import current_app as app
from flask import render_template


@app.route('/')
def home():
    return render_template(
        'home.html',
        title='Jinja test page',
        description='Just learning flask+jinja, nothing to see here.'
    )