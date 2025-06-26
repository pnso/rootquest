from flask import Flask, render_template, request, redirect, url_for
import json
import subprocess
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/labs")
def labs():
    with open("labs/lab_config.json") as f:
        lab_data = json.load(f)
    return render_template("labs.html", labs=lab_data["labs"])

@app.route("/run-lab/<lab_id>", methods=["POST"])
def run_lab(lab_id):
    try:
        subprocess.Popen(["docker", "run", "-it", "--rm", lab_id])
        print(f"Launched lab: {lab_id}")
    except Exception as e:
        print(f"Error launching {lab_id}: {e}")
    return redirect(url_for("labs"))

@app.route("/labs/<lab_id>/flag")
def get_flag(lab_id):
    flag_path = os.path.join("labs", lab_id, "flag.txt")
    try:
        with open(flag_path) as f:
            flag = f.read().strip()
        return f"<h1>Flag: {flag}</h1>"
    except Exception as e:
        return f"Error reading flag for {lab_id}: {e}"

if __name__ == "__main__":
    app.run(debug=True)
