from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
from flask.helpers import url_for

app = Flask(__name__)

@app.route("/")
def start():
    return render_template("trivia.html")

@app.route("/correct")
def correct():
    return f"Correct!!!"

@app.route("/login", methods = ["POST"])
def login():  
    if request.form.get("answer"):
        user_answer = request.form.get("answer").lower()
    elif request.json:
        data = request.json
        user_answer = data["answer"]
    else:
        return redirect("/")
    
    if user_answer == "china":
        return redirect("/correct")
    else:
        return redirect("/")


if __name__ == "__main__":
    app.run(host="localhost", port=3000)
