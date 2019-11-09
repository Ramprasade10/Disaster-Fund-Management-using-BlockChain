from flask import Flask, flash, redirect, render_template, request, session, abort,url_for,json
import os,donation
import matplotlib.pyplot as plt
import io,smtplib
import base64
import datetime
from passlib.hash import sha256_crypt
app = Flask(__name__)

@app.route('/donation',methods=["POST","GET"])
def donationFunction():
    if request.method == "POST":
        block = request.form.to_dict()
        block.pop('cvv')
        print(block)
        timestamp = datetime.datetime.now()
        block["timestamp"]=timestamp
        prev_hash="0"
        with open('static/donation.json') as myfile:
            print (list(myfile))
            print(len(list(myfile)))

            if len(list(myfile)):
                print(len(list(myfile)))
                prev_hash=list(myfile)[-1]["prev_hash"] 
        block["prev_hash"]=prev_hash
        block_hash=blockhash(block,prev_hash)
        block["block_hash"]=block_hash
        # block=message    
        file = open("static/donation.json", "a")
        file.write(str(block).replace("'", '"'))
        # file.write("\n")
        file.close()

        # print( 'Block<hash: {}, prev_hash: {}, messages: {}, time: {}>'.format(self.hash, self.prev_hash, len(self.messages), self.timestamp))
        return render_template('donation.html')
    return render_template('donation.html')

def blockhash(values,prev_hash=""):
    concat=""
    for x in values:
        concat+=str(x)
    concat+=prev_hash
    print(concat)
    return(sha256_crypt.hash(concat))

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