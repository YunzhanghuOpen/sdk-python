# -*- coding: utf-8 -*-

from yunzhanghu_sdk.client.api.model.dataservice import *
from yunzhanghu_sdk.client.api.dataservice_client import DataServiceClient
from yunzhanghu_sdk.example.utils.config_init import init_config

# 对账文件获取
if __name__ == "__main__":
    dataservice_client = DataServiceClient(config=init_config())

    # 查询日订单文件
    req = GetDailyOrderFileRequest(
        order_date="",
    )
    resp = dataservice_client.get_daily_order_file(req)
    print("查询日订单文件返回：", resp.code, resp.message, resp.data)

    # 查询日流水文件
    req = GetDailyBillFileV2Request(
        bill_date="",
    )
    resp = dataservice_client.get_daily_bill_file_v2(req)
    print("查询日流水文件返回：", resp.code, resp.message, resp.data)

    # 查询平台企业预付业务服务费记录
    req = ListDealerRechargeRecordV2Request(
        begin_at="",
        end_at="",
    )
    resp = dataservice_client.list_dealer_recharge_record_v2(req)
    print("查询平台企业预付业务服务费记录返回：", resp.code, resp.message, resp.data)

    # 查询日订单数据
    req = ListDailyOrderRequest(
        order_date="",
        offset="",
        length="",
        channel="",
        data_type="",
    )
    resp = dataservice_client.list_daily_order(req)
    print("查询日订单数据返回：", resp.code, resp.message, resp.data)

    # 查询日订单文件（支付和退款订单）
    req = GetDailyOrderFileV2Request(
        order_date="",
    )
    resp = dataservice_client.get_daily_order_file_v2(req)
    print("查询日订单文件（支付和退款订单）返回：", resp.code, resp.message, resp.data)

    # 查询日流水数据
    req = ListDailyBillRequest(
        bill_date="",
        offset="",
        length="",
        data_type="",
    )
    resp = dataservice_client.list_daily_bill(req)
    print("查询日流水数据返回：", resp.code, resp.message, resp.data)

    # 获取余额日账单数据
    req = ListBalanceDailyStatementRequest(
        statement_date="",
    )
    resp = dataservice_client.list_balance_daily_statement(req)
    print("获取余额日账单数据返回：", resp.code, resp.message, resp.data)
