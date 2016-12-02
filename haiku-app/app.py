# We import the flask package
from flask import Flask

# The following line tells our python interpreter, this is the main
# file to run.
# We also created an object called "app"
app = Flask(__name__)

# TODO: Add your views here
@app.route("/") # Between the quotes is the url we want to route to
def index():
    return "Hello world"

if __name__ == "__main__":
    app.run()
