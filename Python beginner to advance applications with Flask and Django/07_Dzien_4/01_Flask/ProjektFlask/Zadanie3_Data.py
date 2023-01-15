from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    today = format(datetime.today(), "%Y-%m-%d")
    return f"Dziaj jest {today}"

if __name__ == '__main__':
    app.run(debug=True)