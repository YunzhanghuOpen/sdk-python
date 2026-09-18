"""钱包余额扣减"""

from ...base import BaseRequest


class WalletDeductUserInfo(BaseRequest):
    """
    劳动者信息

    :type real_name: string
    :param real_name: 姓名

    :type id_card: string
    :param id_card: 证件号

    :type card_type: string
    :param card_type: 证件类型编码
    """
    def __init__(
        self,
        real_name = None,
        id_card = None,
        card_type = None
    ):
        super().__init__()
        self.real_name = real_name
        self.id_card = id_card
        self.card_type = card_type


class WalletDeductWalletBalance(BaseRequest):
    """
    钱包余额信息

    :type total_balance: string
    :param total_balance: 钱包总余额

    :type available_balance: string
    :param available_balance: 可用余额

    :type frozen_balance: string
    :param frozen_balance: 冻结余额

    :type version: str
    :param version: 版本号
    """
    def __init__(
        self,
        total_balance = None,
        available_balance = None,
        frozen_balance = None,
        version = None
    ):
        super().__init__()
        self.total_balance = total_balance
        self.available_balance = available_balance
        self.frozen_balance = frozen_balance
        self.version = version


class CreateWalletDeductRequest(BaseRequest):
    """
    申请钱包余额扣减请求-请求

    :type broker_id: string
    :param broker_id: 综合服务主体 ID

    :type dealer_id: string
    :param dealer_id: 平台企业 ID

    :type user_info: WalletDeductUserInfo
    :param user_info: 劳动者信息

    :type wallet_id: string
    :param wallet_id: 钱包 ID

    :type order_id: string
    :param order_id: 平台企业订单号

    :type scene: string
    :param scene: 业务场景

    :type amount: string
    :param amount: 申请扣减金额

    :type remark: string
    :param remark: 备注

    :type notify_url: string
    :param notify_url: 通知地址
    """
    def __init__(
        self,
        broker_id = None,
        dealer_id = None,
        user_info = None,
        wallet_id = None,
        order_id = None,
        scene = None,
        amount = None,
        remark = None,
        notify_url = None
    ):
        super().__init__()
        self.broker_id = broker_id
        self.dealer_id = dealer_id
        self.user_info = user_info
        self.wallet_id = wallet_id
        self.order_id = order_id
        self.scene = scene
        self.amount = amount
        self.remark = remark
        self.notify_url = notify_url


class CreateWalletDeductResponse(BaseRequest):
    """
    申请钱包余额扣减返回-响应

    :type order_id: string
    :param order_id: 平台企业订单号

    :type ref: string
    :param ref: 云账户钱包余额扣减订单号

    :type amount: string
    :param amount: 扣减金额
    """
    def __init__(
        self,
        order_id = None,
        ref = None,
        amount = None
    ):
        super().__init__()
        self.order_id = order_id
        self.ref = ref
        self.amount = amount


class QueryWalletDeductRequest(BaseRequest):
    """
    查询钱包余额扣减申请结果请求-请求

    :type broker_id: string
    :param broker_id: 综合服务主体 ID

    :type dealer_id: string
    :param dealer_id: 平台企业 ID

    :type order_id: string
    :param order_id: 平台企业订单号

    :type ref: string
    :param ref: 云账户钱包余额扣减订单号
    """
    def __init__(
        self,
        broker_id = None,
        dealer_id = None,
        order_id = None,
        ref = None
    ):
        super().__init__()
        self.broker_id = broker_id
        self.dealer_id = dealer_id
        self.order_id = order_id
        self.ref = ref


class QueryWalletDeductResponse(BaseRequest):
    """
    查询钱包余额扣减申请结果返回-响应

    :type broker_id: string
    :param broker_id: 综合服务主体 ID

    :type dealer_id: string
    :param dealer_id: 平台企业 ID

    :type user_info: WalletDeductUserInfo
    :param user_info: 劳动者信息

    :type wallet_id: string
    :param wallet_id: 钱包 ID

    :type order_id: string
    :param order_id: 平台企业订单号

    :type scene: string
    :param scene: 业务场景

    :type ref: string
    :param ref: 云账户钱包余额扣减订单号

    :type amount: string
    :param amount: 扣减金额

    :type remark: string
    :param remark: 备注

    :type status: string
    :param status: 申请处理状态

    :type status_detail: string
    :param status_detail: 申请处理状态详情

    :type status_message: string
    :param status_message: 申请处理状态描述

    :type status_detail_message: string
    :param status_detail_message: 申请处理状态详情描述

    :type created_at: string
    :param created_at: 创建时间

    :type finished_at: string
    :param finished_at: 处理完成时间

    :type user_received_amount: string
    :param user_received_amount: 劳动者实收金额

    :type user_debt_repayment_amount: string
    :param user_debt_repayment_amount: 劳动者历史订单需补缴税费金额

    :type wallet_outflow_amount: string
    :param wallet_outflow_amount: 钱包出账金额

    :type wallet_balance: WalletDeductWalletBalance
    :param wallet_balance: 钱包余额信息
    """
    def __init__(
        self,
        broker_id = None,
        dealer_id = None,
        user_info = None,
        wallet_id = None,
        order_id = None,
        scene = None,
        ref = None,
        amount = None,
        remark = None,
        status = None,
        status_detail = None,
        status_message = None,
        status_detail_message = None,
        created_at = None,
        finished_at = None,
        user_received_amount = None,
        user_debt_repayment_amount = None,
        wallet_outflow_amount = None,
        wallet_balance = None
    ):
        super().__init__()
        self.broker_id = broker_id
        self.dealer_id = dealer_id
        self.user_info = user_info
        self.wallet_id = wallet_id
        self.order_id = order_id
        self.scene = scene
        self.ref = ref
        self.amount = amount
        self.remark = remark
        self.status = status
        self.status_detail = status_detail
        self.status_message = status_message
        self.status_detail_message = status_detail_message
        self.created_at = created_at
        self.finished_at = finished_at
        self.user_received_amount = user_received_amount
        self.user_debt_repayment_amount = user_debt_repayment_amount
        self.wallet_outflow_amount = wallet_outflow_amount
        self.wallet_balance = wallet_balance


class CompleteWalletDeductRequest(BaseRequest):
    """
    提交钱包余额扣减结果请求-请求

    :type broker_id: string
    :param broker_id: 综合服务主体 ID

    :type dealer_id: string
    :param dealer_id: 平台企业 ID

    :type order_id: string
    :param order_id: 平台企业订单号

    :type ref: string
    :param ref: 云账户钱包余额扣减订单号

    :type status: string
    :param status: 结算状态

    :type trade_no: string
    :param trade_no: 平台企业扣减交易流水号

    :type finished_at: string
    :param finished_at: 支付完成时间
    """
    def __init__(
        self,
        broker_id = None,
        dealer_id = None,
        order_id = None,
        ref = None,
        status = None,
        trade_no = None,
        finished_at = None
    ):
        super().__init__()
        self.broker_id = broker_id
        self.dealer_id = dealer_id
        self.order_id = order_id
        self.ref = ref
        self.status = status
        self.trade_no = trade_no
        self.finished_at = finished_at


class CompleteWalletDeductResponse(BaseRequest):
    """
    提交钱包余额扣减结果返回-响应
    """
    def __init__(self):
        super().__init__()


class NotifyWalletDeductRequest(BaseRequest):
    """
    钱包余额扣减申请结果回调通知请求-请求

    :type notify_type: string
    :param notify_type: 通知类型

    :type broker_id: string
    :param broker_id: 综合服务主体 ID

    :type dealer_id: string
    :param dealer_id: 平台企业 ID

    :type user_info: WalletDeductUserInfo
    :param user_info: 劳动者信息

    :type wallet_id: string
    :param wallet_id: 钱包 ID

    :type order_id: string
    :param order_id: 平台企业订单号

    :type scene: string
    :param scene: 业务场景

    :type ref: string
    :param ref: 云账户钱包余额扣减订单号

    :type amount: string
    :param amount: 扣减金额

    :type remark: string
    :param remark: 备注

    :type status: string
    :param status: 申请处理状态

    :type status_detail: string
    :param status_detail: 申请处理状态详情

    :type status_message: string
    :param status_message: 申请处理状态描述

    :type status_detail_message: string
    :param status_detail_message: 申请处理状态详情描述

    :type created_at: string
    :param created_at: 创建时间

    :type finished_at: string
    :param finished_at: 处理完成时间

    :type user_received_amount: string
    :param user_received_amount: 劳动者实收金额

    :type user_debt_repayment_amount: string
    :param user_debt_repayment_amount: 劳动者历史订单需补缴税费金额

    :type wallet_outflow_amount: string
    :param wallet_outflow_amount: 钱包出账金额

    :type wallet_balance: WalletDeductWalletBalance
    :param wallet_balance: 钱包余额信息
    """
    def __init__(
        self,
        notify_type = None,
        broker_id = None,
        dealer_id = None,
        user_info = None,
        wallet_id = None,
        order_id = None,
        scene = None,
        ref = None,
        amount = None,
        remark = None,
        status = None,
        status_detail = None,
        status_message = None,
        status_detail_message = None,
        created_at = None,
        finished_at = None,
        user_received_amount = None,
        user_debt_repayment_amount = None,
        wallet_outflow_amount = None,
        wallet_balance = None
    ):
        super().__init__()
        self.notify_type = notify_type
        self.broker_id = broker_id
        self.dealer_id = dealer_id
        self.user_info = user_info
        self.wallet_id = wallet_id
        self.order_id = order_id
        self.scene = scene
        self.ref = ref
        self.amount = amount
        self.remark = remark
        self.status = status
        self.status_detail = status_detail
        self.status_message = status_message
        self.status_detail_message = status_detail_message
        self.created_at = created_at
        self.finished_at = finished_at
        self.user_received_amount = user_received_amount
        self.user_debt_repayment_amount = user_debt_repayment_amount
        self.wallet_outflow_amount = wallet_outflow_amount
        self.wallet_balance = wallet_balance
