"""连续劳务税费退补"""

from ...base import BaseRequest


class NotifyClearTaxDoneRequest(BaseRequest):
    """
    连续劳务税费清缴完成通知-请求

    :type notify_id: string
    :param notify_id: 通知 ID

    :type notify_time: string
    :param notify_time: 通知时间

    :type data: ClearTaxData
    :param data: 返回数据
    """
    def __init__(
        self,
        notify_id = None,
        notify_time = None,
        data = None
    ):
        super().__init__()
        self.notify_id = notify_id
        self.notify_time = notify_time
        self.data = data


class ClearTaxData(BaseRequest):
    """
    连续劳务税费清缴完成数据-响应

    :type tax_month: string
    :param tax_month: 报税属期

    :type broker_id: string
    :param broker_id: 综合服务主体 ID

    :type dealer_id: string
    :param dealer_id: 平台企业 ID

    :type tax_clear_num: string
    :param tax_clear_num: 清缴次数

    :type refund_tax_labor_num: string
    :param refund_tax_labor_num: 退补税用户数量

    :type refund_tax_order_num: string
    :param refund_tax_order_num: 退补税订单数量

    :type total_amount: string
    :param total_amount: 订单总金额

    :type cur_total_refund_tax: string
    :param cur_total_refund_tax: 本批次退补税费总额

    :type total_refund_tax: string
    :param total_refund_tax: 退补税费总额

    :type history_refund_tax: string
    :param history_refund_tax: 历史已退补税费总额

    :type total_tax: string
    :param total_tax: 本批次预扣税费总额

    :type receive_total_tax: string
    :param receive_total_tax: 本批次实缴税费总额

    :type cur_total_refund_labor_tax: string
    :param cur_total_refund_labor_tax: 本批次退补给用户税费总额

    :type cur_total_refund_dealer_tax: string
    :param cur_total_refund_dealer_tax: 本批次退补给平台企业税费总额

    :type cur_total_refund_broker_tax: string
    :param cur_total_refund_broker_tax: 本批次退补给云账户税费总额

    :type batch_id: string
    :param batch_id: 批次号

    :type batch_create_time: string
    :param batch_create_time: 批次生成时间
    """
    def __init__(
        self,
        tax_month = None,
        broker_id = None,
        dealer_id = None,
        tax_clear_num = None,
        refund_tax_labor_num = None,
        refund_tax_order_num = None,
        total_amount = None,
        cur_total_refund_tax = None,
        total_refund_tax = None,
        history_refund_tax = None,
        total_tax = None,
        receive_total_tax = None,
        cur_total_refund_labor_tax = None,
        cur_total_refund_dealer_tax = None,
        cur_total_refund_broker_tax = None,
        batch_id = None,
        batch_create_time = None
    ):
        super().__init__()
        self.tax_month = tax_month
        self.broker_id = broker_id
        self.dealer_id = dealer_id
        self.tax_clear_num = tax_clear_num
        self.refund_tax_labor_num = refund_tax_labor_num
        self.refund_tax_order_num = refund_tax_order_num
        self.total_amount = total_amount
        self.cur_total_refund_tax = cur_total_refund_tax
        self.total_refund_tax = total_refund_tax
        self.history_refund_tax = history_refund_tax
        self.total_tax = total_tax
        self.receive_total_tax = receive_total_tax
        self.cur_total_refund_labor_tax = cur_total_refund_labor_tax
        self.cur_total_refund_dealer_tax = cur_total_refund_dealer_tax
        self.cur_total_refund_broker_tax = cur_total_refund_broker_tax
        self.batch_id = batch_id
        self.batch_create_time = batch_create_time


class GetClearTaxInfoRequest(BaseRequest):
    """
    查询税费清缴完成结果请求-请求

    :type broker_id: string
    :param broker_id: 综合服务主体 ID

    :type dealer_id: string
    :param dealer_id: 平台企业 ID

    :type tax_month: string
    :param tax_month: 报税属期
    """
    def __init__(
        self,
        broker_id = None,
        dealer_id = None,
        tax_month = None
    ):
        super().__init__()
        self.broker_id = broker_id
        self.dealer_id = dealer_id
        self.tax_month = tax_month


class GetClearTaxInfoResponse(BaseRequest):
    """
    查询税费清缴完成结果返回-响应

    :type batch_list: list
    :param batch_list: 清缴批次列表
    """
    def __init__(
        self,
        batch_list = None
    ):
        super().__init__()
        self.batch_list = batch_list


class GetClearTaxFileRequest(BaseRequest):
    """
    查询税费清缴明细文件请求-请求

    :type broker_id: string
    :param broker_id: 综合服务主体 ID

    :type dealer_id: string
    :param dealer_id: 平台企业 ID

    :type tax_month: string
    :param tax_month: 报税属期

    :type batch_id: string
    :param batch_id: 批次号
    """
    def __init__(
        self,
        broker_id = None,
        dealer_id = None,
        tax_month = None,
        batch_id = None
    ):
        super().__init__()
        self.broker_id = broker_id
        self.dealer_id = dealer_id
        self.tax_month = tax_month
        self.batch_id = batch_id


class GetClearTaxFileResponse(BaseRequest):
    """
    查询税费清缴明细文件返回-响应

    :type url: string
    :param url: 下载地址
    """
    def __init__(
        self,
        url = None
    ):
        super().__init__()
        self.url = url


class NotifyRefundTaxDoneRequest(BaseRequest):
    """
    连续劳务税费退补完成通知-请求

    :type notify_id: string
    :param notify_id: 通知 ID

    :type notify_time: string
    :param notify_time: 通知时间

    :type data: RefundTaxData
    :param data: 返回数据
    """
    def __init__(
        self,
        notify_id = None,
        notify_time = None,
        data = None
    ):
        super().__init__()
        self.notify_id = notify_id
        self.notify_time = notify_time
        self.data = data


class RefundTaxData(BaseRequest):
    """
    连续劳务税费退补完成数据-响应

    :type broker_id: string
    :param broker_id: 综合服务主体 ID

    :type dealer_id: string
    :param dealer_id: 平台企业 ID

    :type tax_clear_num: string
    :param tax_clear_num: 清缴次数

    :type tax_month: string
    :param tax_month: 报税属期

    :type refund_tax_labor_num: string
    :param refund_tax_labor_num: 退补税用户数量

    :type refund_tax_order_num: string
    :param refund_tax_order_num: 退补税订单数量

    :type total_amount: string
    :param total_amount: 订单总金额

    :type cur_total_refund_tax: string
    :param cur_total_refund_tax: 本批次退补税费总额

    :type total_refund_tax: string
    :param total_refund_tax: 退补税费总额

    :type history_refund_tax: string
    :param history_refund_tax: 历史已退补税费总额

    :type total_tax: string
    :param total_tax: 本批次预扣税费总额

    :type receive_total_tax: string
    :param receive_total_tax: 本批次实缴税费总额

    :type cur_total_refund_labor_tax: string
    :param cur_total_refund_labor_tax: 本批次退补给用户税费总额

    :type cur_total_refund_dealer_tax: string
    :param cur_total_refund_dealer_tax: 本批次退补给平台企业税费总额

    :type cur_total_refund_broker_tax: string
    :param cur_total_refund_broker_tax: 本批次退补给云账户税费总额

    :type batch_id: string
    :param batch_id: 批次号

    :type batch_refund_tax_status: string
    :param batch_refund_tax_status: 批次退补税状态

    :type batch_create_time: string
    :param batch_create_time: 批次生成时间

    :type batch_refund_tax_finished_time: string
    :param batch_refund_tax_finished_time: 批次退补税成功时间

    :type refund_tax_finished_labor_num: string
    :param refund_tax_finished_labor_num: 已完成税费退补的用户数量

    :type refund_tax_finished_amount: string
    :param refund_tax_finished_amount: 已完成的税费退补总额
    """
    def __init__(
        self,
        broker_id = None,
        dealer_id = None,
        tax_clear_num = None,
        tax_month = None,
        refund_tax_labor_num = None,
        refund_tax_order_num = None,
        total_amount = None,
        cur_total_refund_tax = None,
        total_refund_tax = None,
        history_refund_tax = None,
        total_tax = None,
        receive_total_tax = None,
        cur_total_refund_labor_tax = None,
        cur_total_refund_dealer_tax = None,
        cur_total_refund_broker_tax = None,
        batch_id = None,
        batch_refund_tax_status = None,
        batch_create_time = None,
        batch_refund_tax_finished_time = None,
        refund_tax_finished_labor_num = None,
        refund_tax_finished_amount = None
    ):
        super().__init__()
        self.broker_id = broker_id
        self.dealer_id = dealer_id
        self.tax_clear_num = tax_clear_num
        self.tax_month = tax_month
        self.refund_tax_labor_num = refund_tax_labor_num
        self.refund_tax_order_num = refund_tax_order_num
        self.total_amount = total_amount
        self.cur_total_refund_tax = cur_total_refund_tax
        self.total_refund_tax = total_refund_tax
        self.history_refund_tax = history_refund_tax
        self.total_tax = total_tax
        self.receive_total_tax = receive_total_tax
        self.cur_total_refund_labor_tax = cur_total_refund_labor_tax
        self.cur_total_refund_dealer_tax = cur_total_refund_dealer_tax
        self.cur_total_refund_broker_tax = cur_total_refund_broker_tax
        self.batch_id = batch_id
        self.batch_refund_tax_status = batch_refund_tax_status
        self.batch_create_time = batch_create_time
        self.batch_refund_tax_finished_time = batch_refund_tax_finished_time
        self.refund_tax_finished_labor_num = refund_tax_finished_labor_num
        self.refund_tax_finished_amount = refund_tax_finished_amount


class GetRefundTaxInfoRequest(BaseRequest):
    """
    查询税费退补完成结果请求-请求

    :type broker_id: string
    :param broker_id: 综合服务主体 ID

    :type dealer_id: string
    :param dealer_id: 平台企业 ID

    :type tax_month: string
    :param tax_month: 报税属期

    :type batch_id: string
    :param batch_id: 批次号
    """
    def __init__(
        self,
        broker_id = None,
        dealer_id = None,
        tax_month = None,
        batch_id = None
    ):
        super().__init__()
        self.broker_id = broker_id
        self.dealer_id = dealer_id
        self.tax_month = tax_month
        self.batch_id = batch_id


class GetRefundTaxLaborInfoRequest(BaseRequest):
    """
    查询税费退补涉及劳动者请求-请求

    :type broker_id: string
    :param broker_id: 综合服务主体 ID

    :type dealer_id: string
    :param dealer_id: 平台企业 ID

    :type batch_id: string
    :param batch_id: 批次号

    :type tax_month: string
    :param tax_month: 税款所属期

    :type offset: int
    :param offset: 偏移量

    :type length: int
    :param length: 每页返回条数
    """
    def __init__(
        self,
        broker_id = None,
        dealer_id = None,
        batch_id = None,
        tax_month = None,
        offset = None,
        length = None
    ):
        super().__init__()
        self.broker_id = broker_id
        self.dealer_id = dealer_id
        self.batch_id = batch_id
        self.tax_month = tax_month
        self.offset = offset
        self.length = length


class GetRefundTaxLaborInfoResponse(BaseRequest):
    """
    查询税费退补涉及劳动者返回-响应

    :type tax_month: string
    :param tax_month: 税款所属期

    :type batch_id: string
    :param batch_id: 批次号

    :type batch_create_time: string
    :param batch_create_time: 批次生成时间

    :type labor_num: string
    :param labor_num: 退补税劳动者数量

    :type order_num: string
    :param order_num: 退补税订单数量

    :type total_num: string
    :param total_num: 总数据条数

    :type labor_refund_info: list
    :param labor_refund_info: 退补税劳动者明细
    """
    def __init__(
        self,
        tax_month = None,
        batch_id = None,
        batch_create_time = None,
        labor_num = None,
        order_num = None,
        total_num = None,
        labor_refund_info = None
    ):
        super().__init__()
        self.tax_month = tax_month
        self.batch_id = batch_id
        self.batch_create_time = batch_create_time
        self.labor_num = labor_num
        self.order_num = order_num
        self.total_num = total_num
        self.labor_refund_info = labor_refund_info


class LaborRefundInfo(BaseRequest):
    """
    退补税劳动者明细-响应

    :type real_name: string
    :param real_name: 劳动者姓名

    :type id_card: string
    :param id_card: 劳动者证件号

    :type refund_tax: string
    :param refund_tax: 本批次退补给劳动者税费总额

    :type tax_refund_status: string
    :param tax_refund_status: 退补税状态

    :type receiving_account: string
    :param receiving_account: 劳动者收款账户

    :type receiving_channel: string
    :param receiving_channel: 劳动者收款账号

    :type refund_tax_finished_time: string
    :param refund_tax_finished_time: 退补税费时间
    """
    def __init__(
        self,
        real_name = None,
        id_card = None,
        refund_tax = None,
        tax_refund_status = None,
        receiving_account = None,
        receiving_channel = None,
        refund_tax_finished_time = None
    ):
        super().__init__()
        self.real_name = real_name
        self.id_card = id_card
        self.refund_tax = refund_tax
        self.tax_refund_status = tax_refund_status
        self.receiving_account = receiving_account
        self.receiving_channel = receiving_channel
        self.refund_tax_finished_time = refund_tax_finished_time
