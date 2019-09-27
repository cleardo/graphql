# coding=utf-8

"""
网关接口用例
- 频道相关
"""
from config.gbl import *
from api_call.auxo_channel_gateway.channel import Channel
from data_struct.auxo_channel_gateway.channel_data import *


###########################################
# 遵循unittest框架的测试用例：
#   1.测试类要继承于unittest.TestCase类
#   2.测试方法要以“test_”开头
###########################################
class ChannelTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rand_o = CoRand()
        cls.rest_o = Restful()

        cls.channel_o = Channel(ENVIRONMENT)

        # 默认项目的频道1
        cls.channel_id_1 = '09fa3cef-2e4b-45c7-91e6-ecb7ded3ee86'
        # 默认项目的频道2，用于更新 等
        cls.channel_id_2 = '83e78a20-e8df-43c0-964f-e92c6d1d3c37'

    def setUp(self):
        pass

    def tearDown(self):
        """
        回收数据
        """
        pass

    # ------------------ 查询频道列表 ------------------ #
    def test_get_channel_list_without_status_ok(self):
        """
        查询频道列表，不传status：返回的列表中，含有两个符合默认查询状态的频道
        level:1,2,3
        """
        # 查询频道列表
        res_get_list = self.channel_o.get_channel_list(status=None)
        data_dict = self.rest_o.parse_response(res_get_list, OK, GET_CHANNEL_LIST_FAILED)
        is_find_1 = False
        is_find_2 = False
        for channel in data_dict:
            ChannelVo(channel)
            if channel['id'] == self.channel_id_1:
                is_find_1 = True
            if channel['id'] == self.channel_id_2:
                is_find_2 = True
        assert_that(is_find_1, equal_to(True))
        assert_that(is_find_2, equal_to(True))

    # -------- 根据资源名称查询各个频道下的资源 --------- #
    def test_get_resource_by_invalid_name_ok(self):
        """
        查询资源，name=随机字符串内容：返回的列表中，每个频道的page均为空
        level:1,2,5,6
        """
        # 查询资源
        find_data = ResourceFindVo(name=self.rand_o.randomword(10))
        res_get_list = self.channel_o.search_channel_resource(find_data)
        resource_get = self.rest_o.parse_response(res_get_list, OK, SEARCH_CHANNEL_RESOURCE_BY_NAME_FAILED)
        for channel in resource_get:
            assert_that(len(channel['page']['items']), equal_to(0))
