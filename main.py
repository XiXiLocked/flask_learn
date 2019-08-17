from flask import Flask
from flask import session, redirect, url_for, flash

from flask import render_template
from flask_bootstrap import Bootstrap

from flask_moment import Moment
from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY']='0101010101010101'
booststrap = Bootstrap(app)
moment = Moment(app)

class NameForm(FlaskForm):
    name = StringField("What's your name?",validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/',methods = ['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        oname = session.get('name')
        if oname is not None and oname != form.name.data:
            flash('Looks like you have changed your name')
        session['name']= form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', current_time = datetime.utcnow(), form = form, name = session.get('name'))

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500

@app.route('/der')
def der():
    return render_template('der.html')
