from flask import Flask
from flask import  request

app = Flask(__name__)

form = ''' 
    <html> 
        <body>
            <form method = "POST">
            <input type="text" value="Imie domyslne" name = "user">
            <input type = "submit">
            </form >
        </body>
    </html>
    '''
@app.route('/', methods=["GET", "POST"])
def login():
    #text = " x"

    #user = request.form['nm']


    if request.method == 'GET':
       return  form
    else:
        #name = request.form.get("user")
        name = request.form["user"]
        return f"Twoje imie to {name}"


if __name__ == '__main__':
    app.run(debug=True, port="5002")

















