from flask import Blueprint, render_template, redirect, url_for, session
from .forms import AddItemForm, RemoveItemForm


bp = Blueprint('main_bp', __name__, template_folder='templates')


@bp.route('/')
def dashboard():
    return render_template(
        'dashboard.html',
        title='Flask Redis tutorial.',
    )


@bp.route('/add_item', methods=('GET', 'POST'))
def add_item():
    form = AddItemForm()
    if form.validate_on_submit():
        session[form.key.data] = form.value.data
        return redirect(url_for('main_bp.dashboard'))
    return render_template(
        'add_item.html',
        title='Add item to redis session.',
        form=form
    )


@bp.route('/remove_item', methods=('GET', 'POST'))
def remove_item():
    form = RemoveItemForm()
    if form.validate_on_submit():
        session.pop(form.key.data)
        return redirect(url_for('main_bp.dashboard'))
    return render_template(
        'remove_item.html',
        title='Remove item from redis session.',
        form=form
    )

