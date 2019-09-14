import os
import socket

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    # for i in range(100000):
    #     i += 1
    # target = os.environ.get('TARGET', 'World')
    # return 'Hello {}!\n'.format(target)
    return socket.gethostname()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
