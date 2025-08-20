# -*- coding: utf-8 -*-

from yunzhanghu_sdk.client.api.model.calculatelabor import *
from yunzhanghu_sdk.client.api.calculatelabor_client import CalculateLaborServiceClient
from yunzhanghu_sdk.example.utils.config_init import init_config
from yunzhanghu_sdk.utils import Utils

# 连续劳务税费试算
if __name__ == "__main__":
    conf = init_config()
    client = CalculateLaborServiceClient(config=conf)

     # 连续劳务税费试算（计算器）
    req = LaborCaculatorRequest(
        dealer_id = conf.dealer_id,
        broker_id = conf.broker_id,
        month_settlement_list = [
            Utils.copy_dict(MonthSettlement(month=1,month_pre_tax_amount="10.00",).__dict__),
            Utils.copy_dict(MonthSettlement(month=2,month_pre_tax_amount="10.00",).__dict__),
        ],
    )
    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义 request-id
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.labor_caculator(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)

    # 订单税费试算
    req = CalcTaxRequest(
        dealer_id = conf.dealer_id,
        broker_id = conf.broker_id,
        real_name = "张三",
        id_card =   "11010519491231002X",
        pay =      "99",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义 request-id
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.calc_tax(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)
