#! /usr/bin/env python
#coding=utf-8
#这里需要引入三个模块
import time, subprocess, sched, thread
    
# 第一个参数确定任务的时间，返回从某个特定的时间到现在经历的秒数 
# 第二个参数以某种人为的方式衡量时间 
schedule = sched.scheduler(time.time, time.sleep) 
    
def perform_command(cmd, inc):
    subprocess.Popen(cmd, shell=True)
def reminder(cmd, inc = 60):
    # enter用来安排某事件的发生时间，从现在起第n秒开始启动
    schedule.enter(inc, 0, perform_command, (cmd, inc))
    # 持续运行，直到计划时间队列变成空为止 
    schedule.run() 
    thread.exit_thread()    
if __name__=='__main__':    
    print("您的计算机将于10秒钟后关闭:") 
    thread.start_new_thread(reminder, ("shutdown -s", 10))
    print'在这个等待过程中并不耽误我们干一些其他事情'
