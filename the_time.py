#!/usr/bin/env python
#-*- encoding: gbk -*-
import time
def time_now(time_id):
    feedback = None    
    T=int(time.time())
    if time_id==2 or time_id==3:
        T+=86400
    elif time_id==4 or time_id==5:
        T+=172800
    elif time_id==6 or time_id==7:
        T+=259200
    elif time_id==8 or time_id==9:
        T-=86400
    elif time_id==10 or time_id==11:
        T-=172800
    elif time_id==12 or time_id==13:
        T-=259200
    Time=time.strftime("%H:%M", time.localtime())
    Year=int(time.strftime("%Y", time.localtime(T)))
    Month=int(time.strftime("%m", time.localtime(T)))
    Day=int(time.strftime("%d", time.localtime(T)))
    Week=int(time.strftime("%w", time.localtime(T)))
    Date="%d年%d月%d日 "%(Year,Month,Day)
    if Week==0:
        Week='星期日 '
    elif Week==1:
        Week='星期一 '
    elif Week==2:
        Week='星期二 '
    elif Week==3:
        Week='星期三 '
    elif Week==4:
        Week='星期四 '
    elif Week==5:
        Week='星期五 '
    elif Week==6:
        Week='星期六 '
    if time_id==0:
        feedback = '今天是'+Date
    elif time_id==1:
        feedback = '今天是'+Week
    elif time_id==2:
        feedback = '明天是'+Date
    elif time_id==3:
        feedback = '明天是'+Week
    elif time_id==4:
        feedback = '后天是'+Date
    elif time_id==5:
        feedback = '后天是'+Week
    elif time_id==6:
        feedback = '大后天是'+Date
    elif time_id==7:
        feedback = '大后天是'+Week
    elif time_id==8:
        feedback = '昨天是'+Date
    elif time_id==9:
        feedback = '昨天是'+Week
    elif time_id==10:
        feedback = '前天是'+Date
    elif time_id==11:
        feedback = '前天是'+Week
    elif time_id==12:
        feedback = '大前天是'+Date
    elif time_id==13:
        feedback = '大前天是'+Week
    if time_id==14:
        feedback = '现在时间是'+Time    
    elif time_id==15:
        feedback = '今天是'+Date+Week
    elif time_id==16:
        feedback = Date+Week+Time
    return feedback
if __name__=='__main__':
    info=raw_input('我能为你做些什么？')
    if '几号' in info:
        if '今天' in info:
            time_now(0)
        elif '明天' in info:
            time_now(2)
        elif '大后天' in info:
            time_now(6)
        elif '后天' in info:
            time_now(4)
        elif '昨天' in info:
            time_now(8)
        elif '大前天' in info:
            time_now(12)
        elif '前天' in info:
            time_now(10)
    elif '星期几' in info:
        if '今天' in info:
            time_now(1)
        elif '明天' in info:
            time_now(3)
        elif '大后天' in info:
            time_now(7)
        elif '后天' in info:
            time_now(5)
        elif '昨天' in info:
            time_now(9)
        elif '大前天' in info:
            time_now(13)
        elif '前天' in info:
            time_now(11)
    elif info == '时间'or info == '现在时间':
        time_now(14)
    elif info == '日期':
        time_now(15)
    elif '时间' in info and '日期' in info:
        time_now(16)
