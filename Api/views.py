import re
import paramiko
from django.shortcuts import render
from django.http import JsonResponse
from Service.models import *
import datetime
import time
def savedata(request):
    result = {}
    if request.method == "POST" and request.POST:
        req_data = request.POST
        service = Service()
        service.host = req_data.get("hostName")
        service.ip = req_data.get("Ip")
        service.mac = req_data.get("macs")
        service.cpu = req_data.get("cpu")
        service.mem = req_data.get("Mem")
        service.model = req_data.get("Model")
        service.disk = req_data.get("Disk")
        service.system = req_data.get("system")
        service.save()
        result["statue"] = "success"
    else:
        result["statue"] = "error"
    return JsonResponse(result)


def parApi(command,user_id,ip,port=22):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    user = ServerUser.objects.get(id = user_id)
    ssh.connect(ip, port, user.serverUserName, user.serverUserPasswd)
    return ssh.exec_command(command)

def setcpu(request):
    command = request.GET.get("command")
    ipaddr = request.GET.get("ipaddr")
    userId = request.GET.get("userId")
    port = int(request.GET.get("port", 22))
    serverId = request.GET.get("serverId")

    stdin,stdout,stderr = parApi(command,userId,ipaddr,port)

    for num,line in enumerate(stdout.readlines()):
        line = line.strip()
        if num >= 2:
            cupIDLE = re.split(r"\s+",line)[-3]
            cpu_used = 100-int(cupIDLE)
            cpu = CpuData()
            cpu.serviceid = serverId
            cpu.cpuload = cpu_used
            cpu.time = datetime.datetime.now()
            cpu.save()
        else:
            pass
    return JsonResponse({"statue":"success"})

def doCommand(request):
    command = request.GET.get("command")
    ipaddr = request.GET.get("ipaddr")
    userId = request.GET.get("userId")
    port = int(request.GET.get("port", 22))
    serverId = request.GET.get("serverId")
    stdin, stdout, stderr = parApi(command, userId, ipaddr, port)

    data = stdout.read()
    print(data)
    # print(data)
    # result = ""
    # for line in stdout.readlines():
    #    result += "%s\n"%line
    # result.replace(" ","&nbsp;")
    return JsonResponse({"result":"success"})

def test(request):
    result = {"state":""}
    if request.method == "GET" and request.GET:
        result["state"] = "GET"
    else:
        result["state"] = "POST"
    return JsonResponse(result)


# def parApi(request):
#     if request.method == "GET" and request.GET:
#         command = request.GET.get("command")
#         ipaddr = request.GET.get("ipaddr")
#         serverId = request.GET.get("serverId")
#         serverId = int(request.GET.get("port",22))
#
#         ssh = paramiko.SSHClient()
#         ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         ssh.connect("192.168.1.18",22,"root","123")
#         stdin,stdout,stderr = ssh.exec_command(command)
#         return stdin,stdout,stderr
        # for i in range(12):
        #     line = stdout.readline().strip()
        #     line_list = re.split(r"\s+",line)
        #     print(line_list[-3])
    #
    # def parApi(command, user_id, ip, port=22):
    #     def outer(func):
    #         def inner(request):
    #             ssh = paramiko.SSHClient()
    #             ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #             user = ServerUser.objects.get(id=user_id)
    #             ssh.connect(ip, port, user.serverUserName, user.serverUserPasswd)
    #             stdin, stdout, stderr = ssh.exec_command(command)
    #             func(request, stdin, stdout, stderr)
    #
    #         return inner
    #
    #     return outer
# Create your views here.
