# -*- coding: utf-8 -*-

from model.custom import CustomRequest, CustomResponse
from yunzhanghu_sdk.client.api.custom_client import *
from yunzhanghu_sdk.example.utils.config_init import init_config

# 通用请求函数，以“银行卡实时支付”接口为例
if __name__ == "__main__":
    conf = init_config()
    client = CustomClient(config=conf)

    # 接口请求地址
    req_url = "/api/payment/v1/order-bankpay"
    # 接口请求方式
    method_type = "POST"
    # 构建业务请求参数
    req = CustomRequest(
        order_id = "202009010016562012987",
        dealer_id = conf.dealer_id,
        broker_id = conf.broker_id,
        real_name = "张三",
        card_no = "6228888888888888888",
        id_card = "11010519891231002X",
        phone_no = "188****8888",
        pay = "100.00",
        pay_remark = "",
        notify_url = "https://www.example.com",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义 request-id
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.do_request(req_url, method_type, req)
        if resp.code == "0000":
            # 操作成功
            resp_data = CustomResponse(**resp.data)
            print("操作成功 ", resp_data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)
