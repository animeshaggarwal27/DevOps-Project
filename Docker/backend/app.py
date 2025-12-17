from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/healthz")
def healthz():
    return "OK", 200

@app.post("/submit")
def submit():
    # Accept form or JSON
    item_name = request.form.get("itemName") or (request.json or {}).get("itemName")
    item_desc = request.form.get("itemDescription") or (request.json or {}).get("itemDescription")

    if not item_name or not item_desc:
        return jsonify({"ok": False, "error": "itemName and itemDescription are required"}), 400

    # TODO: persist to DB if needed. For now, just echo back.
    return jsonify({
        "ok": True,
        "message": "Received by Flask",
        "data": {"itemName": item_name, "itemDescription": item_desc}
    }), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
