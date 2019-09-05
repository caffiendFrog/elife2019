import sys
from api import api
from flask import Flask
from flask_cors import CORS, cross_origin

def setup():
    application = Flask(__name__)
    application.register_blueprint(api, url_prefix = '/api/')
    application.config['SECRET_KEY'] = 'Guess what? Chicken butt.'
    CORS(application)
    return application

app = setup()

if __name__ == '__main__':
#    app = setup()
#    app.config['file'] = sys.argv[1]
    app.run(debug = True, port = 5000)