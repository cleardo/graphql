# coding=utf-8
from src.lib.queryGraphql import *
from src.testcases.configuration.GraphqlQueryLib import *
from src.testcases.mdm_portal.GraphqlQueryLib import *
import unittest
import json
import platform
import time
import random
import logging


def getRandomTagidList(tagGroup="QATester"):
    """
    获取指定tagGroup下的Tagid
    :param tagGroup:
    :return:            Tangid列表
    """
    r = queryTags(showprint=False)
    tagIdList = []
    for index in range(len(r["data"]['Tags'])):
        if r["data"]["Tags"][index]["group"] == tagGroup:
            for i in range(len(r["data"]["Tags"][index]["values"])):
                tagIdList.append(r["data"]["Tags"][index]["values"][i]["id"])
    if len(tagIdList) == 0:
        return logging.error("[数据获取错误] - [{tagGroup}下没有Tag]".format(tagGroup=tagGroup))
    return tagIdList


def getRandomConfigurationIdList(Size=5):
    """
    获取随机的configurationId
    :param Size:                configurationId数量 defualt=5
    :return:                    随机的configurationIdList
    """
    configurationIdList = []
    r = queryConfigurationList(pageNumber=0, pageSize=5, showprint=False)
    for index in range(Size):
        configurationIdList.append(r["data"]["configurationList"]["configurations"][index]["configurationId"])
    return configurationIdList


def getRandomPanelSNAndName(Size=5):
    """
    获取随机的面板SN和Name
    :param                  Size: 获取数量
    :return:                [{'SN': SN, 'name': name}, {'SN': SN, 'name': name}, ...]
    取值方式:
                            SN = PanelList[index]['SN']
                            name = PanelList[index]['name']
    """
    r = queryPanels(pageSize=Size, offset=0, showprint=False)
    PanelList = []
    for index in range(Size):
        SN = r["data"]["Panels"]["panels"][index]["serialNumber"]
        name = r["data"]["Panels"]["panels"][index]["name"]
        PanelList.append({'SN': SN, 'name': name})
    return PanelList


def getTimeStr(prefix='', arg=''):
    """
    :param arg: 其他参数
    :param prefix: 前缀
    :return: 前缀 + 当前时间
    """
    return prefix + time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time())) + arg


if __name__ == '__main__':
    print(getRandomTagidList())
