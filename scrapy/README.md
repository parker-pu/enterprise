# enterprise
爬取企业信息

## 目标结果
- 表结构如下

字段 | 类型 | 说明
---|--- | ---
pk_md5 | String(32) | 数据的唯一属性id
erp_code | String(150) | 统一社会信用代码
taxpayers_code | String(100) | 纳税人识别号
registration_number | String(100) | 注册号
organization_code | String(100) | 机构代码
name | String(100) | 名称
legal_representative | String(200) | 法定代表人
erp_type | String(200) | 企业类型
erp_status | String(50) | 经营状态
registered_cap | String(50) | 注册资本
establish_date | String(20) | 成立日期
region | String(50) | 登记机关
approved_date | String(50) | 经营期限
industry | String(50) | 行业
business_scope | String(255) | 经营范围
forward_label | String(255) | 前瞻标签
exhibition_label | String(255) | 展会标签
source_link_url | String(255) | 网页链接
html_body | LONGTEXT | 网页内容
insert_time | DateTime | 插入时间
update_time | DateTime | 更新时间