from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, welcome to my multi container application!'

if  __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)