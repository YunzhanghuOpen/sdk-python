# -*- coding: utf-8 -*-

from yunzhanghu_sdk.client.api.model.apiusersign import *
from yunzhanghu_sdk.client.api.apiusersign_client import ApiUserSignServiceClient
from yunzhanghu_sdk.example.utils.config_init import init_config

# 用户签约（API 签约）
if __name__ == "__main__":
    client = ApiUserSignServiceClient(config=init_config())

    # 获取协议预览 URL
    req = ApiUserSignContractRequest(
        dealer_id="",
        broker_id="",
    )
    resp = client.api_user_sign_contract(req)
    print("获取协议预览 URL 返回：", resp.code, resp.message, resp.data)

    # 用户签约
    req = ApiUserSignRequest(
        broker_id="",
        dealer_id="",
        real_name="",
        id_card="",
        card_type="",
    )
    resp = client.api_user_sign(req)
    print("用户签约返回：", resp.code, resp.message, resp.data)

    # 获取用户签约状态
    req = GetApiUserSignStatusRequest(
        dealer_id="",
        broker_id="",
        real_name="",
        id_card="",
    )
    resp = client.get_api_user_sign_status(req)
    print("获取用户签约状态返回：", resp.code, resp.message, resp.data)

    # 用户解约（测试账号专用接口）
    req = ApiUserSignReleaseRequest(
        broker_id="",
        dealer_id="",
        real_name="",
        id_card="",
        card_type="",
    )
    resp = client.api_user_sign_release(req)
    print("用户解约（测试账号专用接口）返回：", resp.code, resp.message, resp.data)
