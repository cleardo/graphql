# coding=utf-8
# from nd.rest import unittest
from config import prome_config
import platform
from prome_lib.graphql_query import GraphqlQuery
import warnings
import time
import random


class DataOperate(object):
    def __init__(self):
        self.GraphqlQuery = GraphqlQuery()

    # 传入 pageSize， offset 获取 指定页面的指定PanelSN信息
    def getPanelSNByPageAndOffset(self, pageSize, offset, showprint=False):
        response, body = self.GraphqlQuery.panels(pageSize, offset, showprint=showprint)
        SN = body['data']['Panels']['panels'][0]['serialNumber']
        return SN

    # 传入groupName 获取 group所在Body中的索引 和 tag 数量
    def getGroupInfo(self, groupName=None):
        groupIndex = None
        response, body = self.GraphqlQuery.tags(showprint=False)
        for i in range(len(body['data']['Tags'])):
            GetgroupName = body['data']['Tags'][i]['group']
            if GetgroupName == groupName:
                groupIndex = i
        tagNum = len(body['data']['Tags'][groupIndex]['values'])
        if groupIndex is None:
            def get_error():
                EnterGroupNameError = " Group: %s is not exist!" % groupName
                warnings.warn(EnterGroupNameError)
            return get_error()
        else:
            return groupIndex, tagNum

    # 输入 groupName 获取Tag list
    def getTagListByGroupName(self, groupName):
        """
        :param groupName:
        :return:
        取值方式：
        tagid = tagidList[i]['tagid']
        tagname = tagidList[i]['tagname']
        """

        tagList = []
        r, b = self.GraphqlQuery.tags(showprint=False)
        groupIndex = None

        # 获取grouName 在tag response 中的索引
        for i in range(len(b['data']['Tags'])):
            if b['data']['Tags'][i]['group'] == groupName:
                groupIndex = i
                break

        if groupIndex is not None:
            tagNum = len(b['data']['Tags'][groupIndex]['values'])

        if groupIndex is not None:
            for i in range(tagNum):
                tagid = b['data']['Tags'][groupIndex]['values'][i]['id']
                tagName = b['data']['Tags'][groupIndex]['values'][i]['value']
                tagList.append({
                    "tagid": "%s" % tagid,
                    "tagname": "%s" % tagName,
                    })
        if len(tagList) == 0:
            def get_error():
                EnterGroupNameError = "Group: %s is not exist!" % groupName
                warnings.warn(EnterGroupNameError)
            return get_error()
        else:
            return tagList

    # 输入 groupName 和 tagIndex 获取 tagid和name
    def getTagidByGroupNameAndTagIndex(self, groupName=None, tagIndex=0):
        tagid = None
        response, bodys = self.GraphqlQuery.tags(showprint=False)
        if groupName is not None:
            groupIndex, tagNum = self.getGroupInfo(groupName)
            if groupIndex is not None:
                tagid = bodys['data']['Tags'][groupIndex]['values'][tagIndex]['id']
                tagName = bodys['data']['Tags'][groupIndex]['values'][tagIndex]['value']
        if tagid is None:
            def get_error():
                EnterGroupNameError = "Group: %s is not exist!" % groupName
                warnings.warn(EnterGroupNameError)
            return get_error()
        else:
            return tagid, tagName

    # 通过groupName 查找指定tag Value 的 Tagid
    def getTagidByGroupNameAndTagValue(self, groupName, tagValue):
        groupIndex = None
        response, body = self.GraphqlQuery.tags(showprint=False)
        for i in range(len(body['data']['Tags'])):
            if body['data']['Tags'][i]['group'] == groupName:
                groupIndex = i
        # 成功获取groupIndex
        if groupIndex is not None:
            tagNum = len(body['data']['Tags'][groupIndex]['values'])
            for i in range(tagNum):
                get_tag_value = body['data']['Tags'][groupIndex]['values'][i]['value']
                if get_tag_value == tagValue:
                    tagId = body['data']['Tags'][groupIndex]['values'][i]['id']
                    return tagId

    # 输入前缀获取当前时间
    def getTimeStr(self, prefix=''):
        TimeStr = prefix + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return TimeStr

    # 随机获取指定数量的随机 SN和 name, Listlen为数量，
    def getRandomPanelSnAndNameList(self, Listlen=5, showprint=False):
        """

        :param Listlen:
        :param showprint:
        :return:
        取值方式：
        serialNumber = PanelList[i]['serialNumber']
        name = PanelList[i]['name']
        """
        pageSize = Listlen + 1
        offset = int(random.uniform(2, 5))
        PanelList = []
        Random_list = self.getDeduplicationRandomList(1, pageSize, Listlen)
        response, body = self.GraphqlQuery.panels(pageSize, offset, showprint=showprint)
        for i in range(Listlen):
            random_param = Random_list[i]
            Name = body['data']['Panels']['panels'][random_param]['name']
            SN = body['data']['Panels']['panels'][random_param]['serialNumber']
            PanelList.append({
                        "name": "%s" % Name,
                        "serialNumber": "%s" % SN,
                        })
        return PanelList

    # 生成指定范围和数量的去重随机数列
    # a = 范围下限， b = 范围上限， c = 数量
    def getDeduplicationRandomList(self, a, b, c):
        if b - a > 0 and a > 0 and b > 0 and c > 0:
            IntList = []
            for i in range(b-a):
                IntList.append(i)
            IntList = random.sample(IntList, c)
            return IntList
        else:
            return -1

    def getRandomConfigurationIdList(self, pageSize=10, showprint=False):
        ConfigurationIdList = []
        r, b = self.GraphqlQuery.configurationList(1, 6666, showprint=showprint)
        total = b['data']['configurationList']['total']
        randomParam = self.getDeduplicationRandomList(1, total, pageSize)
        for i in range(pageSize):
            index = randomParam[i]
            configurationId = b['data']['configurationList']['configurations'][index]['configurationId']
            ConfigurationIdList.append(configurationId)
        return ConfigurationIdList

    # 通过Description获取ConfigurationIdList
    def getConfigurationIdListByDescription(self, descriptions, showprint=False):
        ConfigurationIdList = []
        r, b = self.GraphqlQuery.configurationList(1, 6666, showprint=showprint)
        total = b['data']['configurationList']['total']
        for i in range(total):
            description = b['data']['configurationList']['configurations'][i]['description']
            configurationId = b['data']['configurationList']['configurations'][i]['configurationId']
            if description == descriptions:
                ConfigurationIdList.append(configurationId)
        if len(ConfigurationIdList) != 0:
            return ConfigurationIdList
        else:
            return warnings.warn(" The Name: %s not exist!") % names

    # 通过configurationList filters 模糊搜索获取configurationId
    def getConfigurationIdListByName(self, name, showprint=False):
        ConfigurationIdList = []
        r, b = self.GraphqlQuery.configurationListFilters(name, showprint=showprint)
        total = b['data']['configurationList']['total']
        for i in range(total):
            configurationId = b['data']['configurationList']['configurations'][i]['configurationId']
            ConfigurationIdList.append(configurationId)
        if len(ConfigurationIdList) != 0:
            return ConfigurationIdList
        else:
            return warnings.warn(" The Name: %s not exist!") % names









