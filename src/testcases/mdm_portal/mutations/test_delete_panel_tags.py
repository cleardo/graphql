# coding=utf-8
from src.lib.queryGraphql import *
from src.lib.operateData import *
from src.testcases.mdm_portal.GraphqlQueryLib import *
import unittest
import json


class DeletePanelTags(unittest.TestCase):

    # 测试 delete panel tag 接口，删除group=QATester下的一个tagId
    def test_delete_panel_tags(self):
        tagId = getRandomTagidList()[0]
        r = queryDeleteTag(tagId)
        self.assertEqual(r["data"]["deleteTag"]["group"], "QATester")
        self.assertEqual(r["data"]["deleteTag"]["id"], tagId)

    # 测试 删除的tagid 为不存在的值
    def test_delete_error_panel_tags(self):
        tagId = getTimeStr('test_tag_id')
        r = queryDeleteTag(tagId)
        self.assertIsNotNone(r["errors"])
