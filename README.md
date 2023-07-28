# 云账户 SDK for Python

欢迎使用云账户 SDK for Python。  
云账户是一家专注为平台企业和新就业形态劳动者提供高质量灵活就业服务的新时代企业。云账户 SDK 对云账户综合服务平台 API 接口进行封装，帮助您快速接入到云账户综合服务平台。云账户 SDK for Python 为您提供签约、支付、回调、数据查询等功能，帮助您完成与云账户综合服务平台的接口对接及业务开发。
如果您在使用过程中遇到任何问题，请在当前 GitHub 提交 Issues，或发送邮件至技术支持组 [techsupport@yunzhanghu.com](mailto:techsupport@yunzhanghu.com)。

### 环境要求

云账户 SDK for Python 支持 Python 3.0 及以上版本。

### 配置密钥

#### 1、获取配置

使用云账户 SDK for Python 前，您需先获取 dealer_id、broker_id、3DES Key、App Key、云账户公钥。
获取方式：使用开户邮件中的账号登录【[云账户综合服务平台](https://service.yunzhanghu.com)】，选择“业务中心 > 业务管理 > 对接信息”，查看并获取以上配置信息。
![获取配置信息](https://yos.yunzhanghu.com/getobject/duijiexinxi.png?isAttachment=false&fileID=9487bd54b93a5abf49003c2b8ce7e069bfa24220&signature=X%2BR7PocQgPqSpR2xM1TgYU6lAapr%2FB9p3aFof03Gcfw%3D)

#### 2、生成密钥

- 方式一：使用 OpenSSL 生成 RSA 公私钥

```
① ⽣成私钥 private_key.pem

OpenSSL-> genrsa -out private_key.pem 2048   // 建议密钥⻓度⾄少为 2048 位

OpenSSL-> pkcs8 -topk8 -inform PEM -in private_key.pem -outform PEM -nocrypt -out private_key_pkcs8.pem  // 将私钥转为 PKCS8 格式

② ⽣成公钥⽂件 pubkey.pem

OpenSSL-> rsa -in private_key.pem -pubout -out pubkey.pem

```

- 方式二：使用工具生成

登录【[云账户开放平台](https://open.yunzhanghu.com)】，选择“开发工具下载 > 开发助手 > 工具下载”，下载安装“云账户开放平台开发助手”。

#### 3、配置密钥

登录【[云账户综合服务平台](https://service.yunzhanghu.com)】，选择“业务中心 > 业务管理 > 对接信息”，单击页面右上角的“编辑”，配置平台企业公钥。
![配置平台企业公钥信息](https://yos.yunzhanghu.com/getobject/dujiexinxi-2.png?isAttachment=false&fileID=84e3cd1684a61c1e32eb0e7b7f43390cd053206b&signature=mqW8Zbk7h3gYXfzjR99pK%2B0pgVLcLly3VjBB2KsqDvQ%3D)


## 安装 Python SDK

### 通过 PIP 安装

推荐通过 Python 包管理工具 PIP 获取并安装云账户 SDK for Python。PIP 详细介绍请参考[ PIP 官网](https://pypi.org) 。

1. 执行以下命令安装云账户 SDK for Python：

   > pip3 install yunzhanghu_sdk

2. 在您的代码中引用对应模块代码，具体引用方式可参考下文示例

### 通过源码包安装

1. 前往 [Github 仓库](https://github.com/YunzhanghuOpen/sdk-python) 下载源码压缩包。
2. 解压源码包到您项目的合适位置。
3. 在您的代码中引用对应模块代码，可参考示例。


## 快速使用

### 示例功能列表

- [用户信息验证](yunzhanghu_sdk/example/authentication_example.py)
- [用户签约（H5 签约）](yunzhanghu_sdk/example/h5usersign_example.py) or [用户签约（API 签约）](yunzhanghu_sdk/example/apiusersign_example.py)
- [个体工商户注册（云账户新经济 H5）](yunzhanghu_sdk/example/bizlicxjjh5_example.py) or [个体工商户注册（云账户新经济 H5+API）](yunzhanghu_sdk/example/bizlicxjjh5api_example.py)
- [实时支付](yunzhanghu_sdk/example/payment_example.py)
- [异步通知](yunzhanghu_sdk/example/notify_example.py)
- [对账文件获取](yunzhanghu_sdk/example/dataservice_example.py)
- [发票开具](yunzhanghu_sdk/example/invoice_example.py)

#### 示例

```
#提示：
   #为了保护秘钥安全，建议将密钥配置到环境变量中或者配置文件中。
   #请勿在代码中使用硬编码密钥，可能导致密钥暴露，存在安全隐患。

from yunzhanghu_sdk.client.api.model.payment import GetOrderRequest
from yunzhanghu_sdk.client.api.payment_client import PaymentClient
from yunzhanghu_sdk.config import *

if __name__ == "__main__":
    # 平台企业 ID，登录云账户综合服务平台，选择“业务中心 > 业务管理 > 对接信息”获取
    dealer_id = "xxx"
    # 综合服务主体 ID，登录云账户综合服务平台，选择“业务中心 > 业务管理 > 对接信息”获取
    broker_id = "xxx"
    # 签名算法，登录云账户综合服务平台，选择“业务中心 > 业务管理 > 对接信息”获取
    # 签名算法为 RSA，参数固定为：rsa
    sign_type = "rsa"
    # 平台企业 App Key，登录云账户综合服务平台，选择“业务中心 > 业务管理 > 对接信息”获取
    app_key = "xxx"
    # 平台企业 3DES Key，登录云账户综合服务平台，选择“业务中心 > 业务管理 > 对接信息”获取
    des3key = "xxx"
    # 平台企业私钥，自行生成 RSA 公私钥，私钥请妥善保存，谨防泄露。平台企业公钥请登录云账户综合服务平台配置，选择“业务中心 > 业务管理 > 对接信息”，单击页面右上角的“编辑”，完成平台企业公钥配置。
    dealer_private_key = '''
    -----BEGIN PRIVATE KEY-----
    xxx
    -----END PRIVATE KEY-----
    '''
    # 云账户公钥，登录云账户综合服务平台，选择“业务中心 > 业务管理 > 对接信息”获取
    yzh_public_key = '''
    -----BEGIN PUBLIC KEY-----
    xxx
    -----END PUBLIC KEY-----
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
        order_id="",
        channel="",
        data_type=""
    )
    # 建议自定义并将 request-id 记录在日志中
    # request.request_id = "XXXXX"
    client = PaymentClient(config)
    resp = client.get_order(request)

    print(resp.code, resp.message, resp.request_id, resp.data)