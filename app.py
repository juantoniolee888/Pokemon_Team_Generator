from flask import Flask, render_template, url_for
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def main():
    return render_template('base.html')


@app.route('/home')
def home():
	return render_template('home.html')
