from datetime import datetime, date, time
from unittest.case import TestCase
from dirty_filters.basic import BaseFilter, IntegerFilter, FloatFilter, StringFilter, ToDateTimeFilter, ToDateFilter, \
    ToTimeFilter, DateTimeToStrFilter, DateToStrFilter, TimeToStrFilter, Strip, RemoveStr, ReplaceStr, RegexReplaceStr

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


class ToDateTimeFilterTest(TestCase):

    def setUp(self):
        self.filter = ToDateTimeFilter(parse_format="%Y-%m-%d %H:%M:%S")

    def test_filter_int(self):
        self.assertEqual(datetime(2014, 6, 9, 13, 40, 34),
                         self.filter(1402321234))

    def test_filter_str(self):
        self.assertEqual(datetime(year=2014, month=8, day=1, hour=12, minute=43, second=8),
                         self.filter("2014-08-01 12:43:08"))

    def test_filter_str_fail(self):
        self.assertIsNone(self.filter("a12"))

    def test_filter_float(self):
        self.assertEqual(datetime(2014, 6, 9, 13, 40, 34, 230000),
                         self.filter(1402321234.23))

    def test_filter_dict(self):
        self.assertIsNone(self.filter({}))

    def test_filter_list(self):
        self.assertIsNone(self.filter([]))

    def test_filter_datetime(self):
        self.assertEqual(datetime(2014, 6, 9, 13, 40, 34, 230000),
                         self.filter(datetime(2014, 6, 9, 13, 40, 34, 230000)))


class ToDateFilterTest(TestCase):

    def setUp(self):
        self.filter = ToDateFilter(parse_format="%Y-%m-%d")

    def test_filter_int(self):
        self.assertEqual(date(2014, 6, 9),
                         self.filter(1402321234))

    def test_filter_str(self):
        self.assertEqual(date(year=2014, month=8, day=1),
                         self.filter("2014-08-01"))

    def test_filter_str_fail(self):
        self.assertIsNone(self.filter("a12"))

    def test_filter_float(self):
        self.assertEqual(date(2014, 6, 9),
                         self.filter(1402321234.23))

    def test_filter_dict(self):
        self.assertIsNone(self.filter({}))

    def test_filter_list(self):
        self.assertIsNone(self.filter([]))

    def test_filter_datetime(self):
        self.assertEqual(date(2014, 6, 9),
                         self.filter(datetime(2014, 6, 9, 13, 40, 34, 230000)))

    def test_filter_date(self):
        self.assertEqual(date(2014, 6, 9),
                         self.filter(date(2014, 6, 9)))


class ToTimeFilterTest(TestCase):

    def setUp(self):
        self.filter = ToTimeFilter(parse_format="%H:%M:%S")

    def test_filter_int(self):
        self.assertEqual(time(13, 40, 34),
                         self.filter(1402321234))

    def test_filter_str(self):
        self.assertEqual(time(hour=12, minute=43, second=8),
                         self.filter("12:43:08"))

    def test_filter_str_fail(self):
        self.assertIsNone(self.filter("a12"))

    def test_filter_float(self):
        self.assertEqual(time(13, 40, 34, 230000),
                         self.filter(1402321234.23))

    def test_filter_dict(self):
        self.assertIsNone(self.filter({}))

    def test_filter_list(self):
        self.assertIsNone(self.filter([]))

    def test_filter_datetime(self):
        self.assertEqual(time(13, 40, 34, 230000),
                         self.filter(datetime(2014, 6, 9, 13, 40, 34, 230000)))

    def test_filter_date(self):
        self.assertIsNone(self.filter(date(2014, 6, 9)))

    def test_filter_time(self):
        self.assertEqual(time(13, 40, 34, 230000),
                         self.filter(time(13, 40, 34, 230000)))


class DateTimeToStrFilterTest(TestCase):

    def setUp(self):
        self.filter = DateTimeToStrFilter(parse_format="%Y-%m-%d %H:%M:%S%z")

    def test_filter_int(self):
        self.assertIsNone(self.filter(1402321234))

    def test_filter_datetime(self):
        self.assertEqual("2014-08-01 12:43:08",
                         self.filter(datetime(year=2014, month=8, day=1, hour=12, minute=43, second=8)))

    def test_filter_str_fail(self):
        self.assertIsNone(self.filter("a12"))

    def test_filter_float(self):
        self.assertIsNone(self.filter(1402321234.23))

    def test_filter_dict(self):
        self.assertIsNone(self.filter({}))

    def test_filter_list(self):
        self.assertIsNone(self.filter([]))

    def test_filter_date(self):
        self.assertEqual('2014-06-09 00:00:00', self.filter(date(2014, 6, 9)))

    def test_filter_time(self):
        self.assertEqual('1900-01-01 13:40:34', self.filter(time(13, 40, 34, 230000)))


class DateToStrFilterTest(TestCase):

    def setUp(self):
        self.filter = DateToStrFilter(parse_format="%Y-%m-%d")

    def test_filter_int(self):
        self.assertIsNone(self.filter(1402321234))

    def test_filter_datetime(self):
        self.assertEqual("2014-08-01",
                         self.filter(datetime(year=2014, month=8, day=1, hour=12, minute=43, second=8)))

    def test_filter_str_fail(self):
        self.assertIsNone(self.filter("a12"))

    def test_filter_float(self):
        self.assertIsNone(self.filter(1402321234.23))

    def test_filter_dict(self):
        self.assertIsNone(self.filter({}))

    def test_filter_list(self):
        self.assertIsNone(self.filter([]))

    def test_filter_date(self):
        self.assertEqual('2014-06-09', self.filter(date(2014, 6, 9)))

    def test_filter_time(self):
        self.assertEqual('1900-01-01', self.filter(time(13, 40, 34, 230000)))


class TimeToStrFilterTest(TestCase):

    def setUp(self):
        self.filter = TimeToStrFilter(parse_format="%H:%M:%S%z")

    def test_filter_int(self):
        self.assertIsNone(self.filter(1402321234))

    def test_filter_datetime(self):
        self.assertEqual("12:43:08",
                         self.filter(datetime(year=2014, month=8, day=1, hour=12, minute=43, second=8)))

    def test_filter_str_fail(self):
        self.assertIsNone(self.filter("a12"))

    def test_filter_float(self):
        self.assertIsNone(self.filter(1402321234.23))

    def test_filter_dict(self):
        self.assertIsNone(self.filter({}))

    def test_filter_list(self):
        self.assertIsNone(self.filter([]))

    def test_filter_date(self):
        self.assertEqual('00:00:00', self.filter(date(2014, 6, 9)))

    def test_filter_time(self):
        self.assertEqual('13:40:34', self.filter(time(13, 40, 34, 230000)))


class StripTest(TestCase):

    def setUp(self):
        self.filter = Strip()

    def test_filter_str_1(self):
        self.assertEqual("a12", self.filter(" a12"))

    def test_filter_str_2(self):
        self.assertEqual("a12", self.filter("    a12 "))

    def test_filter_str_3(self):
        self.assertEqual("a12", self.filter("a12     "))

    def test_filter_int(self):
        self.assertIsNone(self.filter(1402321234))

    def test_filter_float(self):
        self.assertIsNone(self.filter(1402321234.23))

    def test_filter_dict(self):
        self.assertIsNone(self.filter({}))

    def test_filter_list(self):
        self.assertIsNone(self.filter([]))

    def test_filter_date(self):
        self.assertIsNone(self.filter(date(2014, 6, 9)))

    def test_filter_time(self):
        self.assertIsNone(self.filter(time(13, 40, 34, 230000)))

    def test_filter_datetime(self):
        self.assertIsNone(self.filter(datetime(year=2014, month=8, day=1, hour=12, minute=43, second=8)))


class StripCharsTest(TestCase):

    def setUp(self):
        self.filter = Strip(chars="qwa")

    def test_filter_str_1(self):
        self.assertEqual("12", self.filter("qwa12"))

    def test_filter_str_2(self):
        self.assertEqual("12", self.filter("qa12aq"))

    def test_filter_str_3(self):
        self.assertEqual("12", self.filter("12qwqw"))

    def test_filter_int(self):
        self.assertIsNone(self.filter(1402321234))

    def test_filter_float(self):
        self.assertIsNone(self.filter(1402321234.23))

    def test_filter_dict(self):
        self.assertIsNone(self.filter({}))

    def test_filter_list(self):
        self.assertIsNone(self.filter([]))

    def test_filter_date(self):
        self.assertIsNone(self.filter(date(2014, 6, 9)))

    def test_filter_time(self):
        self.assertIsNone(self.filter(time(13, 40, 34, 230000)))

    def test_filter_datetime(self):
        self.assertIsNone(self.filter(datetime(year=2014, month=8, day=1, hour=12, minute=43, second=8)))


class RemoveStrTest(TestCase):

    def setUp(self):
        self.filter = RemoveStr(strings=['asas', 'bbb', 'xxxx'])

    def test_filter_str_1(self):
        self.assertEqual(" wew fdsdse  eerwed", self.filter("asas wewbbb fdsdse bbb eerwed"))

    def test_filter_str_2(self):
        self.assertEqual("", self.filter("asasbbbxxxxasasxxxx"))

    def test_filter_str_3(self):
        self.assertEqual("wew fdsdse eerwed", self.filter("wew fdsdse eerwed"))

    def test_filter_int(self):
        self.assertIsNone(self.filter(1402321234))

    def test_filter_float(self):
        self.assertIsNone(self.filter(1402321234.23))

    def test_filter_dict(self):
        self.assertIsNone(self.filter({}))

    def test_filter_list(self):
        self.assertIsNone(self.filter([]))

    def test_filter_date(self):
        self.assertIsNone(self.filter(date(2014, 6, 9)))

    def test_filter_time(self):
        self.assertIsNone(self.filter(time(13, 40, 34, 230000)))

    def test_filter_datetime(self):
        self.assertIsNone(self.filter(datetime(year=2014, month=8, day=1, hour=12, minute=43, second=8)))


class RemoveStrLimitedTest(TestCase):

    def setUp(self):
        self.filter = RemoveStr(strings=['asas', 'bbb', 'xxxx'], count=1)

    def test_filter_str_1(self):
        self.assertEqual(" wew fdsdse bbb eerwed", self.filter("asas wewbbb fdsdse bbb eerwed"))

    def test_filter_str_2(self):
        self.assertEqual("asasxxxx", self.filter("asasbbbxxxxasasxxxx"))

    def test_filter_str_3(self):
        self.assertEqual("wew fdsdse eerwed", self.filter("wew fdsdse eerwed"))

    def test_filter_int(self):
        self.assertIsNone(self.filter(1402321234))

    def test_filter_float(self):
        self.assertIsNone(self.filter(1402321234.23))

    def test_filter_dict(self):
        self.assertIsNone(self.filter({}))

    def test_filter_list(self):
        self.assertIsNone(self.filter([]))

    def test_filter_date(self):
        self.assertIsNone(self.filter(date(2014, 6, 9)))

    def test_filter_time(self):
        self.assertIsNone(self.filter(time(13, 40, 34, 230000)))

    def test_filter_datetime(self):
        self.assertIsNone(self.filter(datetime(year=2014, month=8, day=1, hour=12, minute=43, second=8)))


class ReplaceStrTest(TestCase):

    def setUp(self):
        self.filter = ReplaceStr(str_replace={'asas': 'ddd', 'bbb': 'zzz', 'xxxx': '999'})

    def test_filter_str_1(self):
        self.assertEqual("ddd wewzzz fdsdse zzz eerwed", self.filter("asas wewbbb fdsdse bbb eerwed"))

    def test_filter_str_2(self):
        self.assertEqual("dddzzz999ddd999", self.filter("asasbbbxxxxasasxxxx"))

    def test_filter_str_3(self):
        self.assertEqual("wew fdsdse eerwed", self.filter("wew fdsdse eerwed"))

    def test_filter_int(self):
        self.assertIsNone(self.filter(1402321234))

    def test_filter_float(self):
        self.assertIsNone(self.filter(1402321234.23))

    def test_filter_dict(self):
        self.assertIsNone(self.filter({}))

    def test_filter_list(self):
        self.assertIsNone(self.filter([]))

    def test_filter_date(self):
        self.assertIsNone(self.filter(date(2014, 6, 9)))

    def test_filter_time(self):
        self.assertIsNone(self.filter(time(13, 40, 34, 230000)))

    def test_filter_datetime(self):
        self.assertIsNone(self.filter(datetime(year=2014, month=8, day=1, hour=12, minute=43, second=8)))


class ReplaceStrLimitedTest(TestCase):

    def setUp(self):
        self.filter = ReplaceStr(str_replace={'asas': 'ddd', 'bbb': 'zzz', 'xxxx': '999'}, count=1)

    def test_filter_str_1(self):
        self.assertEqual("ddd wewzzz fdsdse bbb eerwed", self.filter("asas wewbbb fdsdse bbb eerwed"))

    def test_filter_str_2(self):
        self.assertEqual("dddzzz999asasxxxx", self.filter("asasbbbxxxxasasxxxx"))

    def test_filter_str_3(self):
        self.assertEqual("wew fdsdse eerwed", self.filter("wew fdsdse eerwed"))

    def test_filter_int(self):
        self.assertIsNone(self.filter(1402321234))

    def test_filter_float(self):
        self.assertIsNone(self.filter(1402321234.23))

    def test_filter_dict(self):
        self.assertIsNone(self.filter({}))

    def test_filter_list(self):
        self.assertIsNone(self.filter([]))

    def test_filter_date(self):
        self.assertIsNone(self.filter(date(2014, 6, 9)))

    def test_filter_time(self):
        self.assertIsNone(self.filter(time(13, 40, 34, 230000)))

    def test_filter_datetime(self):
        self.assertIsNone(self.filter(datetime(year=2014, month=8, day=1, hour=12, minute=43, second=8)))


class RegexReplaceStrTest(TestCase):

    def setUp(self):
        self.filter = RegexReplaceStr(str_replace={'.s.s': 'ddd', 'b(.)b': r'zzz\1', 'e(.+)d': r'999\1'})

    def test_filter_str_1(self):
        self.assertEqual("ddd w999wzzzb fddde zzzb eerwe", self.filter("asas wewbbb fdsdse bbb eerwed"))

    def test_filter_str_2(self):
        self.assertEqual("dddzzzbxxxxdddxxxx", self.filter("asasbbbxxxxasasxxxx"))

    def test_filter_str_3(self):
        self.assertEqual("w999w fddde eerwe", self.filter("wew fdsdse eerwed"))

    def test_filter_int(self):
        self.assertIsNone(self.filter(1402321234))

    def test_filter_float(self):
        self.assertIsNone(self.filter(1402321234.23))

    def test_filter_dict(self):
        self.assertIsNone(self.filter({}))

    def test_filter_list(self):
        self.assertIsNone(self.filter([]))

    def test_filter_date(self):
        self.assertIsNone(self.filter(date(2014, 6, 9)))

    def test_filter_time(self):
        self.assertIsNone(self.filter(time(13, 40, 34, 230000)))

    def test_filter_datetime(self):
        self.assertIsNone(self.filter(datetime(year=2014, month=8, day=1, hour=12, minute=43, second=8)))
