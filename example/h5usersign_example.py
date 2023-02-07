# -*- coding: utf-8 -*-
from yzh_py.client.api.model.h5usersign import *
from yzh_py.client.api.h5usersign_client import H5UsersignClient
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
    # H5 预申请签约接口
    h5userpresignrequest = H5UserPresignRequest(
        dealer_id="",
        broker_id="",
        real_name="",
        id_card="",
        certificate_type="",
    )
    h5userpresignrequest_res = H5UsersignClient.h5_user_presign(h5userpresignrequest)
    print("H5 预申请签约接口返回：", h5userpresignrequest_res.code, h5userpresignrequest_res.message,
          h5userpresignrequest_res.data)

    # H5 签约接口
    h5usersignrequest = H5UserSignRequest(
        token="",
        color="",
        url="",
        redirect_url="",
    )
    h5usersignrequest_res = H5UsersignClient.h5_user_sign(h5usersignrequest)
    print("H5 签约接口返回：", h5usersignrequest_res.code, h5usersignrequest_res.message, h5usersignrequest_res.data)

    # H5 获取用户签约状态
    geth5usersignstatusrequest = GetH5UserSignStatusRequest(
        dealer_id="",
        broker_id="",
        real_name="",
        id_card="",
    )
    geth5usersignstatusrequest_res = H5UsersignClient.get_h5_user_sign_status(geth5usersignstatusrequest)
    print("H5 获取用户签约状态返回：", geth5usersignstatusrequest_res.code, geth5usersignstatusrequest_res.message,
          geth5usersignstatusrequest_res.data)

    # H5 对接测试解约接口
    h5userreleaserequest = H5UserReleaseRequest(
        broker_id="",
        dealer_id="",
        real_name="",
        id_card="",
        certificate_type="",
    )
    h5userreleaserequest_res = H5UsersignClient.h5_user_release(h5userreleaserequest)
    print("H5 对接测试解约接口返回：", h5userreleaserequest_res.code, h5userreleaserequest_res.message,
          h5userreleaserequest_res.data)





