# 基础信息配置
class Config(object):
    """

    :type host: string
    :param host: 请求域名

    :type dealer_id: string
    :param dealer_id: 平台企业 ID

    :type sign_type: string
    :param sign_type: 签名类型

    :type app_key: string
    :param app_key: app_key

    :type des3key: string
    :param des3key: des3key

    :type dealer_private_key: string
    :param dealer_private_key: 平台企业私钥

    :type yzh_public_key: string
    :param yzh_public_key: 云账户公钥
    """
    def __init__(self, host, dealer_id, sign_type, app_key, des3key, dealer_private_key: str, yzh_public_key: str):
        self.host = host
        self.dealer_id = dealer_id
        self.sign_type = sign_type
        self.app_key = app_key
        self.des3key = des3key
        self.dealer_private_key = dealer_private_key
        self.yzh_public_key = yzh_public_key
        self.check_config()

    def check_config(self):
        if self.dealer_private_key is not None:
            self.dealer_private_key = self.dealer_private_key.strip()
        if self.yzh_public_key is not None:
            self.yzh_public_key = self.yzh_public_key.strip()
        if self.sign_type != "sha256" and self.sign_type != "rsa":
            raise ValueError('wrong encrypt type')
        if self.host is None:
            self.host = "https://api-service.yunzhanghu.com"
