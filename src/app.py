from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def Login():
    return render_template('Login.html')

@app.route('/vista1')
def vista1():
    return render_template('vista1.html')

@app.route('/SingUp')
def SignUp():
    return render_template('SignUp.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)