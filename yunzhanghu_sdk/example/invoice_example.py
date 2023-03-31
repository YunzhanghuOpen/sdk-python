# -*- coding: utf-8 -*-

from yunzhanghu_sdk.client.api.model.invoice import *
from yunzhanghu_sdk.client.api.invoice_client import InvoiceClient
from yunzhanghu_sdk.example.utils.config_init import init_config

# 发票开具
if __name__ == "__main__":
    invoice_client = InvoiceClient(config=init_config())

    # 查询平台企业已开具和待开具发票金额
    req = GetInvoiceStatRequest(
        broker_id="",
        dealer_id="",
        year="",
    )
    resp = invoice_client.get_invoice_stat(req)
    print("查询平台企业已开具和待开具发票金额返回：", resp.code, resp.message, resp.data)

    # 查询可开具发票额度和发票开具信息
    req = GetInvoiceAmountRequest(
        broker_id="",
        dealer_id="",
    )
    resp = invoice_client.get_invoice_amount(req)
    print("查询可开具发票额度和发票开具信息返回：", resp.code, resp.message, resp.data)

    # 发票开具申请
    req = ApplyInvoiceRequest(
        invoice_apply_id="",
        broker_id="",
        dealer_id="",
        amount="",
        invoice_type="",
        bank_name_account="",
        goods_services_name="",
        remark="",
    )
    resp = invoice_client.apply_invoice(req)
    print("发票开具申请返回：", resp.code, resp.message, resp.data)

    # 查询发票开具申请状态
    req = GetInvoiceStatusRequest(
        invoice_apply_id="",
        application_id="",
    )
    resp = invoice_client.get_invoice_status(req)
    print("查询发票开具申请状态返回：", resp.code, resp.message, resp.data)

    # 查询发票信息
    req = GetInvoiceInformationRequest(
        invoice_apply_id="",
        application_id="",
    )
    resp = invoice_client.get_invoice_information(req)
    print("查询发票信息返回：", resp.code, resp.message, resp.data)

    # 下载 PDF 版发票
    req = GetInvoiceFileRequest(
        invoice_apply_id="",
        application_id="",
    )
    resp = invoice_client.get_invoice_file(req)
    print("下载 PDF 版发票返回：", resp.code, resp.message, resp.data)

    # 发送发票扫描件压缩包下载链接邮件
    req = SendReminderEmailRequest(
        invoice_apply_id="",
        application_id="",
    )
    resp = invoice_client.send_reminder_email(req)
    print("发送发票扫描件压缩包下载链接邮件返回：", resp.code, resp.message, resp.data)
