from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
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
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    encrypt_rot = request.form["rot"]
    encrypt_text = request.form["text"]

    encrypt_rot = int(encrypt_rot)

    encrypted = rotate_string(encrypt_text, encrypt_rot)
    return  "<h1>" + form.format(encrypted) + "</h1>"

app.run()
