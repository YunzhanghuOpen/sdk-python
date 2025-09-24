# -*- coding: utf-8 -*-

from yunzhanghu_sdk.client.api.model.realname import *
from yunzhanghu_sdk.client.api.realname_client import RealNameServiceClient
from yunzhanghu_sdk.example.utils.config_init import init_config
from yunzhanghu_sdk.utils import Utils

# 用户实名认证信息收集
if __name__ == "__main__":
    conf = init_config()
    client = RealNameServiceClient(config=conf)


    # 用户实名认证信息收集-人脸认证方式
    req = CollectRealNameInfoRequest(
        dealer_id = conf.dealer_id,
        broker_id = conf.broker_id,
        real_name = "张三",
        id_card = "11010519491231002X",
        realname_result = 1,
        realname_time = "2025-09-09 19:19:19",
        realname_type = 1,
        realname_trace_id = "1413536187796566016",
        realname_platform = "xxxxxxx公司",
        face_image_collect_type = 1,
        face_image = "https://www.example.com/file_name.png",
        face_verify_score = "89.12",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义 request-id
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.collect_real_name_info(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)


    # 用户实名认证信息收集-银行卡四要素认证方式
    req = CollectRealNameInfoRequest(
        dealer_id = conf.dealer_id,
        broker_id = conf.broker_id,
        real_name = "张三",
        id_card = "11010519491231002X",
        realname_result = 1,
        realname_time = "2025-09-09 19:19:19",
        realname_type = 2,
        realname_trace_id = "1413536187796566016",
        realname_platform = "xxxxxxx公司",
        bank_no = "6127000xxxxxxx16",
        bank_phone = "188xxx8888",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义 request-id
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.collect_real_name_info(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)


    # 用户实名认证信息收集-人工审核
    req = CollectRealNameInfoRequest(
        dealer_id = conf.dealer_id,
        broker_id = conf.broker_id,
        real_name = "张三",
        id_card = "11010519491231002X",
        realname_result = 1,
        realname_time = "2025-09-09 19:19:19",
        realname_type = 3,
        realname_trace_id = "1413536187796566016",
        realname_platform = "xxxxxxx公司",
        face_image_collect_type = 1,
        face_image = "https://www.example.com/file_name.png",
        face_verify_score = "89.12",
        bank_no = "6127000xxxxxxx16",
        bank_phone = "188xxx8888",
        reviewer = "908xxx8888"
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义 request-id
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.collect_real_name_info(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)


     # 用户实名认证信息查询
    req = QueryRealNameInfoRequest(
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
        resp = client.query_real_name_info(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)