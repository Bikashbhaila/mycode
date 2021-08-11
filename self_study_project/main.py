import threading
from flask import Flask, render_template, request, redirect
import speech_recognition as sr

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    transcript = ""
    if request.method == "POST":
        print("Form data rec'd.")

        # check if input file exists
        if "file" not in request.files:
            return redirect(request.url)

        # if file exists get files data
        file = request.files["file"]
        # if file name is blank
        if file.filename == "":
            return redirect(request.url)
        
        # init recognizer
        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key = None)
            print(transcript)
        
    return render_template("index.html", transcript = transcript)



if __name__ == "__main__":
    app.run(debug = True, threaded = True)
