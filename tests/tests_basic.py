from unittest.case import TestCase
from dirty_filters.basic import BaseFilter, IntegerFilter, FloatFilter, StringFilter

__author__ = 'alfred'


class BaseFilterTest(TestCase):

    def setUp(self):
        self.filter = BaseFilter()

    def test_filter_int(self):
        self.assertEqual(12, self.filter(12))

    def test_filter_str(self):
        self.assertEqual("a12", self.filter("a12"))

    def test_filter_float(self):
        self.assertEqual(12.23, self.filter(12.23))

    def test_filter_dict(self):
        self.assertEqual({}, self.filter({}))

    def test_filter_list(self):
        self.assertEqual([], self.filter([]))


class IntegerFilterTest(TestCase):

    def setUp(self):
        self.filter = IntegerFilter()

    def test_filter_int(self):
        self.assertEqual(12, self.filter(12))

    def test_filter_str(self):
        self.assertEqual(12, self.filter("12"))

    def test_filter_str_fail(self):
        self.assertIsNone(self.filter("a12"))

    def test_filter_float(self):
        self.assertEqual(12, self.filter(12.23))

    def test_filter_float_str(self):
        self.assertEqual(12, self.filter("12.23"))

    def test_filter_dict(self):
        self.assertIsNone(self.filter({}))

    def test_filter_list(self):
        self.assertIsNone(self.filter([]))


class FloatFilterTest(TestCase):

    def setUp(self):
        self.filter = FloatFilter()

    def test_filter_int(self):
        self.assertEqual(12.0, self.filter(12))

    def test_filter_str(self):
        self.assertEqual(12.0, self.filter("12"))

    def test_filter_str_fail(self):
        self.assertIsNone(self.filter("a12"))

    def test_filter_float(self):
        self.assertEqual(12.23, self.filter(12.23))

    def test_filter_float_str(self):
        self.assertEqual(12.23, self.filter("12.23"))

    def test_filter_dict(self):
        self.assertIsNone(self.filter({}))

    def test_filter_list(self):
        self.assertIsNone(self.filter([]))


class StringFilterTest(TestCase):

    def setUp(self):
        self.filter = StringFilter()

    def test_filter_int(self):
        self.assertEqual("12", self.filter(12))

    def test_filter_str_fail(self):
        self.assertEqual("a12", self.filter("a12"))

    def test_filter_float(self):
        self.assertEqual("12.23", self.filter(12.23))

    def test_filter_dict(self):
        self.assertEqual("{}", self.filter({}))

    def test_filter_list(self):
        self.assertEqual("[]", self.filter([]))
