# -*- encoding=utf8 -*-
__author__ = "lan"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir="G:/PCR", devices=[
            "Android://127.0.0.1:5037/emulator-5554?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=ADBTOUCH",
    ])


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath="G:/PCR")



#  进入登录页
touch(Template(r"tpl1591432088255.png", record_pos=(-0.334, -0.094), resolution=(1600, 900)))


#进入首页
touch(Template(r"tpl1591432134084.png", record_pos=(-0.34, 0.247), resolution=(1600, 900)))

#关闭公告
touch(Template(r"tpl1591432196319.png", record_pos=(0.001, 0.215), resolution=(1600, 900)))

sleep(2.0)

#进入冒险、收菜
touch(Template(r"tpl1591432342475.png", record_pos=(0.001, 0.257), resolution=(1600, 900)))

#进入JJC
touch(Template(r"tpl1591432945059.png", record_pos=(0.108, 0.144), resolution=(1600, 900)))

touch(Template(r"tpl1591433014849.png", record_pos=(-0.193, 0.075), resolution=(1600, 900)))
touch(Template(r"tpl1591433661947.png", record_pos=(-0.001, 0.102), resolution=(1600, 900)))


#返回冒险、进入PJJC

sleep(1.0)
touch(Template(r"tpl1591434670952.png", record_pos=(-0.407, 0.255), resolution=(1600, 900)))

sleep(3.0)
touch(Template(r"tpl1591432342475.png", record_pos=(0.001, 0.257), resolution=(1600, 900)))


touch(Template(r"tpl1591433155402.png", record_pos=(0.358, 0.14), resolution=(1600, 900)))

touch(Template(r"tpl1591433014849.png", record_pos=(-0.193, 0.075), resolution=(1600, 900)))
touch(Template(r"tpl1591433661947.png", record_pos=(-0.001, 0.102), resolution=(1600, 900)))

#工会之家收集物品
sleep(3.0)
touch(Template(r"tpl1591450693894.png", record_pos=(0.149, 0.259), resolution=(1600, 900)))

touch(Template(r"tpl1591450723419.png", record_pos=(0.437, 0.16), resolution=(1600, 900)))
touch(Template(r"tpl1591450741225.png", record_pos=(-0.003, 0.216), resolution=(1600, 900)))




