"""钱包余额变更结果回调通知"""

from ...base import BaseRequest
from .walletbalancequery import WalletBalanceQueryUserInfo, WalletBalanceQueryWalletBalance


class NotifyWalletBalanceChangeRequest(BaseRequest):
    """
    钱包余额变更结果回调通知请求-请求

    :type notify_type: string
    :param notify_type: 通知类型

    :type broker_id: string
    :param broker_id: 综合服务主体 ID

    :type dealer_id: string
    :param dealer_id: 平台企业 ID

    :type user_info: WalletBalanceQueryUserInfo
    :param user_info: 劳动者信息

    :type wallet_id: string
    :param wallet_id: 钱包 ID

    :type change_id: string
    :param change_id: 余额变化批次 ID

    :type change_amount: string
    :param change_amount: 钱包余额变更金额

    :type user_debt_repayment_personal_amount: string
    :param user_debt_repayment_personal_amount: 需补缴个税

    :type user_debt_repayment_added_amount: string
    :param user_debt_repayment_added_amount: 需补缴增附税

    :type changed_at: string
    :param changed_at: 余额变化时间

    :type wallet_balance: WalletBalanceQueryWalletBalance
    :param wallet_balance: 钱包余额信息
    """
    def __init__(
        self,
        notify_type = None,
        broker_id = None,
        dealer_id = None,
        user_info = None,
        wallet_id = None,
        change_id = None,
        change_amount = None,
        user_debt_repayment_personal_amount = None,
        user_debt_repayment_added_amount = None,
        changed_at = None,
        wallet_balance = None
    ):
        super().__init__()
        self.notify_type = notify_type
        self.broker_id = broker_id
        self.dealer_id = dealer_id
        self.user_info = user_info
        self.wallet_id = wallet_id
        self.change_id = change_id
        self.change_amount = change_amount
        self.user_debt_repayment_personal_amount = user_debt_repayment_personal_amount
        self.user_debt_repayment_added_amount = user_debt_repayment_added_amount
        self.changed_at = changed_at
        self.wallet_balance = wallet_balance
