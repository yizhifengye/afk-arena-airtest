# -*- encoding=utf8 -*-
__author__ = "littletommytan"

from airtest.core.api import *

auto_setup(__file__)


start_app("com.lilithgames.hgame.cn")

wait(Template(r"tpl1579175860795.png", record_pos=(-0.006, 0.65), resolution=(1080, 1920)),999999999999999)
touch(Template(r"tpl1579175860795.png", record_pos=(-0.006, 0.65), resolution=(1080, 1920)))

sum = 0
passTime = 0
while True:
    #     失败重来
    if exists(Template(r"tpl1579177798301.png", record_pos=(0.002, 0.706), resolution=(1080, 1920))):
        touch(Template(r"tpl1579177798301.png", record_pos=(0.002, 0.706), resolution=(1080, 1920)))
        try:
            touch(Template(r"tpl1579177798301.png", record_pos=(0.002, 0.706), resolution=(1080, 1920))) 
        except:
            pass
#     战斗
    if exists(Template(r"tpl1579177952990.png", record_pos=(-0.005, 0.801), resolution=(1080, 1920))):
        sum = sum + 1
        print ("The Stage you' ve pass: " , passTime)
        print ("Current Stage trying time: " , sum)
        try:
            touch(Template(r"tpl1579177952990.png", record_pos=(-0.005, 0.801), resolution=(1080, 1920)))
        except:
            pass
        
        
#     下一关
    if exists(Template(r"tpl1579178918677.png", record_pos=(-0.004, 0.653), resolution=(1080, 1920))):
        sum = 0
        passTime = passTime + 1
        print ("This Stage trying time: " , sum)
        try:
            touch(Template(r"tpl1579178918677.png", record_pos=(-0.004, 0.653), resolution=(1080, 1920))) 
        except:
            pass
        
        
    #  首领
    if exists(Template(r"tpl1579182748899.png", record_pos=(0.001, 0.475), resolution=(1080, 1920))):
        try:
            touch(Template(r"tpl1579182748899.png", record_pos=(0.001, 0.475), resolution=(1080, 1920)))
        except:
            pass

