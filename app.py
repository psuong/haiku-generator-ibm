import os
import sys
from flask import Flask, jsonify, render_template, request
from haiku_generator import generate_random_lines, generate_line

app_args = {"local": "127.0.0.1",
            "external": "0.0.0.0"}

app = Flask(__name__)

#Set whitespace trimming
app.jinja_env.trim_blocks = True;
app.jinja_env.lstrip_blocks = True;

# Global Variables
post_request = "POST"
get_request = "GET"


@app.route("/", methods = ["GET", "POST"])
def index():
    """
    Renders the default page for the app to render.
    """

    # General dictionary to hold all of the variables in the html template
    context_dict = {
        "page_title": "Haiku Generator",
        "form_action": "/",
        "haiku": None
    }

    if request.method == post_request:
        # Update the haiku if the app received a post request
        # TODO: Write a function which generates the sentences
        context_dict["haiku"] = generate_random_lines()

    # Render the template here
    return render_template("main.html", **context_dict)


def run():
    """
    This runs the main file of the program
    """
    port = os.getenv('PORT', '5000')
    app.run(host=app_args[sys.argv[1]], port=int(port), debug=True)


if __name__ == "__main__":
    # TODO: create a run function which takes a system argument to switch between
    # local and external host
    # app.run(host='0.0.0.0', port=int(port))
	# app.run(debug=True, host='127.0.0.1', port=int(port))

    run()
