from flask import Flask, render_template, request
import checkmypass_inp

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template('index.html')

@app.route("/", methods = ['GET', 'POST'])
def check_password():
    user_password = request.form.get('user_password')
    print(user_password)
    count = -1
    risk = False
    safe = False
    count = int(checkmypass_inp.main(user_password))
    if count > 0: 
        risk = True
    else:
        safe = True
    return render_template('index.html', count = count, risk = risk, safe = safe)
