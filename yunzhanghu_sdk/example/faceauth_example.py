# -*- coding: utf-8 -*-

from yunzhanghu_sdk.client.api.model.faceauth import *
from yunzhanghu_sdk.client.api.faceauth_client import FaceAuthServiceClient
from yunzhanghu_sdk.example.utils.config_init import init_config

# 人脸识别实名核验
if __name__ == "__main__":
    conf = init_config()
    client = FaceAuthServiceClient(config=conf)

    # 申请人脸识别实名核验
    req = ApplyFaceAuthRequest(
        dealer_id = conf.dealer_id,
        broker_id = conf.broker_id,
        verification_id = "verificationId123456789",
        real_name = "张三",
        id_card = "11010519491231002X",
        callback_url = "https://www.example.com",
        redirect_url = "https://www.example.com",
        color = "#8171ff",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义 request-id
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.apply_face_auth(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)

    # 查询人脸识别实名核验结果
    req = GetFaceAuthResultRequest(
        dealer_id = conf.dealer_id,
        broker_id = conf.broker_id,
        record_id = "recordId123456789",
        verification_id = "verificationId123456789",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义 request-id
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.get_face_auth_result(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)
