from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder="templates")

features = [
    "mean radius",
    "mean texture",
    "mean perimeter",
    "mean area",
    "mean smoothness",
    "mean compactness"
]

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template(
        "index.html",
        result=None,
        features=features,
        entered_values={}
    )

if __name__ == "__main__":
    app.run(debug=True)