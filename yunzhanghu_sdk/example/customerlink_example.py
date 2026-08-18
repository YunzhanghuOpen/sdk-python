# -*- coding: utf-8 -*-

from yunzhanghu_sdk.example.utils.config_init import init_config
from yunzhanghu_sdk.utils import Utils

# 生成专属服务链接
if __name__ == "__main__":
    conf = init_config()
    ret = Utils.get_customer_link(conf, "https://www.example.com", 'testmemberid')
    print(ret)
