from flask import url_for, redirect, render_template
from flask import current_app as app, request
from .forms import ContactForm


@app.route('/', methods=('GET', 'POST'))
def contact():
    form = ContactForm(request.form)
    if request.method == 'POST' and form.validate():
        return 'success!'
    return render_template('contact.html', form=form)
