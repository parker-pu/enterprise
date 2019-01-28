# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy_redis.spiders import RedisSpider


class QySpider(RedisSpider):
    name = 'xh_qy'

    # redis key
    redis_key = "xh:qy_index"

    # 每批次获取的数量
    redis_batch_size = 10

    # 基础的搜索地址，从该页面获取到验证码
    search_url = 'http://xinhua.qudaba.com/search?key={}'

    def __init__(self, *args, **kwargs):
        super(QySpider, self).__init__(*args, **kwargs)

    def make_requests_from_url(self, url):
        """ This method is deprecated.

        :param url: 其实不是url，是从 redis 获取到的数据
        :return: 返回的是 Scrapy 的 Request 请求

        重写 Scrapy 的 make_requests_from_url 方法，在请求里面加上请求的内容
        """
        return Request(url, dont_filter=True, meta={'search_name': url})

    def parse(self, response):
        print(response.body)
