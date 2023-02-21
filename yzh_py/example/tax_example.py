# -*- coding: utf-8 -*-
from yzh_py.client.api.model.tax import *
from yzh_py.client.api.tax_client import TaxClient
from yzh_py.example.utils.configinit import init_config

# 个人所得税扣缴明细表
if __name__ == '__main__':
    TaxClient = TaxClient(config=init_config())
    # 下载个人所得税扣缴明细表
    gettaxfilerequest = GetTaxFileRequest(
        dealer_id="",
        ent_id="",
        year_month="",
    )
    gettaxfilerequest_res = TaxClient.get_tax_file(gettaxfilerequest)
    print("下载个人所得税扣缴明细表返回：", gettaxfilerequest_res.code, gettaxfilerequest_res.message, gettaxfilerequest_res.data)

    # 查询纳税人是否为跨集团用户
    getusercrossrequest = GetUserCrossRequest(
        dealer_id="",
        year="",
        id_card="",
        ent_id="",
    )
    getusercrossrequest_res = TaxClient.get_user_cross(getusercrossrequest)
    print("查询纳税人是否为跨集团用户返回：", getusercrossrequest_res.code, getusercrossrequest_res.message,
          getusercrossrequest_res.data)
