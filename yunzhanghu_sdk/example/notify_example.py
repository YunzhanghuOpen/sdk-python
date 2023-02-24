# -*- coding: utf-8 -*-

from flask import Flask, request
from gevent import pywsgi
from yunzhanghu_sdk.message import notifyDecoder
from yunzhanghu_sdk.example.utils.configinit import init_config

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
            "【异步通知】data:{} mess:{} timestamp:{} sign_type:{} sign:{}".format(data, mess, timestamp, sign_type, sign))
        # 验证签名+解密
        verify_result, res_data = notifyDecoder(config.yzh_public_key, config.app_key, config.des3key, data, mess, timestamp, sign)
        if verify_result:
            # 业务逻辑处理
            # ToDo List
            # 。。。
            resp = "success"
    return resp


if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 8000), app)
    server.serve_forever()