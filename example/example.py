# -*- coding: utf-8 -*-

from yzh_py.client.api.model.payment import GetOrderRequest
from yzh_py.client.api.payment_client import PaymentClient
from yzh_py.config import *

if __name__ == "__main__":
    dealer_id = "xxx"
    broker_id = "xxx"
    sign_type = "xxx"
    app_key = "xxx"
    des3key = "xxx"
    private_key = '''
    -----BEGIN PRIVATE KEY-----
    xxx
    '''
    public_key = '''
    xxx
    '''
    config = Config(
        host="https://api-service.yunzhanghu.com",
        dealer_id=dealer_id,
        sign_type=sign_type,
        app_key=app_key,
        des3key=des3key,
        private_key=private_key,
        public_key=public_key,
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
