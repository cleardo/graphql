# coding=utf-8
from src.lib.queryGraphql import *
from src.lib.operateData import *
from src.testcases.mdm_portal.GraphqlQueryLib import *


# 批量创建tagid
class BatchData(object):

    def __init__(self):
        pass

    def bat_create_tag(self, times):
        group = "QATester"

        for i in range(times):
            tagname = getTimeStr("QATester-CreateTag", str(i))
            queryCreateTag(group=group, tagname=tagname)


if __name__ == '__main__':
    BatchData().bat_create_tag(50)
