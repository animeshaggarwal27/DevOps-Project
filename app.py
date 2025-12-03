from flask import Flask, jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient
import json

app = Flask(__name__)

# ----------------------
# MongoDB ATLAS CONNECTION
# ----------------------
client = MongoClient("YOUR_MONGODB_ATLAS_CONNECTION_STRING")
db = client["test_database"]
collection = db["test_collection"]

# ----------------------
# API ROUTE → Reads from file & returns JSON
# ----------------------
@app.route("/api")
def api_data():
    with open("data.json", "r") as file:
        data = json.load(file)
    return jsonify(data)

# ----------------------
# FORM PAGE
# ----------------------
@app.route("/", methods=["GET", "POST"])
def form_page():
    if request.method == "POST":
        try:
            # Read form data
            name = request.form.get("name")
            email = request.form.get("email")

            # Insert into MongoDB
            collection.insert_one({"name": name, "email": email})

            # Redirect to success page
            return redirect(url_for("success_page"))

        except Exception as e:
            # Stay on same page and display error
            return render_template("form.html", error=str(e))

    return render_template("form.html", error=None)

# ----------------------
# SUCCESS PAGE
# ----------------------
@app.route("/success")
def success_page():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)
