#coding:utf-8
from django.shortcuts import render_to_response
from django.http import JsonResponse
from GodWork.views import login_valid
from Service.models import *
from django.http import HttpResponse

import paramiko
import json

@login_valid
def list(request):
    statue = "服务器展示页"
    table_list = Service.objects.all()
    return render_to_response("list.html", locals())


def content(request,ids):
    service_data = Service.objects.get(id = int(ids))
    user_list = ServerUser.objects.filter(serviceid=ids)
    hostname = service_data.host.strip()
    statue = "%s 详情页"%hostname.encode("utf-8")
    host_data = {
        "host_name":service_data.host,
        "ip":service_data.ip,
        "mac":service_data.mac,
        "cpu":service_data.cpu,
        "mem":service_data.mem,
        "disk":service_data.disk,
        "system":service_data.system,
        "model":service_data.model,
        "id":service_data.id
    }
    return render_to_response("server_content.html",locals())


def getCpu(request):
    if request.method == "GET" and request.GET:
        print(request.GET)
        serverId = request.GET.get("serverId")
        cpuData = CpuData.objects.filter(serviceid=int(serverId)).order_by("time")[0:12]
        cpu_list = []
        for num,cpu in enumerate(cpuData):#enumerate 是枚举 讲序列元素和其索引同时展现出来
            cpu_dict = {}
            cpu_dict["data"] = cpu.cpuload
            cpu_dict["year"] = cpu.time.strftime("%Y-%m-%dT%H:%M:%S")
            cpu_list.append(cpu_dict)
        return JsonResponse({"data":cpu_list})
    else:
        return JsonResponse({"err":"method must be get"})
# Create your views here.


def push_data(request):
    response = HttpResponse()
    data = request.POST.get('data', '')
    data = json.loads(data)
    print data
    hostinfo = [
        'host',
        'ip',
        'mac',
        'cpu',
        'mem',
        'disk',
        'system',
        'model'
    ]
    svc = Service()
    for k in hostinfo:
        setattr(svc, k, data[k])
    print svc.ip
    svc.save()
    response.write(json.dumps(u'成功'))
    return response