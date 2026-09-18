"""钱包余额提现"""

from ...base import BaseRequest


class WalletWithdrawUserInfo(BaseRequest):
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


class WalletWithdrawWalletBalance(BaseRequest):
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


class CreateWalletWithdrawRequest(BaseRequest):
    """
    发起钱包余额提现请求-请求

    :type broker_id: string
    :param broker_id: 综合服务主体 ID

    :type dealer_id: string
    :param dealer_id: 平台企业 ID

    :type user_info: WalletWithdrawUserInfo
    :param user_info: 劳动者信息

    :type wallet_id: string
    :param wallet_id: 钱包 ID

    :type order_id: string
    :param order_id: 平台企业订单号

    :type wx_app_id: string
    :param wx_app_id: 平台企业的微信 AppID

    :type amount: string
    :param amount: 提现金额

    :type channel: string
    :param channel: 提现渠道

    :type account: string
    :param account: 收款账号

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
        wx_app_id = None,
        amount = None,
        channel = None,
        account = None,
        remark = None,
        notify_url = None
    ):
        super().__init__()
        self.broker_id = broker_id
        self.dealer_id = dealer_id
        self.user_info = user_info
        self.wallet_id = wallet_id
        self.order_id = order_id
        self.wx_app_id = wx_app_id
        self.amount = amount
        self.channel = channel
        self.account = account
        self.remark = remark
        self.notify_url = notify_url


class CreateWalletWithdrawResponse(BaseRequest):
    """
    发起钱包余额提现返回-响应

    :type order_id: string
    :param order_id: 平台企业订单号

    :type ref: string
    :param ref: 云账户钱包余额提现订单号

    :type amount: string
    :param amount: 提现金额
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


class QueryWalletWithdrawRequest(BaseRequest):
    """
    查询钱包余额提现结果请求-请求

    :type broker_id: string
    :param broker_id: 综合服务主体 ID

    :type dealer_id: string
    :param dealer_id: 平台企业 ID

    :type channel: string
    :param channel: 提现渠道

    :type order_id: string
    :param order_id: 平台企业订单号

    :type ref: string
    :param ref: 云账户钱包余额提现订单号
    """
    def __init__(
        self,
        broker_id = None,
        dealer_id = None,
        channel = None,
        order_id = None,
        ref = None
    ):
        super().__init__()
        self.broker_id = broker_id
        self.dealer_id = dealer_id
        self.channel = channel
        self.order_id = order_id
        self.ref = ref


class QueryWalletWithdrawResponse(BaseRequest):
    """
    查询钱包余额提现结果返回-响应

    :type broker_id: string
    :param broker_id: 综合服务主体 ID

    :type dealer_id: string
    :param dealer_id: 平台企业 ID

    :type user_info: WalletWithdrawUserInfo
    :param user_info: 劳动者信息

    :type wallet_id: string
    :param wallet_id: 钱包 ID

    :type order_id: string
    :param order_id: 平台企业订单号

    :type ref: string
    :param ref: 云账户钱包余额提现订单号

    :type amount: string
    :param amount: 提现金额

    :type channel: string
    :param channel: 提现渠道

    :type account: string
    :param account: 收款账号

    :type wx_app_id: string
    :param wx_app_id: 平台企业的微信 AppID

    :type remark: string
    :param remark: 备注

    :type status: string
    :param status: 订单状态

    :type status_detail: string
    :param status_detail: 订单状态详情

    :type status_message: string
    :param status_message: 订单状态描述

    :type status_detail_message: string
    :param status_detail_message: 订单状态详情描述

    :type created_at: string
    :param created_at: 创建时间

    :type finished_at: string
    :param finished_at: 完成时间

    :type user_received_amount: string
    :param user_received_amount: 劳动者实收金额

    :type user_debt_repayment_amount: string
    :param user_debt_repayment_amount: 劳动者历史订单需补缴税费金额

    :type user_debt_repayment_personal_amount: string
    :param user_debt_repayment_personal_amount: 劳动者历史订单需补缴个税金额

    :type user_debt_repayment_added_amount: string
    :param user_debt_repayment_added_amount: 劳动者历史订单需补缴增附税金额

    :type wallet_outflow_amount: string
    :param wallet_outflow_amount: 钱包出账金额

    :type wallet_balance: WalletWithdrawWalletBalance
    :param wallet_balance: 钱包余额信息
    """
    def __init__(
        self,
        broker_id = None,
        dealer_id = None,
        user_info = None,
        wallet_id = None,
        order_id = None,
        ref = None,
        amount = None,
        channel = None,
        account = None,
        wx_app_id = None,
        remark = None,
        status = None,
        status_detail = None,
        status_message = None,
        status_detail_message = None,
        created_at = None,
        finished_at = None,
        user_received_amount = None,
        user_debt_repayment_amount = None,
        user_debt_repayment_personal_amount = None,
        user_debt_repayment_added_amount = None,
        wallet_outflow_amount = None,
        wallet_balance = None
    ):
        super().__init__()
        self.broker_id = broker_id
        self.dealer_id = dealer_id
        self.user_info = user_info
        self.wallet_id = wallet_id
        self.order_id = order_id
        self.ref = ref
        self.amount = amount
        self.channel = channel
        self.account = account
        self.wx_app_id = wx_app_id
        self.remark = remark
        self.status = status
        self.status_detail = status_detail
        self.status_message = status_message
        self.status_detail_message = status_detail_message
        self.created_at = created_at
        self.finished_at = finished_at
        self.user_received_amount = user_received_amount
        self.user_debt_repayment_amount = user_debt_repayment_amount
        self.user_debt_repayment_personal_amount = user_debt_repayment_personal_amount
        self.user_debt_repayment_added_amount = user_debt_repayment_added_amount
        self.wallet_outflow_amount = wallet_outflow_amount
        self.wallet_balance = wallet_balance


class CancelWalletWithdrawRequest(BaseRequest):
    """
    取消挂起的钱包余额提现订单请求-请求

    :type broker_id: string
    :param broker_id: 综合服务主体 ID

    :type dealer_id: string
    :param dealer_id: 平台企业 ID

    :type order_id: string
    :param order_id: 平台企业订单号

    :type ref: string
    :param ref: 云账户钱包余额提现订单号
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


class CancelWalletWithdrawResponse(BaseRequest):
    """
    取消挂起的钱包余额提现订单返回-响应
    """
    def __init__(self):
        super().__init__()


class RetryWalletWithdrawRequest(BaseRequest):
    """
    重试挂起的钱包余额提现订单请求-请求

    :type broker_id: string
    :param broker_id: 综合服务主体 ID

    :type dealer_id: string
    :param dealer_id: 平台企业 ID

    :type order_id: string
    :param order_id: 平台企业订单号

    :type ref: string
    :param ref: 云账户钱包余额提现订单号
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


class RetryWalletWithdrawResponse(BaseRequest):
    """
    重试挂起的钱包余额提现订单返回-响应
    """
    def __init__(self):
        super().__init__()


class GetWalletWithdrawReceiptFileRequest(BaseRequest):
    """
    查询钱包余额提现电子回单请求-请求

    :type broker_id: string
    :param broker_id: 综合服务主体 ID

    :type dealer_id: string
    :param dealer_id: 平台企业 ID

    :type order_id: string
    :param order_id: 平台企业订单号

    :type ref: string
    :param ref: 云账户钱包余额提现订单号

    :type receipt_type: string
    :param receipt_type: 回单类型，付款回单、退汇回单，若为空默认为付款回单
    """
    def __init__(
        self,
        broker_id = None,
        dealer_id = None,
        order_id = None,
        ref = None,
        receipt_type = None
    ):
        super().__init__()
        self.broker_id = broker_id
        self.dealer_id = dealer_id
        self.order_id = order_id
        self.ref = ref
        self.receipt_type = receipt_type


class GetWalletWithdrawReceiptFileResponse(BaseRequest):
    """
    查询钱包余额提现电子回单返回-响应

    :type expire_time: string
    :param expire_time: 链接失效时间

    :type file_name: string
    :param file_name: 回单名

    :type url: string
    :param url: 电子回单的下载链接，有效期 24 小时
    """
    def __init__(
        self,
        expire_time = None,
        file_name = None,
        url = None
    ):
        super().__init__()
        self.expire_time = expire_time
        self.file_name = file_name
        self.url = url


class NotifyWalletWithdrawRequest(BaseRequest):
    """
    通知钱包余额提现结果回调通知请求-请求

    :type notify_type: string
    :param notify_type: 通知类型

    :type broker_id: string
    :param broker_id: 综合服务主体 ID

    :type dealer_id: string
    :param dealer_id: 平台企业 ID

    :type user_info: WalletWithdrawUserInfo
    :param user_info: 劳动者信息

    :type wallet_id: string
    :param wallet_id: 钱包 ID

    :type order_id: string
    :param order_id: 平台企业订单号

    :type ref: string
    :param ref: 云账户钱包提现订单号

    :type amount: string
    :param amount: 提现金额支付金额

    :type channel: string
    :param channel: 提现渠道

    :type account: string
    :param account: 收款账号

    :type wx_app_id: string
    :param wx_app_id: 平台企业的微信 AppID

    :type remark: string
    :param remark: 备注

    :type status: string
    :param status: 订单状态

    :type status_detail: string
    :param status_detail: 订单状态详情

    :type status_message: string
    :param status_message: 订单状态描述

    :type status_detail_message: string
    :param status_detail_message: 订单状态详情描述

    :type created_at: string
    :param created_at: 创建时间

    :type finished_at: string
    :param finished_at: 完成时间

    :type user_received_amount: string
    :param user_received_amount: 劳动者实收金额

    :type user_debt_repayment_amount: string
    :param user_debt_repayment_amount: 劳动者历史订单需补缴税费金额

    :type user_debt_repayment_personal_amount: string
    :param user_debt_repayment_personal_amount: 劳动者历史订单需补缴个税金额

    :type user_debt_repayment_added_amount: string
    :param user_debt_repayment_added_amount: 劳动者历史订单需补缴增附税金额

    :type wallet_outflow_amount: string
    :param wallet_outflow_amount: 钱包出账金额

    :type wallet_balance: WalletWithdrawWalletBalance
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
        ref = None,
        amount = None,
        channel = None,
        account = None,
        wx_app_id = None,
        remark = None,
        status = None,
        status_detail = None,
        status_message = None,
        status_detail_message = None,
        created_at = None,
        finished_at = None,
        user_received_amount = None,
        user_debt_repayment_amount = None,
        user_debt_repayment_personal_amount = None,
        user_debt_repayment_added_amount = None,
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
        self.ref = ref
        self.amount = amount
        self.channel = channel
        self.account = account
        self.wx_app_id = wx_app_id
        self.remark = remark
        self.status = status
        self.status_detail = status_detail
        self.status_message = status_message
        self.status_detail_message = status_detail_message
        self.created_at = created_at
        self.finished_at = finished_at
        self.user_received_amount = user_received_amount
        self.user_debt_repayment_amount = user_debt_repayment_amount
        self.user_debt_repayment_personal_amount = user_debt_repayment_personal_amount
        self.user_debt_repayment_added_amount = user_debt_repayment_added_amount
        self.wallet_outflow_amount = wallet_outflow_amount
        self.wallet_balance = wallet_balance
