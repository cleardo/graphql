# coding=utf-8

"""
频道网关接口
"""
import urllib
from api_call.auxo_channel_gateway.http import *


class Channel(BaseHttp):
    def __init__(self, env):
        super(Channel, self).__init__(env=env)

    # ------------------ 频道 ------------------- #
    def get_channel_list(self, status=None, token_type=2):
        """
        GET /v1/channels 查询频道列表
        返回值：[ChannelVo] 类型
        """
        method = 'GET'
        url = '/channels'
        if status is not None:
            url += '?status=' + str(status)

        self.set_auth(token_type=token_type, url=url, method=method)
        response = self.get(url)

        return response

    def search_channel_resource(self, resource_find_data=None, token_type=2):
        """
        POST /v1/channels/resources/actions/find 根据资源名称查询各个频道下的资源
        body参数：ResourceFindVo 类型
        返回值：[ChannelResourceFindResultVo] 类型
        """
        # 请求基本信息：方法、url
        method = 'POST'
        url = '/channels/resources/actions/find'

        # 参数结构对象实例数值获取
        body_data = resource_find_data.get()

        # 身份信息设置
        self.set_auth(token_type=token_type, url=url, method=method)

        # 发送请求
        response = self.post(url, body_data)

        # 返回响应
        return response
