# -*- coding: utf-8 -*-

from yunzhanghu_sdk.client.api.model.h5usersign import *
from yunzhanghu_sdk.client.api.h5usersign_client import H5UserSignServiceClient
from yunzhanghu_sdk.example.utils.config_init import init_config

# 用户签约（H5 签约）
if __name__ == "__main__":
    conf = init_config()
    client = H5UserSignServiceClient(config=conf)

    # 预申请签约
    req = H5UserPresignRequest(
        dealer_id = conf.dealer_id,
        broker_id = conf.broker_id,
        real_name = "张三",
        id_card = "11010519491231002X",
        certificate_type = 0,
        collect_phone_no = 0,
        page_open_way = 1,
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义 request-id
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
        token = "7db97222-2dfb-484b-b8ac-e39a69d2aba0",
        color = "#8171ff",
        url = "https://www.example.com",
        redirect_url = "https://www.example.com",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义 request-id
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
        dealer_id = conf.dealer_id,
        broker_id = conf.broker_id,
        real_name = "张三",
        id_card = "11010519491231002X",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义 request-id
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
        dealer_id = conf.dealer_id,
        broker_id = conf.broker_id,
        real_name = "张三",
        id_card = "11010519491231002X",
        certificate_type = 0,
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义 request-id
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
