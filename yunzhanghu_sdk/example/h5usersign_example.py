# -*- coding: utf-8 -*-

from yunzhanghu_sdk.client.api.model.h5usersign import *
from yunzhanghu_sdk.client.api.h5usersign_client import H5UserSignServiceClient
from yunzhanghu_sdk.example.utils.config_init import init_config

# 用户签约（H5 签约）
if __name__ == "__main__":
    client = H5UserSignServiceClient(config=init_config())

    # 预申请签约
    req = H5UserPresignRequest(
        dealer_id = "",
        broker_id = "",
        real_name = "",
        id_card = "",
        certificate_type=0,
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如平台企业未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.h5_user_presign(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)

    # 申请签约
    req = H5UserSignRequest(
        token = "",
        color = "",
        url = "",
        redirect_url = "",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如平台企业未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.h5_user_sign(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)

    # 获取用户签约状态
    req = GetH5UserSignStatusRequest(
        dealer_id = "",
        broker_id = "",
        real_name = "",
        id_card = "",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如平台企业未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.get_h5_user_sign_status(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)

    # 用户解约（测试账号专用接口）
    req = H5UserReleaseRequest(
        broker_id = "",
        dealer_id = "",
        real_name = "",
        id_card = "",
        certificate_type = 0,
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如平台企业未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.h5_user_release(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)
