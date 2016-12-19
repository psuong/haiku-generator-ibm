# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Global Variables
post_request = "POST"
get_request = "GET"


@app.route("/", methods = ["GET", "POST"])
def index():
    """
    Renders the default page for the app to render.
    """
    context_dict = {
        "page_title": "Haiku Generator",
        "form_action": "/",
        "haiku": None
    }

    if request.method == post_request:
        return "POST"
    return render_template("main.html", **context_dict)


port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(debug=True, host='127.0.0.1', port=int(port))
