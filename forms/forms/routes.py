from flask import url_for, redirect, render_template
from flask import current_app as app
from .forms import ContactForm


@app.route('/', methods=('GET', 'POST'))
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        return 'success!'
    return render_template('contact.html', form=form)
