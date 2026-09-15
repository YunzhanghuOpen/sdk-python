"""钱包余额入账"""

from ...base import BaseRequest


class WalletIncomeUserInfo(BaseRequest):
    """
    劳动者信息

    :type real_name: string
    :param real_name: 姓名

    :type id_card: string
    :param id_card: 证件号

    :type card_type: string
    :param card_type: 证件类型编码

    :type phone_no: string
    :param phone_no: 手机号
    """
    def __init__(
        self,
        real_name = None,
        id_card = None,
        card_type = None,
        phone_no = None
    ):
        super().__init__()
        self.real_name = real_name
        self.id_card = id_card
        self.card_type = card_type
        self.phone_no = phone_no


class WalletIncomePlatformInfo(BaseRequest):
    """
    平台信息

    :type platform_name: string
    :param platform_name: 互联网平台名称

    :type user_id: string
    :param user_id: 劳动者 ID

    :type user_nickname: string
    :param user_nickname: 劳动者名称或昵称
    """
    def __init__(
        self,
        platform_name = None,
        user_id = None,
        user_nickname = None
    ):
        super().__init__()
        self.platform_name = platform_name
        self.user_id = user_id
        self.user_nickname = user_nickname


class WalletIncomeWalletBalance(BaseRequest):
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


class WalletIncomeFeeInfo(BaseRequest):
    """
    服务费信息

    :type total_fee: string
    :param total_fee: 总服务费

    :type total_fee_rate: string
    :param total_fee_rate: 总服务费率

    :type dealer_fee: string
    :param dealer_fee: 平台企业加成服务费

    :type dealer_fee_rate: string
    :param dealer_fee_rate: 平台企业加成服务费率

    :type dealer_deduct_fee: string
    :param dealer_deduct_fee: 抵扣账户支付的加成服务费

    :type dealer_payable_fee: string
    :param dealer_payable_fee: 抵扣后应支付的加成服务费

    :type user_fee: string
    :param user_fee: 劳动者加成服务费

    :type user_fee_rate: string
    :param user_fee_rate: 劳动者加成服务费率
    """
    def __init__(
        self,
        total_fee = None,
        total_fee_rate = None,
        dealer_fee = None,
        dealer_fee_rate = None,
        dealer_deduct_fee = None,
        dealer_payable_fee = None,
        user_fee = None,
        user_fee_rate = None
    ):
        super().__init__()
        self.total_fee = total_fee
        self.total_fee_rate = total_fee_rate
        self.dealer_fee = dealer_fee
        self.dealer_fee_rate = dealer_fee_rate
        self.dealer_deduct_fee = dealer_deduct_fee
        self.dealer_payable_fee = dealer_payable_fee
        self.user_fee = user_fee
        self.user_fee_rate = user_fee_rate


class WalletIncomeTaxParty(BaseRequest):
    """
    税费承担方明细

    :type total_tax: string
    :param total_tax: 税费总额

    :type personal_tax: string
    :param personal_tax: 个人所得税

    :type value_added_tax: string
    :param value_added_tax: 增值税

    :type additional_tax: string
    :param additional_tax: 附加税

    :type additional_urban_tax: string
    :param additional_urban_tax: 城市维护建设税

    :type additional_tuition_tax: string
    :param additional_tuition_tax: 教育费附加

    :type additional_local_tuition_tax: string
    :param additional_local_tuition_tax: 地方教育附加
    """
    def __init__(
        self,
        total_tax = None,
        personal_tax = None,
        value_added_tax = None,
        additional_tax = None,
        additional_urban_tax = None,
        additional_tuition_tax = None,
        additional_local_tuition_tax = None
    ):
        super().__init__()
        self.total_tax = total_tax
        self.personal_tax = personal_tax
        self.value_added_tax = value_added_tax
        self.additional_tax = additional_tax
        self.additional_urban_tax = additional_urban_tax
        self.additional_tuition_tax = additional_tuition_tax
        self.additional_local_tuition_tax = additional_local_tuition_tax


class WalletIncomeTaxDetail(BaseRequest):
    """
    计税信息

    :type personal_tax_rate: string
    :param personal_tax_rate: 个税税率

    :type deduct_tax: string
    :param deduct_tax: 个税速算扣除数

    :type basic_deducted: string
    :param basic_deducted: 基本减除费用扣除

    :type total: WalletIncomeTaxParty
    :param total: 税费总额及明细

    :type user: WalletIncomeTaxParty
    :param user: 劳动者承担税费

    :type dealer: WalletIncomeTaxParty
    :param dealer: 平台企业承担税费

    :type broker: WalletIncomeTaxParty
    :param broker: 云账户承担税费
    """
    def __init__(
        self,
        personal_tax_rate = None,
        deduct_tax = None,
        basic_deducted = None,
        total = None,
        user = None,
        dealer = None,
        broker = None
    ):
        super().__init__()
        self.personal_tax_rate = personal_tax_rate
        self.deduct_tax = deduct_tax
        self.basic_deducted = basic_deducted
        self.total = total
        self.user = user
        self.dealer = dealer
        self.broker = broker


class WalletIncomeTaxInfo(BaseRequest):
    """
    税费信息

    :type original: WalletIncomeTaxDetail
    :param original: 下单计税信息

    :type current: WalletIncomeTaxDetail
    :param current: 当前计税信息
    """
    def __init__(
        self,
        original = None,
        current = None
    ):
        super().__init__()
        self.original = original
        self.current = current


class WalletIncomeCancelFeeInfo(BaseRequest):
    """
    取消计税退还服务费信息

    :type total_fee: string
    :param total_fee: 总服务费

    :type dealer_fee: string
    :param dealer_fee: 平台企业加成服务费

    :type dealer_deduct_fee: string
    :param dealer_deduct_fee: 抵扣账户支付的加成服务费

    :type dealer_payable_fee: string
    :param dealer_payable_fee: 抵扣后应支付的加成服务费

    :type user_fee: string
    :param user_fee: 劳动者加成服务费
    """
    def __init__(
        self,
        total_fee = None,
        dealer_fee = None,
        dealer_deduct_fee = None,
        dealer_payable_fee = None,
        user_fee = None
    ):
        super().__init__()
        self.total_fee = total_fee
        self.dealer_fee = dealer_fee
        self.dealer_deduct_fee = dealer_deduct_fee
        self.dealer_payable_fee = dealer_payable_fee
        self.user_fee = user_fee


class WalletIncomeCancelTaxInfo(BaseRequest):
    """
    取消计税退还税费信息

    :type total: WalletIncomeTaxParty
    :param total: 税费总额及明细

    :type user: WalletIncomeTaxParty
    :param user: 劳动者承担税费

    :type dealer: WalletIncomeTaxParty
    :param dealer: 平台企业承担税费

    :type broker: WalletIncomeTaxParty
    :param broker: 云账户承担税费
    """
    def __init__(
        self,
        total = None,
        user = None,
        dealer = None,
        broker = None
    ):
        super().__init__()
        self.total = total
        self.user = user
        self.dealer = dealer
        self.broker = broker


class WalletIncomeCancelDetail(BaseRequest):
    """
    取消计税处理明细

    :type fee_info: WalletIncomeCancelFeeInfo
    :param fee_info: 服务费信息

    :type tax_info: WalletIncomeCancelTaxInfo
    :param tax_info: 税费信息

    :type wallet_outflow_amount: string
    :param wallet_outflow_amount: 劳动者钱包扣减金额

    :type user_debt_repayment_amount: string
    :param user_debt_repayment_amount: 历史订单补缴税费退回金额

    :type wallet_balance: WalletIncomeWalletBalance
    :param wallet_balance: 钱包余额信息
    """
    def __init__(
        self,
        fee_info = None,
        tax_info = None,
        wallet_outflow_amount = None,
        user_debt_repayment_amount = None,
        wallet_balance = None
    ):
        super().__init__()
        self.fee_info = fee_info
        self.tax_info = tax_info
        self.wallet_outflow_amount = wallet_outflow_amount
        self.user_debt_repayment_amount = user_debt_repayment_amount
        self.wallet_balance = wallet_balance


class CreateWalletIncomeRequest(BaseRequest):
    """
    发起钱包余额入账请求-请求

    :type broker_id: string
    :param broker_id: 综合服务主体 ID

    :type dealer_id: string
    :param dealer_id: 平台企业 ID

    :type user_info: WalletIncomeUserInfo
    :param user_info: 劳动者信息

    :type wallet_id: string
    :param wallet_id: 钱包 ID

    :type platform_info: WalletIncomePlatformInfo
    :param platform_info: 平台信息

    :type order_id: string
    :param order_id: 平台企业订单号

    :type amount: string
    :param amount: 下单金额

    :type earned_at: string
    :param earned_at: 获得收入时间

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
        platform_info = None,
        order_id = None,
        amount = None,
        earned_at = None,
        remark = None,
        notify_url = None
    ):
        super().__init__()
        self.broker_id = broker_id
        self.dealer_id = dealer_id
        self.user_info = user_info
        self.wallet_id = wallet_id
        self.platform_info = platform_info
        self.order_id = order_id
        self.amount = amount
        self.earned_at = earned_at
        self.remark = remark
        self.notify_url = notify_url


class CreateWalletIncomeResponse(BaseRequest):
    """
    发起钱包余额入账返回-响应

    :type order_id: string
    :param order_id: 平台企业订单号

    :type ref: string
    :param ref: 云账户钱包入账订单号

    :type amount: string
    :param amount: 税前收入金额
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


class QueryWalletIncomeRequest(BaseRequest):
    """
    查询钱包余额入账结果请求-请求

    :type broker_id: string
    :param broker_id: 综合服务主体 ID

    :type dealer_id: string
    :param dealer_id: 平台企业 ID

    :type order_id: string
    :param order_id: 平台企业订单号

    :type ref: string
    :param ref: 云账户钱包入账订单号
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


class QueryWalletIncomeResponse(BaseRequest):
    """
    查询钱包余额入账结果返回-响应

    :type broker_id: string
    :param broker_id: 综合服务主体 ID

    :type dealer_id: string
    :param dealer_id: 平台企业 ID

    :type user_info: WalletIncomeUserInfo
    :param user_info: 劳动者信息

    :type wallet_id: string
    :param wallet_id: 钱包 ID

    :type platform_info: WalletIncomePlatformInfo
    :param platform_info: 平台信息

    :type order_id: string
    :param order_id: 平台企业订单号

    :type ref: string
    :param ref: 云账户钱包入账订单号

    :type amount: string
    :param amount: 下单金额

    :type before_tax_amount: string
    :param before_tax_amount: 税前金额

    :type remark: string
    :param remark: 备注

    :type earned_at: string
    :param earned_at: 获得收入时间

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

    :type fee_info: WalletIncomeFeeInfo
    :param fee_info: 服务费信息

    :type tax_info: WalletIncomeTaxInfo
    :param tax_info: 税费信息

    :type user_debt_repayment_amount: string
    :param user_debt_repayment_amount: 劳动者历史订单需补缴税费金额

    :type wallet_inflow_amount: string
    :param wallet_inflow_amount: 钱包入账金额

    :type wallet_balance: WalletIncomeWalletBalance
    :param wallet_balance: 钱包余额信息
    """
    def __init__(
        self,
        broker_id = None,
        dealer_id = None,
        user_info = None,
        wallet_id = None,
        platform_info = None,
        order_id = None,
        ref = None,
        amount = None,
        before_tax_amount = None,
        remark = None,
        earned_at = None,
        status = None,
        status_detail = None,
        status_message = None,
        status_detail_message = None,
        created_at = None,
        finished_at = None,
        fee_info = None,
        tax_info = None,
        user_debt_repayment_amount = None,
        wallet_inflow_amount = None,
        wallet_balance = None
    ):
        super().__init__()
        self.broker_id = broker_id
        self.dealer_id = dealer_id
        self.user_info = user_info
        self.wallet_id = wallet_id
        self.platform_info = platform_info
        self.order_id = order_id
        self.ref = ref
        self.amount = amount
        self.before_tax_amount = before_tax_amount
        self.remark = remark
        self.earned_at = earned_at
        self.status = status
        self.status_detail = status_detail
        self.status_message = status_message
        self.status_detail_message = status_detail_message
        self.created_at = created_at
        self.finished_at = finished_at
        self.fee_info = fee_info
        self.tax_info = tax_info
        self.user_debt_repayment_amount = user_debt_repayment_amount
        self.wallet_inflow_amount = wallet_inflow_amount
        self.wallet_balance = wallet_balance


class CancelWalletIncomeRequest(BaseRequest):
    """
    取消钱包收入计税订单请求-请求

    :type broker_id: string
    :param broker_id: 综合服务主体 ID

    :type dealer_id: string
    :param dealer_id: 平台企业 ID

    :type order_id: string
    :param order_id: 平台企业订单号

    :type ref: string
    :param ref: 云账户钱包入账订单号

    :type cancel_order_id: string
    :param cancel_order_id: 取消钱包收入计税订单号
    """
    def __init__(
        self,
        broker_id = None,
        dealer_id = None,
        order_id = None,
        ref = None,
        cancel_order_id = None
    ):
        super().__init__()
        self.broker_id = broker_id
        self.dealer_id = dealer_id
        self.order_id = order_id
        self.ref = ref
        self.cancel_order_id = cancel_order_id


class CancelWalletIncomeResponse(BaseRequest):
    """
    取消钱包收入计税订单返回-响应

    :type broker_id: string
    :param broker_id: 综合服务主体 ID

    :type dealer_id: string
    :param dealer_id: 平台企业 ID

    :type order_id: string
    :param order_id: 平台企业订单号

    :type ref: string
    :param ref: 云账户钱包入账订单号

    :type cancel_order_id: string
    :param cancel_order_id: 取消钱包收入计税订单号

    :type cancel_result_type: string
    :param cancel_result_type: 取消结果类型

    :type cancel_detail: WalletIncomeCancelDetail
    :param cancel_detail: 取消明细
    """
    def __init__(
        self,
        broker_id = None,
        dealer_id = None,
        order_id = None,
        ref = None,
        cancel_order_id = None,
        cancel_result_type = None,
        cancel_detail = None
    ):
        super().__init__()
        self.broker_id = broker_id
        self.dealer_id = dealer_id
        self.order_id = order_id
        self.ref = ref
        self.cancel_order_id = cancel_order_id
        self.cancel_result_type = cancel_result_type
        self.cancel_detail = cancel_detail


class NotifyWalletIncomeRequest(BaseRequest):
    """
    钱包余额入账结果回调通知请求-请求

    :type notify_type: string
    :param notify_type: 通知类型

    :type broker_id: string
    :param broker_id: 综合服务主体 ID

    :type dealer_id: string
    :param dealer_id: 平台企业 ID

    :type user_info: WalletIncomeUserInfo
    :param user_info: 劳动者信息

    :type wallet_id: string
    :param wallet_id: 钱包 ID

    :type platform_info: WalletIncomePlatformInfo
    :param platform_info: 平台信息

    :type order_id: string
    :param order_id: 平台企业订单号

    :type ref: string
    :param ref: 云账户钱包入账订单号

    :type amount: string
    :param amount: 下单金额

    :type before_tax_amount: string
    :param before_tax_amount: 税前金额

    :type remark: string
    :param remark: 备注

    :type earned_at: string
    :param earned_at: 获得收入时间

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

    :type fee_info: WalletIncomeFeeInfo
    :param fee_info: 服务费信息

    :type tax_info: WalletIncomeTaxInfo
    :param tax_info: 税费信息

    :type user_debt_repayment_amount: string
    :param user_debt_repayment_amount: 劳动者历史订单需补缴税费金额

    :type wallet_inflow_amount: string
    :param wallet_inflow_amount: 钱包入账金额

    :type wallet_balance: WalletIncomeWalletBalance
    :param wallet_balance: 钱包余额信息
    """
    def __init__(
        self,
        notify_type = None,
        broker_id = None,
        dealer_id = None,
        user_info = None,
        wallet_id = None,
        platform_info = None,
        order_id = None,
        ref = None,
        amount = None,
        before_tax_amount = None,
        remark = None,
        earned_at = None,
        status = None,
        status_detail = None,
        status_message = None,
        status_detail_message = None,
        created_at = None,
        finished_at = None,
        fee_info = None,
        tax_info = None,
        user_debt_repayment_amount = None,
        wallet_inflow_amount = None,
        wallet_balance = None
    ):
        super().__init__()
        self.notify_type = notify_type
        self.broker_id = broker_id
        self.dealer_id = dealer_id
        self.user_info = user_info
        self.wallet_id = wallet_id
        self.platform_info = platform_info
        self.order_id = order_id
        self.ref = ref
        self.amount = amount
        self.before_tax_amount = before_tax_amount
        self.remark = remark
        self.earned_at = earned_at
        self.status = status
        self.status_detail = status_detail
        self.status_message = status_message
        self.status_detail_message = status_detail_message
        self.created_at = created_at
        self.finished_at = finished_at
        self.fee_info = fee_info
        self.tax_info = tax_info
        self.user_debt_repayment_amount = user_debt_repayment_amount
        self.wallet_inflow_amount = wallet_inflow_amount
        self.wallet_balance = wallet_balance
