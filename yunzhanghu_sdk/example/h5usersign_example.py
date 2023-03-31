# -*- coding: utf-8 -*-

from yunzhanghu_sdk.client.api.model.h5usersign import *
from yunzhanghu_sdk.client.api.h5usersign_client import H5UserSignServiceClient
from yunzhanghu_sdk.example.utils.config_init import init_config

# 用户签约（H5 签约）
if __name__ == "__main__":
    h5_user_sign_client = H5UserSignServiceClient(config=init_config())

    # 预申请签约
    req = H5UserPresignRequest(
        dealer_id="",
        broker_id="",
        real_name="",
        id_card="",
        certificate_type="",
    )
    resp = h5_user_sign_client.h5_user_presign(req)
    print("预申请签约返回：", resp.code, resp.message, resp.data)

    # 申请签约
    req = H5UserSignRequest(
        token="",
        color="",
        url="",
        redirect_url="",
    )
    resp = h5_user_sign_client.h5_user_sign(req)
    print("申请签约返回：", resp.code, resp.message, resp.data)

    # 获取用户签约状态
    req = GetH5UserSignStatusRequest(
        dealer_id="",
        broker_id="",
        real_name="",
        id_card="",
    )
    resp = h5_user_sign_client.get_h5_user_sign_status(req)
    print("获取用户签约状态返回：", resp.code, resp.message, resp.data)

    # 用户解约（测试账号专用接口）
    req = H5UserReleaseRequest(
        broker_id="",
        dealer_id="",
        real_name="",
        id_card="",
        certificate_type="",
    )
    resp = h5_user_sign_client.h5_user_release(req)
    print("用户解约（测试账号专用接口）返回：", resp.code, resp.message, resp.data)
