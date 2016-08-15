from flask_app import app
from flask import render_template, request
from .forms import CheckBoxForm

@app.route("/")
@app.route("/index")
def index():
	person = "Jacob"
	form_checkbox = CheckBoxForm(request.form)

	if request.method == 'POST' and form_getdata.validate():
		return redirect(url_for('showplots'))

	return render_template('index.html', 
		person = person,
		form_checkbox = form_checkbox)

@app.route("/showplots", methods=['GET', 'POST'])
def showplots():
	
	checkbox1 = request.args.get('checkbox') if request.args.get('checkbox') else 'n'
	checkbox2 = request.args.get('checkbox2') if request.args.get('checkbox2') else 'n'

	return render_template('showplots.html', 
		checkbox1 = checkbox1,
		checkbox2 = checkbox2)