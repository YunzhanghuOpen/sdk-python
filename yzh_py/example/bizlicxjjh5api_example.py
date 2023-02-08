# -*- coding: utf-8 -*-
from yzh_py.client.api.model.bizlicxjjh5api import *
from yzh_py.client.api.bizlicxjjh5api_client import Bizlicxjjh5ApiClient
from yzh_py.example.utils.configinit import init_config

if __name__ == '__main__':
    Bizlicxjjh5ApiClient = Bizlicxjjh5ApiClient(config=init_config())
    # 工商实名信息录入
    h5precollectbizlicmsgrequest = H5PreCollectBizlicMsgRequest(
        dealer_id="",
        broker_id="",
        dealer_user_id="",
        phone_no="",
        id_card="",
        real_name="",
        id_card_address="",
        id_card_agency="",
        id_card_nation="",
        id_card_validity_start="",
        id_card_validity_end="",
    )
    h5precollectbizlicmsgrequest_res = Bizlicxjjh5ApiClient.h5_pre_collect_bizlic_msg(h5precollectbizlicmsgrequest)
    print("工商实名信息录入返回：", h5precollectbizlicmsgrequest_res.code, h5precollectbizlicmsgrequest_res.message,
          h5precollectbizlicmsgrequest_res.data)

    # 预启动
    h5apigetstarturlrequest = H5APIGetStartUrlRequest(
        dealer_id="",
        broker_id="",
        dealer_user_id="",
        client_type="",
        notify_url="",
        color="",
        return_url="",
        custom_title="",
    )
    h5apigetstarturlrequest_res = Bizlicxjjh5ApiClient.h5_a_p_i_get_start_url(h5apigetstarturlrequest)
    print("预启动返回：", h5apigetstarturlrequest_res.code, h5apigetstarturlrequest_res.message,
          h5apigetstarturlrequest_res.data)

    # 查询个体工商户状态
    h5apiecocityaicstatusrequest = H5APIEcoCityAicStatusRequest(
        dealer_id="",
        broker_id="",
        dealer_user_id="",
        id_card="",
        real_name="",
        open_id="",
    )
    h5apiecocityaicstatusrequest_res = Bizlicxjjh5ApiClient.h5_a_p_i_eco_city_aic_status(h5apiecocityaicstatusrequest)
    print("查询个体工商户状态返回：", h5apiecocityaicstatusrequest_res.code, h5apiecocityaicstatusrequest_res.message,
          h5apiecocityaicstatusrequest_res.data)
