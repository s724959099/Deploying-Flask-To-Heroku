from flask import *

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "hello"


if __name__ == '__main__':
    app.run(debug=True)
