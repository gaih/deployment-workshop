from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World"


if __name__ == "__main__":
    app.run()
