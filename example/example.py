# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os
import sys

from src.config.config import *
from src.model.payment import *
from src.payment_client import PaymentClient

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


if __name__ == "__main__":
    dealer_id = "25331815"
    broker_id = "27532644"
    sign_type = "rsa"
    app_key = "0gyU31LaiFfZRrfqq3UZiUl7JVk516ES"
    des3key = "Isg2WsfdbyM4Dt6sJ1yzx6iP"
    private_key = '''
    -----BEGIN PRIVATE KEY-----
    MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDACZcSLLFF8KX2/L+Zo5cAsUxuFdj1XBHJvJ8pr5jlM8YXKocNHcwMbG5fFl/+5HW41skqntBLl9IXHkO9QhL7jBh1RvOg22WK7ivzWKG3ZeX3cYfCJ/q2G3YIom5pYjksGhkqUaKPcruYhCcJi55eHPNMiqvxT3A2HmuDHHa/E7TgQTiC9u5tx7aNcLNxz90OC62PBUDb9Z8p6samH5eHinYpplHG8n1jJX6WXimOxHVXRW5C5bnkeCoMcnylLYkWpMYck7jXsFEF3qu8gktjXgmj8Hc3sXcm5uaDwa3hIwswAQJGJWUpHPunuGjkhTRLM3uKKn2NVSLwdGufsZj7AgMBAAECggEBAK4WQ4hrUY04ugtsVvkdrt8m20WUsqjC/TEnuBXfJLjrNXF80Q8X6wl8JpY2v3FfhES7GYR0khllGURx4DCqvHCjMOzoFCXHnobSoK8qsveB/XZSyiI9ge8id98d+P+51mBfjF6rwLVP6jY53vWtRzTEA99oerT4MZ4t94LVA+T0kW0bF+46vO12++7PkXWCtB5XNEYHBU9bp3UNxb68HNccareOXkVcnMHZ0u26Ltw/ZAgXowJlYVlxS9JAQbvkEC9/gu17eEIbIXzOWZhepkrueDnPRKsA9hkXTbRPbc4uAh2ISX5m9tzqjTiuXaF3DovOuXv40OPinQxdfqil5MECgYEA9PMfQH/C+3EGZQYDo7YJwEIPV0n9PzAWVEZQMdDYgztY9+bFpkJ4gft3TOi76Jqe7Be+TR8IpOwruLfD4Fa5rpjvAWZ1TWHgTM3lrHosJWZWFKR4fIjZtTeu4FI0j8jihdWAbJENxJuEBJcNuakt9bBN3VsdmuZmU7MvieOh6KECgYEAyLNlBT1Ze+DEz7NjZBb8QZl5fzQulDWFttfGVMhO60v+d5hrOb2KZyuVyOLZW8raS8qmCG2TTg0y2Kcz53nJ6FMhUGZFn7VP529dd7EPBHZO1r5T8PgqcAQ29w7Nm/7su1aWh75NijCqDK++HL6yWVamfp4bvBIleS5FgsKUEBsCgYAIhYzIyakW5k+6pALsZyDft2yhNMnCsQGV3PxdP07JAf+OYFDv/9ABdaYo3s/qv7ZXsFvGgxXh5vV+b6Y438uF73whKFdcYdNT2LXs0jNG+dB012P5sSkhzNYgp7t8ZRi8XzkgjctU07Q8FKU9mE0pBwEuekUFZo6YytsUiP7RAQKBgQCst211P+GVMM5Oa/NZvEoj7f7X0EFRfGnw+uoMJkF8Tm7T3xBPpWTI+oIxWb9yNjT8So3t7NZ6sfMS7XlGd9GhJIEj3o+GLJNx+K24BmCFF4crWKmGUxq6QXZH0K5y08RIR/DNKqEyDkUZG9iAhj+XkHFBv7DgfcFP8tkQ+YBQBwKBgHiM1XPYvXPPW/LHJE1LR+wfoMxYp96/PsXbfxOwe5faHt+QDeFOx2oSOGW4/aCDDaf4oDVqqr6jEqrszZZ0ade7mYlW652td/f9vxIzPUsoeAEV8D5lgwndKKz2gs/tF7buP/drmAx3NKYvP2EVSbuWiGzRX/nNUsg+/RKCR56k
    -----END PRIVATE KEY-----
    '''
    public_key = '''
    -----BEGIN RSA PUBLIC KEY-----
    MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDM8TIYAVN+xwvTyNOttvt+rVGoKy0L34nVq4mPouOmRD8UyqpZvXq/bE+Fdl07jvn4u7hRkOk8V1q+zDwCei1rs0T3FcAhRlzk00vuE/BxE+KvoIyor9epZjn+3/0Y/u+tp1WJHXFF/6K/DpxThbmoTR5sbSPGVxNMgAMmu6PVLQIDAQAB
    -----END RSA PUBLIC KEY-----
    '''
    config = Config(
        host="https://api-service.yunzhanghu.com",
        dealer_id=dealer_id,
        sign_type=sign_type,
        app_key=app_key,
        des3key=des3key,
        private_key=private_key,
        public_key=public_key,
    )
    # 获取订单详情
    request = GetOrderRequest(
        order_id="232211231231231",
        channel="微信",
        data_type="encryption"
    )
    client = PaymentClient(config)
    resp = client.get_order(request)

    print(resp.code, resp.message, resp.data)
