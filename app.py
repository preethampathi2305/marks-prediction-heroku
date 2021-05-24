#loading model
import pickle
with open("model.pkl","rb") as f:
    lr=pickle.load(f)

from flask import Flask,render_template,redirect
from flask.globals import request
#__name__=__main__
app = Flask(__name__)

#sending arguments to html
#fav_artists=['dr.dre','kendrick lamar','ice cube','eminem']

@app.route('/') 
def hello():
    return render_template("home.html")

'''@app.route('/about')
def about():
    return "<h1> About us</h1>"'''

'''@app.route('/home')
def home():
    return redirect('/')'''
#getting input and returning output
@app.route('/submit',methods=['POST'])
def submitting():
    if request.method=='POST':
        num=request.form['exname']
    return render_template("home.html",marks=lr.predict([[num]]))



if __name__ == '__main__':
    app.debug=True # with this restarting server for every change is not needed it updates automatically
    app.run()