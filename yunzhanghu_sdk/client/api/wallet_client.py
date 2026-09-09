"""钱包余额查询"""

from .model.wallet import *
from ..base import BaseClient
from ...utils import Utils


class WalletServiceClient(BaseClient):
    """钱包余额查询客户端"""

    def __init__(self, config):
        super().__init__(config)

    def query_wallet_balance(self, request: QueryWalletBalanceRequest):
        """ 查询钱包余额

        :type request: QueryWalletBalanceRequest
        :param request: the QueryWalletBalanceRequest request parameters class.

        :return: QueryWalletBalanceResponse
        """
        return self._post(
            "/api/wallet/v1/balance",
            request.request_id,
            Utils.copy_dict(request.__dict__)
        )
