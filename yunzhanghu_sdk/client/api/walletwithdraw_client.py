"""钱包余额提现"""

from .model.walletwithdraw import *
from ..base import BaseClient
from ...utils import Utils


class WalletWithdrawServiceClient(BaseClient):
    """钱包余额提现客户端"""

    def __init__(self, config):
        super().__init__(config)

    def create_wallet_withdraw(self, request: CreateWalletWithdrawRequest):
        """ 发起钱包余额提现

        :type request: CreateWalletWithdrawRequest
        :param request: the CreateWalletWithdrawRequest request parameters class.

        :return: CreateWalletWithdrawResponse
        """
        return self._post(
            "/api/payout/v1/create",
            request.request_id,
            Utils.copy_dict(request.__dict__)
        )

    def query_wallet_withdraw(self, request: QueryWalletWithdrawRequest):
        """ 查询钱包余额提现结果

        :type request: QueryWalletWithdrawRequest
        :param request: the QueryWalletWithdrawRequest request parameters class.

        :return: QueryWalletWithdrawResponse
        """
        return self._get(
            "/api/payout/v1/query",
            request.request_id,
            Utils.copy_dict(request.__dict__)
        )
