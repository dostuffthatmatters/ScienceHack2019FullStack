from flask_backend import app

@app.route("/", methods=["GET"])
def index():
    return {"Status": "Ok"}, 200
