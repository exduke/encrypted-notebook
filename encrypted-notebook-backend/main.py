"""
@describe:
@fileName: main.py
@time    : 2024/6/21 13:15
@author  : duke
"""
from flask import Flask, render_template, request
import webbrowser
# import json

from src.cfg import DEV, DATA_PATH, WEB_PATH, PORT
from src.utils.rsa_local import encode, decode, summon_key_from_md5

app = Flask(__name__,
            static_folder=WEB_PATH,  # 设置静态文件夹目录
            template_folder=WEB_PATH,
            static_url_path="")  # 设置vue编译输出目录dist文件夹，为Flask模板文件目录


@app.route('/')
def index():
    return render_template('index.html', name='index')


@app.route('/save', methods=['POST'])
def save():
    n, e, _ = summon_key_from_md5(request.args['key'])
    data = encode(request.data, e, n)
    with open(DATA_PATH + '/data', 'wb') as f:
        f.write(data)
    return 'succeed'


@app.route('/load', methods=['GET'])
def load():
    n, _, d = summon_key_from_md5(request.args['key'])
    with open(DATA_PATH + '/data', 'rb') as f:
        data = f.read()
    return decode(data, d, n)


@app.route('/encrypt', methods=['POST'])
def encrypt():
    n, e, _ = summon_key_from_md5(request.args['key'])
    return encode(request.data, e, n)


@app.route('/decrypt', methods=['POST'])
def decrypt():
    n, _, d = summon_key_from_md5(request.args['key'])
    return decode(request.data, d, n)


if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:23333')

    app.run(
        debug=DEV,  # 调试
        host='0.0.0.0',  # ip
        port=PORT,  # 端口
        # ssl_context='adhoc',  # 默认SSL证书，实现https
        threaded=True,  # 多线程
    )
