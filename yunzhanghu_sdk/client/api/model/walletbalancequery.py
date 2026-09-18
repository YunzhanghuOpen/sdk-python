"""钱包余额查询"""

from ...base import BaseRequest


class WalletBalanceQueryUserInfo(BaseRequest):
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


class WalletBalanceQueryWalletBalance(BaseRequest):
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


class QueryWalletBalanceRequest(BaseRequest):
    """
    查询钱包余额请求-请求

    :type broker_id: string
    :param broker_id: 综合服务主体 ID

    :type dealer_id: string
    :param dealer_id: 平台企业 ID

    :type user_info: WalletBalanceQueryUserInfo
    :param user_info: 劳动者信息

    :type wallet_id: string
    :param wallet_id: 钱包 ID
    """
    def __init__(
        self,
        broker_id = None,
        dealer_id = None,
        user_info = None,
        wallet_id = None
    ):
        super().__init__()
        self.broker_id = broker_id
        self.dealer_id = dealer_id
        self.user_info = user_info
        self.wallet_id = wallet_id


class QueryWalletBalanceResponse(BaseRequest):
    """
    查询钱包余额返回-响应

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
