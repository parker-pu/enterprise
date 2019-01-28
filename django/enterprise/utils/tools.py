# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Author  : pu yong_jun

"""
这个文件里面是一些小程序
"""


def fill_default(value, default):
    """ 这个函数的作用是用来返回一个填充值的函数
    :param value: 需要判断的值
    :param default: 默认的填充值
    :return:
    """
    if value:
        return value
    return default


def diff_arr(arr1, arr2):
    """ 对比两个数组的不同
    :param arr1:
    :param arr2:
    :return:
    """
    return list(set(arr1) - set(arr2))


def handel_bool(value):
    """ 返回Python的 True 与 False
    :param value:
    :return:
    """
    if str(value).upper() == 'TRUE':
        return True
    return False
