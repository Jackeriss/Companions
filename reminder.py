#! /usr/bin/env python
#-*- encoding: gbk -*-
import time, sched, os, thread
schedule = sched.scheduler(time.time, time.sleep)
def perform_command(inc):
    os.startfile("bin\\reminder.exe")
def reminder(inc = 60):
    schedule.enter(inc, 0, perform_command, (inc,))
    schedule.run() 
    thread.exit_thread()
def cancel():
    if not schedule.empty():
        for i in range(0,len(schedule.queue)):
            schedule.cancel(schedule.queue[i])
