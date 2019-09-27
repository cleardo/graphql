# coding=utf-8
# from nd.rest import unittest
from prome_lib.graphql_query import GraphqlQuery
from prome_lib.operate_data import DataOperate
from config import prome_config as con
import unittest
import time


class DeletePanelTags(unittest.TestCase):

    def setUp(self):
        self.GQ = GraphqlQuery()
        self.DO = DataOperate()

    def test_delete_panel_tags(self):

        times = 1
        group = "QAtestr-DeletePanelTag"
        tagname = self.DO.getTimeStr("QATester_will_delete_Tags_of_Panel")
        self.GQ.createTag(group, tagname, showprint=False)
        panelList = self.DO.getRandomPanelSnAndNameList(times)
        time.sleep(3)
        tagList = self.DO.getTagListByGroupName(group)

        def delete_tag(i):
            SN = panelList[i]['serialNumber']
            tagid = tagList[i]['tagid']
            print "############## Testing %d Delete Panel Tag ##############" % (i + 1)
            print '\nfrom Panel: %s\ndelete tagid: %s' % (SN, tagid)
            print 'tag id belong to Group: ', group
            response, body = self.GQ.deletePanelTags(SN, tagid)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(body['data']['deletePanelTags'], "success")

        for i in range(times):
            delete_tag(i)
