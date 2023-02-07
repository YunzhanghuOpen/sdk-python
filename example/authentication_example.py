# -*- coding: utf-8 -*-
from yzh_py.client.api.model.authentication import *
from yzh_py.client.api.authentication_client import AuthenticationClient
from yzh_py.config import *

if __name__ == '__main__':
    # dealer_id 平台企业 ID
    dealer_id = "xxx"
    # broker_id 综合服务主体 ID
    broker_id = "xxx"
    # sign_type 签名类型
    sign_type = "xxx"
    # app_key
    app_key = "xxx"
    # des3key
    des3key = "xxx"
    # dealer_private_key 平台企业私钥
    dealer_private_key = '''
        -----BEGIN PRIVATE KEY-----
        xxx
        '''
    # yzh_public_key 云账户公钥
    yzh_public_key = '''
        xxx
        '''

    # 初始化配置参数
    config = Config(
        # host 请求域名
        host="https://api-service.yunzhanghu.com",
        dealer_id=dealer_id,
        sign_type=sign_type,
        app_key=app_key,
        des3key=des3key,
        dealer_private_key=dealer_private_key,
        yzh_public_key=yzh_public_key,
    )

    # 银行卡四要素鉴权请求（下发短信验证码）
    bankcardfourauthverifyrequest = BankCardFourAuthVerifyRequest(
        card_no="",
        id_card="",
        real_name="",
        mobile="",
    )
    bankcardfourauthverifyrequest_res = AuthenticationClient.bank_card_four_auth_verify(bankcardfourauthverifyrequest)
    print("银行卡四要素鉴权请求（下发短信验证码）返回：", bankcardfourauthverifyrequest_res.code, bankcardfourauthverifyrequest_res.message,
          bankcardfourauthverifyrequest_res.data)

    # 银行卡四要素确认鉴权（上传短信验证码）
    bankcardfourauthconfirmrequest = BankCardFourAuthConfirmRequest(
        card_no="",
        id_card="",
        real_name="",
        mobile="",
        captcha="",
        ref="",
    )
    bankcardfourauthconfirmrequest_res = AuthenticationClient.bank_card_four_auth_confirm(
        bankcardfourauthconfirmrequest)
    print("银行卡四要素确认鉴权（上传短信验证码）返回：", bankcardfourauthconfirmrequest_res.code, bankcardfourauthconfirmrequest_res.message,
          bankcardfourauthconfirmrequest_res.data)

    # 银行卡四要素验证
    bankcardfourverifyrequest = BankCardFourVerifyRequest(
        card_no="",
        id_card="",
        real_name="",
        mobile="",
    )
    bankcardfourverifyrequest_res = AuthenticationClient.bank_card_four_verify(bankcardfourverifyrequest)
    print("银行卡四要素验证返回：", bankcardfourverifyrequest_res.code, bankcardfourverifyrequest_res.message,
          bankcardfourverifyrequest_res.data)

    # 银行卡三要素验证
    bankcardthreeverifyrequest = BankCardThreeVerifyRequest(
        card_no="",
        id_card="",
        real_name="",
    )
    bankcardthreeverifyrequest_res = AuthenticationClient.bank_card_three_verify(bankcardthreeverifyrequest)
    print("银行卡三要素验证返回：", bankcardthreeverifyrequest_res.code, bankcardthreeverifyrequest_res.message,
          bankcardthreeverifyrequest_res.data)

    # 身份证实名验证
    idcardverifyrequest = IDCardVerifyRequest(
        id_card="",
        real_name="",
    )
    idcardverifyrequest_res = AuthenticationClient.i_d_card_verify(idcardverifyrequest)
    print("身份证实名验证返回：", idcardverifyrequest_res.code, idcardverifyrequest_res.message, idcardverifyrequest_res.data)

    # 上传免验证用户名单信息
    userexemptedinforequest = UserExemptedInfoRequest(
        card_type="",
        id_card="",
        real_name="",
        comment_apply="",
        broker_id="",
        dealer_id="",
        user_images="",
        country="",
        birthday="",
        gender="",
        notify_url="",
        ref="",
    )
    userexemptedinforequest_res = AuthenticationClient.user_exempted_info(userexemptedinforequest)
    print("上传免验证用户名单信息返回：", userexemptedinforequest_res.code, userexemptedinforequest_res.message,
          userexemptedinforequest_res.data)

    # 查看免验证用户名单是否存在
    userwhitecheckrequest = UserWhiteCheckRequest(
        id_card="",
        real_name="",
    )
    userwhitecheckrequest_res = AuthenticationClient.user_white_check(userwhitecheckrequest)
    print("查看免验证用户名单是否存在返回：", userwhitecheckrequest_res.code, userwhitecheckrequest_res.message,
          userwhitecheckrequest_res.data)

    # 银行卡信息查询接口
    getbankcardinforequest = GetBankCardInfoRequest(
        card_no="",
        bank_name="",
    )
    getbankcardinforequest_res = AuthenticationClient.get_bank_card_info(getbankcardinforequest)
    print("银行卡信息查询接口返回：", getbankcardinforequest_res.code, getbankcardinforequest_res.message,
          getbankcardinforequest_res.data)












