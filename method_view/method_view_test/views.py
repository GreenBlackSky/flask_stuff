from flask import render_template, request
from flask.views import MethodView

from .forms import Add_Form
from .logic import add_nums


class Add_View(MethodView):
    def get(self):
        return render_template(
            "add.html",
            form=Add_Form(),
            result=0
        )

    def post(self):
        form = Add_Form(request.form)
        if form.validate():
            result = add_nums(int(form.num1.data), int(form.num2.data))
        else:
            result = 'Not valid values'
        return render_template(
            "add.html",
            form=Add_Form(),
            result=result
        )
