from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

#nam = input("Enter your name : ")
files_folder = "files"


@app.route("/")
def homePage():
    files = os.listdir(files_folder) 
    return render_template("index.html", files = files)

@app.route("/files/<fileNa>")
def downFile(fileNa):
    return send_from_directory(files_folder, fileNa)

if __name__ == "__main__":
    app.run(debug=True, host = "0.0.0.0")