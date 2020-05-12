from flask import current_app as app
from .views import Add_View


app.add_url_rule('/', view_func=Add_View.as_view('add_view'))