from app import app,db
from flask_admin import Admin
from app.models import Flight,Passenger
from wtforms.widgets import TextArea
from flask_login import current_user
from wtforms import TextAreaField
from flask_admin.contrib.sqla import ModelView

admin=Admin(app=app, name="Adminstrator",template_mode='bootstrap4')
admin.add_view(ModelView(Flight,db.session))
admin.add_view(ModelView(Passenger,db.session))



