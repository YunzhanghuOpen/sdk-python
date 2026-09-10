# -*- coding: utf-8 -*-

from yunzhanghu_sdk.client.api.model.walletdeduct import *
from yunzhanghu_sdk.client.api.walletdeduct_client import WalletDeductServiceClient
from yunzhanghu_sdk.example.utils.config_init import init_config
from yunzhanghu_sdk.utils import Utils

# 钱包余额扣减
if __name__ == "__main__":
    conf = init_config()
    client = WalletDeductServiceClient(config=conf)

    # 申请钱包余额扣减
    req = CreateWalletDeductRequest(
        dealer_id = conf.dealer_id,
        broker_id = conf.broker_id,
        user_info = Utils.copy_dict(WalletDeductUserInfo(
            real_name = "张三",
            id_card = "11010519491231002X",
            card_type = "idcard",
        ).__dict__),
        wallet_id = "wallet_123456",
        order_id = "20200903001656212987",
        scene = "3",
        amount = "300.00",
        remark = "根据平台企业规则扣减",
        notify_url = "https://www.example.com/realtime/notify",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义 request-id
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.create_wallet_deduct(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)

    # 查询钱包余额扣减申请结果
    req = QueryWalletDeductRequest(
        dealer_id = conf.dealer_id,
        broker_id = conf.broker_id,
        order_id = "20200903001656212987",
        ref = "176826728300002",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义 request-id
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.query_wallet_deduct(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)

    # 提交钱包余额扣减结果
    req = CompleteWalletDeductRequest(
        dealer_id = conf.dealer_id,
        broker_id = conf.broker_id,
        order_id = "20200903001656212987",
        ref = "176826728300002",
        status = "1",
        trade_no = "202010150030000001",
        finished_at = "2020-10-15 00:30:00",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义 request-id
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.complete_wallet_deduct(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)
