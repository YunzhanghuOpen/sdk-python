# -*- coding: utf-8 -*-
from yzh_py.client.api.model.payment import *
from yzh_py.client.api.payment_client import PaymentClient
from yzh_py.example.utils.configinit import init_config

# 实时支付
if __name__ == '__main__':
    PaymentClient = PaymentClient(config=init_config())
    # 银行卡实时下单
    createbankpayorderrequest = CreateBankpayOrderRequest(
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
    createbankpayorderrequest_res=PaymentClient.create_bankpay_order(createbankpayorderrequest)
    print("银行卡实时下单返回：", createbankpayorderrequest_res.code,createbankpayorderrequest_res.message,createbankpayorderrequest_res.data)

    # 支付宝实时下单
    createalipayorderrequest = CreateAlipayOrderRequest(
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
    createalipayorderrequest_res=PaymentClient.create_alipay_order(createalipayorderrequest)
    print("支付宝实时下单返回：", createalipayorderrequest_res.code,createalipayorderrequest_res.message,createalipayorderrequest_res.data)

    # 微信实时下单
    createwxpayorderrequest = CreateWxpayOrderRequest(
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
    createwxpayorderrequest_res = PaymentClient.create_wxpay_order(createwxpayorderrequest)
    print("微信实时下单返回：", createwxpayorderrequest_res.code, createwxpayorderrequest_res.message, createwxpayorderrequest_res.data)

    # 查询单笔订单信息
    getorderrequest = GetOrderRequest(
        order_id="",
        channel="",
        data_type="",
    )
    getorderrequest_res = PaymentClient.get_order(getorderrequest)
    print("查询单笔订单信息返回：", getorderrequest_res.code, getorderrequest_res.message, getorderrequest_res.data)

    # 查询平台企业汇款信息
    getdealervarechargeaccountrequest = GetDealerVARechargeAccountRequest(
        broker_id="",
        dealer_id="",
    )
    getdealervarechargeaccountrequest_res = PaymentClient.get_dealer_v_a_recharge_account(getdealervarechargeaccountrequest)
    print("查询平台企业汇款信息返回：", getdealervarechargeaccountrequest_res.code, getdealervarechargeaccountrequest_res.message,getdealervarechargeaccountrequest_res.data)

    # 取消待支付订单
    cancelorderrequest = CancelOrderRequest(
        dealer_id="",
        order_id="",
        ref="",
        channel="",
    )
    cancelorderrequest_res = PaymentClient.cancel_order(cancelorderrequest)
    print("取消待支付订单返回：", cancelorderrequest_res.code, cancelorderrequest_res.message, cancelorderrequest_res.data)

    # 查询平台企业余额
    listaccountrequest = ListAccountRequest(
        dealer_id="",
    )
    listaccountrequest_res = PaymentClient.list_account(listaccountrequest)
    print("查询平台企业余额返回：", listaccountrequest_res.code, listaccountrequest_res.message, listaccountrequest_res.data)

    # 查询电子回单
    getelereceiptfilerequest = GetEleReceiptFileRequest(
        order_id="",
        ref="",
    )
    getelereceiptfilerequest_res = PaymentClient.get_ele_receipt_file(getelereceiptfilerequest)
    print("查询电子回单返回：", getelereceiptfilerequest_res.code, getelereceiptfilerequest_res.message,getelereceiptfilerequest_res.data)

    # 批次下单
    createbatchorderrequest = CreateBatchOrderRequest(
        batch_id="",
        dealer_id="",
        broker_id="",
        channel="",
        wx_app_id="",
        total_pay="",
        total_count="",
        order_list="",
    )
    createbatchorderrequest_res = PaymentClient.create_batch_order(createbatchorderrequest)
    print("批次下单返回：", createbatchorderrequest_res.code, createbatchorderrequest_res.message,
          createbatchorderrequest_res.data)

    # 批次确认
    confirmbatchorderrequest = ConfirmBatchOrderRequest(
        batch_id="",
        dealer_id="",
        broker_id="",
        channel="",
    )
    confirmbatchorderrequest_res = PaymentClient.confirm_batch_order(confirmbatchorderrequest)
    print("批次确认返回：", confirmbatchorderrequest_res.code, confirmbatchorderrequest_res.message,
          confirmbatchorderrequest_res.data)