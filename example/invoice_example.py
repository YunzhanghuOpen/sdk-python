# -*- coding: utf-8 -*-
from yzh_py.client.api.model.invoice import *
from yzh_py.client.api.invoice_client import InvoiceClient
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

    # 查询平台企业已开具和待开具发票金额
    getinvoicestatrequest = GetInvoiceStatRequest(
        broker_id="",
        dealer_id="",
        year="",
    )
    getinvoicestatrequest_res = InvoiceClient.get_invoice_stat(getinvoicestatrequest)
    print("查询平台企业已开具和待开具发票金额返回：", getinvoicestatrequest_res.code, getinvoicestatrequest_res.message,
          getinvoicestatrequest_res.data)

    # 查询可开票额度和开票信息
    getinvoiceamountrequest = GetInvoiceAmountRequest(
        broker_id="",
        dealer_id="",
    )
    getinvoiceamountrequest_res = InvoiceClient.get_invoice_amount(getinvoiceamountrequest)
    print("查询可开票额度和开票信息返回：", getinvoiceamountrequest_res.code, getinvoiceamountrequest_res.message,
          getinvoiceamountrequest_res.data)

    # 开票申请
    applyinvoicerequest = ApplyInvoiceRequest(
        invoice_apply_id="",
        broker_id="",
        dealer_id="",
        amount="",
        invoice_type="",
        bank_name_account="",
        goods_services_name="",
        remark="",
    )
    applyinvoicerequest_res = InvoiceClient.apply_invoice(applyinvoicerequest)
    print("开票申请返回：", applyinvoicerequest_res.code, applyinvoicerequest_res.message, applyinvoicerequest_res.data)

    # 查询开票申请状态
    getinvoicestatusrequest = GetInvoiceStatusRequest(
        invoice_apply_id="",
        application_id="",
    )
    getinvoicestatusrequest_res = InvoiceClient.get_invoice_status(getinvoicestatusrequest)
    print("查询开票申请状态返回：", getinvoicestatusrequest_res.code, getinvoicestatusrequest_res.message,
          getinvoicestatusrequest_res.data)

    # 下载 PDF 版发票
    getinvoicefilerequest = GetInvoiceFileRequest(
        invoice_apply_id="",
        application_id="",
    )
    getinvoicefilerequest_res = InvoiceClient.get_invoice_file(getinvoicefilerequest)
    print("下载 PDF 版发票返回：", getinvoicefilerequest_res.code, getinvoicefilerequest_res.message,
          getinvoicefilerequest_res.data)

    # 发送发票扫描件压缩包下载链接邮件
    sendreminderemailrequest = SendReminderEmailRequest(
        invoice_apply_id="",
        application_id="",
    )
    sendreminderemailrequest_res = InvoiceClient.send_reminder_email(sendreminderemailrequest)
    print("发送发票扫描件压缩包下载链接邮件返回：", sendreminderemailrequest_res.code, sendreminderemailrequest_res.message,
          sendreminderemailrequest_res.data)












