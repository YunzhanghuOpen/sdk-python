# -*- coding: utf-8 -*-
from yunzhanghu_sdk.client.api.model.authentication import *
from yunzhanghu_sdk.client.api.authentication_client import AuthenticationClient
from yunzhanghu_sdk.example.utils.configinit import init_config

# 用户信息验证
if __name__ == '__main__':
    AuthenticationClient = AuthenticationClient(config=init_config())
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

    # 银行卡四要素确认请求（上传短信验证码）
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
    idcardverifyrequest_res = AuthenticationClient.id_card_verify(idcardverifyrequest)
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

    # 银行卡信息查询
    getbankcardinforequest = GetBankCardInfoRequest(
        card_no="",
        bank_name="",
    )
    getbankcardinforequest_res = AuthenticationClient.get_bank_card_info(getbankcardinforequest)
    print("银行卡信息查询返回：", getbankcardinforequest_res.code, getbankcardinforequest_res.message,
          getbankcardinforequest_res.data)