from flask import Flask
from flask_monitor import register_metrics
from prometheus_client import make_wsgi_app
from werkzeug import run_simple
from werkzeug.middleware.dispatcher import DispatcherMiddleware


app = Flask(__name__)

register_metrics(app)

app.config["APP_VERSION"] = "v0.1.2"
dispatcher = DispatcherMiddleware(app.wsgi_app, {"/metrics": make_wsgi_app()})


@app.route("/")
def hello_world():
    return f'<p>Hello, world!</p>'


if __name__ == '__main__':
    run_simple(hostname="172.17.0.2", port=5000, application=dispatcher)