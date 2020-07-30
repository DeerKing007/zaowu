from flask import Flask
from flask import render_template




# 实例化app对象
app = Flask(__name__)


@app.route('/')
@app.route("/zaowu/index")
def spiderBot():
    '''首页'''
    return render_template('index.html')


if __name__ == "__main__":
    app.config['JSON_AS_ASCII'] = False  # json中文编码问题的解决
    app.run(host='0.0.0.0', port=5000,  # 任何ip都可以访问
            use_reloader=False  # 取消自动加载，也是避免DEBUG模式下创建两个实例的问题
            )
