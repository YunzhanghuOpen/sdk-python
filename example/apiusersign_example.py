# -*- coding: utf-8 -*-
from yzh_py.client.api.model.apiusersign import *
from yzh_py.client.api.apiusersign_client import ApiusersignClient
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

    # 获取协议预览 URL
    apiusesigncontractrequest = ApiUseSignContractRequest(
        dealer_id="",
        broker_id="",
    )
    apiusesigncontractrequest_res = ApiusersignClient.api_use_sign_contract(apiusesigncontractrequest)
    print("获取协议预览 URL返回：", apiusesigncontractrequest_res.code, apiusesigncontractrequest_res.message,
          apiusesigncontractrequest_res.data)

    # 用户签约
    apiusersignrequest = ApiUserSignRequest(
        broker_id="",
        dealer_id="",
        real_name="",
        id_card="",
        card_type="",
    )
    apiusersignrequest_res = ApiusersignClient.api_user_sign(apiusersignrequest)
    print("用户签约返回：", apiusersignrequest_res.code, apiusersignrequest_res.message, apiusersignrequest_res.data)

    # 获取用户签约状态
    getapiusersignstatusrequest = GetApiUserSignStatusRequest(
        dealer_id="",
        broker_id="",
        real_name="",
        id_card="",
    )
    getapiusersignstatusrequest_res = ApiusersignClient.get_api_user_sign_status(getapiusersignstatusrequest)
    print("获取用户签约状态返回：", getapiusersignstatusrequest_res.code, getapiusersignstatusrequest_res.message,
          getapiusersignstatusrequest_res.data)

    # 用户解约（测试账号专用接口）
    apiusersignreleaserequest = ApiUserSignReleaseRequest(
        broker_id="",
        dealer_id="",
        real_name="",
        id_card="",
        card_type="",
    )
    apiusersignreleaserequest_res = ApiusersignClient.api_user_sign_release(apiusersignreleaserequest)
    print("用户解约（测试账号专用接口）返回：", apiusersignreleaserequest_res.code, apiusersignreleaserequest_res.message,
          apiusersignreleaserequest_res.data)


