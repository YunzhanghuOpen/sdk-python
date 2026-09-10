# -*- coding: utf-8 -*-

from yunzhanghu_sdk.client.api.model.walletincome import *
from yunzhanghu_sdk.client.api.walletincome_client import WalletIncomeServiceClient
from yunzhanghu_sdk.example.utils.config_init import init_config
from yunzhanghu_sdk.utils import Utils

# 钱包余额入账
if __name__ == "__main__":
    conf = init_config()
    client = WalletIncomeServiceClient(config=conf)

    # 发起钱包余额入账
    req = CreateWalletIncomeRequest(
        dealer_id = conf.dealer_id,
        broker_id = conf.broker_id,
        user_info = Utils.copy_dict(WalletIncomeUserInfo(
            real_name = "张三",
            id_card = "11010519491231002X",
            card_type = "idcard",
            phone_no = "13800000000",
        ).__dict__),
        wallet_id = "wallet_123456",
        platform_info = Utils.copy_dict(WalletIncomePlatformInfo(
            platform_name = "xxx平台",
            user_id = "123456",
            user_nickname = "张三",
        ).__dict__),
        order_id = "20200903001656212987",
        amount = "300.00",
        earned_at = "2020-09-01 10:00:00",
        remark = "9月直播收入",
        notify_url = "https://www.example.com/income/notify",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义 request-id
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.create_wallet_income(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)

    # 查询钱包余额入账结果
    req = QueryWalletIncomeRequest(
        dealer_id = conf.dealer_id,
        broker_id = conf.broker_id,
        order_id = "20200903001656212987",
        ref = "176826728300001",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义 request-id
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.query_wallet_income(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)

    # 取消钱包收入计税订单
    req = CancelWalletIncomeRequest(
        dealer_id = conf.dealer_id,
        broker_id = conf.broker_id,
        order_id = "20200903001656212987",
        ref = "176826728300001",
        cancel_order_id = "20200903001656212988",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义 request-id
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.cancel_wallet_income(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)
