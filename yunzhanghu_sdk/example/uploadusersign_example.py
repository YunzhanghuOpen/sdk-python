# -*- coding: utf-8 -*-

from yunzhanghu_sdk.client.api.model.uploadusersign import *
from yunzhanghu_sdk.client.api.uploadusersign_client import UploadUserSignServiceClient
from yunzhanghu_sdk.example.utils.config_init import init_config

# 签约信息上传
if __name__ == "__main__":
    client = UploadUserSignServiceClient(config=init_config())

    # 用户签约信息上传
    req = UploadUserSignRequest(
        dealer_id = "",
        broker_id = "",
        real_name = "",
        id_card = "",
        phone = "",
        is_abroad = False,
        notify_url = "",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义 request-id
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.upload_user_sign(req)
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
    req = GetUploadUserSignStatusRequest(
        dealer_id = "",
        broker_id = "",
        real_name = "",
        id_card = "",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义 request-id
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.get_upload_user_sign_status(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)
