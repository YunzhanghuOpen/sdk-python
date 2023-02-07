# -*- coding: utf-8 -*-
from yzh_py.client.api.model.bizlicxjjh5 import *
from yzh_py.client.api.bizlicxjjh5_client import Bizlicxjjh5Client
from yzh_py.config import *



if __name__ == '__main__':
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
        host="https://api-aic.yunzhanghu.com",
        dealer_id=dealer_id,
        sign_type=sign_type,
        app_key=app_key,
        des3key=des3key,
        dealer_private_key=dealer_private_key,
        yzh_public_key=yzh_public_key,
    )

    # 预启动
    h5getstarturlrequest = H5GetStartUrlRequest(
        dealer_id="",
        broker_id="",
        dealer_user_id="",
        client_type="",
        notify_url="",
        color="",
        return_url="",
        custom_title="",
    )
    h5getstarturlrequest_res = Bizlicxjjh5Client.h5_get_start_url(h5getstarturlrequest)
    print("预启动返回：", h5getstarturlrequest_res.code, h5getstarturlrequest_res.message, h5getstarturlrequest_res.data)

    # 查询个体工商户状态
    h5ecocityaicstatusrequest = H5EcoCityAicStatusRequest(
        dealer_id="",
        broker_id="",
        dealer_user_id="",
        id_card="",
        real_name="",
        open_id="",
    )
    h5ecocityaicstatusrequest_res = Bizlicxjjh5Client.h5_eco_city_aic_status(h5ecocityaicstatusrequest)
    print("查询个体工商户状态返回：", h5ecocityaicstatusrequest_res.code, h5ecocityaicstatusrequest_res.message,
          h5ecocityaicstatusrequest_res.data)





