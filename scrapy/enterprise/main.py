# encoding: utf-8

""" 
@version: v1.0 
@author: pu_yongjun
"""
from scrapy import cmdline

if __name__ == '__main__':
    cmdline.execute('scrapy crawl qym_full'.split())
