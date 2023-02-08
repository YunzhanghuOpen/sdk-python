# -*- coding: utf-8 -*-
from yzh_py.config import *


def init_config():
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
    config = Config(
        # host 请求域名
        host="https://api-service.yunzhanghu.com",
        # 个体户注册域名
        # host="https://api-aic.yunzhanghu.com",
        dealer_id=dealer_id,
        sign_type=sign_type,
        app_key=app_key,
        des3key=des3key,
        dealer_private_key=dealer_private_key,
        yzh_public_key=yzh_public_key,
    )
    return config
