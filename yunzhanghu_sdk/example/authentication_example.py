# -*- coding: utf-8 -*-

from yunzhanghu_sdk.client.api.model.authentication import *
from yunzhanghu_sdk.client.api.authentication_client import AuthenticationClient
from yunzhanghu_sdk.example.utils.config_init import init_config

# 用户信息验证
if __name__ == "__main__":
    authentication_client = AuthenticationClient(config=init_config())

    # 银行卡四要素鉴权请求（下发短信验证码）
    req = BankCardFourAuthVerifyRequest(
        card_no="",
        id_card="",
        real_name="",
        mobile="",
    )
    resp = authentication_client.bank_card_four_auth_verify(req)
    print("银行卡四要素鉴权请求（下发短信验证码）返回：", resp.code, resp.message, resp.data)

    # 银行卡四要素确认请求（上传短信验证码）
    req = BankCardFourAuthConfirmRequest(
        card_no="",
        id_card="",
        real_name="",
        mobile="",
        captcha="",
        ref="",
    )
    resp = authentication_client.bank_card_four_auth_confirm(req)
    print("银行卡四要素确认鉴权（上传短信验证码）返回：", resp.code, resp.message, resp.data)

    # 银行卡四要素验证
    req = BankCardFourVerifyRequest(
        card_no="",
        id_card="",
        real_name="",
        mobile="",
    )
    resp = authentication_client.bank_card_four_verify(req)
    print("银行卡四要素验证返回：", resp.code, resp.message, resp.data)

    # 银行卡三要素验证
    req = BankCardThreeVerifyRequest(
        card_no="",
        id_card="",
        real_name="",
    )
    resp = authentication_client.bank_card_three_verify(req)
    print("银行卡三要素验证返回：", resp.code, resp.message, resp.data)

    # 身份证实名验证
    req = IDCardVerifyRequest(
        id_card="",
        real_name="",
    )
    resp = authentication_client.id_card_verify(req)
    print("身份证实名验证返回：", resp.code, resp.message, resp.data)

    # 上传免验证用户名单信息
    req = UserExemptedInfoRequest(
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
    resp = authentication_client.user_exempted_info(req)
    print("上传免验证用户名单信息返回：", resp.code, resp.message, resp.data)

    # 查看免验证用户名单是否存在
    req = UserWhiteCheckRequest(
        id_card="",
        real_name="",
    )
    resp = authentication_client.user_white_check(req)
    print("查看免验证用户名单是否存在返回：", resp.code, resp.message, resp.data)

    # 银行卡信息查询
    req = GetBankCardInfoRequest(
        card_no="",
        bank_name="",
    )
    resp = authentication_client.get_bank_card_info(req)
    print("银行卡信息查询返回：", resp.code, resp.message, resp.data)