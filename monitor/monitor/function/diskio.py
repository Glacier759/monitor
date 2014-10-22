#!/usr/bin/env python
# coding=utf-8

#  ------------------------------------
#  Create date : 2014-10-20 22:08
#  Author : Wangzhaojiang
#  Email : wangzhaojiang2013@gmail.com
#  ------------------------------------
import re


def getdata_diskio():
    f = open('/proc/vmstat', 'r')
    content = f.readlines()

    option = ['^pgpgin', '^pgpgout']

    data = {}

    for each_line in content:
        for search in option:
            result = re.findall(search, each_line)
            if len(result) != 0:
                result = each_line.split()

                data[result[0]] = int(result[1])
                
                break

    return data


def diskio():
    data_old = getdata_diskio()
    old_time = time.strftime('%Y-%m-%d-%H:%M',time.localtime(time.time()))
    print old_time
    new_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    data_new = getdata_diskio()


diskio()
