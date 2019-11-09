# -*- coding: utf-8 -*-
from flask import Flask, flash, redirect, render_template, request, session, abort,url_for,json
import os,simple_chain

app = Flask(__name__)

@app.route('/',methods=["post","get"])
@app.route('/login',methods=["post","get"])
def login():
    error=None
    if request.method == "POST":
        if request.form['username']!="1234" or request.form['password'] !="1234":
            error="Invalid credentials.Please try again"
        else:
            return redirect(url_for('vote'))

    return render_template('login.html',error=error)

@app.route('/vote',methods=['POST','get'])
def vote():
    if request.method == "POST":
        votes=request.form['vote']
        simple_chain.doit(votes)
    else:
        return render_template('vote.html')
    return redirect('thanks')

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')


@app.route('/lol')
def showjson():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT,"static", "blockchain.json")
    data = json.load(open(json_url))
    return render_template('showjson.jade', data=data)


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='127.0.0.1', port=8000)
