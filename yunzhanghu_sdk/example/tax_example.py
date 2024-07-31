# -*- coding: utf-8 -*-

from yunzhanghu_sdk.client.api.model.tax import *
from yunzhanghu_sdk.client.api.tax_client import TaxClient
from yunzhanghu_sdk.example.utils.config_init import init_config

# 个人所得税申报明细表
if __name__ == "__main__":
    conf = init_config()
    client = TaxClient(config=conf)

    # 下载个人所得税申报明细表
    req = GetTaxFileRequest(
        dealer_id = conf.dealer_id,
        ent_id = "accumulus_tj",
        year_month = "2020-01",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义 request-id
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.get_tax_file(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)

    # 查询纳税人是否为跨集团用户
    req = GetUserCrossRequest(
        dealer_id = conf.dealer_id,
        year = "2020",
        id_card = "11010519491231002X",
        ent_id = "accumulus_tj",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义 request-id
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.get_user_cross(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)
