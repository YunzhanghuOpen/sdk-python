"""人脸识别实名核验"""

from .model.faceauth import *
from ..base import BaseClient
from ...utils import Utils


class FaceAuthServiceClient(BaseClient):
    """人脸识别实名核验客户端"""

    def __init__(self, config):
        super().__init__(config)

    def apply_face_auth(self, request: ApplyFaceAuthRequest):
        """ 申请人脸识别实名核验

        :type request: ApplyFaceAuthRequest
        :param request: the ApplyFaceAuthRequest request parameters class.

        :return: ApplyFaceAuthResponse
        """
        return self._post(
            "/api/user/v1/face/auth",
            request.request_id,
            Utils.copy_dict(request.__dict__)
        )

    def get_face_auth_result(self, request: GetFaceAuthResultRequest):
        """ 查询人脸识别实名核验结果

        :type request: GetFaceAuthResultRequest
        :param request: the GetFaceAuthResultRequest request parameters class.

        :return: GetFaceAuthResultResponse
        """
        return self._get(
            "/api/user/v1/face/auth_result",
            request.request_id,
            Utils.copy_dict(request.__dict__)
        )
