# -*- coding: utf-8 -*-

from yunzhanghu_sdk.client.api.model.payment import *
from yunzhanghu_sdk.client.api.payment_client import PaymentClient
from yunzhanghu_sdk.example.utils.config_init import init_config

# 实时支付
if __name__ == "__main__":
    client = PaymentClient(config=init_config())

    # 银行卡实时支付
    req = CreateBankpayOrderRequest(
        order_id = "",
        dealer_id = "",
        broker_id = "",
        real_name = "",
        card_no = "",
        id_card = "",
        phone_no = "",
        pay = "",
        pay_remark = "",
        notify_url = "",
        project_id = "",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如平台企业未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.create_bankpay_order(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)

    # 支付宝实时支付
    req = CreateAlipayOrderRequest(
        order_id = "",
        dealer_id = "",
        broker_id = "",
        real_name = "",
        card_no = "",
        id_card = "",
        phone_no = "",
        pay = "",
        pay_remark = "",
        notify_url = "",
        project_id = "",
        check_name = "",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如平台企业未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.create_alipay_order(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)

    # 微信实时支付
    req = CreateWxpayOrderRequest(
        order_id = "",
        dealer_id = "",
        broker_id = "",
        real_name = "",
        openid = "",
        id_card = "",
        phone_no = "",
        pay = "",
        pay_remark = "",
        notify_url = "",
        wx_app_id = "",
        wxpay_mode = "",
        project_id = "",
        notes = "",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如平台企业未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.create_wxpay_order(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)

    # 查询单笔订单信息
    req = GetOrderRequest(
        order_id = "",
        channel = "",
        data_type = "",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如平台企业未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.get_order(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)

    # 查询平台企业余额
    req = ListAccountRequest(
        dealer_id = "",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如平台企业未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.list_account(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)

    # 查询电子回单
    req = GetEleReceiptFileRequest(
        order_id = "",
        ref = "",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如平台企业未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.get_ele_receipt_file(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)

    # 取消待支付订单
    req = CancelOrderRequest(
        dealer_id = "",
        order_id = "",
        ref = "",
        channel = "",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如平台企业未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.cancel_order(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)

    # 查询平台企业汇款信息
    req = GetDealerVARechargeAccountRequest(
        broker_id = "",
        dealer_id = "",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如平台企业未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.get_dealer_va_recharge_account(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)

    # 批次下单
    req = CreateBatchOrderRequest(
        batch_id = "",
        dealer_id = "",
        broker_id = "",
        channel = "",
        wx_app_id = "",
        total_pay = "",
        total_count = "",
        order_list=[],
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如平台企业未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.create_batch_order(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)

    # 批次确认
    req = ConfirmBatchOrderRequest(
        batch_id = "",
        dealer_id = "",
        broker_id = "",
        channel = "",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如平台企业未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.confirm_batch_order(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)

    # 批次撤销
    req = CancelBatchOrderRequest(
        batch_id = "",
        dealer_id = "",
        broker_id = "",
    )

    # request-id：请求 ID，请求的唯一标识
    # 建议平台企业自定义 request-id，并记录在日志中，便于问题发现及排查
    # 如平台企业未自定义 request-id，将使用 SDK 中的 UUID 方法自动生成。注意：UUID 方法生成的 request-id 不能保证全局唯一，推荐自定义
    req.request_id = "requestIdExample123456789"
    try:
        resp = client.cancel_batch_order(req)
        if resp.code == "0000":
            # 操作成功
            print("操作成功 ", resp.data)
        else:
            # 失败返回
            print("失败返回 ", "code：" + resp.code + " message：" + resp.message + " request_id：" + resp.request_id)
    except Exception as e:
        # 发生异常
        print(e)
