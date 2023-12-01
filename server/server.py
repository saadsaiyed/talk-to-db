from flask import Flask

app = Flask(__name__)

#Frontend API Route
@app.route("/api/home")
def home():
    return {"home": ["please add some css to make me pretty"]}

if __name__ == "__main__":
    app.run(debug=True)