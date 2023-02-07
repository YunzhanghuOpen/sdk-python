# -*- coding: utf-8 -*-

from yzh_py.client.api.model.payment import GetOrderRequest
from yzh_py.client.api.payment_client import PaymentClient
from yzh_py.config import *

if __name__ == "__main__":
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
    # 初始化配置参数
    config = Config(
        # host 请求域名
        host="https://api-service.yunzhanghu.com",
        dealer_id=dealer_id,
        sign_type=sign_type,
        app_key=app_key,
        des3key=des3key,
        dealer_private_key=dealer_private_key,
        yzh_public_key=yzh_public_key,
    )
    # 获取订单详情
    request = GetOrderRequest(
        order_id="232211231231231",
        channel="微信",
        data_type="encryption"
    )
    # 自定义 request-id
    # request.request_id = "XXXXX"
    client = PaymentClient(config)
    resp = client.get_order(request)

    print(resp.code, resp.message, resp.request_id, resp.data)

