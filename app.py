from flask import Flask
import redis 

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, decode_responses=True)


@app.route('/')
def welcome():
    return 'Hello, welcome to my multi container app!'

@app.route('/')
def count():
    count = client.incr('hits')
    return f'This webpage has been viewed {count} time(s)'

if  __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)