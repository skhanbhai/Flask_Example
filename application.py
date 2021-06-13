from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Hello there good sir. This is my Web Page'


if __name__ == "__main__":
    application.run()