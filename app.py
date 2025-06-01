from flask import Flask
import redis 
import os

app = Flask(__name__)
redis_host = os.getnev("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))
r = redis.Redis(host=redis_host, port=redis_port)


@app.route('/')
def welcome():
    return '''
    <html>
    <head>
        <title>Welcome to My Multi-Container App</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                margin: 0;
                padding: 0;
                background: linear-gradient(to right, #00c6ff, #0072ff);
                color: #fff;
                display: flex;
                flex-direction: column;
                height: 100vh;
                align-items: center;
                justify-content: center;
            }

            h1 {
                font-size: 3rem;
                margin-bottom: 0.5em;
            }

            p {
                font-size: 1.2rem;
                max-width: 600px;
                text-align: center;
                line-height: 1.6;
            }

            .tagline {
                font-style: italic;
                color: #e0f7ff;
                margin-top: 1em;
            }

            footer {
                position: absolute;
                bottom: 20px;
                font-size: 0.9rem;
                color: #cceeff;
            }
        </style>
    </head>
    <body>
    <main>
        <h1>Welcome to My Multi-Container App</h1>
        <p>
            This application is designed with scalability and modularity in mind, utilizing Docker containers and Flask for lightweight, fast deployments. It's part of my commitment to building robust, production-ready services.
        </p>
        <div class="tagline">Built for modern development. Ready for production.</div>
    </main>
    <footer>
        &copy; 2025 | Crafted by Kadar Ahmed
    </footer>
    </body>
    </html>

    '''

@app.route('/count')
def count():
    visit_count = r.incr('visits')
    return f'''
    <html>
    <head>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                margin: 0;
                padding: 0;
                background: linear-gradient(to right, #ff758c, #ff7eb3);
                color: #fff;
                display: flex;
                flex-direction: column;
                height: 100vh;
                align-items: center;
                justify-content: center;
            }}

            h1 {{
                font-size: 2.5rem;
                margin-bottom: 0.5em;
            }}

            .count {{
                font-size: 4rem;
                font-weight: bold;
                margin: 0.5em 0;
                color: #fffbe6;
            }}

            p {{
                font-size: 1.1rem;
                text-align: center;
                max-width: 500px;
                line-height: 1.6;
            }}

            footer {{
                position: absolute;
                bottom: 20px;
                font-size: 0.9rem;
                color: #ffeeee;
            }}
        </style>
    </head>
    <body>
        <main>
            <h1>Visitor Count</h1>
            <div class="count">{visit_count}</div>
            <p>This counter is powered by <strong>Redis</strong>, demonstrating the ability to integrate persistent, in-memory data stores in a distributed system. Every visit increments the count, showing state across containers.</p>
        </main>
        <footer>
            &copy; 2025 | Scalable Systems by Kadar Ahmed
        </footer>
    </body>
    </html>
    '''

if  __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)