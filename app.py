from flask import Flask, render_template, url_for, request
app = Flask(__name__, static_url_path='/static')


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

if __name__ == '__main__':
    app.run(host='0.0.0.0')
