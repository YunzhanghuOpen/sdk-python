# -*- coding: utf-8 -*-

from yunzhanghu_sdk.client.api.model.usercollect import *
from yunzhanghu_sdk.client.api.usercollect_client import UserCollectServiceClient
from yunzhanghu_sdk.example.utils.config_init import init_config

# 用户信息收集
if __name__ == "__main__":
    conf = init_config()
    client = UserCollectServiceClient(config=conf)

    # 查询手机号码绑定状态
    req = GetUserCollectPhoneStatusRequest(
        dealer_id = conf.dealer_id,
        broker_id = conf.broker_id,
        dealer_user_id = "userId1234567890",
        real_name = "张三",
        id_card = "11010519491231002X",
        certificate_type = 0,
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义 request-id
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.get_user_collect_phone_status(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)

    # 获取收集手机号码页面
    req = GetUserCollectPhoneUrlRequest(
        token = "4ecd2791c8a44ed0b0480c4063fb30f0",
        color = "",
        url = "https://www.example.com",
        redirect_url = "",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义 request-id
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.get_user_collect_phone_url(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)
