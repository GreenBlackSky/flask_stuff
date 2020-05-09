from flask import Blueprint, render_template


bp = Blueprint(
    'main_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@bp.route('/', methods=['GET'])
def home():
    return render_template(
        'index.html',
        title='Home',
        body="Home"
    )


@bp.route('/about', methods=['GET'])
def about():
    return render_template(
        'index.html',
        title='About',
        body="About"
    )


@bp.route('/etc', methods=['GET'])
def etc():
    return render_template(
        'index.html',
        title='Etc',
        body="Etc"
    )