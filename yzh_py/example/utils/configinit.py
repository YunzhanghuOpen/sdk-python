# -*- coding: utf-8 -*-
from yzh_py.config import *


def init_config():
    # 平台企业 ID，登录云账户综合服务平台，选择“业务中心 > 业务管理 > 对接信息”获取
    dealer_id = "xxx"
    # 综合服务主体 ID，登录云账户综合服务平台，选择“业务中心 > 业务管理 > 对接信息”获取
    broker_id = "xxx"
    # 签名方式，登录云账户综合服务平台，选择“业务中心 > 业务管理 > 对接信息”获取，默认为 RSA 签名方式。
    # rsa：RSA 签名方式   sha256：HMAC 签名方式
    sign_type = "xxx"
    # 平台企业 App Key，登录云账户综合服务平台，选择“业务中心 > 业务管理 > 对接信息”获取
    app_key = "xxx"
    # 平台企业 3DES Key，登录云账户综合服务平台，选择“业务中心 > 业务管理 > 对接信息”获取
    des3key = "xxx"
    # 平台企业私钥，自行生成 RSA 公私钥，私钥请妥善保存，谨防泄露。平台企业公钥请登录云账户综合服务平台配置，选择“业务中心 > 业务管理 > 对接信息”，单击页面右上角的“编辑”，完成平台企业公钥配置。
    dealer_private_key = '''
    -----BEGIN PRIVATE KEY-----
    xxx
    '''
    # 云账户公钥，登录云账户综合服务平台，选择“业务中心 > 业务管理 > 对接信息”获取
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
