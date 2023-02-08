# -*- coding: utf-8 -*-
from yzh_py.client.api.model.bizlicxjjh5 import *
from yzh_py.client.api.bizlicxjjh5_client import Bizlicxjjh5Client
from yzh_py.example.utils.configinit import init_config

if __name__ == '__main__':
    Bizlicxjjh5Client = Bizlicxjjh5Client(config=init_config())
    # 预启动
    h5getstarturlrequest = H5GetStartUrlRequest(
        dealer_id="",
        broker_id="",
        dealer_user_id="",
        client_type="",
        notify_url="",
        color="",
        return_url="",
        custom_title="",
    )
    h5getstarturlrequest_res = Bizlicxjjh5Client.h5_get_start_url(h5getstarturlrequest)
    print("预启动返回：", h5getstarturlrequest_res.code, h5getstarturlrequest_res.message, h5getstarturlrequest_res.data)

    # 查询个体工商户状态
    h5ecocityaicstatusrequest = H5EcoCityAicStatusRequest(
        dealer_id="",
        broker_id="",
        dealer_user_id="",
        id_card="",
        real_name="",
        open_id="",
    )
    h5ecocityaicstatusrequest_res = Bizlicxjjh5Client.h5_eco_city_aic_status(h5ecocityaicstatusrequest)
    print("查询个体工商户状态返回：", h5ecocityaicstatusrequest_res.code, h5ecocityaicstatusrequest_res.message,
          h5ecocityaicstatusrequest_res.data)