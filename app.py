from flask import Flask, jsonify, render_template
from sqlalchemy import create_engine
from config import db_user, db_password, db_host, db_port, db_name


app = Flask(__name__)
engine = create_engine(f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/language.json")
def language():
    results = engine.execute("SELECT * FROM programming_language")
    return jsonify([dict(_) for _ in results])

@app.route("/api/visual1.json")
def visual1():
    results = engine.execute("SELECT * FROM programming_language")
    return jsonify([dict(_) for _ in results])

if __name__ == '__main__':
    app.run(debug=True)




