# coding=utf-8

"""
断言库的使用示例
"""
import unittest
import datetime
import types
from hamcrest import *
from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.hasmethod import hasmethod

__author__ = 'Administrator'


class IsGivenDayOfWeek(BaseMatcher):
    def __init__(self, day):
        """
        初始化
        """
        self.day = day  # Monday is 0, Sunday is 6

    def _matches(self, item):
        """
        匹配方法，item是被断言的数据
        """
        if not hasmethod(item, 'weekday'):  # 判断是否有.weekday()的方法
            return False
        return item.weekday() == self.day

    def describe_to(self, description):
        """
        产生断言失败时的消息（即description内容）
        """
        day_as_string = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                         'Friday', 'Saturday', 'Sunday']
        description.append_text('calendar date falling on ') \
            .append_text(day_as_string[self.day])


class AssertTest(unittest.TestCase):
    foo = 1
    bar = 2
    name = 'Jon'

    def test_has_properties(self):
        """
        测试属性断言方法
        """
        # 类对象的多个属性存在，且其值相同
        assert_that(self, has_properties({'foo': equal_to(1), 'bar': equal_to(2)}))
        assert_that(self, has_properties({'foo': 1, 'bar': 2}))
        assert_that(self, has_properties(foo=equal_to(1), bar=equal_to(2)))
        assert_that(self, has_properties(foo=1, bar=2))
        assert_that(self, has_properties('foo', equal_to(1), 'bar', equal_to(2)))
        assert_that(self, has_properties('foo', 1, 'bar', 2))

        # 类对象的某个属性存在，且其值符合匹配
        assert_that(self, has_property('name'))
        assert_that(self, has_property('name', starts_with('J')))
        assert_that(self, has_property('name', 'Jon'))

    def test_equal_to(self):
        """
        测试两者值相等
        """
        count = 3
        assert_that(count, equal_to(3))

    def test_has_length(self):
        """
        测试对象的长度
        """
        name = 'Jay'
        assert_that(name, has_length(3))

    def test_has_string(self):
        """
        测试包含子串
        """
        name = 'Jeanne'
        assert_that(name, has_string(name))
        assert_that(name, has_string(starts_with('J')))
        assert_that(name, has_string(ends_with('e')))

    def test_instance_of(self):
        """
        测试实例类型
        """
        name = '1'
        assert_that(name, instance_of(str))
        # num与num2为同类型、值相同的实例
        num = 1
        assert_that(num, instance_of(int))
        num2 = 1
        assert_that(num2, same_instance(num))

    def test_types(self):
        """
        测试实例、类型的类型
        """
        # 实例类型
        assert_that(type([]), types.ListType)

        # 类型的类型
        assert_that(type(list), types.ListType)

    def test_none(self):
        """
        测试是否为none值
        """
        # 为None的值
        none_obj = None
        assert_that(none_obj, none())

        # 不为None的值
        not_none_obj = 1
        assert_that(not_none_obj, not_none())

    def test_close_to(self):
        """
        测试数值的估计
        """
        num = 2.85
        assert_that(num, close_to(3.0, 0.25))

    def test_greater_or_less_than(self):
        """
        测试数值之间的大小关系
        """
        num1 = 11
        num2 = 12
        num3 = 12

        assert_that(num2, greater_than(num1))
        assert_that(num3, greater_than_or_equal_to(num1))
        assert_that(num3, greater_than_or_equal_to(num2))
        assert_that(num1, less_than(num2))
        assert_that(num1, less_than_or_equal_to(num2))
        assert_that(num2, less_than_or_equal_to(num3))

    def test_contains_string(self):
        """
        测试字符串包含
        """
        name = 'Cinderella Cinder'

        assert_that(name, contains_string('rel'))  # 包含
        assert_that(name, ends_with('der'))  # 结尾
        assert_that(name, starts_with('Cin'))  # 开头
        assert_that(name, string_contains_in_order('rel', 'ind'))  # 顺序包含

    def test_match_string(self):
        """
        测试字符串相等
        """
        name = 'Cinderella Cinder'

        assert_that(name, equal_to_ignoring_case('CinDereLla ciNder'))  # 忽略大小写，内容相等
        assert_that(name, equal_to_ignoring_whitespace(' Cinderella     Cinder  '))  # 忽略空白符，单词相等
        assert_that(name, matches_regexp('Cinderella+'))  # 正则匹配

    def test_is_not(self):
        """
        测试否定方法
        """
        cheese = True
        smelly = False

        assert_that(cheese, is_not(equal_to(smelly)))
        assert_that(cheese, is_not(smelly))
        assert_that(cheese, not_(smelly))  # ‘not_’是‘is_not’的缩写

    def test_has_key(self):
        """
        测试字典键值
        """
        data = {
            'foo': 1,
            'bar': 2,
            'name': 'Jon'
        }

        assert_that(data, has_key('foo'))
        assert_that(data, has_key(equal_to('bar')))

        assert_that(data, has_value(2))
        assert_that(data, has_value(equal_to('Jon')))

    def on_a_saturday(self):
        return IsGivenDayOfWeek(5)

    def test_custom_method(self):
        """
        测试自定义断言方法
        """
        day = datetime.date(2008, 04, 26)
        assert_that(day, is_(self.on_a_saturday()))


if __name__ == "__main__":
    pass
