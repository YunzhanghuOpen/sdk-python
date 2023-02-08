# -*- coding: utf-8 -*-
from yzh_py.client.api.model.invoice import *
from yzh_py.client.api.invoice_client import InvoiceClient
from yzh_py.example.utils.configinit import init_config

# 发票开具
if __name__ == '__main__':
    InvoiceClient = InvoiceClient(config=init_config())
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