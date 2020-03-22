from flask import Flask
import redis

conn = redis.Redis('redis-service')
app = Flask(__name__)

@app.route('/')
def hello_world():
    t = conn.hgetall("1467810369")
    return "<h1><strong>" + str(t) + "</strong></h1>"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)