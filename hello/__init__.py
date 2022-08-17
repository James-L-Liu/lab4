from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return '<p style="color:green">Hello, world !!!</p>'

    return app

