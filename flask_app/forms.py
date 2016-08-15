from flask_wtf import Form
from wtforms import BooleanField

class CheckBoxForm(Form):
	checkbox = BooleanField('checkbox', default=False)
	checkbox2 = BooleanField('checkbox2', default=True)