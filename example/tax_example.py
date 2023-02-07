# -*- coding: utf-8 -*-
from yzh_py.client.api.model.tax import *
from yzh_py.client.api.tax_client import TaxClient
from yzh_py.config import *



if __name__ == '__main__':
    # dealer_id 平台企业 ID
    dealer_id = "xxx"
    # broker_id 综合服务主体 ID
    broker_id = "xxx"
    # sign_type 签名类型
    sign_type = "xxx"
    # app_key
    app_key = "xxx"
    # des3key
    des3key = "xxx"
    # dealer_private_key 平台企业私钥
    dealer_private_key = '''
        -----BEGIN PRIVATE KEY-----
        xxx
        '''
    # yzh_public_key 云账户公钥
    yzh_public_key = '''
        xxx
        '''

    # 初始化配置参数
    config = Config(
        # host 请求域名
        host="https://api-service.yunzhanghu.com",
        dealer_id=dealer_id,
        sign_type=sign_type,
        app_key=app_key,
        des3key=des3key,
        dealer_private_key=dealer_private_key,
        yzh_public_key=yzh_public_key,
    )

    # 下载个税扣缴明细表
    gettaxfilerequest = GetTaxFileRequest(
        dealer_id="",
        ent_id="",
        year_month="",
    )
    gettaxfilerequest_res = TaxClient.get_tax_file(gettaxfilerequest)
    print("下载个税扣缴明细表返回：", gettaxfilerequest_res.code, gettaxfilerequest_res.message, gettaxfilerequest_res.data)

    # GetUserCross 查询纳税人是否为跨集团用户
    getusercrossrequest = GetUserCrossRequest(
        dealer_id="",
        year="",
        id_card="",
        ent_id="",
    )
    getusercrossrequest_res = TaxClient.get_user_cross(getusercrossrequest)
    print("GetUserCross 查询纳税人是否为跨集团用户返回：", getusercrossrequest_res.code, getusercrossrequest_res.message,
          getusercrossrequest_res.data)






