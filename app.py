from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool

engine = create_engine(
    "sqlite://", 
    connect_args={"check_same_thread": False}, 
    poolclass=StaticPool
)



app = Flask(__name__, static_url_path='/static')
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///registration.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import *
with app.app_context():
    db.create_all()

@app.route('/')
def main():
    return render_template('login.html')

@app.route('/home', methods = ['POST', 'GET'])
def home():
	if request.method == 'POST':
		form_data = request.form
		username = form_data.get("username")
		password = form_data.get("password")
		return render_template('home.html',username=username)

@app.route('/<username>/home')
def user_home(username):
		return render_template('home.html',username=username)



@app.route('/new_account')
def new_account():
	return render_template('create_account.html')


@app.route('/check', methods = ['POST', 'GET'])
def check():
	if request.method == 'POST':
		username = request.form.get("username")
		password = request.form.get("password")
		trainer = request.form.get("trainer")
		
		in_use = db.session.query(User).filter_by(username=username).first()
		if in_use is not None:
			print(in_use.username)
			return 'fail'
		new_user = User(username=username, password=password, trainer=trainer)
		db.session.add(new_user)
		db.session.commit()
		
		return render_template('login.html')





if __name__ == '__main__':
    app.run(host='0.0.0.0')
