### What is this repository for?
This repository is for Professor Barnett's Operating System's class. This is a
haiku generator which is built directly on IBM Bluemix's webapp service.

### Installation
This project runs on **Python 2.7**.

To meet all the requirements for the Flask App run:

`pip install -r requirements.txt`

This reads the requirments.txt file and installs all of the packages into your python package manager.

#### Optional Installations
For sanity's sake, we can create a virtualenv, which is a local directory specified for the Flask App. To create a virtualenv (virtual environment). You must have virtual environment installed in your Python Packet Manager!

`virtualenv venv`
This creates a directory called venv.

#### On Windows
In your current directory via your terminal/command prompt run,

`venv/Scripts/activate`

#### On UNIX
In your current directory via your terminal run,

`source venv/bin/activate`

### Running the Application
To run this app on localhost simply write in your terminal:

`python app.py local`

For an IPV4 compliant port you can run:

`python app.py external`
