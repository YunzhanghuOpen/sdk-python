# -*- coding: utf-8 -*-

from yunzhanghu_sdk.client.api.model.bizlicxjjh5api import *
from yunzhanghu_sdk.client.api.bizlicxjjh5api_client import BizlicXjjH5APIServiceClient
from yunzhanghu_sdk.example.utils.config_init import init_config

# 个体工商户注册（云账户新经济 H5+API）
if __name__ == "__main__":
    conf = init_config()
    client = BizlicXjjH5APIServiceClient(config=conf)

    # 工商实名信息录入
    req = H5PreCollectBizlicMsgRequest(
        dealer_id = conf.dealer_id,
        broker_id = conf.broker_id,
        dealer_user_id = "user1234567890",
        phone_no = "+86-188****8888",
        id_card = "11010519491231002X",
        real_name = "张三",
        id_card_address = "",
        id_card_agency = "",
        id_card_nation = "20",
        id_card_validity_start = "2022-02-22",
        id_card_validity_end = "2042-01-01",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义 request-id
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.h5_pre_collect_bizlic_msg(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)

    # 预启动
    req = H5APIGetStartUrlRequest(
        dealer_id = conf.dealer_id,
        broker_id = conf.broker_id,
        dealer_user_id = "01720374",
        client_type = 2,
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
        resp = client.h5_api_get_start_url(req)
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
    req = H5APIEcoCityAicStatusRequest(
        dealer_id = conf.dealer_id,
        broker_id = conf.broker_id,
        open_id = "open1234567890",
        real_name = "张三",
        id_card = "11010519491231002X",
        dealer_user_id = "user1234567890",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义 request-id
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.h5_api_eco_city_aic_status(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)
