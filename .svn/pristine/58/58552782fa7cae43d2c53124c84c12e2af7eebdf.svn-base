# coding=utf-8

"""
示范如何处理查询串中参数项变动的情况
"""

import urllib
from nd.rest.rand import CoRand
from api_call.http_util import HttpUnity

__author__ = 'Administrator'


def get_url(url_prefix, req_param):
    """
    遍历参数字典，不为None的值赋值给查询串的相同字段
    url_prefix：url前缀
    req_param：传入的查询参数
    """
    query_dict = dict()
    for key in req_param.keys():
        if req_param[key] is not None:
            query_dict[key] = req_param[key]

    url = url_prefix + urllib.urlencode(query_dict)
    return url


class Others(HttpUnity):
    def __init__(self, env):
        HttpUnity.__init__(self, env)

    def query_params_example(self, req_param):
        """
        示范url中查询串参数的处理
        """
        # 1.根据传入的参数情况，拼接url的查询串
        url_prefix = "/v0.1/dentries/actions/asynpack?"
        url = get_url(url_prefix, req_param)
        print "url： ", url

        # 2.发出http请求，此处省略
        # ..............


if __name__ == "__main__":
    # 传入的参数中，字段名与接口规定的一致
    # 当次不需要传的字段取值为None
    req_param = dict()
    req_param['session'] = CoRand.uuid()
    req_param['rename'] = None
    req_param['is_asyn'] = True
    other_o = Others(env='test')
    other_o.query_params_example(req_param)
