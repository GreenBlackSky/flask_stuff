from flask import current_app as app, render_template


@app.route('/', methods=['GET'])
def home():
    return render_template(
        'index.html',
        title='Home',
        body="Home"
    )


@app.route('/about', methods=['GET'])
def about():
    return render_template(
        'index.html',
        title='About',
        body="About"
    )


@app.route('/etc', methods=['GET'])
def etc():
    return render_template(
        'index.html',
        title='Etc',
        body="Etc"
    )