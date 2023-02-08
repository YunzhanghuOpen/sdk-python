# -*- coding: utf-8 -*-

from flask import Flask, request
from gevent import pywsgi
from yzh_py.message import verify_sign_rsa, decrypt
from yzh_py.example.utils.configinit import init_config

# 异步通知

app = Flask(__name__)

config = init_config()


@app.route('/yzh/notify', methods=['POST'])
def yzh_notify():
    resp = "fail"
    print("【请求平台企业 ID】：", request.headers.get("dealer-id"))
    if request.method == 'POST':
        data = request.form['data']
        mess = request.form['mess']
        timestamp = request.form['timestamp']
        sign = request.form['sign']
        sign_type = request.form['sign_type']
        print(
            "【异步通知】data:{} mess:{} timestamp:{} sign_type:{} sign:{}".format(data, mess, timestamp, sign_type, sign), )
        # 验证签名
        if verify_sign_rsa(config.yzh_public_key, config.app_key, data, mess, timestamp, sign):
            # 验签通过，解密
            res_data = decrypt(config.des3key, data)
            #  业务逻辑处理
            #  TodoList
            #  。。。
            resp = "success"

    return resp


if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 8000), app)
    server.serve_forever()