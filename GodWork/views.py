#! /usr/bin/env python
# -*-coding:utf-8-*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from User.models import User
from User.forms import *
import hashlib

def hashpassword(password):
    """
     本系统采用hash md5 加密的方式对登录密码进行加密
    """
    h = hashlib.md5()
    h.update(password.encode("utf-8"))
    return h.hexdigest()

def user_exit(username):
    try:
        User.objects.get(username=username)
        return True
    except:
        return False

def user_valid(username,passwd):
    try:
        user = User.objects.get(username=username)
        print 'user_valid-->', user.username, user.password
        if user.password == hashpassword(passwd):
            return True
        else:
            return False
    except:
        return False

def login_valid(func): #这是一个装饰器的函数，外层的函数是用来接收被装饰函数的的
    def inner(request,*args,**kwargs):
        try:
            username = request.session["username"] #尝试获取session
            return func(request)#index(request) 如果获取到执行被装饰函数
        except KeyError as e: #否则返回404页面
            if repr(e) == "KeyError('username',)":
                err = "当前用户未登录请登录"
            else:
                err = str(e)
            url = "/404/"+err
            #url = "/404?err="+err
            #/404/当前用户未登录，请登录
            return HttpResponseRedirect(url)
    return inner
#repr 是将类当中魔术方法__repr__的结果返回回来


@login_valid  #index = login_valid(index)  # login_valid(index) = inner  #index = inner
def index(request):
    statue = "首页"
    return render_to_response("index.html", locals())

@login_valid
def test(request):
    user = user_exit("while")
    user_1 = user_valid("whileb","whileb")
    # username = request.session["username"]
    req = dir(request)
    return render_to_response("test.html",locals())

# @login_valid
def register(request):
    statue = "用户注册"
    if request.method == "POST" and request.POST:
        registerFrom = RegisterForm(request.POST, request.FILES)
        print(registerFrom.is_valid())
        if registerFrom.is_valid():
            clear_data = registerFrom.cleaned_data
            u = User(
                username=clear_data.get('username'),
                password=hashpassword(clear_data.get("password")),
                email=clear_data.get("email"),
                phone=clear_data.get("phone"),
                photo=clear_data.get("photo")
            )
            u.save()

            #del request.COOKIES["username"]
            #del request.session["username"]
            return HttpResponseRedirect("/login")
    else:
        registerFrom = RegisterForm()
    return render_to_response("register.html",locals())

def logout(request):
    del request.COOKIES["username"]
    del request.session["username"]
    return render_to_response("logout.html")


def login(request):
    result = {}
    # User.objects.filter(username='huangxiaoxue').delete()
    users = User.objects.all()
    for obj in users:
        print obj.username, obj.password
    if request.method == "POST" and request.POST:
        username = request.POST.get("username","")
        password = request.POST.get("password","")
        print username,password,user_valid(username,password)
        if username and password and user_valid(username,password):
            response = HttpResponseRedirect("/index")
            response.set_cookie("username",username)
            request.session["username"] = username
            return response
        else:
            result["error"] = "用户或者密码错误"
            return render_to_response("login.html", locals())
    else:
        return render_to_response("login.html", locals(), context_instance=RequestContext(request))


def forbiden(request,error):
    return render_to_response("404.html",locals())




def base(request):
    return render_to_response("base.html",locals())

def list(request):
    statue = "列表展示页"
    table_list = [
        {
            "host": "bian-PC",
            "ip": "192.168.0.204",
            "system": "redhat7",
            "online": "是",
            "model": "联想System x3850"
        },{
            "host": "while-PC",
            "ip": "192.168.0.106",
            "system": "Windows7",
            "online": "否",
            "model": "HPE DL380 Gen9"
        },{
            "host": "readhat-PC",
            "ip": "192.168.0.9",
            "system": "redhat7",
            "online": "是",
            "model": "联想System x3850"
        },{
            "host": "centos-PC",
            "ip": "192.168.0.16",
            "system": "centos7",
            "online": "是",
            "model": "联想System x3850"
        },{
            "host": "ubuntu-PC",
            "ip": "192.168.0.48",
            "system": "ubuntu14.1",
            "online": "否",
            "model": "HPE DL380 Gen9"
        },{
            "host": "while-PC",
            "ip": "192.168.0.26",
            "system": "Windows7",
            "online": "是",
            "model": "HPE DL380 Gen9"
        },{
            "host": "for-PC",
            "ip": "192.168.0.14",
            "system": "Windows10",
            "online": "否",
            "model": "HPE DL380 Gen9"
        }
    ]
    return render_to_response("list.html", locals())







