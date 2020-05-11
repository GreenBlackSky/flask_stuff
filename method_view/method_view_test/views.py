from flask import render_template
from flask.views import MethodView

from forms import Add_Form
from logic import add_nums


class Add_View(MethodView):
    def get(self):
        form = Add_Form()
        return render_template("add.html", form=form)

    def post(self):
        pass