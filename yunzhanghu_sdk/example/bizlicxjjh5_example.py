# -*- coding: utf-8 -*-

from yunzhanghu_sdk.client.api.model.bizlicxjjh5 import *
from yunzhanghu_sdk.client.api.bizlicxjjh5_client import BizlicXjjH5ServiceClient
from yunzhanghu_sdk.example.utils.config_init import init_config

# 个体工商户注册（云账户新经济 H5）
if __name__ == "__main__":
    client = BizlicXjjH5ServiceClient(config=init_config())

    # 预启动
    req = H5GetStartUrlRequest(
        dealer_id="",
        broker_id="",
        dealer_user_id="",
        client_type="",
        notify_url="",
        color="",
        return_url="",
        customer_title="",
    )
    resp = client.h5_get_start_url(req)
    print("预启动返回：", resp.code, resp.message, resp.data)

    # 查询个体工商户状态
    req = H5EcoCityAicStatusRequest(
        dealer_id="",
        broker_id="",
        dealer_user_id="",
        id_card="",
        real_name="",
        open_id="",
    )
    resp = client.h5_eco_city_aic_status(req)
    print("查询个体工商户状态返回：", resp.code, resp.message, resp.data)
