# coding=utf-8
# from nd.rest import unittest
from prome_lib.graphql_query import GraphqlQuery
from prome_lib.operate_data import DataOperate
import unittest
from config import prome_config as con


class UpdatePanelTags(unittest.TestCase):

    def setUp(self):
        self.GQ = GraphqlQuery()
        self.DO = DataOperate()

    def test_update_panel_tags(self):
        times = 2

        def update_panel_tags(i):
            group = "QAtestr-PanelTagTest"
            tagname = self.DO.getTimeStr("QATester_addPanelTags")
            r, b = self.GQ.createTag(group, tagname, showprint=False)
            # 获取 group下的 QAtest Test Update Panel Tags id
            tagid = b['data']['createTag']['id']
            # 随机选取2个 Pnael 加入Tag
            PanelList = self.DO.getRandomPanelSnAndNameList(2)
            serialNumber = PanelList[i]['serialNumber']
            name = PanelList[i]['name']
            print "####################Testing %d Update Panel Tags####################" % (i + 1)
            print '\nAdd Panel SN  is :', serialNumber
            print '\nAdd Panel Name is :', name
            print '\nAdd Tags  is :', tagid
            r, b = self.GQ.updatepanelTags(serialNumber, tagid)
            self.assertEqual(r.status_code, 200)
            self.assertEquals(b['data']['updatePanelTags'], 'success')

        for i in range(times):
            update_panel_tags(i)
