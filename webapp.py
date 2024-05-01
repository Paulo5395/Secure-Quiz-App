import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

app.secret_key=os.environ["SECRET_KEY"];

@app.route("/")
def render_main():
    return render_template("home.html")

@app.route("/startOver")
def startOver():
    session.clear() #clears variable values and creates a new session
    return redirect("/") # url_for('renderMain') could be replaced with '/'

@app.route("/p1")
def render_page1():
    page_number = 1

    return render_template("page1.html", page_number = page_number)

@app.route("/p2", methods=['GET','POST'])
def render_page2():
    session["answer1"]=request.form['optradio']

    page_number = 2

    return render_template("page2.html")

@app.route("/p3", methods=['GET','POST'])
def render_page3():
    page_number = 3

    session["answer2"]=request.form['optradio']

    return render_template("page3.html", page_number = page_number)
    
if __name__=="__main__":
    app.run(debug=True)