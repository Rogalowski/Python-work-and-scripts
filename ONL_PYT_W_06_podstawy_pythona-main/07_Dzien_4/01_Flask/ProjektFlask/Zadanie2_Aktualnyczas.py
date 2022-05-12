from datetime import datetime
from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    now = format(datetime.now().time(), "%H:%M:%S")
    return f"Teraz jest godzina {now}"
if __name__ == '__main__':
    app.run(debug=True)