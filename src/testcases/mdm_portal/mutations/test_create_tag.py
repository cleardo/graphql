# coding=utf-8
from src.lib.queryGraphql import *
from src.lib.operateData import *
from src.testcases.mdm_portal.GraphqlQueryLib import *
import unittest
import json


class CreateTag(unittest.TestCase):

    # 测试createTag
    def test_create_tag(self):
        group = "QATester"
        tagname = getTimeStr("QATester-CreateTag")
        r = queryCreateTag(group=group, tagname=tagname)
        self.assertEqual(r['data']['createTag']['group'], group)
        self.assertEqual(r['data']['createTag']['value'], tagname)

    # 测试已存在的tagName
    def test_create_existed_tag(self):
        group = "QATester"
        tagname = getTimeStr("QATester-CreateTag")
        queryCreateTag(group=group, tagname=tagname, showprint=False)
        r = queryCreateTag(group=group, tagname=tagname)
        self.assertIsNotNone(r["errors"])

    # 测试tagName为空
    def test_create_empty_tag(self):
        group = "QATester"
        r = queryCreateTag(group=group, tagname="")
        self.assertIsNotNone(r["errors"])
