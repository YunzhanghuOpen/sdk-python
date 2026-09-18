"""钱包余额扣减"""

from .model.walletdeduct import *
from ..base import BaseClient
from ...utils import Utils


class WalletDeductServiceClient(BaseClient):
    """钱包余额扣减客户端"""

    def __init__(self, config):
        super().__init__(config)

    def create_wallet_deduct(self, request: CreateWalletDeductRequest):
        """ 申请钱包余额扣减

        :type request: CreateWalletDeductRequest
        :param request: the CreateWalletDeductRequest request parameters class.

        :return: CreateWalletDeductResponse
        """
        return self._post(
            "/api/payout/v1/direct/create",
            request.request_id,
            Utils.copy_dict(request.__dict__)
        )

    def query_wallet_deduct(self, request: QueryWalletDeductRequest):
        """ 查询钱包余额扣减申请结果

        :type request: QueryWalletDeductRequest
        :param request: the QueryWalletDeductRequest request parameters class.

        :return: QueryWalletDeductResponse
        """
        return self._get(
            "/api/payout/v1/direct/query",
            request.request_id,
            Utils.copy_dict(request.__dict__)
        )

    def complete_wallet_deduct(self, request: CompleteWalletDeductRequest):
        """ 提交钱包余额扣减结果

        :type request: CompleteWalletDeductRequest
        :param request: the CompleteWalletDeductRequest request parameters class.

        :return: CompleteWalletDeductResponse
        """
        return self._post(
            "/api/payout/v1/direct/complete",
            request.request_id,
            Utils.copy_dict(request.__dict__)
        )
