# -*- coding: utf-8 -*-
from yzh_py.client.api.model.dataservice import *
from yzh_py.client.api.dataservice_client import DataserviceClient
from yzh_py.example.utils.configinit import init_config

# 对账文件获取
if __name__ == '__main__':
    DataserviceClient = DataserviceClient(config=init_config())
    # 查询日订单文件
    getdailyorderfilerequest = GetDailyOrderFileRequest(
        order_date="",
    )
    getdailyorderfilerequest_res = DataserviceClient.get_daily_order_file(getdailyorderfilerequest)
    print("查询日订单文件返回：", getdailyorderfilerequest_res.code, getdailyorderfilerequest_res.message,
          getdailyorderfilerequest_res.data)

    # 查询日流水文件
    getdailybillfilev2request = GetDailyBillFileV2Request(
        bill_date="",
    )
    getdailybillfilev2request_res = DataserviceClient.get_daily_bill_file_v2(getdailybillfilev2request)
    print("查询日流水文件返回：", getdailybillfilev2request_res.code, getdailybillfilev2request_res.message,
          getdailybillfilev2request_res.data)

    # 查询平台企业预付业务服务费记录
    listdealerrechargerecordv2request = ListDealerRechargeRecordV2Request(
        begin_at="",
        end_at="",
    )
    listdealerrechargerecordv2request_res = DataserviceClient.list_dealer_recharge_record_v2(
        listdealerrechargerecordv2request)
    print("查询平台企业预付业务服务费记录返回：", listdealerrechargerecordv2request_res.code,
          listdealerrechargerecordv2request_res.message, listdealerrechargerecordv2request_res.data)

    # 查询日订单数据
    listdailyorderrequest = ListDailyOrderRequest(
        order_date="",
        offset="",
        length="",
        channel="",
        data_type="",
    )
    listdailyorderrequest_res = DataserviceClient.list_daily_order(listdailyorderrequest)
    print("查询日订单数据返回：", listdailyorderrequest_res.code, listdailyorderrequest_res.message,
          listdailyorderrequest_res.data)

    # 查询日订单文件（支付和退款订单）
    getdailyorderfilev2request = GetDailyOrderFileV2Request(
        order_date="",
    )
    getdailyorderfilev2request_res = DataserviceClient.get_daily_order_file_v2(getdailyorderfilev2request)
    print("查询日订单文件（支付和退款订单）返回：", getdailyorderfilev2request_res.code, getdailyorderfilev2request_res.message,
          getdailyorderfilev2request_res.data)

    # 查询日流水数据
    listdailybillrequest = ListDailyBillRequest(
        bill_date="",
        offset="",
        length="",
        data_type="",
    )
    listdailybillrequest_res = DataserviceClient.list_daily_bill(listdailybillrequest)
    print("查询日流水数据返回：", listdailybillrequest_res.code, listdailybillrequest_res.message, listdailybillrequest_res.data)

    # 获取余额日账单数据
    listbalancedailystatementrequest = ListBalanceDailyStatementRequest(
        statement_date="",
    )
    listbalancedailystatementrequest_res = DataserviceClient.list_balance_daily_statement(
        listbalancedailystatementrequest)
    print("获取余额日账单数据返回：", listbalancedailystatementrequest_res.code, listbalancedailystatementrequest_res.message,
          listbalancedailystatementrequest_res.data)