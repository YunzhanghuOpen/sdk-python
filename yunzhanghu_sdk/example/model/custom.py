"""自定义请求实体示例"""

from yunzhanghu_sdk.client.base import BaseRequest


class CustomRequest(BaseRequest):
    """
    银行卡实时支付请求参数

    :type order_id: string
    :param order_id: 平台企业订单号

    :type dealer_id: string
    :param dealer_id: 平台企业 ID

    :type broker_id: string
    :param broker_id: 综合服务主体 ID

    :type real_name: string
    :param real_name: 姓名

    :type card_no: string
    :param card_no: 银行卡号

    :type id_card: string
    :param id_card: 身份证号码

    :type phone_no: string
    :param phone_no: 手机号

    :type pay: string
    :param pay: 订单金额

    :type pay_remark: string
    :param pay_remark: 订单备注

    :type notify_url: string
    :param notify_url: 回调地址
    """

    def __init__(
            self,
            order_id = None,
            dealer_id = None,
            broker_id = None,
            real_name = None,
            card_no = None,
            id_card = None,
            phone_no = None,
            pay = None,
            pay_remark = None,
            notify_url = None
    ):
        super().__init__()
        self.order_id = order_id
        self.dealer_id = dealer_id
        self.broker_id = broker_id
        self.real_name = real_name
        self.card_no = card_no
        self.id_card = id_card
        self.phone_no = phone_no
        self.pay = pay
        self.pay_remark = pay_remark
        self.notify_url = notify_url


class CustomResponse(BaseRequest):
    """
    银行卡实时支付响应参数

    :type order_id: string
    :param order_id: 平台企业订单号

    :type ref: string
    :param ref: 综合服务平台流水号

    :type pay: string
    :param pay: 订单金额
    """

    def __init__(
            self,
            order_id = None,
            ref = None,
            pay = None
    ):
        super().__init__()
        self.order_id = order_id
        self.ref = ref
        self.pay = pay
