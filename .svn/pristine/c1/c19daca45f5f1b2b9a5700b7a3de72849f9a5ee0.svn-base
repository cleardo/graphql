# coding=utf-8

import os
import json
import time
import types
from hamcrest import *
import datetime
from nd.rest.restful import Restful

import sys
reload(sys)
sys.setdefaultencoding('utf8')


# #################### http状态码 宏定义 ################## #
OK = 200  # 请求成功
CREATED = 201  # 资源创建成功
ACCEPTED = 202  # pOST，DELETE或者PATCH请求提交成功，稍后将异步的进行处理
NO_CONTENT = 204  # Response中包含一些Header和一个状态行， 但不包括实体的主题内容（没有response body）
NOT_MIDIFIED = 304  # 资源最新，使用客户端缓存
BAD_REQUEST = 400  # 无效请求(默认)
REQUIRE_ARGUMENT = 400  # 缺少参数
INVALID_ARGUMENT = 400  # 无效参数(格式不对,长度过长或过短等)
UNAUTHORIZED = 401  # 未授权(默认)
AUTH_TOKEN_EXPIRED = 401  # 授权已过期
AUTH_INVALID_TOKEN = 401  # 无效的授权(如token不存在、需要mac签名、mac签名无效、nonce无效、重复提交等)
AUTH_INVALID_TIMESTAMP = 401  # 无效的时间戳，当时间戳与系统的差异大于5分钟后，产生该错误，客户端需要进行校时操作。
REQUEST_DENIED = 403  # 请求受限(默认)
AUTH_DENIED = 403  # 授权受限（无权限或IP地址受限等）
NOT_FOUND = 404  # 请求的路径不存在(默认)
METHOD_NOT_ALLOWED = 405  # 请求的方法不支持
NOT_ACCEPTABLE = 406  # 服务器无法提供请求时指定的数据响应格式
GONE = 410  # 被请求的资源在服务器上已经不再可用，而且没有任何已知的转发地址
UNSUPPORTED_MEDIA_TYPE = 415  # 服务器不支持请求所提交的数据格式
REQUEST_RATE_LIMITED = 429  # 请求过于频繁
INTERNAL_SERVER_ERROR = 500  # 服务器内部错误(默认)
BAD_GATEWAY = 502  # 无效网关
SERVICE_UNAVAILABLE = 503  # 服务不可用


INVALID_AUTH_TIMESTAMP = '无效的时间戳，当时间戳与系统的差异大于5分钟'


# #################### 数据类公共方法 ################## #
def copy_dict(ori_dict, dollar=True):
    """
    复制字典，但是过滤为None的字段
    参数：ori_dict 原字典数据
    return：param_dict 过滤了为None的字段、以及self
    """
    param_dict = dict()
    for key in ori_dict:
        if key != 'self' and ori_dict[key] is not None:
            # 若dollar=True，则在以下参数名前面加“$”（GQL的用法）；
            # 否则，不在以下列表的参数名前加“$”
            if dollar and (key in ['offset', 'limit', 'filter', 'order', 'result', 'select']):
                param_dict['$' + key] = ori_dict[key]
            else:
                param_dict[key] = ori_dict[key]

    return param_dict


def convert_list(ori_dict):
    """
    将param转换成list
    参数：ori_dict 原字典数据
    return：param_list 将dict转换成key-value的list存放
    """
    param_list = []

    for key in ori_dict.keys():
        param = {}
        value = ori_dict[key]
        param['key'] = key
        param['value'] = value
        param_list.append(param)

    return param_list


def get_dict(data):
    """
    复制内容：
    若data为dict，直接复制；
    否则先转换成dict，再复制
    """
    if isinstance(data, types.StringType):
        param_dict = json.loads(data)
    else:
        assert_that(type(data), types.DictType)
        param_dict = data

    return param_dict


def get_sorted_list(org_list, org_id, position, target_id):
    """
    获取排序后的list
    参数：org_list：初始列表
    参数：org_id；需要移动的id
    参数：position：插入到目的id的前面或后面
    参数：target_id：目的id
    返回：排序后的list
    """
    if target_id == org_id:
        return org_list
    org_list.remove(org_id)
    # org_index = org_list.index(org_id)

    target_index = org_list.index(target_id)

    insert_index = 0

    if position == "up":
        insert_index = target_index
    else:
        insert_index = target_index + 1

    org_list.insert(insert_index, org_id)
    return org_list


class BaseData(object):
    """
    数据的基础类
    """

    def __init__(self):
        """
        将初始化传入的参数赋值给成员变量
        """
        self.params = dict()

    def get(self):
        """
        返回初始的数据
        """
        return self.params


def get_expect_time(interval_days=0, interval_hour=0, interval_min=0, interval_second=0, time_type=0):
    """
    获取时间，精准到毫秒（13位时间戳）
    type：
    0        获取未来时间
    其他     获取之前的时间
    """
    if time_type == 0:
        later_time = datetime.datetime.now() + datetime.timedelta(
            days=interval_days, hours=interval_hour, minutes=interval_min, seconds=interval_second
        )
        return later_time.strftime("%Y-%m-%d %H:%M:%S")
    else:
        earlier_time = datetime.datetime.now() - datetime.timedelta(
            days=interval_days, hours=interval_hour, minutes=interval_min, seconds=interval_second
        )
        return earlier_time.strftime("%Y-%m-%d %H:%M:%S")


class PageResultVo(object):
    """
    分页数据
    """
    def __init__(self, data):
        """
        {
            "count": 0,
            "items": [
                {}
            ]
        }
        """
        self.params = data

        assert_that(self.params, has_key('count'))
        assert_that(self.params, has_key('items'))


class PagerResult(object):
    """
    分页数据
    """
    def __init__(self, data):
        """
        {
            "total": 0,
            "items": [
                {}
            ]
        }
        """
        self.params = data

        assert_that(self.params, has_key('total'))
        assert_that(self.params, has_key('items'))


rest_o = Restful()


def assert_error_token(error_data):
    """
    断言使用了错误的uc token
    :param error_data: 接口返回的数据（data），已转换为字典
    :return:
    """
    error_code = 'UC/AUTH_INVALID_TIMESTAMP'
    error_message = INVALID_AUTH_TIMESTAMP
    rest_o.parse_error_info(error_data, error_code, error_message)


def compare_info(info_1, info_2, skip_keys=['create_time', 'update_time']):
    """
    对比两个字典数据的信息
    :param info_1:
    :param info_2:
    :param skip_keys: 跳过不对比的key的列表
    :return: 无
    """
    for key in info_1:
        if key in skip_keys:
            continue
        message = '与原先的值不一致 key:%s' % key
        assert_that(info_1[key], equal_to(info_2[key]), message)
