from flask import Flask, render_template

app = Flask(__name__,template_folder='./templates/')

@app.route("/",methods=['GET'])
def index():
    # return "<p>Hello, World!</p>"
    return render_template('index.html')

if __name__ == '__main__':
    # Binds to all available network interfaces on port 5000
    app.run(host='192.168.86.6')
