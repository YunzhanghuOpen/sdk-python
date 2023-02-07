# -*- coding: utf-8 -*-

from flask import Flask, request, redirect, url_for
from gevent import pywsgi
from yzh_py.message import verify_sign_rsa, decrypt

app = Flask(__name__)

# dealer_id 平台企业 ID
dealer_id = "xxx"
# broker_id 综合服务主体 ID
broker_id = "xxx"
# sign_type 签名类型
sign_type = "xxx"
# app_key
app_key = "xxx"
# des3key
des3key = "xxx"
# dealer_private_key 平台企业私钥
dealer_private_key = '''
   -----BEGIN PRIVATE KEY-----
   xxx
   '''
# yzh_public_key 云账户公钥
yzh_public_key = '''
   xxx
   '''


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
        if verify_sign_rsa(yzh_public_key, app_key, data, mess, timestamp, sign):
            # 验签通过，解密
            res_data = decrypt(des3key, data)
            #  业务逻辑处理
            #  TodoList
            #  。。。
            resp = "success"

    return resp


if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 8000), app)
    server.serve_forever()
