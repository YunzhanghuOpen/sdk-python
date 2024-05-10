# -*- coding: utf-8 -*-
from yunzhanghu_sdk.config import *


def init_config():
    # 平台企业 ID，登录云账户综合服务平台，选择“业务中心 > 业务管理 > 对接信息”获取
    dealer_id = ""
    # 综合服务主体 ID，登录云账户综合服务平台，选择“业务中心 > 业务管理 > 对接信息”获取
    broker_id = ""
    # 签名方式，登录云账户综合服务平台，选择“业务中心 > 业务管理 > 对接信息”获取
    # 签名方式为 RSA，参数固定为：rsa
    sign_type = ""
    # 平台企业 App Key，登录云账户综合服务平台，选择“业务中心 > 业务管理 > 对接信息”获取
    app_key = ""
    # 平台企业 3DES Key，登录云账户综合服务平台，选择“业务中心 > 业务管理 > 对接信息”获取
    des3key = ""
    # 平台企业私钥，自行生成 RSA 公私钥，私钥请妥善保存，谨防泄露。平台企业公钥请登录云账户综合服务平台配置，选择“业务中心 > 业务管理 > 对接信息”，单击页面右上角的“编辑”，完成平台企业公钥配置。
    dealer_private_key = '''
    -----BEGIN PRIVATE KEY-----
    XXXXX
    -----END PRIVATE KEY-----
    '''
    # 云账户公钥，登录云账户综合服务平台，选择“业务中心 > 业务管理 > 对接信息”获取
    yzh_public_key = '''
    -----BEGIN PUBLIC KEY-----
    XXXXX
    -----END PUBLIC KEY-----
    '''
    config = Config(
        # 生产环境请求域名
        host = "https://api-service.yunzhanghu.com",
        # 沙箱环境请求域名
        # host = "https://api-service.yunzhanghu.com/sandbox",
        # 个体工商户注册请求域名
        # host = "https://api-aic.yunzhanghu.com",
        dealer_id = dealer_id,
        broker_id = broker_id,
        sign_type = sign_type,
        app_key = app_key,
        des3key = des3key,
        dealer_private_key = dealer_private_key,
        yzh_public_key = yzh_public_key,
        # 自定义超时时间
        timeout = 30,
    )
    return config
