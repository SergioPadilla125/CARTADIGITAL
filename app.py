from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def home():
    with open("menu.json", encoding="utf-8") as f:
        menu = json.load(f)
    return render_template("index.html", menu=menu)

if __name__ == "__main__":
    app.run(debug=True)
