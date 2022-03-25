from flask import Flask
import datetime
from flask import request

 
app = Flask(__name__)
 
@app.route("/")
def content():
    date = datetime.datetime.now()
    info = request.headers.get('User-Agent')

    return f"<h1>Current Date:</h1>{date}<h1>Browser fingerprint: </h1>{info}"
 
if __name__ == "__main__":
    app.run()
