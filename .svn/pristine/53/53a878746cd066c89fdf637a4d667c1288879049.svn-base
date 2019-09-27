# coding=utf-8
# from nd.rest import unittest
from prome_lib.graphql_query import GraphqlQuery
from prome_lib.operate_data import DataOperate
import unittest
import random
from config import prome_config as con


class AddPanelTags(unittest.TestCase):

    def setUp(self):
        self.GQ = GraphqlQuery()
        self.DO = DataOperate()

    def test_add_panel_tags(self):

        times = 2
        PanelList = self.DO.getRandomPanelSnAndNameList(times)

        def add_panel_tags(i):
            group = "QAtestr-DeletePanelTag"
            tagname = self.DO.getTimeStr("QATester_will_delete_Tags_of_Panel")
            r, b = self.GQ.createTag(group, tagname, showprint=False)
            # 获取 group下的 QAtest Test Update Panel Tags id
            tagid = b['data']['createTag']['id']
            # 随机选取 Pnael 加入Tag
            serialNumber = PanelList[i]['serialNumber']
            name = PanelList[i]['name']
            self.GQ.addpanelTags(serialNumber, tagid, showprint=False)
            # 再将其删除
            print "####################Testing %d Delete Panel Tags####################" % (i + 1)
            print '\nDelete Tags Panel SN  is :', serialNumber
            print '\nDelete Tags Panel Name is :', name
            print '\nDelete Tags  is :', tagid
            r, b = self.GQ.deletePanelTags(serialNumber, tagid)
            self.assertEqual(r.status_code, 200)
            self.assertEquals(b['data']['deletePanelTags'], 'success')

        for i in range(times):
            add_panel_tags(i)
