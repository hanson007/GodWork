# -*- coding: UTF-8 -*-
from django.test import TestCase
# Create your tests here.
import urllib
import urllib2
import json


def post(url, data):
    req = urllib2.Request(url)
    data = urllib.urlencode(data)
    # enable cookie
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    response = opener.open(req, data)
    return response.read()


def main():
    posturl = "http://192.168.93.128:9000/service/push_data/"
    data = {'email': 'myemail', 'password': 'mypass', 'autologin': '1', 'submit': '登 录', 'type': ''}
    data = {'data': json.dumps(data)}
    data = post(posturl, data)
    res = json.loads(data)
    print res

if __name__ == '__main__':
    main()


