"""人脸识别实名核验"""

from ...base import BaseRequest


class ApplyFaceAuthRequest(BaseRequest):
    """
    申请人脸识别实名核验请求-请求

    :type broker_id: string
    :param broker_id: 综合服务主体 ID

    :type dealer_id: string
    :param dealer_id: 平台企业 ID

    :type verification_id: string
    :param verification_id: 平台企业实名核验 ID

    :type real_name: string
    :param real_name: 姓名

    :type id_card: string
    :param id_card: 身份证号码

    :type callback_url: string
    :param callback_url: 回调地址

    :type redirect_url: string
    :param redirect_url: 跳转 URL

    :type color: string
    :param color: 主题颜色
    """
    def __init__(
        self,
        broker_id = None,
        dealer_id = None,
        verification_id = None,
        real_name = None,
        id_card = None,
        callback_url = None,
        redirect_url = None,
        color = None
    ):
        super().__init__()
        self.broker_id = broker_id
        self.dealer_id = dealer_id
        self.verification_id = verification_id
        self.real_name = real_name
        self.id_card = id_card
        self.callback_url = callback_url
        self.redirect_url = redirect_url
        self.color = color


class ApplyFaceAuthResponse(BaseRequest):
    """
    申请人脸识别实名核验返回-响应

    :type record_id: string
    :param record_id: 人脸识别实名核验唯一 ID

    :type verification_id: string
    :param verification_id: 平台企业实名核验 ID

    :type verification_url: string
    :param verification_url: 人脸识别实名核验 H5 页面地址
    """
    def __init__(
        self,
        record_id = None,
        verification_id = None,
        verification_url = None
    ):
        super().__init__()
        self.record_id = record_id
        self.verification_id = verification_id
        self.verification_url = verification_url


class GetFaceAuthResultRequest(BaseRequest):
    """
    查询人脸识别实名核验结果请求-请求

    :type broker_id: string
    :param broker_id: 综合服务主体 ID

    :type dealer_id: string
    :param dealer_id: 平台企业 ID

    :type record_id: string
    :param record_id: 人脸识别实名核验唯一 ID

    :type verification_id: string
    :param verification_id: 平台企业实名核验 ID
    """
    def __init__(
        self,
        broker_id = None,
        dealer_id = None,
        record_id = None,
        verification_id = None
    ):
        super().__init__()
        self.broker_id = broker_id
        self.dealer_id = dealer_id
        self.record_id = record_id
        self.verification_id = verification_id


class GetFaceAuthResultResponse(BaseRequest):
    """
    查询人脸识别实名核验结果返回-响应

    :type real_name: string
    :param real_name: 姓名

    :type id_card: string
    :param id_card: 身份证号码

    :type record_id: string
    :param record_id: 人脸识别实名核验唯一 ID

    :type verification_id: string
    :param verification_id: 平台企业实名核验 ID

    :type status: string
    :param status: 实名核验状态

    :type verify_time: string
    :param verify_time: 实名核验完成时间

    :type detail: FaceAuthDetail
    :param detail: 实名核验失败详情
    """
    def __init__(
        self,
        real_name = None,
        id_card = None,
        record_id = None,
        verification_id = None,
        status = None,
        verify_time = None,
        detail = None
    ):
        super().__init__()
        self.real_name = real_name
        self.id_card = id_card
        self.record_id = record_id
        self.verification_id = verification_id
        self.status = status
        self.verify_time = verify_time
        self.detail = detail


class FaceAuthDetail(BaseRequest):
    """
    人脸识别实名核验失败详情-响应

    :type fail_reason: string
    :param fail_reason: 实名核验失败原因
    """
    def __init__(
        self,
        fail_reason = None
    ):
        super().__init__()
        self.fail_reason = fail_reason


class NotifyFaceAuthRequest(BaseRequest):
    """
    人脸识别实名核验结果回调通知请求-请求

    :type broker_id: string
    :param broker_id: 综合服务主体 ID

    :type dealer_id: string
    :param dealer_id: 平台企业 ID

    :type real_name: string
    :param real_name: 姓名

    :type id_card: string
    :param id_card: 身份证号码

    :type record_id: string
    :param record_id: 人脸识别实名核验唯一 ID

    :type verification_id: string
    :param verification_id: 平台企业实名核验 ID

    :type status: string
    :param status: 实名核验状态

    :type verify_time: string
    :param verify_time: 实名核验完成时间

    :type detail: FaceAuthDetail
    :param detail: 实名核验失败详情
    """
    def __init__(
        self,
        broker_id = None,
        dealer_id = None,
        real_name = None,
        id_card = None,
        record_id = None,
        verification_id = None,
        status = None,
        verify_time = None,
        detail = None
    ):
        super().__init__()
        self.broker_id = broker_id
        self.dealer_id = dealer_id
        self.real_name = real_name
        self.id_card = id_card
        self.record_id = record_id
        self.verification_id = verification_id
        self.status = status
        self.verify_time = verify_time
        self.detail = detail
