from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    # Binds to all available network interfaces on port 5000
    app.run(host='192.168.86.6')
