from flask import Flask, flash, redirect, render_template, request, session, abort,url_for
import os,jsonlines
import matplotlib.pyplot as plt
import io,smtplib
import base64,json
import datetime,time
from passlib.hash import sha256_crypt
import warnings
warnings.filterwarnings(action="ignore")
import pandas as pd
from sklearn.model_selection import train_test_split  #uses only some part of data & is time saving
from sklearn.linear_model import  LogisticRegression


app = Flask(__name__)

@app.route('/donation',methods=["POST","GET"])
def donationFunction():
    if request.method == "POST":
        block = request.form.to_dict()
        block.pop('cvv')
        print(block)
        timestamp = time.time()
        block["timestamp"]=timestamp
        prev_hash="0"
        with jsonlines.open('static/donation.jsonl') as reader:
            for obj in reader:
                # print(type(obj))
                if obj:
                    print((obj)["block_hash"])
                    prev_hash=(obj)["block_hash"]
        block["prev_hash"]=prev_hash
        block_hash=blockhash(block,prev_hash)
        block["block_hash"]=block_hash
        with jsonlines.open('static/donation.jsonl', mode='a') as writer:
            writer.write(block)
            dis={"Olympics":1,"Common wealth":2}
            item={"food":1,"cloth":2,"water":3,"water":4}

        nn_pred(block["amount"],dis[block["disaster"]],item[block["item"]])
        sendmail("")
        # print( 'Block<hash: {}, prev_hash: {}, messages: {}, time: {}>'.format(self.hash, self.prev_hash, len(self.messages), self.timestamp))
        return render_template('donation.html')
    return render_template('donation.html')


@app.route('/viewDonation')
def viewDonationFunction():
    donations= []
    with jsonlines.open('static/donation.jsonl') as reader:
        print(reader)
        for obj in reader:
            # print(type(obj))
            donations.append(obj)
    # print(donations)
    return render_template('viewDonation.html',donations=donations)

@app.route('/citizen_rescue')
def citizen_rescue():
    with jsonlines.open('static/donation.jsonl') as reader:
        print(reader)
        for obj in reader:
            # print(type(obj))
            if obj:
                print((obj)["block_hash"])
                prev_hash=(obj)["block_hash"]
    
    # block=
    with jsonlines.open('static/citizen.jsonl', mode='a') as writer:
        writer.write(block)
    # print(donations)
    return render_template('citizen_rescue.html',donations=donations)


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        if request.form["username"] == 'admin' and request.form["password"] == "admin":
            session['user'] = 'admin'
            return redirect(url_for('govtView'))
        return render_template('login.html')
    return render_template('login.html')


@app.route('/logout', methods=["POST", "GET"])
def logout():
    session.pop('user',None)
    return redirect(url_for('login'))


@app.route('/govtView',methods=["POST","GET"])
def govtView():
    if session['user'] == 'admin':
        return render_template('govtView.html')
    else:
        message= "Wrong credentials"
        return render_template('login.html',message=message)



@app.route('/assignFunds', methods=["POST", "GET"])
def assignFunds():
    return render_template('govtView.html')

def predict_and_plot():
    return render_template('govtView.html')
    filename= 'data.csv'
    hnames= ['deathtoll','mag','req_fund']
    dataframe=pd.read_csv(filename,names=hnames)
    array= dataframe.values
    dataframe.plot(x ='deathtoll', y='req_fund', kind = 'line')
    #plt.show()

    #separate array into input and output components
    x=array[:,0:2]  #input column
    y=array[:,2]     #output column

    test_data_size=0.1 #hides 33% data from machine so that it will be used for testing
    #seed=4
    x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=test_data_size) #,random_state=seed)

    model= LogisticRegression()
    model.fit(x_train,y_train)
    r=model.predict([[2089,8.9]])
    print(r)
    ra1=[2089]
    \
    #ra.plot(x ='deathtoll', y='req_fund', kind = 'dotted-line',marker='d')
    plt.plot(ra1,r,marker='o',markerfacecolor='red',markersize=7,
            linestyle='dashed',color='blue')
    plt.show()
@app.route('/displayCreds', methods=["POST", "GET"])
def displayCreds():
    return render_template('govtView.html')


@app.route('/updateEvent', methods=["POST", "GET"])
def updateEvent():
    disasters = []
    with jsonlines.open('static/disaster.jsonl') as reader:
        print(reader)
        for obj in reader:
            # print(type(obj))
    # print(donations)
            disasters.append(obj)
    return render_template('updateEvent.html',disasters=disasters)


@app.route('/expenditure', methods=["POST", "GET"])
def expenditure():
    return render_template('expenditure.html')

def blockhash(values,prev_hash=""):
    concat=""
    for x in values:
        concat+=str(x)
    concat+=prev_hash
    print(concat)
    return(sha256_crypt.hash(concat))
def predict_and_plot():
    return render_template('govtView.html')
    filename= 'data.csv'
    hnames= ['deathtoll','mag','req_fund']
    dataframe=pd.read_csv(filename,names=hnames)
    array= dataframe.values
    dataframe.plot(x ='deathtoll', y='req_fund', kind = 'line')
    #plt.show()

    #separate array into input and output components
    x=array[:,0:2]  #input column
    y=array[:,2]     #output column

    test_data_size=0.1 #hides 33% data from machine so that it will be used for testing
    #seed=4
    x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=test_data_size) #,random_state=seed)

    model= LogisticRegression()
    model.fit(x_train,y_train)
    r=model.predict([[2089,8.9]])
    print(r)
    ra1=[2089]
    #ra.plot(x ='deathtoll', y='req_fund', kind = 'dotted-line',marker='d')
    plt.plot(ra1,r,marker='o',markerfacecolor='red',markersize=7,
            linestyle='dashed',color='blue')
    plt.show()
def pred():
    filename= 'data.csv'
    hnames= ['deathtoll','mag','req_fund']
    dataframe=pd.read_csv(filename,names=hnames)
    array= dataframe.values

    #separate array into input and output components
    x=array[:,0:2]  #input column
    y=array[:,2]     #output column

    test_data_size=0.1 #hides 33% data from machine so that it will be used for testing
    #seed=4
    x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=test_data_size) #,random_state=seed)

    model= LogisticRegression()
    model.fit(x_train,y_train)
    r=model.predict([[160,3.7]])
    print(r)

# sendmail("portalnie@gmail.com","Data Integrity Lost","","")
def sendmail(to,mail_subject,mail_body,mail_attach,filename=""):
    fromaddr = "portalnie@gmail.com"
    toaddr = to
    # instance of MIMEMultipart 
    msg = MIMEMultipart() 
    # storing the senders email address   
    msg['From'] = fromaddr 
    # storing the receivers email address  
    msg['To'] = toaddr 
    # storing the subject  
    msg['Subject'] = mail_subject
    # string to store the body of the mail 
    body = mail_body
    # attach the body with the msg instance 
    # open the file to be sent  
    attachment = mail_attach
    noattach=1 if attachment else 0
    if attachment:
    # To change the payload into encoded form 
        msg.attach(MIMEText(body, 'plain')) 
        p = MIMEBase('application', 'octet-stream') 
        p.set_payload((attachment).read()) 
    # encode into base64 
        encoders.encode_base64(p) 

        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    # attach the instance 'p' to instance 'msg' 
        msg.attach(p) 
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    # start TLS for security 
    s.starttls() 
    # Authentication, provide account password here
    s.login(fromaddr, "portalniewelcome") 
    # Converts the Multipart msg into a string 
    text = msg.as_string() if noattach else 'Subject: {}\n\n{}'.format(mail_subject,mail_body)
    #if noattach else mail_body
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 
    # terminating the session 
    s.quit() 


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
