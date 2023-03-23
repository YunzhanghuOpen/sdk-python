# -*- coding: utf-8 -*-
from yunzhanghu_sdk.client.api.model.payment import *
from yunzhanghu_sdk.client.api.payment_client import PaymentClient
from yunzhanghu_sdk.example.utils.configinit import init_config

# 实时支付
if __name__ == '__main__':
    PaymentClient = PaymentClient(config=init_config())
    # 银行卡实时支付
    req = CreateBankpayOrderRequest(
        order_id="",
        dealer_id="",
        broker_id="",
        real_name="",
        card_no="",
        id_card="",
        phone_no="",
        pay="",
        pay_remark="",
        notify_url="",
        project_id="",
    )
    resp = PaymentClient.create_bankpay_order(req)
    print("银行卡实时支付返回：", resp.code, resp.message, resp.data)

    # 支付宝实时支付
    req = CreateAlipayOrderRequest(
        order_id="",
        dealer_id="",
        broker_id="",
        real_name="",
        card_no="",
        id_card="",
        phone_no="",
        pay="",
        pay_remark="",
        notify_url="",
        project_id="",
        check_name="",
    )
    resp = PaymentClient.create_alipay_order(req)
    print("支付宝实时支付返回：", resp.code,resp.message,resp.data)

    # 微信实时支付
    req = CreateWxpayOrderRequest(
        order_id="",
        dealer_id="",
        broker_id="",
        real_name="",
        openid="",
        id_card="",
        phone_no="",
        pay="",
        pay_remark="",
        notify_url="",
        wx_app_id="",
        wxpay_mode="",
        project_id="",
        notes="",
    )
    resp = PaymentClient.create_wxpay_order(req)
    print("微信实时支付返回：", resp.code, resp.message, resp.data)

    # 查询单笔订单信息
    req = GetOrderRequest(
        order_id="",
        channel="",
        data_type="",
    )
    resp = PaymentClient.get_order(req)
    print("查询单笔订单信息返回：", resp.code, resp.message, resp.data)

    # 查询平台企业余额
    req = ListAccountRequest(
        dealer_id="",
    )
    resp = PaymentClient.list_account(req)
    print("查询平台企业余额返回：", resp.code, resp.message, resp.data)

    # 查询电子回单
    req = GetEleReceiptFileRequest(
        order_id="",
        ref="",
    )
    resp = PaymentClient.get_ele_receipt_file(req)
    print("查询电子回单返回：", resp.code, resp.message, resp.data)

    # 取消待支付订单
    req = CancelOrderRequest(
        dealer_id="",
        order_id="",
        ref="",
        channel="",
    )
    resp = PaymentClient.cancel_order(req)
    print("取消待支付订单返回：", resp.code, resp.message, resp.data)

    # 查询平台企业汇款信息
    req = GetDealerVARechargeAccountRequest(
        broker_id="",
        dealer_id="",
    )
    resp = PaymentClient.get_dealer_va_recharge_account(req)
    print("查询平台企业汇款信息返回：", resp.code, resp.message, resp.data)

    # 批次下单
    req = CreateBatchOrderRequest(
        batch_id="",
        dealer_id="",
        broker_id="",
        channel="",
        wx_app_id="",
        total_pay="",
        total_count="",
        order_list="",
    )
    resp = PaymentClient.create_batch_order(req)
    print("批次下单返回：", resp.code, resp.message, resp.data)

    # 批次确认
    req = ConfirmBatchOrderRequest(
        batch_id="",
        dealer_id="",
        broker_id="",
        channel="",
    )
    resp = PaymentClient.confirm_batch_order(req)
    print("批次确认返回：", resp.code, resp.message, resp.data)