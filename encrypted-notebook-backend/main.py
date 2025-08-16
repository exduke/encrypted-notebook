"""
@describe:
@fileName: main.py
@time    : 2024/6/21 13:15
@author  : duke
"""
from flask import Flask, render_template, request
import webbrowser
from cfg import DEV, DATA_PATH, WEB_PATH, PORT, HISTORY_NUM
from utils import encode, decode, get_sorted_files
import os
import time

app = Flask(__name__,
            static_folder=WEB_PATH,  # 设置静态文件夹目录
            template_folder=WEB_PATH,
            static_url_path="")  # 设置vue编译输出目录dist文件夹，为Flask模板文件目录


@app.route('/')
def index():
    return render_template('index.html', name='index')


@app.route('/save', methods=['POST'])
def save():
    data = encode(request.data, bytes.fromhex(request.args['key']))
    with open(os.path.join(DATA_PATH, str(time.time_ns())), 'wb') as f:
        f.write(data)
    files = get_sorted_files(DATA_PATH)
    if len(files) > HISTORY_NUM:
        os.remove(os.path.join(DATA_PATH, files[0]))
    return 'succeed'


@app.route('/load', methods=['GET'])
def load():
    with open(os.path.join(DATA_PATH, get_sorted_files(DATA_PATH)[-1]), 'rb') as f:
        data = f.read()
    return decode(data, bytes.fromhex(request.args['key']))


@app.route('/encrypt', methods=['POST'])
def encrypt():
    return encode(request.data, bytes.fromhex(request.args['key']))


@app.route('/decrypt', methods=['POST'])
def decrypt():
    return decode(request.data, bytes.fromhex(request.args['key']))


if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:23333')

    app.run(
        debug=DEV,  # 调试
        host='0.0.0.0',  # ip
        port=PORT,  # 端口
        # ssl_context='adhoc',  # 默认SSL证书，实现https
        threaded=True,  # 多线程
    )
