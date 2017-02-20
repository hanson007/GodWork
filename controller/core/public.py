# -*- coding: UTF-8 -*-
import datetime


class Currency(object):
    #  通用帮助
    def __init__(self,request):
        self.request = request

    def rq_get(self,key):
        return self.request.GET.get(key, '').strip()


class datetime_help(object):
    # 日期时间帮助
    def __init__(self):
        pass

    def strptime(self, value, format):
        datetime = datetime.datetime.strptime(value, format)