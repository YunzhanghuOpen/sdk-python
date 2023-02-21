# -*- coding: utf-8 -*-
from yzh_py.client.api.model.h5usersign import *
from yzh_py.client.api.h5usersign_client import H5UsersignClient
from yzh_py.example.utils.configinit import init_config

# H5 签约
if __name__ == '__main__':
    H5UsersignClient = H5UsersignClient(config=init_config())
    # 预申请签约
    h5userpresignrequest = H5UserPresignRequest(
        dealer_id="",
        broker_id="",
        real_name="",
        id_card="",
        certificate_type="",
    )
    h5userpresignrequest_res = H5UsersignClient.h5_user_presign(h5userpresignrequest)
    print("预申请签约返回：", h5userpresignrequest_res.code, h5userpresignrequest_res.message,
          h5userpresignrequest_res.data)

    # 申请签约
    h5usersignrequest = H5UserSignRequest(
        token="",
        color="",
        url="",
        redirect_url="",
    )
    h5usersignrequest_res = H5UsersignClient.h5_user_sign(h5usersignrequest)
    print("申请签约返回：", h5usersignrequest_res.code, h5usersignrequest_res.message, h5usersignrequest_res.data)

    # 获取用户签约状态
    geth5usersignstatusrequest = GetH5UserSignStatusRequest(
        dealer_id="",
        broker_id="",
        real_name="",
        id_card="",
    )
    geth5usersignstatusrequest_res = H5UsersignClient.get_h5_user_sign_status(geth5usersignstatusrequest)
    print("获取用户签约状态返回：", geth5usersignstatusrequest_res.code, geth5usersignstatusrequest_res.message,
          geth5usersignstatusrequest_res.data)

    # 用户解约（测试账号专用接口）
    h5userreleaserequest = H5UserReleaseRequest(
        broker_id="",
        dealer_id="",
        real_name="",
        id_card="",
        certificate_type="",
    )
    h5userreleaserequest_res = H5UsersignClient.h5_user_release(h5userreleaserequest)
    print("用户解约（测试账号专用接口）返回：", h5userreleaserequest_res.code, h5userreleaserequest_res.message,
          h5userreleaserequest_res.data)