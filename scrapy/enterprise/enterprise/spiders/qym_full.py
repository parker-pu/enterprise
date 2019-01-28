# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from enterprise.items import EnterpriseItem
from utils.base_tools import gen_md5, get_now_datetime


class QymSpider(CrawlSpider):
    name = 'qym_full'
    allowed_domains = ['qichamao.com']
    start_urls = ['https://www.qichamao.com']

    # 设置解析link的规则，callback是指解析link返回的响应数据的的方法
    rules = [
        Rule(
            LinkExtractor(
                allow='.*?orgcompany/searchitemdtl.*?',
                allow_domains='qichamao.com'
            ),
            callback='erp_parse', follow=True
        ),
    ]

    @staticmethod
    def erp_parse(response):
        """ 这个函数是解析的主函数
        :param response:
        :return:
        """
        # 页面主要信息
        page_main_info = response.xpath(
            '*//ul[@class="art-basic"]/li'
            '|*//ul[@class="art-basic art-basic-swot"]/li'
        )

        item_dict = dict()
        for li in page_main_info:
            type_name = str(li.xpath(
                'span[@class="tit"]/text()'
            ).extract_first()).strip()

            type_value = str(li.xpath(
                'span[@class="info"]'
            ).xpath('string(.)').extract_first()).strip()

            item_dict[type_name] = type_value

        erp_info_dict = dict()
        # 企业基本信息
        erp_info_dict['erp_code'] = item_dict.get('统一社会信用代码：')
        erp_info_dict['taxpayers_code'] = item_dict.get('纳税人识别号：')
        erp_info_dict['registration_number'] = item_dict.get('注册号：')
        erp_info_dict['organization_code'] = item_dict.get('机构代码：')
        erp_info_dict['name'] = item_dict.get('名称：')
        erp_info_dict['legal_representative'] = item_dict.get('法定代表人：')
        erp_info_dict['erp_type'] = item_dict.get('企业类型：')
        erp_info_dict['erp_status'] = item_dict.get('经营状态：')
        erp_info_dict['registered_cap'] = item_dict.get('注册资本：')
        erp_info_dict['establish_date'] = item_dict.get('成立日期：')
        erp_info_dict['region'] = item_dict.get('所属地区：')
        erp_info_dict['approved_date'] = item_dict.get('核准日期：')
        erp_info_dict['business_scope'] = item_dict.get('经营范围：')

        # 行业标签
        erp_info_dict['industry'] = item_dict.get('所属行业：')
        erp_info_dict['forward_label'] = item_dict.get('前瞻标签：')
        erp_info_dict['exhibition_label'] = item_dict.get('展会标签：')

        # 额外的基础信息
        erp_info_dict['source_link_url'] = response.url
        erp_info_dict['html_body'] = response.body
        erp_info_dict['pk_md5'] = gen_md5(response.url)
        erp_info_dict['update_time'] = get_now_datetime()

        # 返回企业信息
        erp_item = EnterpriseItem()
        erp_item['table_name'] = 'qym_erp_info'
        erp_item['data_rows'] = [erp_info_dict]
        yield erp_item
