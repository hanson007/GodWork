#!/usr/bin/python env
# -*- coding: UTF-8 -*-
# Description:                    
# Author:           黄小雪
# Date:             2017年01月25日
# Company:          东方银谷

import urllib
import urllib2
import json
import paramiko
import re




# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(host1['ip'], 22, host1['username'], host1['password'])
# stdin, stdout, stderr = ssh.exec_command("ls")
# for i in stdout.readlines():
#     print i
# ssh.close()


class Ssh(object):
    # paramiko 连接

    def __init__(self, host):
        self.ip = host['ip']
        self.port = host['port']
        self.username = host['username']
        self.password = host['password']

        self._ssh = self._connect()

    def _connect(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, self.port, self.username, self.password)
        return ssh

    def command(self, cmd):
        # 执行命令
        stdin, stdout, stderr = self._ssh.exec_command(cmd)
        return stdin, stdout, stderr


def get_hostname(ssh):
    stdin, stdout, stderr = ssh.command("hostname")
    hostname = stdout.readlines()[0].strip()
    return hostname


def get_mac(ssh):
    stdin, stdout, stderr = ssh.command("ifconfig")
    mac = ''
    for line in stdout.readlines():
        mac = re_mac(line)
        if mac:
            break
    return mac


def re_mac(line):
    matchObj = re.search(r"((?=.*eth0)(?=.*HWaddr).*)", line)
    if matchObj:
        macobj = re.search(r"(([0-9a-fA-F]{2,2}:){5,5}[0-9a-fA-F]{2,2}\s*$)", line)
        mac = macobj.group()
    else:
        mac = ""

    return mac


def get_cpu(ssh):
    stdin, stdout, stderr = ssh.command("cat /proc/cpuinfo")
    cpu = ''
    for line in stdout.readlines():
        if 'model name' in line:
            cpu = line.split(':')[1]
    return cpu


def get_mem(ssh):
    stdin, stdout, stderr = ssh.command("cat /proc/meminfo")
    mem = ''
    for line in stdout.readlines():
        if 'MemTotal' in line:
            memobj = re.search(r"(\d+)", line)
            mem = memobj.group()
    return mem


def get_disk(ssh):
    stdin, stdout, stderr = ssh.command("df -TH")
    disk = ''
    for line in stdout.readlines():
        cont = line.split()[2]
        diskobj = re.search(r"(\d+G)", cont)
        if diskobj:
            disk = diskobj.group()
    return disk


def get_system(ssh):
    stdin, stdout, stderr = ssh.command("uname -r")
    system = stdout.readlines()[0].strip()
    return system


def get_model(ssh):
    stdin, stdout, stderr = ssh.command("dmidecode | grep 'Product'")
    model = stdout.readlines()[0].split(':')[1].strip()
    return model


def post(url, data):
    req = urllib2.Request(url)
    data = urllib.urlencode(data)
    # enable cookie
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    response = opener.open(req, data)
    return response.read()

if __name__ == '__main__':
    host1 = {
        'ip': '192.168.93.137',
        'port': 22,
        'username': 'root',
        'password': '123.com',
        'session_timeout': 60,
    }

    ssh = Ssh(host1)
    hostname = get_hostname(ssh)
    mac = get_mac(ssh)
    cpu = get_cpu(ssh)
    mem = get_mem(ssh)
    disk = get_disk(ssh)
    system = get_system(ssh)
    model = get_model(ssh)

    data = {
        'host': hostname,
        'mac': mac,
        'cpu': cpu,
        'mem': mem,
        'disk': disk,
        'system': system,
        'model': model,
        'ip': host1['ip']
    }
    print data
    posturl = "http://192.168.93.128:9000/service/push_data/"
    data = {'data': json.dumps(data)}
    data = post(posturl, data)
    res = json.loads(data)
    print res
