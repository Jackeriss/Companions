#!/usr/bin/env python
#-*- encoding: gbk -*-
import os,random,webbrowser,string,time,re,sched,thread
from shell import shell
from shell import shellcon
from calc import *
from the_time import *
from weather import *
from movie import *
from zhidao import *
from wiki import *
from _is_ import _is_
from reminder import *
from count_down import *
from exact_time import *
from blur import *
from xiaohua import *
from neihan import *
from iciba import *

en_punctuation=['+','-','*','/','^','!','"','#','$','%','&','\'','(',')',',','.',';','<','=','>','?','@','[','\\',']','^','_','`','{','|','}','~']
cn_punctuation=['！','“','”','￥','&','‘','’','（','）','，','。','；','《','》','？','【','、','】','…','—','·']
operator=['+','-','*','/','^','!','加','减','乘','除','次方','平方','立方','根号','阶乘','次幂','的正弦','的余弦','的正切','的余切','的正割','的余割','sin','cos','tan','cot','sec','csc','ln']
number=['0','1','2','3','4','5','6','7','8','9']
Q=['吗','呢','么','啥','哪','谁','咋','如何','怎样','咋样','为何','有没有','喜欢不喜欢','行不行','是不是','能不能','会不会','好不好','','','']
schedule = sched.scheduler(time.time, time.sleep)
windows_path = shell.SHGetPathFromIDList(shell.SHGetSpecialFolderLocation(0,shellcon.CSIDL_WINDOWS))
programfiles_path = shell.SHGetPathFromIDList(shell.SHGetSpecialFolderLocation(0,shellcon.CSIDL_PROGRAM_FILES))
def baidu(key):
    feedback=None
    url="http://www.baidu.com/baidu?word="+key
    webbrowser.open_new_tab(url)
    feedback='正在为您搜索"'+key+'"'
    return feedback
def main(info):  
    feedback = None
    special_format=False
###########################################################################################
#calc
###########################################################################################
    op=False
    nu=False
    current_theme_file=open("data/settings/current_theme.txt","r")
    current_theme=current_theme_file.readline()
    current_theme_file.close()
    for i in range(0,len(operator)):
        if operator[i] in info:
            op=True
    for i in range(0,len(number)):
        if number[i] in info:
            nu=True
    if op==True and nu==True:
        feedback = calc(info)
###########################################################################################
#去符号
###########################################################################################
    q=False
    if info[-2:]=='？'or info[-1:]=='?':
        q=True
    origin_info=info
    info=info.decode("gbk").encode("utf8") 
    for i in range(0,len(en_punctuation)):
        while en_punctuation[i].decode("gbk").encode("utf8") in info:
            info=info[:info.index(en_punctuation[i].decode("gbk").encode("utf8"))]+info[info.index(en_punctuation[i].decode("gbk").encode("utf8"))+1:]
    for i in range(0,len(cn_punctuation)):
        while cn_punctuation[i].decode("gbk").encode("utf8") in info:
            info=info[:info.index(cn_punctuation[i].decode("gbk").encode("utf8"))]+info[info.index(cn_punctuation[i].decode("gbk").encode("utf8"))+3:]
    info=info.decode("utf8").encode("gbk")

###########################################################################################
#cancel
###########################################################################################
    if '取消' in info:
        if '关机' in info or '关闭计算机'in info or '关闭电脑'in info:        
            subprocess.Popen('shutdown -a', shell=True)
            feedback ='您的关机计划已取消(设置关机计划时会自动取消之前的关机计划)'
        elif '重启' in info or '重新启动' in info:        
            subprocess.Popen('shutdown -a', shell=True)
            feedback ='您的重启计划已取消(设置重启计划时会自动取消之前的重启计划)'
        elif '注销' in info:        
            subprocess.Popen('shutdown -a', shell=True)
            feedback ='您的注销计划已取消'
        elif '提醒' in info:
            cancel()
            feedback ='已将所有提醒事项取消'

###########################################################################################
#search
########################################################################################### 
    if '搜索' in info:
        info=info[info.index('搜索')+4:]
        feedback=baidu(info)
    elif '搜一下' in info:
        info=info[info.index('搜一下')+6:]
        feedback=baidu(info)
    elif '百度一下' in info:
        info=info[info.index('百度一下')+8:]
        feedback=baidu(info)
    elif 'baidu一下' in info:
        info=info[info.index('baidu一下')+9:]
        feedback=baidu(info)
###########################################################################################
#weather
###########################################################################################
    if '天气'in info or '下雨吗'in info or '下雨了吗'in info or '有雨吗'in info or '下不下雨'in info or '什么天'in info or '晴天吗'in info or '下雪吗'in info or '下不下雪'in info or '温度'in info or '多少度'in info or '几度'in info or '气温'in info:
        city=False
        city_file=open("data/db/city1.txt","r")
        for i in range (0,2586):
            city_info=city_file.readline()
            city_name=city_info[10:].strip(" \n")
            if city_name in info:
                city=True
                break
        if city:
            feedback = city_weather(city_name)
        else:
            feedback = local_weather()
        if feedback:
            special_format = True
###########################################################################################
#xiaohua
###########################################################################################
    if "讲个笑话" in info or "内涵段子" in info:
        feedback=xiaohua()
        style_path_file=open("data/settings/style_path.txt","r")
        style_path=style_path_file.read()
        style_path_file.close()
        href_file=open(style_path+"href.txt","r")
        href=href_file.read()
        href_file.close()
        feedback = '<p style="font-family:Microsoft Yahei;font:24px">'+feedback+'，do，御坂强忍着笑声说道<br><a style="text-decoration:none;color:#'+href+'" href="#">再来一个</a></p>'
        special_format=True
    if "内涵图" in info or "搞笑图" in info:
        feedback=neihan()
        style_path_file=open("data/settings/style_path.txt","r")
        style_path=style_path_file.read()
        style_path_file.close()
        href_file=open(style_path+"href.txt","r")
        href=href_file.read()
        href_file.close()
        feedback = feedback+'<a style="font-family:Microsoft Yahei;font:24px;text-decoration:none;color:#'+href+'" href="#">再来一个</a>'
        special_format=True
    if "让我开心一下" in info or "让我高兴一下" in info:
        style_path_file=open("data/settings/style_path.txt","r")
        style_path=style_path_file.read()
        style_path_file.close()
        href_file=open(style_path+"href.txt","r")
        href=href_file.read()
        href_file.close()
        if random.randint(0,1)==0:
            feedback=xiaohua()
            feedback = '<p style="font-family:Microsoft Yahei;font:24px">'+feedback+'，do，御坂强忍着笑声说道<br><a style="text-decoration:none;color:#'+href+'" href="#">再来一个</a></p>'
        else:
            feedback=neihan()
            feedback = feedback+'<a style="font-family:Microsoft Yahei;font:24px;text-decoration:none;color:#'+href+'" href="#">再来一个</a>'
        special_format=True
###########################################################################################
#run
###########################################################################################
    exe=sys_app=sys_game=sys=web=None
    start=False
    if info[:4]=='打开':
        b=info[4:]
        start=True
    else:
        b=info
    if b=='显示桌面':
        os.startfile("bin\\Shows Desktop.lnk")
        feedback="正在为您显示桌面"
    elif b=='控制面板':
        sys_app='control'
    elif b=='显示':
        sys_app='DpiScaling'
    elif b=='计算器':
        sys_app='calc'
    elif b=='画图':
        sys_app='mspaint'
    elif b=='便笺':
        sys_app='StikyNot'
    elif b=='截图工具':
        sys_app='SnippingTool'     
    elif b=='录音机':
        sys_app='SoundRecorder'
    elif b.lower()=='cmd' or b=='命令行' or b=='命令提示符':
        sys_app='cmd'
    elif b=='放大镜':
        sys_app='Magnify'
    elif b.lower()=='windows移动中心' or b=='移动中心':
        sys_app='mblctr'
    elif b=='系统配置':
        sys_app='msconfig'
    elif b=='系统信息':
        sys_app='msinfo32'
    elif b=='用户账户':
        sys_app='Netplwiz'
    elif b=='屏幕键盘':
        sys_app='osk'
    elif b=='注册表编辑器' or b=='注册表':
        sys_app='regedt32'
    elif b=='音量合成器' or b=='音量合成' or b=='音量控制器' or b=='音量控制' or b=='音量':
        sys_app='SndVol'
    elif b=='任务管理器' or b.lower()=='windows任务管理器':
        sys_app='taskmgr'
    elif b=='关于' or b.lower()=='关于windows' or b.lower()=='windows版本' or b=='系统版本':
        sys_app='winver'
    elif b=='磁盘清理':
        sys_app='cleanmgr'
    elif b=='磁盘碎片整理':
        sys_app='dfrgui'
    elif b=='管理' or b=='计算机管理':
        sys_app='CompMgmtLauncher'
    elif b=='资源监视器':
        sys_app='resmon'
    elif b.lower()=='windows功能' or b.lower()=='打开或关闭windows功能':
        sys_app='OptionalFeatures'
    elif b=='备份和还原' or b=='备份' or b=='系统备份':
        sys_app='sdclt'
    elif b=='系统还原':
        sys_app='rstrui'
    elif b=='系统属性' or b=='系统高级属性' or b=='高级系统设置' or b=='高级系统属性':
        sys_app='SystemPropertiesAdvanced'
    elif b=='用户账户控制' or b=='账户控制':
        sys_app='UserAccountControlSettings'
    elif b=='轻松访问中心' or b=='轻松访问':
        sys_app='Utilman'
    elif b=='服务':
        sys_app='services.msc'
    elif b=='磁盘管理' or b=='磁盘管理器':
        sys_app='diskmgmt.msc'
    elif b=='设备管理器' or b=='设备管理':
        sys_app='devmgmt.msc'
    elif b=='打印管理' or b=='打印机管理' or b=='打印机':
        sys_app='printmanagement.msc'    
    elif b=='扫雷':
        sys_game='MineSweeper'
    elif b=='空当接龙':
        sys_game='FreeCell'
    elif b=='纸牌':
        sys_game='Solitaire'
    elif b=='蜘蛛纸牌':
        sys_game='SpiderSolitaire'
    elif b=='麻将':
        sys_game='Mahjong'
    elif b=='红心大战':
        sys_game='Hearts'
    elif b=='国际象棋':
        sys_game='Chess'
    elif b=='双陆棋':
        sys_game='InternetBackgammon'
    elif b=='三维弹球':
        sys_game='3DPinlinkall'
    elif b=='跳棋':
        sys_game='InternetCheckers'
    elif b=='黑桃王':
        sys_game='InternetSpades'
    elif b=='记事本':
        sys='notepad'
    elif b=='写字板':
        sys='write'
    elif b=='帮助' or b=='Windows帮助和支持':
        sys='winhlp32'
    elif b=='库' or b=='计算机' or b=='我的电脑' or b.lower()=='windows资源管理器':
        sys='explorer'
    elif b=='回收站':
        os.popen('explorer.exe ::{645FF040-5081-101B-9F08-00AA002F954E}')
        feedback='正在为您打开%s'%b
    elif b=='网上邻居' or b=='网络':
        os.popen('explorer.exe ::{208D2C60-3AEA-1069-A2D7-08002B30309D}')
        feedback='正在为您打开%s'%b
    elif b=='我的文档':
        os.popen('explorer.exe ::{450D8FBA-AD25-11D0-98A8-0800361B1103}')
        feedback='正在为您打开%s'%b
    elif b.lower()=='c盘'or b.lower()=='c':
        os.popen('%SystemRoot%\explorer.exe /n,/e,C:\\')
        feedback='正在为您打开%s盘'%b[:1]
    elif b.lower()=='d盘'or b.lower()=='d':
        os.popen('%SystemRoot%\explorer.exe /n,/e,D:\\')
        feedback='正在为您打开%s盘'%b[:1]
    elif b.lower()=='e盘'or b.lower()=='e':
        os.popen('%SystemRoot%\explorer.exe /n,/e,E:\\')
        feedback='正在为您打开%s盘'%b[:1]
    elif b.lower()=='f盘'or b.lower()=='f':
        os.popen('%SystemRoot%\explorer.exe /n,/e,F:\\')
        feedback='正在为您打开%s盘'%b[:1]
    elif b.lower()=='g盘'or b.lower()=='g':
        os.popen('%SystemRoot%\explorer.exe /n,/e,G:\\')
        feedback='正在为您打开%s盘'%b[:1]
    elif b.lower()=='h盘'or b.lower()=='h':
        os.popen('%SystemRoot%\explorer.exe /n,/e,H:\\')
        feedback='正在为您打开%s盘'%b[:1]
    elif b.lower()=='i盘'or b.lower()=='i':
        os.popen('%SystemRoot%\explorer.exe /n,/e,J:\\')
        feedback='正在为您打开%s盘'%b[:1]
    elif b.lower()=='j盘'or b.lower()=='j':
        os.popen('%SystemRoot%\explorer.exe /n,/e,K:\\')
        feedback='正在为您打开%s盘'%b[:1]
    elif b=='百度'or b=='浏览器'or b.lower()=='baidu':
        web='http://www.baidu.com'
    elif b=='贴吧'or b=='百度贴吧'or b=='tieba':
        web='http://tieba.baidu.com'
    elif b=='百度云':
        web='http://yun.baidu.com'
    elif b=='百度地图':
        web='http://map.baidu.com'
    elif b=='优酷'or b=='优酷网'or b.lower()=='youku':
        web='http://www.youku.com' 
    elif b=='土豆网':
        web='http://www.tudou.com' 
    elif b=='豆瓣'or b=='豆瓣网'or b.lower()=='douban':
        web='http://www.douban.com'
    elif b=='豆瓣电影':
        web='http://movie.douban.com'
    elif b=='QQ空间'or b.lower()=='qzone':
        web='http://qzone.qq.com'
    elif b=='网易':
        web='http://www.163.com'
    elif b=='网易邮箱'or b=='163邮箱':
        web='http://mail.163.com'
    elif b.lower()=='qq邮箱':
        web='http://mail.qq.com'
    elif b=='网易云音乐'or b=='网易音乐':
        web='http://music.163.com'
    elif b=='爱奇艺'or b.lower()=='iqiyi':
        web='http://www.iqiyi.com'
    elif b.lower()=='豆瓣fm':
        web='http://fm.douban.com'
    elif b=='搜狐'or b=='搜狐网':
        web='http://www.sohu.com'
    elif b=='搜狐视频':
        web='http://tv.sohu.com'
    elif b=='新浪'or b=='新浪网'or b.lower()=='sina':
        web='http://www.sina.com'
    elif b=='微博'or b=='新浪微博'or b.lower()=='weibo':
        web='http://www.weibo.com'
    elif b=='腾讯网'or b.lower()=='tencent':
        web='http://www.qq.com'
    elif b=='人人网':
        web='http://www.renren.com'
    elif b=='凤凰网':
        web='http://www.ifeng.com'
    elif b=='携程'or b=='携程网':
        web='http://www.ctrip.com'
    elif b=='去哪儿'or b=='去哪儿网'or b=='去哪'or b=='去哪网':
        web='http://www.qunar.com'
    elif b=='中关村'or b=='中关村在线':
        web='http://www.zol.com.cn'
    elif b=='汽车之家'or b=='autohome':
        web='http://www.autohome.com'
    elif b=='赶集网':
        web='http://www.ganji.com'
    elif b=='央视网'or b.lower()=='cctv':
        web='http://www.ctrip.com'
    elif b=='人民网':
        web='http://www.people.com.cn'
    elif b=='新华网':
        web='http://www.xinhuanet.com' 
    elif b=='环球网':
        web='http://www.huanqiu.com'
    elif b=='联合早报'or b=='联合早报网':
        web='http://www.zaobao.com'
    elif b=='网易新闻':
        web='http://news.163.com'
    elif b=='淘宝'or b=='淘宝网'or b.lower()=='taobao':
        web='http://www.taobao.com'
    elif b=='天猫'or b=='天猫网':
        web='http://www.tmall.com'
    elif b=='京东'or b=='京东网':
        web='http://www.jd.com'
    elif b=='亚马逊'or b.lower()=='amazon':
        web='http://www.amazon.cn'
    elif b=='苏宁易购':
        web='http://www.suning.com'
    elif b=='当当'or b=='当当网':
        web='http://www.dangdang.com'
    elif b=='美团'or b=='美团网':
        web='http://www.meituan.com'
    elif b=='美团外卖':
        web='http://waimai.meituan.com'
    elif b=='饿了么':
        web='http://www.ele.me'
    elif b=='美丽街':
        web='http://www.meilijie.com'
    elif b=='美丽说':
        web='http://www.meilishuo.com'
    elif b=='唯品会':
        web='http://www.vip.com'
    elif b=='1号店':
        web='http://www.yhd.com'
    elif b=='聚美优品':
        web='http://www.jumei.com'
    elif b=='聚划算':
        web='http://ju.taobao.com'
    elif b=='糯米'or b=='百度糯米'or b=='糯米团购':
        web='http://www.nuomi.com'
    elif b=='凡客'or b=='凡客诚品':
        web='http://www.vancl.com'
    elif b=='拉手'or b=='拉手网':
        web='http://www.lashou.com'
    elif b=='yitao':
        web='http://www.etao.com'
    elif b=='蘑菇街':
        web='http://www.mogujie.com'
    elif b=='爱淘宝':
        web='http://ai.taobao.com'
    elif b=='天涯网'or b=='天涯社区':
        web='http://www.tianya.com'
    elif b=='百合网':
        web='http://www.baihe.com'
    elif b=='珍爱网':
        web='http://www.zhenai.com'
    elif b=='世纪佳缘':
        web='http://www.jiayuan.com'
    elif b=='威锋网':
        web='http://www.weifeng.com'
    elif b=='猫扑网'or b=='猫扑大杂烩':
        web='http://www.mop.com'
    elif b=='大众点评':
        web='http://www.dianping.com'
    elif b=='58同城':
        web='http://www.58.com'
    elif b=='12306'or b=='火车票':
        web='http://www.12306.cn'
    elif b=='维基'or b=='维基百科'or b=='wikipedia':
        web='http://zh.wikipedia.org'
    elif b=='互动百科':
        web='http://www.baike.com'
    elif b.lower()=='lofter':
        web='http://www.lofter.com'
    elif b=='多看'or b=='多看阅读':
        web='http://www.duokan.com'
    elif b=='暴走漫画':
        web='http://www.baozoumanhua.com'
    elif b=='有妖气'or b=='有妖气漫画':
        web='http://www.u17.com'
    elif b=='果壳'or b=='果壳网':
        web='http://www.guokr.com'
    elif b=='36氪'or b.lower()=='36kr':
        web='http://www.36kr.com'
    elif b=='爱范儿'or b.lower()=='ifanr':
        web='http://www.ifanr.com'
    elif b=='煎蛋'or b=='煎蛋网':
        web='http://www.jiandan.com'
    elif b=='科学松鼠会':
        web='http://www.songshuhui.com'
    elif b=='技术宅社区':
        web='http://www.gn00.com'
    elif b=='技术宅的结界'or b.lower()=='0xaa55':
        web='http://www.0xaa55.com'
    elif b.lower()=='jackeriss'or b.lower()=='jc'or b.lower()=='jack criss':
        web='http://www.jackeriss.com'
    elif b=='斑步自行车社区'or b=='斑步自行车'or b=='斑步竹子自行车'or b=='斑步'or b.lower()=='bamboo bike':
        web='http://www.gn00.com'
    elif b=='慕课'or b=='慕课网':
        web='http://www.imooc.com'
    elif b=='智联招聘':
        web='http://www.zhaopin.com'
    elif b=='前程无忧':
        web='http://www.51job.com'
    elif b=='知乎'or b=='知乎网':
        web='http://www.zhihu.com'
    elif b=='虎嗅'or b=='虎嗅网':
        web='http://www.huxiu.com'
    elif b=='堆糖'or b=='堆糖网':
        web='http://www.duitang.com'
    elif b=='砍柴网':
        web='http://www.ikanchai.com'
    elif b=='哔哩哔哩'or b.lower()=='b站'or b.lower()=='bilibili':
        web='http://www.bilibili.com'
    elif b.lower()=='acfun'or b.lower()=='a站':
        web='http://www.acfun.tv'
    elif b=='斗鱼'or b=='斗鱼直播'or b.lower()=='斗鱼tv':
        web='http://www.douyutv.com'
    elif b.lower()=='yy'or b.lower()=='yy直播':
        web='http://www.yy.com'
    elif b=='战旗'or b.lower()=='战旗tv':
        web='http://www.zhanqi.tv'
    elif b=='17173':
        web='http://www.17173.com'
    elif b=='游民星空':
        web='http://www.gamesky.com'
    elif b=='战网':
        web='http://www.battlenet.cn'
    elif b.lower()=='steam':
        web='http://store.steampowered.com'
    elif b.lower()=='twitch':
        web='http://www.twitch.com'
    elif b=='推特'or b.lower()=='twitter':
        web='http://www.twitter.com'
    elif b=='脸书'or b.lower()=='facebook':
        web='http://www.facebook.com'
    elif b=='谷歌'or b.lower()=='google':
        web='http://www.google.com'
    elif b.lower()=='youtube':
        web='http://www.youtube.com'
    elif b.lower()=='ebay':
        web='http://www.ebay.com'
    elif b.lower()=='github':
        web='http://www.github.com'
    elif b=='雅虎'or b.lower()=='yahoo':
        web='http://www.yahoo.com'
    if sys_app:
        thread.start_new_thread(subprocess.Popen,(sys_app,))
        feedback='正在为您打开%s'%b           
    elif sys_game:
        thread.start_new_thread(os.startfile,(programfiles_path+'/Microsoft Games/'+sys_game+'/'+sys_game+'.exe',))
        feedback='正在为您打开%s'%b 
    elif sys:
        thread.start_new_thread(subprocess.Popen,(sys,))
        feedback='正在为您打开%s'%b
    elif web:
        webbrowser.open_new_tab(web)
        feedback='正在为您打开%s'%b
    if not feedback:
        if info.isalpha():
            if info.count(' ')<2:
                feedback=iciba(info)
###########################################################################################
#the_time
###########################################################################################
    if '几号' in info:
        if '今天' in info:
            feedback=time_now(0)
        elif '明天' in info:
            feedback=time_now(2)
        elif '大后天' in info:
            feedback=time_now(6)
        elif '后天' in info:
            feedback=time_now(4)
        elif '昨天' in info:
            feedback=time_now(8)
        elif '大前天' in info:
            feedback=time_now(12)
        elif '前天' in info:
            feedback=time_now(10)
    elif '星期几' in info or '周几' in info:
        if '今天' in info:
            feedback=time_now(1)
        elif '明天' in info:
            feedback=time_now(3)
        elif '大后天' in info:
            feedback=time_now(7)
        elif '后天' in info:
            feedback=time_now(5)
        elif '昨天' in info:
            feedback=time_now(9)
        elif '大前天' in info:
            feedback=time_now(13)
        elif '前天' in info:
            feedback=time_now(11)
    elif info == '时间' or info == '现在时间' or '几点了' in info or '现在几点' in info:
        feedback=time_now(14)
    elif info == '日期':
        feedback=time_now(15)
    elif '时间' in info and '日期' in info:
        feedback=time_now(16)
###########################################################################################
#chat
###########################################################################################
    chat_file=open("data/db/chat.txt","r")
    over=False
    answer=False
    Type=0
    while not over:
        chat_info=chat_file.readline().strip('\n')
        if chat_info=='':
            over=True
            break
        questions=chat_info[:chat_info.index(':')].split(';')
        answers=chat_info[chat_info.index(':')+1:].split(';')
        for i in range(0,len(questions)):
            if info == questions[i]:                
                answer=random.choice(answers)
                over=True
    chat_file.close()
    if answer:
        feedback = answer
    else:
        re_dirty_words=['不要说脏话，这显得你很low！','我已经警告过你了，请不要说脏话！','我TM的给TM的你TM的脸，你TM的别TM的给脸不要脸！']
        dirty_words_time=0
        dirty_words_file=open("data/db/dirty_words.txt","r")
        over=False
        while not over:
            dirty_words=dirty_words_file.readline().strip('\n')
            if dirty_words=='':
                over=True
                break
            if dirty_words in info:
                dirty_words_time_file=open("data/db/dirty_words_time.txt","r")
                dirty_words_time=int(dirty_words_time_file.readline().strip('\n'))
                feedback=re_dirty_words[dirty_words_time%len(re_dirty_words)]
                dirty_words_time+=1
                dirty_words_time_file.close()
                dirty_words_time_file=open("data/db/dirty_words_time.txt","w")
                dirty_words_time_file.write('%d'%dirty_words_time)
                dirty_words_time_file.close()
                over=True
        dirty_words_file.close()
###########################################################################################
#reminder
###########################################################################################
    if not feedback:
        if '提醒我' in info:
            event=info[info.index('提醒我')+6:]
            if event:
                remind='主人，该'+event+'了！'
                remind_file=open("data/db/reminder.txt","w")
                remind_file.write(remind)
                remind_file.close()
                when=info[:info.index('提醒我')]
                if when:
                    special_format=True
                    style_path_file=open("data/settings/style_path.txt","r")
                    style_path=style_path_file.read()
                    style_path_file.close()
                    href_file=open(style_path+"href.txt","r")
                    href=href_file.read()
                    href_file.close()
                    if '后'in when:
                        (h,m,s)=count_down(when)
                        h=int(h)
                        m=int(m)
                        s=int(s)
                        second=3600*h+60*m+s
                        thread.start_new_thread(reminder, (second,))
                        feedback ='<p style="font-family:Microsoft Yahei;font:24px">OK,不过在我提醒你之前你可不要关掉我哦，否则谁去提醒你？do，御坂耐心地说道<br><a style="text-decoration:none;color:#'+href+'" href="#">取消提醒</a></p>'
                    if not feedback:
                        exact_when=exact_time(when)
                        date=time.strftime("%Y%m%d", time.localtime())
                        whole_time=exact_when+date
                        second=time.mktime(time.strptime(whole_time,"%H:%M%Y%m%d"))-time.time()
                        thread.start_new_thread(reminder, (second,))
                        feedback ='<p style="font-family:Microsoft Yahei;font:24px">OK,不过在我提醒你之前你可不要关掉我哦，否则谁去提醒你？do，御坂耐心地说道<br><a style="text-decoration:none;color:#'+href+'" href="#">取消提醒</a></p>'
                else:
                    feedback="我没搞明白你让我什么时间提醒你，请用更清晰的表达再说一遍。"
            else:
                feedback="我没搞明白你让我提醒你做什么，请用更清晰的表达再说一遍。"
        else:
            shutdown=restart=False
            if '关机' in info:
                if '关机'==info:
                    subprocess.Popen('shutdown -s')
                    feedback='没时间告别了，再见~'
                    shutdown=False
                else:
                    when=info[:info.index('关机')]
                    shutdown=True
            elif '关电脑' in info:
                if '关电脑'==info:
                    subprocess.Popen('shutdown -s')
                    feedback='没时间告别了，再见~'
                    shutdown=False
                else:
                    when=info[:info.index('关电脑')]
                    shutdown=True
            elif '关闭计算机' in info:
                if '关闭计算机'==info:
                    subprocess.Popen('shutdown -s')
                    feedback='没时间告别了，再见~'
                    shutdown=False
                else:
                    when=info[:info.index('关闭计算机')]
                    shutdown=True
            elif '关闭电脑' in info:
                if '关闭电脑'==info:
                    subprocess.Popen('shutdown -s')
                    feedback='没时间告别了，再见~'
                    shutdown=False
                else:
                    when=info[:info.index('关闭电脑')]
                    shutdown=True
            if shutdown:
                special_format=True
                style_path_file=open("data/settings/style_path.txt","r")
                style_path=style_path_file.read()
                style_path_file.close()
                href_file=open(style_path+"href.txt","r")
                href=href_file.read()
                href_file.close()
                if '后'in when:
                    (h,m,s)=count_down(when)
                    h=int(h)
                    m=int(m)
                    s=int(s)
                    second=3600*h+60*m+s
                    subprocess.Popen('shutdown -a', shell=True)
                    subprocess.Popen('shutdown -s -t %d'%second, shell=True)
                    feedback ='<p style="font-family:Microsoft Yahei;font:24px">您的计算机将于'
                    if h!=0:
                        feedback +='%d小时'%h
                    if m!=0:
                        feedback +='%d分钟'%m
                    if s!=0:
                        feedback +='%d秒'%s            
                    feedback = feedback+'后关闭。do，御坂不舍地说道<br><a style="text-decoration:none;color:#'+href+'" href="#">取消关机</a></p>'
                if not feedback:
                    exact_when=exact_time(when)
                    date=time.strftime("%Y%m%d", time.localtime())
                    whole_time=exact_when+date
                    second=time.mktime(time.strptime(whole_time,"%H:%M%Y%m%d"))-time.time()
                    if second<0:
                        second+=86400
                    subprocess.Popen('shutdown -a', shell=True)        
                    subprocess.Popen('shutdown -s -t %d'%second, shell=True)
                    feedback ='<p style="font-family:Microsoft Yahei;font:24px">您的计算机将于'+exact_when+'关闭。do，御坂不舍地说道<br><a style="text-decoration:none;color:#'+href+'" href="#">取消关机</a></p>'
            else:
                if '重新启动' in info:
                    if '重新启动'==info:
                        subprocess.Popen('shutdown -r', shell=True)
                        feedback='放心吧，我们马上就会再见面的！'
                        restart=False
                    else:
                        when=info[:info.index('重新启动')]
                        restart=True
                elif '重启' in info:
                    if '重启'==info:
                        subprocess.Popen('shutdown -r', shell=True)
                        feedback='放心吧，我们马上就会再见面的！'
                        restart=False
                    else:
                        when=info[:info.index('重启')]
                        restart=True
                if restart:
                    special_format=True
                    style_path_file=open("data/settings/style_path.txt","r")
                    style_path=style_path_file.read()
                    style_path_file.close()
                    href_file=open(style_path+"href.txt","r")
                    href=href_file.read()
                    href_file.close()
                    if '后'in when:
                        (h,m,s)=count_down(when)
                        h=int(h)
                        m=int(m)
                        s=int(s)
                        second=3600*h+60*m+s
                        subprocess.Popen('shutdown -a', shell=True)
                        subprocess.Popen('shutdown -r -t %d'%second, shell=True)
                        feedback ='<p style="font-family:Microsoft Yahei;font:24px">您的计算机将于'
                        if h!=0:
                            feedback +='%d小时'%h
                        if m!=0:
                            feedback +='%d分钟'%m
                        if s!=0:
                            feedback +='%d秒'%s
                        feedback +='后重启。do，御坂不舍地说道<br><a style="text-decoration:none;color:#'+href+'" href="#">取消关机</a></p>'                                    
                    if not feedback:
                        exact_when=exact_time(when)
                        date=time.strftime("%Y%m%d", time.localtime())
                        whole_time=exact_when+date
                        second=time.mktime(time.strptime(whole_time,"%H:%M%Y%m%d"))-time.time()
                        if second<0:
                            second+=86400
                        subprocess.Popen('shutdown -a', shell=True)        
                        subprocess.Popen('shutdown -r -t %d'%second, shell=True)
                        feedback ='<p style="font-family:Microsoft Yahei;font:24px">您的计算机将于%s重启。do，御坂不舍地说道<br><a style="text-decoration:none;color:#'+href+'" href="#">取消关机</a></p>'%exact_when
                elif '注销'==info:
                    subprocess.Popen('shutdown -r', shell=True)
                    feedback='你还会回来的对吧？别离开太久，我会很想你的！'
                    logout=False
                elif '休眠'==info:
                    subprocess.Popen('powercfg -h on', shell=True)
                    subprocess.Popen('shutdown -h', shell=True)
                    feedback='冬天来了吗？嘛，不管了，我要休眠了……zzZ'
                    hibernation=False
                elif '睡眠'==info:
                    subprocess.Popen('powercfg -h off', shell=True)
                    subprocess.Popen('rundll32.exe powrprof.dll,SetSuspendState', shell=True)
                    subprocess.Popen('powercfg -h on', shell=True)
                    feedback ='……zzZ 啊？干嘛叫醒我？人家睡得正香呢！'
                elif '锁定'==info or '锁屏'==info or'锁定计算机'==info:
                    subprocess.Popen('rundll32 user32.dll,LockWorkStation', shell=True)
                    feedback ='钥匙拿了吗？那我可锁了啊！'

###########################################################################################
#wiki
###########################################################################################
    if info=="你好" or info=="嗨" or info=="哈喽" or info=="你好啊" or info=="您好":
        if "(" in current_theme and ")" in current_theme:
            feedback="你好，我叫大白，是你的私人健康助手"
    if "你是谁" in info or "你叫啥" in info or "你叫什么" in info or "叫什么名字" in info or "你的名字是什么" in info or "你叫啥名" in info:
        if "(" in current_theme and ")" in current_theme:
            feedback="你好，我叫大白，是你的私人健康助手"
        elif current_theme=="御坂10032号":
            feedback="我的名字是御坂，是姐姐大人的克隆体。"
        elif current_theme=="Stuart":
            feedback="我？Stuart！"
        elif current_theme=="哆啦A梦":
            feedback="我叫哆啦A梦，是一只来自22世纪的猫型机器人！"
    if "你多大了" in info or "你今年多大了" in info or "你几岁了" in info or "你今年几岁" in info or "你的年龄" in info:
        if "(" in current_theme and ")" in current_theme:
            feedback="就算我"+str(int(time.strftime("%Y", time.localtime()))-2014)+"岁吧！"
        elif current_theme=="御坂10032号":
            feedback="御坂今年14岁。"
        elif current_theme=="Stuart":
            feedback="你该看看电影《小黄人》在你们人类出现之前就有我们了！"
        elif current_theme=="哆啦A梦":
            feedback="我2112年出生，所以今年应该是"+str(int(time.strftime("%Y", time.localtime()))-2112)+"岁！"
    if "你的生日" in info or "你什么时候过生日" in info or "你啥时候生日" in info or "你的出生日期" in info or "你什么时候出生的" in info:
        if "(" in current_theme and ")" in current_theme:
            feedback="2014年11月07日 吧啦啦啦~"
        elif current_theme=="御坂10032号":
            feedback="御坂是克隆人，我已经不记得自己什么时候被制造出来了。我只知道姐姐大人的生日是5月2日。"
        elif current_theme=="Stuart":
            feedback="额...呵呵呵..."
        elif current_theme=="哆啦A梦":
            feedback="我是2112年9月3日出生的！"
    if "你是男的还是女的" in info or "你的性别" in info or "你是GG还是MM" in info or "你是妹子吗" in info or "你是汉子还是妹子" in info:
        if "(" in current_theme and ")" in current_theme:
            feedback="我的程序将我的声音设定为男性。"
        elif current_theme=="御坂10032号":
            feedback="御坂是妹妹。"
        elif current_theme=="Stuart":
            feedback="噗，我们貌似没有性别。啊哈哈哈哈！"
        elif current_theme=="哆啦A梦":
            feedback="我是公的！"
    if info=="扫描我" or info.lower()=="scan me":
        if "(" in current_theme and ")" in current_theme:
            feedback="扫描完成！你没有受到外伤，但是，你的荷尔蒙水平和神经递质都显示你有异常情绪波动，常见于青少年人群，症状鉴定：青春期躁动。直到你说“我很满意你的照顾”，我才会结束工作。"
        elif current_theme=="御坂10032号":
            feedback="用我的眼罩吗？"
        elif current_theme=="Stuart":
            feedback="我长那么大的眼睛可不是用来干这个的！"
        else:
            feedback="喂，看清楚了，我又不是大白！"
    if info=="我很满意你的照顾" or info=="我对你的照顾很满意":
        if "(" in current_theme and ")" in current_theme:
            quit()
        elif current_theme=="哆啦A梦":
            feedback="虽然我也是个机器人，但我的使命是让你幸福，在此之前我是不可能离开你的！"
        elif current_theme=="Stuart":
            feedback="谢谢主人！（内心：这个主人也太不卑鄙了，和Gru差远了！）"
        elif current_theme=="御坂10032号":
            feedback="...御坂哪里做的不好吗？"
    if "唱首歌" in info or "唱个歌" in info or "唱歌" in info:
        if current_theme=="Stuart":
            feedback="@sing"
            special_format=True
        elif current_theme=="御坂10032号":
            feedback="小黄人唱歌特别好听，我不骗你，真的！"
        elif current_theme=="哆啦A梦":
            feedback="我们中就小黄人出过专辑！你快去让他给你唱一首吧！"
        else:
            feedback="很抱歉我不会唱歌，不过我听说小黄人个个都是天生的歌手！"
    if info=="任意门" or info=="随意门":
        if current_theme=="哆啦A梦":
            fb=["","前"]
            zeros=["0","00","000"]
            feedback="欢迎来到公元"+random.choice(fb)+str(random.randint(1,99))+random.choice(zeros)+"年"
        elif current_theme=="Stuart":
            feedback="我只听说过红绿色盲，你竟然是黄蓝色盲！呵呵呵！"
        elif current_theme=="御坂10032号":
            feedback="御坂的能力是缺陷电气（Radio Noise），并不能制造你所说的任意门。"
        elif "(" in current_theme and ")" in current_theme:
            feedback="我是白胖子，不是蓝胖子！上一个我就被困在“任意门”中了，你忘了吗？"
    if not feedback:
        try:
            feedback = movie(info)
        except:
            pass
        if feedback:
            special_format=True
    if not feedback:
        try:
            feedback = zhidao(info)
        except:
            pass
    if not feedback:
        try:
            feedback = wiki(info)
        except:
            pass
        if feedback:
            special_format=True
    if not feedback:
        if info[-4:]=="是谁":
            info1=info[:-4]
            try:
                feedback = wiki(info1)
            except:
                pass
            if feedback:
                special_format=True
        elif info[:4]=="谁是":
            info1=info[4:]
            try:
                feedback = wiki(info1)
            except:
                pass
            if feedback:
                special_format=True
    if not feedback or feedback=='<p style="font-family:Microsoft Yahei;font:24px">请检查您的网络连接</p>'or feedback=='请检查您的网络连接':
        temp = None
        temp = blur(info,q)
        if temp:
            feedback=temp
    if not feedback:
        style_path_file=open("data/settings/style_path.txt","r")
        style_path=style_path_file.read()
        style_path_file.close()
        href_file=open(style_path+"href.txt","r")
        href=href_file.read()
        href_file.close()
        feedback = '不知道“'+origin_info+'”是什么意思，你可以<a style="text-decoration:none;color:#'+href+'"href="http://www.baidu.com/baidu?word='+origin_info+'">百度一下</a>'
    if special_format:
        feedback = '<p style="font-family:Microsoft Yahei;font:24px">'+current_theme+'：</p>'+feedback
    else:
        if current_theme=="御坂10032号":
            adv=["一本正经地","一本正经地","一本正经地","认真地","强忍着笑声","耐心地","无奈地","淡定地","淡定地"]
            feedback = '<p style="font-family:Microsoft Yahei;font:24px">'+current_theme+'：'+feedback+'，do，御坂'+random.choice(adv)+'说道</p>'
        else:
            feedback = '<p style="font-family:Microsoft Yahei;font:24px">'+current_theme+'：'+feedback+'</p>'
    return feedback
