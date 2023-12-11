# -*- coding: utf-8 -*-

from yunzhanghu_sdk.client.api.model.bizlicxjjh5 import *
from yunzhanghu_sdk.client.api.bizlicxjjh5_client import BizlicXjjH5ServiceClient
from yunzhanghu_sdk.example.utils.config_init import init_config

# 个体工商户注册（云账户新经济 H5）
if __name__ == "__main__":
    client = BizlicXjjH5ServiceClient(config=init_config())

    # 预启动
    req = H5GetStartUrlRequest(
        dealer_id = "",
        broker_id = "",
        dealer_user_id = "",
        client_type = 0,
        notify_url = "",
        color = "",
        return_url = "",
        customer_title = 0,
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义 request-id
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.h5_get_start_url(req)
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
    req = H5EcoCityAicStatusRequest(
        dealer_id = "",
        broker_id = "",
        dealer_user_id = "",
        id_card = "",
        real_name = "",
        open_id = "",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义 request-id
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.h5_eco_city_aic_status(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)
