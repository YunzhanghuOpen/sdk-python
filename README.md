# 云账户 SDK for Python

欢迎使用云账户 SDK for Python。  
云账户是一家专注为平台企业和新就业形态劳动者提供高质量灵活就业服务的新时代企业。云账户 SDK 对云账户综合服务平台 API 接口进行封装，让您不必关心过多参数请求，帮助您快速接入到云账户综合服务平台。云账户 SDK for Python 为您提供签约、下单、回调、数据查询等功能，帮助您完成与云账户综合服务平台的接口对接及业务开发。  
如果您在使用过程中遇到任何问题，欢迎在当前 GitHub 提交 Issues，或发送邮件至技术支持组 [techsupport@yunzhanghu.com](mailto:techsupport@yunzhanghu.com)。

### 环境要求

云账户 SDK for Python 支持 Python3 及其以上版本。

### 配置密钥

#### 1、获取配置

使用云账户 SDK for Python 前，您需先获取 dealer_id、broker_id、3DES Key、App Key 信息。    
获取方式：使用开户邮件中的账号登录【[云账户综合服务平台](https://service.yunzhanghu.com/user/login)】，选择“业务中心 > 业务管理 > 对接信息”，查看并获取以上配置信息。  
![获取配置信息](https://yos.yunzhanghu.com/getobject/duijiexinxi.png?isAttachment=false&fileID=9487bd54b93a5abf49003c2b8ce7e069bfa24220&signature=X%2BR7PocQgPqSpR2xM1TgYU6lAapr%2FB9p3aFof03Gcfw%3D)

#### 2、生成密钥

- 方式一：使用 OpenSSL 生成 RSA 公私钥

```
① ⽣成私钥 private_key.pem

Openssl-> genrsa -out private_key.pem 2048 位  // 建议密钥⻓度⾄少为 2048 位

OpenSSL-> pkcs8 -topk8 -inform PEM -in private_key.pem -outform PEM -nocrypt -out private_key_pkcs8.pem  // 将私钥转为 PKCS8 格式 

② ⽣成公钥⽂件 pubkey.pem

Openssl-> rsa -in private_key.pem -pubout -out pubkey.pem

```

- 方式二：使用工具生成

请联系云账户技术支持获取 RSA 密钥生成工具

#### 3、配置密钥

登录【[云账户综合服务平台](https://service.yunzhanghu.com/user/login)】，选择“业务中心 > 业务管理 > 对接信息”，单击页面右上角的“编辑”，配置平台企业公钥。
![配置平台企业公钥信息](https://yos.yunzhanghu.com/getobject/dujiexinxi-2.png?isAttachment=false&fileID=84e3cd1684a61c1e32eb0e7b7f43390cd053206b&signature=mqW8Zbk7h3gYXfzjR99pK%2B0pgVLcLly3VjBB2KsqDvQ%3D)


## 安装 Python SDK

### 通过 PIP 安装

通过 PIP 获取安装是使用 SDK 的推荐方法，PIP 是  Python 的包管理工具。关于 PIP 详细可参考[ PIP 官网](https://pypi.org/) 。

1. 执行以下安装命令：

   > pip install yzh_py

2. 在您的代码中引用对应模块代码，可参考示例。

### 通过源码包安装

1. 前往 [Github 仓库](https://github.com/YunzhanghuOpen/sdk-python) 下载源码压缩包
2. 解压源码包到您项目合适的位置
3. 在您的代码中引用对应模块代码，可参考示例


## 快速使用

### 示例功能列表

- [用户信息验证](./example/authentication_example.py)
- [H5 签约](./example/h5usersign_example.py) or [API 签约](./example/apiusersign_example.py)
- [个体工商户注册（新经济 H5）](./example/bizlicxjjh5_example.py) or [个体工商户注册（新经济 H5+API）](./example/bizlicxjjh5api_example.py)
- [实时支付](./example/payment_example.py)
- [异步通知](./example/notify_example.py)
- [对账文件获取](./example/dataservice_example.py)
- [发票开具](./example/invoice_example.py)

#### 示例

```

from yzh_py.client.api.model.payment import GetOrderRequest
from yzh_py.client.api.payment_client import PaymentClient
from yzh_py.config import *

if __name__ == "__main__":
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
    # 获取订单详情
    request = GetOrderRequest(
        order_id="232211231231231",
        channel="微信",
        data_type="encryption"
    )
    # 自定义 request-id
    # request.request_id = "XXXXX"
    client = PaymentClient(config)
    resp = client.get_order(request)

    print(resp.code, resp.message, resp.request_id, resp.data)

```
