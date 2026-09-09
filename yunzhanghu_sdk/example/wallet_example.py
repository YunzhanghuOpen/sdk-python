# -*- coding: utf-8 -*-

from yunzhanghu_sdk.client.api.model.wallet import *
from yunzhanghu_sdk.client.api.wallet_client import WalletServiceClient
from yunzhanghu_sdk.example.utils.config_init import init_config

# 钱包余额查询
if __name__ == "__main__":
    conf = init_config()
    client = WalletServiceClient(config=conf)

    # 查询钱包余额
    req = QueryWalletBalanceRequest(
        dealer_id = conf.dealer_id,
        broker_id = conf.broker_id,
        user_info = WalletUserInfo(
            real_name = "张三",
            id_card = "11010519491231002X",
            card_type = "idcard",
        ),
        wallet_id = "wallet_123456",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义 request-id
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.query_wallet_balance(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)
