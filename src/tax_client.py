from src.base.base_client import *
from src.util.utils import *
from src.model.tax import *


class TaxClient(BaseClient):
    def __init__(self, config):
        super().__init__(config)
    

    def get_tax_file(self, request: GetTaxFileRequest):
        """ 下载个税扣缴明细表
   
        :type request: GetTaxFileRequest
        :param request: the GetTaxFileRequest request parameters class.
    
        :return: GetTaxFileResponse
        """
        return self._post("/api/tax/v1/taxfile/download", request.request_id, Utils.copy_dict(request.__dict__))

    def get_user_cross(self, request: GetUserCrossRequest):
        """ GetUserCross 查询纳税人是否为跨集团用户
   
        :type request: GetUserCrossRequest
        :param request: the GetUserCrossRequest request parameters class.
    
        :return: GetUserCrossResponse
        """
        return self._post("/api/tax/v1/user/cross", request.request_id, Utils.copy_dict(request.__dict__))
     