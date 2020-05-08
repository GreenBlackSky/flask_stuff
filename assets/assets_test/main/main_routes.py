from flask import Blueprint, render_template


main_bp = Blueprint(
    'main_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@main_bp.route('/', methods=['GET'])
def home():
    return render_template(
        'index.html',
        title='Home',
        template='home-static main',
        body="Home"
    )


@main_bp.route('/about', methods=['GET'])
def about():
    return render_template(
        'index.html',
        title='About',
        template='about-static main',
        body="About"
    )


@main_bp.route('/etc', methods=['GET'])
def etc():
    return render_template(
        'index.html',
        title='Etc | Flask-Blueprint Tutorial',
        template='etc-static main',
        body="Etc"
    )