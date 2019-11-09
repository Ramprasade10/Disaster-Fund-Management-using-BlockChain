# -*- coding: utf-8 -*-
from flask import Flask, flash, redirect, render_template, request, session, abort,url_for,json
import os,donation
import matplotlib.pyplot as plt
import io
import base64
import time
app = Flask(__name__)



@app.route('/donation',methods=["POST","GET"])
def donationFunction():
    if request.method == "POST":
        data = request.form.to_dict()
        data.pop('cvv')
        print(data)
        timestamp = time.time()
        
        
#		jsonstring=dumps(dicts)
#		print(jsonstring)
        file = open("static/donation.json", "a")
        file.write(str(data).replace("'", '"'))
        file.close()

        # print( 'Block<hash: {}, prev_hash: {}, messages: {}, time: {}>'.format(self.hash, self.prev_hash, len(self.messages), self.timestamp))
        return render_template('donation.html')
    return render_template('donation.html')
    #index blockchain
    #     index = int(input("Provide the index: "))
    #     if len(chain.chain) > 0:
    #         try:
    #             print(chain.chain[index])
    #         except:
    #             print("An issue occurred")
    # #show blockchain use in visualizaing rhe blockchain
    #     for b in chain.chain:
    #         print(b)
    #         print("----------------")
    #         # elif decide == "5":
    #     if chain.validate():
    #         print("Integrity validated.")
    #         return render_template('thanks.html')

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
