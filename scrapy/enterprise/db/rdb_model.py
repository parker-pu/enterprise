# encoding: utf-8

""" 
@version: v1.0 
@author: pu_yongjun
"""
from sqlalchemy import (
    Column, String, DateTime,
    Table, MetaData, text
)
from sqlalchemy.dialects.mysql import LONGTEXT


class MeCreateTable(object):

    def __init__(self, engine):
        self.engine = engine
        self.metadata = MetaData(self.engine)

    def create_tables(self):
        """ 存放的是一些需要去执行的表结构，针对的是MySQL，其余数据库可能微调
        """
        qy_info = Table(
            "qym_erp_info", self.metadata,

            Column('pk_md5', String(32), primary_key=True),

            Column('erp_code', String(150)),
            Column('taxpayers_code', String(100)),
            Column('registration_number', String(100)),
            Column('organization_code', String(100)),
            Column('name', String(100)),
            Column('legal_representative', String(200)),
            Column('erp_type', String(200)),
            Column('erp_status', String(50)),
            Column('registered_cap', String(50)),
            Column('establish_date', String(20)),
            Column('region', String(50)),
            Column('approved_date', String(50)),
            Column('business_scope', String(50)),
            Column('industry', String(255)),
            Column('forward_label', String(255)),
            Column('exhibition_label', String(255)),
            Column('source_link_url', String(255)),
            Column('html_body', LONGTEXT()),

            Column('insert_time', DateTime, nullable=False,
                   server_default=text("CURRENT_TIMESTAMP")),
            Column(
                'update_time'
                , DateTime
                , server_default=text("CURRENT_TIMESTAMP")
            )
        )

    def create_all(self):
        """ 创建所有的表
        （1）执行 create_tables 创建表的 metadata
        （2）执行 create_all 创建所有表
        """
        self.create_tables()
        self.metadata.create_all(self.engine)
