import os
import socket
import time

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    # for i in range(100000):
    #     i += 1
    # target = os.environ.get('TARGET', 'World')
    # return 'Hello {}!\n'.format(target)
    time1 = time.time()
    sleep_time = request.args.get("time", 0.0, float)
    time.sleep(sleep_time / 1000)
    time2 = time.time()
    return str(time2 - time1)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
