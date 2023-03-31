# -*- coding: utf-8 -*-

from yunzhanghu_sdk.client.api.model.tax import *
from yunzhanghu_sdk.client.api.tax_client import TaxClient
from yunzhanghu_sdk.example.utils.config_init import init_config

# 个人所得税扣缴明细表
if __name__ == "__main__":
    tax_client = TaxClient(config=init_config())

    # 下载个人所得税扣缴明细表
    req = GetTaxFileRequest(
        dealer_id="",
        ent_id="",
        year_month="",
    )
    resp = tax_client.get_tax_file(req)
    print("下载个人所得税扣缴明细表返回：", resp.code, resp.message, resp.data)

    # 查询纳税人是否为跨集团用户
    req = GetUserCrossRequest(
        dealer_id="",
        year="",
        id_card="",
        ent_id="",
    )
    resp = tax_client.get_user_cross(req)
    print("查询纳税人是否为跨集团用户返回：", resp.code, resp.message, resp.data)
