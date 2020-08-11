from flask import Flask
from flask import render_template


# 实例化app对象
app = Flask(__name__)


@app.route('/')
@app.route("/zaowu")
def zaoWu():
    '''首页'''
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
