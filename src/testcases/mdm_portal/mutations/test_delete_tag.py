# coding=utf-8
from src.lib.queryGraphql import *
from src.lib.operateData import *
from src.testcases.mdm_portal.GraphqlQueryLib import *
import unittest
import json


class DeleteTag(unittest.TestCase):

    def test_delete_tag(self):
        tagId = getRandomTagidList()[0]
        queryDeleteTag(tagId)
