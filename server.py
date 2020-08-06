from flask import Flask
from flask import render_template
from gevent import pywsgi


# 实例化app对象
app = Flask(__name__)


@app.route('/')
@app.route("/zaowu/index")
def zaoWu():
    '''首页'''
    return render_template('index.html')


if __name__ == "__main__":
    server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
    server.serve_forever()
