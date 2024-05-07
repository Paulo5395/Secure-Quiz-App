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
    if session.get("answer1") is not None: #check if there is already a value for "answer1"
            session.clear()
            return redirect("/")
    else:
        return render_template("page1.html")

@app.route("/p2", methods=['GET','POST'])
def render_page2():

    if request.method == "POST":
        if session.get("answer1") is not None: #check if there is already a value for "answer1"
            session.clear()
            return redirect("/")
        else:
            if 'optradio' in request.form:
                session["answer1"]=request.form['optradio']
            else:
                session["answer1"] = "None"
        
        return render_template("page2.html")
    else:
        session.clear()
        return redirect("/")
    
@app.route("/p3", methods=['GET','POST'])
def render_page3():

    if request.method == "POST":
        if session.get("answer2") is not None: #check if there is already a value for "answer1"
            session.clear()
            return redirect("/")
        else:
            if 'optradio' in request.form:
                session["answer2"]=request.form['optradio']
            else:
                session["answer2"] = "None"
        
        return render_template("page3.html")
    else:
        session.clear()
        return redirect("/")
    
@app.route("/p4", methods=['GET','POST'])
def render_page4():

    if request.method == "POST":
        if session.get("answer3") is not None: #check if there is already a value for "answer1"
            session.clear()
            return redirect("/")
        else:
            if 'optradio' in request.form:
                session["answer3"]=request.form['optradio']
            else:
                session["answer3"] = "None"
        
        return render_template("page4.html")
    else:
        session.clear()
        return redirect("/")

@app.route("/p5", methods=['GET','POST'])
def render_page5():

    if request.method == "POST":
        if session.get("answer4") is not None: #check if there is already a value for "answer2"
            session.clear()
            return redirect("/")
        else:
            if 'optradio' in request.form:
                session["answer4"]=request.form['optradio']
            else:
                session["answer4"] = "None"

            score = 0
            if session["answer1"] == "3":
                score += 1
            if session["answer2"] == "1":
                score += 1
            if session["answer3"] == "4":
                score += 1
            if session["answer4"] == "2":
                score += 1

            return render_template("page5.html", score = score)
    else:
        session.clear()
        return redirect("/")

if __name__=="__main__":
    app.run(debug=False)