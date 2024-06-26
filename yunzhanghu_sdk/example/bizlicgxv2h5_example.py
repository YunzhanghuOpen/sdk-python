# -*- coding: utf-8 -*-

from yunzhanghu_sdk.client.api.model.bizlicgxv2h5 import *
from yunzhanghu_sdk.client.api.bizlicgxv2h5_client import BizlicGxV2H5ServiceClient
from yunzhanghu_sdk.example.utils.config_init import init_config

# 个体工商户注册（云账户共享大额 H5）
if __name__ == "__main__":
    conf = init_config()
    client = BizlicGxV2H5ServiceClient(config=conf)

    # 预启动
    req = GxV2H5GetStartUrlRequest(
        dealer_id = conf.dealer_id,
        broker_id = conf.broker_id,
        dealer_user_id = "userId1234567890",
        client_type = 1,
        notify_url = "https://www.example.com",
        color = "#007AFF",
        return_url = "https://www.example.com",
        customer_title = 1,
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义 request-id
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.gx_v2_h5_get_start_url(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)

    # 查询个体工商户状态
    req = GxV2H5GetAicStatusRequest(
        dealer_id = conf.dealer_id,
        broker_id = conf.broker_id,
        open_id = "openId1234567890",
        real_name = "张三",
        id_card = "11010519491231002X",
        dealer_user_id = "userId1234567890",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义 request-id
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.gx_v2_h5_get_aic_status(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)
