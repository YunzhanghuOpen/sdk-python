"""钱包余额入账"""

from .model.walletincome import *
from ..base import BaseClient
from ...utils import Utils


class WalletIncomeServiceClient(BaseClient):
    """钱包余额入账客户端"""

    def __init__(self, config):
        super().__init__(config)

    def create_wallet_income(self, request: CreateWalletIncomeRequest):
        """ 发起钱包余额入账

        :type request: CreateWalletIncomeRequest
        :param request: the CreateWalletIncomeRequest request parameters class.

        :return: CreateWalletIncomeResponse
        """
        return self._post(
            "/api/income/v1/create",
            request.request_id,
            Utils.copy_dict(request.__dict__)
        )

    def query_wallet_income(self, request: QueryWalletIncomeRequest):
        """ 查询钱包余额入账结果

        :type request: QueryWalletIncomeRequest
        :param request: the QueryWalletIncomeRequest request parameters class.

        :return: QueryWalletIncomeResponse
        """
        return self._get(
            "/api/income/v1/query",
            request.request_id,
            Utils.copy_dict(request.__dict__)
        )

    def cancel_wallet_income(self, request: CancelWalletIncomeRequest):
        """ 取消钱包收入计税订单

        :type request: CancelWalletIncomeRequest
        :param request: the CancelWalletIncomeRequest request parameters class.

        :return: CancelWalletIncomeResponse
        """
        return self._post(
            "/api/income/v1/cancel-order",
            request.request_id,
            Utils.copy_dict(request.__dict__)
        )
