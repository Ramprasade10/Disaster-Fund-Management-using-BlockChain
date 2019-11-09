# -*- coding: utf-8 -*-
from flask import Flask, flash, redirect, render_template, request, session, abort,url_for,json
import os,citizen
import matplotlib.pyplot as plt
import io
import base64
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


 
def build_graph(x_coordinates, y_coordinates):
    img = io.BytesIO()
    plt.plot(x_coordinates, y_coordinates)
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return 'data:image/png;base64,{}'.format(graph_url)
 
@app.route('/graphs')
def graphs():
    #These coordinates could be stored in DB
    x1 = [0, 1, 2, 3, 4]
    y1 = [10, 30, 40, 5, 50]
    x2 = [0, 1, 2, 3, 4]
    y2 = [50, 30, 20, 10, 50]
    x3 = [0, 1, 2, 3, 4]
    y3 = [0, 30, 10, 5, 30]
 
    graph1_url = build_graph(x1,y1);
    graph2_url = build_graph(x2,y2);
    graph3_url = build_graph(x3,y3);
 
    return render_template('graphs.html',
    graph1=graph1_url,
    graph2=graph2_url,
    graph3=graph3_url)
 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=5555)
