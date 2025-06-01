from flask import Flask
import redis 

app = Flask(__name__)
r = redis.Redis(host='myredis', port=6379)


@app.route('/')
def welcome():
    return 'Hello, welcome to my multi container app!'

@app.route('/count')
def count():
    count = r.incr('visits')
    return f'This webpage has been viewed {count} times'

if  __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)