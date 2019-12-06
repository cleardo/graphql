# coding=utf-8
from src.lib.queryGraphql import *
from src.lib.operateData import *
from src.testcases.configuration.GraphqlQueryLib import *
import unittest
import json


class CreateConfiguration(unittest.TestCase):

    # 创建包含name和description的configuration
    def test_create_configuration(self):
        description = "QATester"
        name = getTimeStr('QATester')
        r = queryCreateConfiguration(name=name, description=description)
        self.assertEqual(r["data"]["createConfiguration"]["description"], description)
        self.assertEqual(r["data"]["createConfiguration"]["name"], name)

    # 创建name为空的configuration
    def test_create_without_name_configuration(self):
        description = "QATester"
        r = queryCreateConfiguration('', description)
        self.assertIsNotNone(r["errors"])

    # 创建description为空的configuration
    def test_create_without_description_configuration(self):
        name = getTimeStr('QATester')
        r = queryCreateConfiguration(name, description='')
        self.assertEqual(r["data"]["createConfiguration"]["name"], name)


if __name__ == '__main__':
    unittest.main()
