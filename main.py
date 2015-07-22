from flask import Flask
import json
app = Flask(__name__)

@app.route("/")
def hello():
	with open("index.html", "r") as index:
		return index.read()


@app.route("/john/look")
def booboo():
	return json.dumps({"yay":"me"})

if __name__ == "__main__":
    app.run()
