#! /usr/bin/env python
#-*- encoding: gbk -*-
import time,os
def delete_pic(name):
    time.sleep(2)
    path1=os.getcwd()+"\\"+name+".jpg"
    path2=os.getcwd()+"\\"+name+".png"
    path3=os.getcwd()+"\\"+name+"1.jpg"
    path4=os.getcwd()+"\\"+name+"1.png"
    if os.path.exists(path1):
        os.remove(path1)
    if os.path.exists(path2):
        os.remove(path2)
    if os.path.exists(path3):
        os.remove(path3)
    if os.path.exists(path4):
        os.remove(path4)
        
