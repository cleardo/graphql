# coding=utf-8

"""
unittest的注释方法演示
"""

import unittest
from unittest import SkipTest

__author__ = 'Administrator'


@SkipTest
class SkipCaseTest(unittest.TestCase):
    def test_skip_case(self):
        print "test_skip_case"


class AnnotationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        setUpClass 整个类的setup方法
        """
        print "- setUpClass"

    @classmethod
    def tearDownClass(cls):
        """
        tearDownClass 整个类的teardown方法
        """
        print "- tearDownClass"

    def setUp(self):
        """
        setup 每个case的setup方法
        """
        print '-- setup 方法执行于本类中每条用例之前'

    def tearDown(self):
        """
        teardown 每个case的teardown方法
        """
        print '-- teardown 方法执行于本类中每条用例之后'

    def test_case(self):
        """
        test_case 没有被屏蔽的测试方法
        """
        assert (3 * 4) == 12
        print "--- test_case"

    @SkipTest  # 屏蔽单个case
    def test_ignore(self):
        """
        test_ignore 类内部被屏蔽的测试方法
        """
        print "--- test_ignore"


if __name__ == "__main__":
    pass
