#!/usr/bin/python env
# -*- coding: UTF-8 -*-
# Description:                    
# Author:           黄小雪
# Date:             2017年03月06日
# Company:          东方银谷
from models import *
from django.http import HttpResponseRedirect


def permission(fun):
    # 权限检测
    def per(request, *args, **kwargs):
        try:
            username = request.session['username']
            user = User.objects.get(username=username)
            user_methods = Method.objects.get(users=user)
            print 'permission check-->', username, user, user_methods.name
            if user_methods.name == 'views':
                rset = fun(request)
                return rset
            else:
                url = "/403/"
                return HttpResponseRedirect(url)
        except Exception, e:  # 否则返回404页面
            url = "/403/"
            return HttpResponseRedirect(url)
    return per
