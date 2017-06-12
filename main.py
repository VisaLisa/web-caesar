from flask import Flask, request
<<<<<<< HEAD
from caesar import rotate_string
=======
>>>>>>> 035b1ecd0590db9b159d1056f770bdeb6945c1a3

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<<<<<<< HEAD
<!DOCTYPE html>

<html>
<head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    <body>
        <form action="/" method="post">
            <label for="rot">Rotate by:</label>
            <input type="text" name="rot" value="0" />
            <textarea name="text">{0}</textarea>
        <input type="submit" />
=======
<!doctype html>
<html>
    <body>
        <form action ="/hello" method="post">
            <label for="first-name">First Name:</label>
            <input id="first-name" type="text" name="first_name" />
            <input type="submit"/>
>>>>>>> 035b1ecd0590db9b159d1056f770bdeb6945c1a3
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
<<<<<<< HEAD
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    encrypt_rot = request.form["rot"]
    encrypt_text = request.form["text"]

    encrypt_rot = int(encrypt_rot)

    encrypted = rotate_string(encrypt_text, encrypt_rot)
    return  "<h1>" + form.format(encrypted) + "</h1>"
    
=======
    return form

@app.route("/hello", methods=['POST'])
def hello():
    first_name = request.form('first_name')
    return '<h1>Hello,' + first_name + '</h1>'

>>>>>>> 035b1ecd0590db9b159d1056f770bdeb6945c1a3
app.run()
