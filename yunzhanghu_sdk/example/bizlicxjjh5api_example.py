# -*- coding: utf-8 -*-

from yunzhanghu_sdk.client.api.model.bizlicxjjh5api import *
from yunzhanghu_sdk.client.api.bizlicxjjh5api_client import BizlicXjjH5APIServiceClient
from yunzhanghu_sdk.example.utils.config_init import init_config

# 个体工商户注册（云账户新经济 H5+API）
if __name__ == "__main__":
    client = BizlicXjjH5APIServiceClient(config=init_config())

    # 工商实名信息录入
    req = H5PreCollectBizlicMsgRequest(
        dealer_id="",
        broker_id="",
        dealer_user_id="",
        phone_no="",
        id_card="",
        real_name="",
        id_card_address="",
        id_card_agency="",
        id_card_nation="",
        id_card_validity_start="",
        id_card_validity_end="",
    )
    resp = client.h5_pre_collect_bizlic_msg(req)
    print("工商实名信息录入返回：", resp.code, resp.message, resp.data)

    # 预启动
    req = H5APIGetStartUrlRequest(
        dealer_id="",
        broker_id="",
        dealer_user_id="",
        client_type="",
        notify_url="",
        color="",
        return_url="",
        customer_title="",
    )
    resp = client.h5_api_get_start_url(req)
    print("预启动返回：", resp.code, resp.message, resp.data)

    # 查询个体工商户状态
    req = H5APIEcoCityAicStatusRequest(
        dealer_id="",
        broker_id="",
        dealer_user_id="",
        id_card="",
        real_name="",
        open_id="",
    )
    resp = client.h5_api_eco_city_aic_status(req)
    print("查询个体工商户状态返回：", resp.code, resp.message, resp.data)
