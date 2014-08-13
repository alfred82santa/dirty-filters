from datetime import date, datetime, time
from functools import wraps
import re

__author__ = 'alfred'


def fallback_none(func):

    @wraps(func)
    def inner_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, TypeError, AttributeError):
            return None

    return inner_func


class BaseFilter:

    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, value, *args, **kwargs):
        return value


class IntegerFilter(BaseFilter):

    @fallback_none
    def __call__(self, value, *args, **kwargs):
        return int(float(value))


class FloatFilter(BaseFilter):

    @fallback_none
    def __call__(self, value, *args, **kwargs):
        return float(value)


class StringFilter(BaseFilter):

    @fallback_none
    def __call__(self, value, *args, **kwargs):
        return str(value)


class BaseDateTimeFilter(BaseFilter):

    def __init__(self, parse_format=None, *args, **kwargs):
        super(BaseDateTimeFilter, self).__init__(*args, **kwargs)
        self._parse_format = parse_format


class ToDateTimeFilter(BaseDateTimeFilter):

    @fallback_none
    def __call__(self, value, *args, **kwargs):
        if isinstance(value, datetime):
            return value
        elif isinstance(value, str):
            return datetime.strptime(value, self._parse_format)
        else:
            return datetime(value)


class ToDateFilter(ToDateTimeFilter):

    @fallback_none
    def __call__(self, value, *args, **kwargs):
        if isinstance(value, date):
            return value

        return super(ToDateFilter, self).__call__(value, *args, **kwargs).date


class ToTimeFilter(ToDateTimeFilter):

    @fallback_none
    def __call__(self, value, *args, **kwargs):
        if isinstance(value, time):
            return value

        return super(ToTimeFilter, self).__call__(value, *args, **kwargs).time


class DateTimeToStrFilter(BaseDateTimeFilter):

    @fallback_none
    def __call__(self, value, *args, **kwargs):
        return value.strftime(value, self._parse_format)


class DateToStrFilter(DateTimeToStrFilter):
    pass


class TimeToStrFilter(DateTimeToStrFilter):
    pass


class Strip(BaseFilter):

    def __init__(self, chars=None, *args, **kwargs):
        super(Strip, self).__init__(*args, **kwargs)
        self._chars = chars

    @fallback_none
    def __call__(self, value, *args, **kwargs):
        return value.strip(self._chars)


class RemoveStr(BaseFilter):

    def __init__(self, strings=None, count=None, *args, **kwargs):
        super(RemoveStr, self).__init__(*args, **kwargs)
        self._strings = strings if strings is not None else []
        self._count = count

    @fallback_none
    def __call__(self, value, *args, **kwargs):
        for string in self._strings:
            value = value.replace(string, '', self._count)

        return value


class ReplaceStr(BaseFilter):
    def __init__(self, str_replace=None, count=None, *args, **kwargs):
        super(RemoveStr, self).__init__(*args, **kwargs)
        self._str_replace = str_replace if str_replace is not None else {}
        self._count = count

    @fallback_none
    def __call__(self, value, *args, **kwargs):
        for string, replace_val in self._str_replace.items():
            value = value.replace(string, replace_val, self._count)

        return value


class RegexReplaceStr(ReplaceStr):

    @fallback_none
    def __call__(self, value, *args, **kwargs):
        for regx, replace_val in self._str_replace.items():
            value = re.sub(regx, replace_val, count=self._count)

        return value





