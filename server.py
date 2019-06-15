# FLASK_APP=test_webapp.py flask run

from flask import Flask as Flask
import datetime

app = Flask(__name__)
#app = any_name(__name__)

@app.route("/")
def hello():
    return "2: " + datetime.datetime.now().ctime()

@app.route("/static")
def static_content():
    return app.send_static_file("static.html")

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8080)
