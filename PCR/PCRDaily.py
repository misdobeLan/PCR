# -*- encoding=utf8 -*-
__author__ = "lan"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "Android://127.0.0.1:5037/192.168.1.101:5555?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=ADBTOUCH",
    ])

# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath="G:/PCR")



#  进入登录页
touch(Template(r"图标.png", record_pos=(-0.358, -0.072), resolution=(1440, 2960)))



#进入首页
touch(Template(r"CRIWARE.png", record_pos=(-0.34, 0.247), resolution=(1600, 900)))

#关闭公告

touch(Template(r"关闭.png", record_pos=(-0.003, 0.216), resolution=(1600, 900)))

sleep(2.0)

##############################进入冒险、收菜JJC、PJJC
touch(Template(r"冒险.png", record_pos=(0.001, 0.257), resolution=(1600, 900)))

#进入JJC
touch(Template(r"战斗竞技场.png", record_pos=(0.108, 0.144), resolution=(1600, 900)))

touch(Template(r"收取.png", record_pos=(-0.193, 0.075), resolution=(1600, 900)))
touch(Template(r"竞技场-OK.png", record_pos=(-0.005, 0.09), resolution=(2960, 1440)))



#返回冒险、进入PJJC

sleep(1.0)
touch(Template(r"我的主页.png", record_pos=(-0.407, 0.255), resolution=(1600, 900)))

sleep(3.0)
touch(Template(r"冒险.png", record_pos=(0.001, 0.257), resolution=(1600, 900)))


touch(Template(r"公主竞技场.png", record_pos=(0.358, 0.14), resolution=(1600, 900)))

touch(Template(r"收取.png", record_pos=(-0.193, 0.075), resolution=(1600, 900)))
touch(Template(r"竞技场-OK.png", record_pos=(-0.005, 0.09), resolution=(2960, 1440)))

#工会之家收集物品
sleep(3.0)
touch(Template(r"工会之家.png", record_pos=(0.149, 0.259), resolution=(1600, 900)))

touch(Template(r"工会之家-全部收取.png", record_pos=(0.437, 0.16), resolution=(1600, 900)))
touch(Template(r"关闭.png", record_pos=(-0.003, 0.216), resolution=(1600, 900)))

#首页收集礼物箱
sleep(3.0)


touch(Template(r"我的主页.png", record_pos=(-0.398, 0.255), resolution=(1280, 720)))

touch(Template(r"礼物.png", record_pos=(0.445, 0.177), resolution=(1280, 720)))

touch(Template(r"礼物-全部收取.png", record_pos=(0.378, 0.174), resolution=(1280, 720)))
touch(Template(r"礼物-全部收取-OK.png", record_pos=(0.1, 0.182), resolution=(2960, 1440)))
touch(Template(r"OK.png", record_pos=(-0.001, 0.102), resolution=(1600, 900)))

touch(Template(r"取消.png", record_pos=(-0.111, 0.213), resolution=(1280, 720)))




##############################地下城、战斗时间90秒（当前为断崖的遗迹）

sleep(3.0)

touch(Template(r"冒险.png", record_pos=(0.001, 0.257), resolution=(1600, 900)))

touch(Template(r"地下城.png", record_pos=(0.409, -0.141), resolution=(1280, 720)))
touch(Template(r"断崖的遗迹.png", record_pos=(0.238, -0.026), resolution=(1280, 720)))
touch(Template(r"地下城确认.png", record_pos=(0.114, 0.103), resolution=(1280, 720)))

touch(Template(r"断崖的遗迹-1层.png", record_pos=(0.289, 0.133), resolution=(1280, 720)))
touch(Template(r"地下城-挑战.png", record_pos=(0.374, 0.191), resolution=(1280, 720)))
touch(Template(r"地下城-我的队伍.png", record_pos=(0.398, -0.188), resolution=(1280, 720)))
touch(Template(r"选择队伍.png", target_pos=6, record_pos=(0.071, -0.086), resolution=(2960, 1440)))

touch(Template(r"地下城-战斗开始.png", record_pos=(0.367, 0.188), resolution=(1280, 720)))

sleep(90.0)
touch(Template(r"地下城-下一步.png", record_pos=(0.365, 0.241), resolution=(1280, 720)))
touch(Template(r"竞技场-OK.png", record_pos=(-0.005, 0.09), resolution=(2960, 1440)))
sleep(3.0)


touch(Template(r"断崖的遗迹-2层.png", record_pos=(-0.216, 0.027), resolution=(1280, 720)))
touch(Template(r"地下城-挑战.png", record_pos=(0.374, 0.191), resolution=(1280, 720)))
touch(Template(r"地下城-战斗开始.png", record_pos=(0.367, 0.188), resolution=(1280, 720)))
sleep(90.0)
touch(Template(r"地下城-下一步.png", record_pos=(0.365, 0.241), resolution=(1280, 720)))
touch(Template(r"竞技场-OK.png", record_pos=(-0.005, 0.09), resolution=(2960, 1440)))
sleep(3.0)


touch(Template(r"断崖的遗迹-3层.png", record_pos=(0.131, -0.012), resolution=(1280, 720)))
touch(Template(r"地下城-挑战.png", record_pos=(0.374, 0.191), resolution=(1280, 720)))
touch(Template(r"地下城-战斗开始.png", record_pos=(0.367, 0.188), resolution=(1280, 720)))
sleep(90.0)
touch(Template(r"地下城-下一步.png", record_pos=(0.365, 0.241), resolution=(1280, 720)))
touch(Template(r"竞技场-OK.png", record_pos=(-0.005, 0.09), resolution=(2960, 1440)))
sleep(3.0)

touch(Template(r"断崖的遗迹-4层.png", record_pos=(-0.173, -0.084), resolution=(1280, 720)))
touch(Template(r"地下城-挑战.png", record_pos=(0.374, 0.191), resolution=(1280, 720)))
touch(Template(r"地下城-战斗开始.png", record_pos=(0.367, 0.188), resolution=(1280, 720)))
sleep(90.0)
touch(Template(r"地下城-下一步.png", record_pos=(0.365, 0.241), resolution=(1280, 720)))
touch(Template(r"竞技场-OK.png", record_pos=(-0.005, 0.09), resolution=(2960, 1440)))
sleep(3.0)

touch(Template(r"断崖的遗迹-5层.png", record_pos=(-0.312, -0.12), resolution=(1280, 720)))
touch(Template(r"地下城-挑战.png", record_pos=(0.374, 0.191), resolution=(1280, 720)))
touch(Template(r"地下城-战斗开始.png", record_pos=(0.367, 0.188), resolution=(1280, 720)))
sleep(90.0)
touch(Template(r"地下城-下一步.png", record_pos=(0.365, 0.241), resolution=(1280, 720)))
touch(Template(r"竞技场-OK.png", record_pos=(-0.005, 0.09), resolution=(2960, 1440)))
sleep(3.0)

touch(Template(r"断崖的遗迹-6层.png", record_pos=(0.074, -0.223), resolution=(1280, 720)))
touch(Template(r"地下城-挑战.png", record_pos=(0.374, 0.191), resolution=(1280, 720)))
touch(Template(r"地下城-战斗开始.png", record_pos=(0.367, 0.188), resolution=(1280, 720)))
sleep(90.0)
touch(Template(r"地下城-下一步.png", record_pos=(0.365, 0.241), resolution=(1280, 720)))
touch(Template(r"竞技场-OK.png", record_pos=(-0.005, 0.09), resolution=(2960, 1440)))
sleep(3.0)



touch(Template(r"断崖的遗迹-7层.png", record_pos=(0.35, -0.111), resolution=(1280, 720)))
touch(Template(r"地下城-挑战.png", record_pos=(0.374, 0.191), resolution=(1280, 720)))
touch(Template(r"地下城-战斗开始.png", record_pos=(0.367, 0.188), resolution=(1280, 720)))
sleep(90.0)
touch(Template(r"地下城-下一步.png", record_pos=(0.365, 0.241), resolution=(1280, 720)))
touch(Template(r"竞技场-OK.png", record_pos=(-0.005, 0.09), resolution=(2960, 1440)))
sleep(3.0)

touch(Template(r"断崖的遗迹-8层.png", record_pos=(-0.028, 0.093), resolution=(1280, 720)))
touch(Template(r"地下城-挑战.png", record_pos=(0.374, 0.191), resolution=(1280, 720)))
touch(Template(r"地下城-战斗开始.png", record_pos=(0.367, 0.188), resolution=(1280, 720)))
sleep(90.0)
touch(Template(r"地下城-下一步.png", record_pos=(0.365, 0.241), resolution=(1280, 720)))
touch(Template(r"竞技场-OK.png", record_pos=(-0.005, 0.09), resolution=(2960, 1440)))
sleep(3.0)

touch(Template(r"断崖的遗迹-9层.png", record_pos=(-0.255, -0.03), resolution=(1280, 720)))
touch(Template(r"地下城-挑战.png", record_pos=(0.374, 0.191), resolution=(1280, 720)))
touch(Template(r"地下城-战斗开始.png", record_pos=(0.367, 0.188), resolution=(1280, 720)))
sleep(90.0)
touch(Template(r"地下城-下一步.png", record_pos=(0.365, 0.241), resolution=(1280, 720)))
touch(Template(r"竞技场-OK.png", record_pos=(-0.005, 0.09), resolution=(2960, 1440)))
sleep(3.0)