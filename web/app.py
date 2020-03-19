from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    s = ""
    for i in range(20):
        s += "<li>number " + str(i) + "</li>"
    return s


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)