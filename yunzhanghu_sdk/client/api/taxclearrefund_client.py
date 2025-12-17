"""连续劳务税费退补"""

from .model.taxclearrefund import *
from ..base import BaseClient
from ...utils import Utils


class TaxClearRefundClient(BaseClient):
    """连续劳务税费退补客户端"""

    def __init__(self, config):
        super().__init__(config)

    def get_clear_tax_info(self, request: GetClearTaxInfoRequest):
        """ 查询税费清缴完成结果

        :type request: GetClearTaxInfoRequest
        :param request: the GetClearTaxInfoRequest request parameters class.

        :return: GetClearTaxInfoResponse
        """
        return self._get(
            "/api/payment/v1/query-clear-tax",
            request.request_id,
            Utils.copy_dict(request.__dict__)
        )

    def get_clear_tax_file(self, request: GetClearTaxFileRequest):
        """ 查询税费清缴明细文件

        :type request: GetClearTaxFileRequest
        :param request: the GetClearTaxFileRequest request parameters class.

        :return: GetClearTaxFileResponse
        """
        return self._get(
            "/api/payment/v1/query-clear-tax/file",
            request.request_id,
            Utils.copy_dict(request.__dict__)
        )

    def get_refund_tax_info(self, request: GetRefundTaxInfoRequest):
        """ 查询税费退补完成结果

        :type request: GetRefundTaxInfoRequest
        :param request: the GetRefundTaxInfoRequest request parameters class.

        :return: RefundTaxData
        """
        return self._get(
            "/api/payment/v1/query-clear-status",
            request.request_id,
            Utils.copy_dict(request.__dict__)
        )
