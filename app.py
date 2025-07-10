from flask import Flask, render_template, request, redirect, url_for, flash
import json
import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('ROOTQUEST_SECRET_KEY', 'fallback_dev_key')

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
def view_flag(lab_id):
    flag_path = f"labs/{lab_id}/flag.txt"
    if not os.path.exists(flag_path):
        return f"Flag not found for {lab_id}", 404
    with open(flag_path) as f:
        return f"<pre>{f.read()}</pre>"

@app.route("/labs/<lab_id>/submit", methods=["GET", "POST"])
def submit_flag(lab_id):
    flag_path = f"labs/{lab_id}/flag.txt"
    if request.method == "POST":
        user_flag = request.form.get("flag", "").strip()
        if not os.path.exists(flag_path):
            flash("Flag file missing!", "error")
        else:
            with open(flag_path) as f:
                correct_flag = f.read().strip()
            if user_flag == correct_flag:
                flash("✅ Correct flag!", "success")
            else:
                flash("❌ Incorrect flag.", "error")
        return redirect(url_for("submit_flag", lab_id=lab_id))

    return render_template("submit.html", lab_id=lab_id)

if __name__ == "__main__":
    app.run(debug=True)
