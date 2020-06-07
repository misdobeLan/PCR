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

##############################进入冒险、收菜JJC、PJJC
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

#首页收集礼物箱
sleep(3.0)


touch(Template(r"tpl1591520373056.png", record_pos=(-0.398, 0.255), resolution=(1280, 720)))

touch(Template(r"tpl1591520393705.png", record_pos=(0.445, 0.177), resolution=(1280, 720)))

touch(Template(r"tpl1591524047695.png", record_pos=(0.378, 0.174), resolution=(1280, 720)))

touch(Template(r"tpl1591524127244.png", record_pos=(0.195, 0.214), resolution=(1280, 720)))
touch(Template(r"tpl1591524140258.png", record_pos=(-0.111, 0.213), resolution=(1280, 720)))


##############################地下城、战斗时间90秒
'''
sleep(3.0)

touch(Template(r"tpl1591432342475.png", record_pos=(0.001, 0.257), resolution=(1600, 900)))

touch(Template(r"tpl1591524258990.png", record_pos=(0.409, -0.141), resolution=(1280, 720)))

touch(Template(r"tpl1591524297122.png", record_pos=(0.289, 0.133), resolution=(1280, 720)))
touch(Template(r"tpl1591524325852.png", record_pos=(0.374, 0.191), resolution=(1280, 720)))
touch(Template(r"tpl1591524433132.png", record_pos=(0.398, -0.188), resolution=(1280, 720)))
touch(Template(r"tpl1591524444046.png", record_pos=(0.321, -0.1), resolution=(1280, 720)))

touch(Template(r"tpl1591524467809.png", record_pos=(0.367, 0.188), resolution=(1280, 720)))

sleep(90.0)
touch(Template(r"tpl1591524536226.png", record_pos=(0.365, 0.241), resolution=(1280, 720)))
touch(Template(r"tpl1591524562464.png", record_pos=(0.002, 0.214), resolution=(1280, 720)))
sleep(3.0)


touch(Template(r"tpl1591524629596.png", record_pos=(-0.216, 0.027), resolution=(1280, 720)))
touch(Template(r"tpl1591524325852.png", record_pos=(0.374, 0.191), resolution=(1280, 720)))
touch(Template(r"tpl1591524467809.png", record_pos=(0.367, 0.188), resolution=(1280, 720)))
sleep(90.0)
touch(Template(r"tpl1591524536226.png", record_pos=(0.365, 0.241), resolution=(1280, 720)))
touch(Template(r"tpl1591524562464.png", record_pos=(0.002, 0.214), resolution=(1280, 720)))
sleep(3.0)

touch(Template(r"tpl1591525454566.png", record_pos=(0.131, -0.012), resolution=(1280, 720)))
touch(Template(r"tpl1591524325852.png", record_pos=(0.374, 0.191), resolution=(1280, 720)))
touch(Template(r"tpl1591524467809.png", record_pos=(0.367, 0.188), resolution=(1280, 720)))
sleep(90.0)
touch(Template(r"tpl1591524536226.png", record_pos=(0.365, 0.241), resolution=(1280, 720)))
touch(Template(r"tpl1591524562464.png", record_pos=(0.002, 0.214), resolution=(1280, 720)))
sleep(3.0)

touch(Template(r"tpl1591525494538.png", record_pos=(-0.173, -0.084), resolution=(1280, 720)))
touch(Template(r"tpl1591524325852.png", record_pos=(0.374, 0.191), resolution=(1280, 720)))
touch(Template(r"tpl1591524467809.png", record_pos=(0.367, 0.188), resolution=(1280, 720)))
sleep(90.0)
touch(Template(r"tpl1591524536226.png", record_pos=(0.365, 0.241), resolution=(1280, 720)))
touch(Template(r"tpl1591524562464.png", record_pos=(0.002, 0.214), resolution=(1280, 720)))
sleep(3.0)

touch(Template(r"tpl1591525540505.png", record_pos=(-0.312, -0.12), resolution=(1280, 720)))
touch(Template(r"tpl1591524325852.png", record_pos=(0.374, 0.191), resolution=(1280, 720)))
touch(Template(r"tpl1591524467809.png", record_pos=(0.367, 0.188), resolution=(1280, 720)))
sleep(90.0)
touch(Template(r"tpl1591524536226.png", record_pos=(0.365, 0.241), resolution=(1280, 720)))
touch(Template(r"tpl1591524562464.png", record_pos=(0.002, 0.214), resolution=(1280, 720)))
sleep(3.0)

touch(Template(r"tpl1591525556947.png", record_pos=(0.074, -0.223), resolution=(1280, 720)))
touch(Template(r"tpl1591524325852.png", record_pos=(0.374, 0.191), resolution=(1280, 720)))
touch(Template(r"tpl1591524467809.png", record_pos=(0.367, 0.188), resolution=(1280, 720)))
sleep(90.0)
touch(Template(r"tpl1591524536226.png", record_pos=(0.365, 0.241), resolution=(1280, 720)))
touch(Template(r"tpl1591524562464.png", record_pos=(0.002, 0.214), resolution=(1280, 720)))
sleep(3.0)




touch(Template(r"tpl1591525589349.png", record_pos=(0.35, -0.111), resolution=(1280, 720)))
touch(Template(r"tpl1591524325852.png", record_pos=(0.374, 0.191), resolution=(1280, 720)))
touch(Template(r"tpl1591524467809.png", record_pos=(0.367, 0.188), resolution=(1280, 720)))
sleep(90.0)
touch(Template(r"tpl1591524536226.png", record_pos=(0.365, 0.241), resolution=(1280, 720)))
touch(Template(r"tpl1591524562464.png", record_pos=(0.002, 0.214), resolution=(1280, 720)))
sleep(3.0)

touch(Template(r"tpl1591525606622.png", record_pos=(-0.028, 0.093), resolution=(1280, 720)))
touch(Template(r"tpl1591524325852.png", record_pos=(0.374, 0.191), resolution=(1280, 720)))
touch(Template(r"tpl1591524467809.png", record_pos=(0.367, 0.188), resolution=(1280, 720)))
sleep(90.0)
touch(Template(r"tpl1591524536226.png", record_pos=(0.365, 0.241), resolution=(1280, 720)))
touch(Template(r"tpl1591524562464.png", record_pos=(0.002, 0.214), resolution=(1280, 720)))
sleep(3.0)

touch(Template(r"tpl1591525632159.png", record_pos=(-0.255, -0.03), resolution=(1280, 720)))
touch(Template(r"tpl1591524325852.png", record_pos=(0.374, 0.191), resolution=(1280, 720)))
touch(Template(r"tpl1591524467809.png", record_pos=(0.367, 0.188), resolution=(1280, 720)))
sleep(90.0)
touch(Template(r"tpl1591524536226.png", record_pos=(0.365, 0.241), resolution=(1280, 720)))
touch(Template(r"tpl1591524562464.png", record_pos=(0.002, 0.214), resolution=(1280, 720)))
sleep(3.0)

'''
