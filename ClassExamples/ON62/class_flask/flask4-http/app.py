from flask import *
app = Flask(__name__)

@app.route('/')
def abc():
	return  render_template('login.html')

@app.route('/login',methods = ['POST'])
def login():
	uname=request.form['uname']
	passwrd=request.form['pass']
	if uname== "ram" and passwrd== "sita":
		return "Welcome %s" %uname
	else : return "not valid user"

if __name__ == '__main__':
	app.run(debug = True)