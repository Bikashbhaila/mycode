from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
from flask.helpers import make_response, url_for
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask import abort

app = Flask(__name__)

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["50 per hour", "500 per day"]
)

@app.route("/")
@limiter.exempt
def start():
    return render_template("trivia.html")

@app.route("/correct")
def correct():
    ans = request.cookies.get("flork")
    if ans == "china":
        return f"Correct!!!"
    else:
        return "You have yet to answer correctly"

@app.route("/login", methods = ["POST"])
@limiter.limit("3 per hour")
def login():
    # store user's answer in a cookie  
    if request.form.get("answer"):
        user_answer = request.form.get("answer")
        if user_answer == "china":
            # resp now contains the response we NORMALLY would have returned
            resp = make_response(redirect("/correct"))
            resp.set_cookie("flork", user_answer)
            return resp
    elif request.json:
        data = request.json
        user_answer = data["answer"]
        if user_answer == "china":
            return redirect("/correct")
    else:
        abort(400) 
    

if __name__ == "__main__":
    app.run(host="localhost", port=3000)
