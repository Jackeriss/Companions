#!/usr/bin/env python
#-*- encoding: GBK -*-
import urllib2,string
from urllib2 import Request, urlopen
def weather(city_code):
    current_theme_file=open("data/settings/current_theme.txt","r")
    current_theme=current_theme_file.readline().strip("\n")
    current_theme_file.close()
    url='http://m.weather.com.cn/mweather/'+city_code+'.shtml'
    page=None
    try:
        page=urllib2.urlopen(url)
    except:
        feedback = '<p style="font-family:Microsoft Yahei;font:24px">请检查您的网络连接</p>'
    if page:
        data=page.read()
        if '空气质量'.decode("gbk").encode("utf8") in data:
            data=data[data.index('空气质量'.decode("gbk").encode("utf8")):]
            yejian=False
            if "夜间".decode("gbk").encode("utf8") in data:
                day1="夜间"
                yejian=True
                data=data[data.index("夜间".decode("gbk").encode("utf8"))+6:]                                
                if ".png".decode("gbk").encode("utf8") in data:
                    day1_img="d".decode("gbk").encode("utf8")+data[data.index(".png".decode("gbk").encode("utf8"))-2:data.index(".png".decode("gbk").encode("utf8"))+4]
                if '<span>'.decode("gbk").encode("utf8") in data and '</span>'.decode("gbk").encode("utf8") in data:
                    day1_tamp=data[data.index("<span>".decode("gbk").encode("utf8"))+6:data.index("</span>".decode("gbk").encode("utf8"))]
            elif "今天".decode("gbk").encode("utf8") in data:
                day1="今天"
                data=data[data.index("今天".decode("gbk").encode("utf8"))+6:]
                if ".png".decode("gbk").encode("utf8") in data:
                    day1_img=data[data.index(".png".decode("gbk").encode("utf8"))-3:data.index(".png".decode("gbk").encode("utf8"))+4]
                if '<span>'.decode("gbk").encode("utf8") in data and '</span>'.decode("gbk").encode("utf8") in data:
                    day1_tamp=data[data.index("<span>".decode("gbk").encode("utf8"))+6:data.index("</span>".decode("gbk").encode("utf8"))]
            if "明天".decode("gbk").encode("utf8") in data:
                day2="明天"
                data=data[data.index("明天".decode("gbk").encode("utf8"))+6:]
                if ".png".decode("gbk").encode("utf8") in data:
                    day2_img=data[data.index(".png".decode("gbk").encode("utf8"))-3:data.index(".png".decode("gbk").encode("utf8"))+4]
                if '<span>'.decode("gbk").encode("utf8") in data and '</span>'.decode("gbk").encode("utf8") in data:
                    day2_tamp=data[data.index("<span>".decode("gbk").encode("utf8"))+6:data.index("</span>".decode("gbk").encode("utf8"))]
            if "后天".decode("gbk").encode("utf8") in data:
                day3="后天"
                data=data[data.index("后天".decode("gbk").encode("utf8"))+6:]
                if ".png".decode("gbk").encode("utf8") in data:
                    day3_img=data[data.index(".png".decode("gbk").encode("utf8"))-3:data.index(".png".decode("gbk").encode("utf8"))+4]
                if '<span>'.decode("gbk").encode("utf8") in data and '</span>'.decode("gbk").encode("utf8") in data:
                    day3_tamp=data[data.index("<span>".decode("gbk").encode("utf8"))+6:data.index("</span>".decode("gbk").encode("utf8"))]
            if "周".decode("gbk").encode("utf8") in data:
                day4=data[data.index("周".decode("gbk").encode("utf8")):data.index("周".decode("gbk").encode("utf8"))+6]
                data=data[data.index("周".decode("gbk").encode("utf8"))+6:]
                if ".png".decode("gbk").encode("utf8") in data:
                    day4_img=data[data.index(".png".decode("gbk").encode("utf8"))-3:data.index(".png".decode("gbk").encode("utf8"))+4]
                if '<span>'.decode("gbk").encode("utf8") in data and '</span>'.decode("gbk").encode("utf8") in data:
                    day4_tamp=data[data.index("<span>".decode("gbk").encode("utf8"))+6:data.index("</span>".decode("gbk").encode("utf8"))]
            if "周".decode("gbk").encode("utf8") in data:
                day5=data[data.index("周".decode("gbk").encode("utf8")):data.index("周".decode("gbk").encode("utf8"))+6]
                data=data[data.index("周".decode("gbk").encode("utf8"))+6:]
                if ".png".decode("gbk").encode("utf8") in data:
                    day5_img=data[data.index(".png".decode("gbk").encode("utf8"))-3:data.index(".png".decode("gbk").encode("utf8"))+4]
                if '<span>'.decode("gbk").encode("utf8") in data and '</span>'.decode("gbk").encode("utf8") in data:
                    day5_tamp=data[data.index("<span>".decode("gbk").encode("utf8"))+6:data.index("</span>".decode("gbk").encode("utf8"))]
            if "周".decode("gbk").encode("utf8") in data:
                day6=data[data.index("周".decode("gbk").encode("utf8")):data.index("周".decode("gbk").encode("utf8"))+6]
                data=data[data.index("周".decode("gbk").encode("utf8"))+6:]
                if ".png".decode("gbk").encode("utf8") in data:
                    day6_img=data[data.index(".png".decode("gbk").encode("utf8"))-3:data.index(".png".decode("gbk").encode("utf8"))+4]
                if '<span>'.decode("gbk").encode("utf8") in data and '</span>'.decode("gbk").encode("utf8") in data:
                    day6_tamp=data[data.index("<span>".decode("gbk").encode("utf8"))+6:data.index("</span>".decode("gbk").encode("utf8"))]
            if "周".decode("gbk").encode("utf8") in data:
                day7=data[data.index("周".decode("gbk").encode("utf8")):data.index("周".decode("gbk").encode("utf8"))+6]
                if ".png".decode("gbk").encode("utf8") in data:
                    day7_img=data[data.index(".png".decode("gbk").encode("utf8"))-3:data.index(".png".decode("gbk").encode("utf8"))+4]
                if '<span>'.decode("gbk").encode("utf8") in data and '</span>'.decode("gbk").encode("utf8") in data:
                    day7_tamp=data[data.index("<span>".decode("gbk").encode("utf8"))+6:data.index("</span>".decode("gbk").encode("utf8"))]
            day4=day4.decode("utf8").encode("gbk")
            day5=day5.decode("utf8").encode("gbk")
            day6=day6.decode("utf8").encode("gbk")
            day7=day7.decode("utf8").encode("gbk")
            day1_img="data/themes/"+current_theme+"/images/weather/"+day1_img.decode("utf8").encode("gbk")
            day2_img="data/themes/"+current_theme+"/images/weather/"+day2_img.decode("utf8").encode("gbk")
            day3_img="data/themes/"+current_theme+"/images/weather/"+day3_img.decode("utf8").encode("gbk")
            day4_img="data/themes/"+current_theme+"/images/weather/"+day4_img.decode("utf8").encode("gbk")
            day5_img="data/themes/"+current_theme+"/images/weather/"+day5_img.decode("utf8").encode("gbk")
            day6_img="data/themes/"+current_theme+"/images/weather/"+day6_img.decode("utf8").encode("gbk")
            day7_img="data/themes/"+current_theme+"/images/weather/"+day7_img.decode("utf8").encode("gbk")
            day1_tamp=day1_tamp.decode("utf8").encode("gbk").replace("/","~").replace("℃","°")
            day2_tamp=day2_tamp.decode("utf8").encode("gbk").replace("/","~").replace("℃","°")
            day3_tamp=day3_tamp.decode("utf8").encode("gbk").replace("/","~").replace("℃","°")
            day4_tamp=day4_tamp.decode("utf8").encode("gbk").replace("/","~").replace("℃","°")
            day5_tamp=day5_tamp.decode("utf8").encode("gbk").replace("/","~").replace("℃","°")
            day6_tamp=day6_tamp.decode("utf8").encode("gbk").replace("/","~").replace("℃","°")
            day7_tamp=day7_tamp.decode("utf8").encode("gbk").replace("/","~").replace("℃","°")
            day1='    '+day1.ljust(20-len(day1))
            day2='    '+day2.ljust(20-len(day2))
            day3='    '+day3.ljust(20-len(day3))
            day4='    '+day4.ljust(20-len(day4))
            day5='    '+day5.ljust(20-len(day5))
            day6='    '+day6.ljust(20-len(day6))
            day7='    '+day7.ljust(20-len(day7))
            if yejian:
                day1_tamp=day1_tamp.rjust(25-len(day1_tamp))
            else:
                day1_tamp=day1_tamp.rjust(27-len(day1_tamp))
            day2_tamp=day2_tamp.rjust(27-len(day2_tamp))
            day3_tamp=day3_tamp.rjust(27-len(day3_tamp))
            day4_tamp=day4_tamp.rjust(27-len(day4_tamp))
            day5_tamp=day5_tamp.rjust(27-len(day5_tamp))
            day6_tamp=day6_tamp.rjust(27-len(day6_tamp))
            day7_tamp=day7_tamp.rjust(27-len(day7_tamp))
            city_file=open("data/db/city1.txt","r")
            for i in range (0,2586):
                city_info=city_file.readline()
                if city_code in city_info :
                    city_name=city_info[10:].strip(" \n")
                    break
            city_file.close()
            title=city_name+"天气预报"
            style_path_file=open("data/settings/style_path.txt","r")
            style_path=style_path_file.read()
            style_path_file.close()
            weather_file=open(style_path+"weather.txt","r")
            weather=weather_file.read()
            weather_file.close()
            feedback=weather+'<div align=center>'+title+'</div></p><pre>'+weather+day1+'<img src="'+day1_img+'">'+day1_tamp+'</p>'+weather+day2+'<img src="'+day2_img+'">'+day2_tamp+'</p>'+weather+day3+'<img src="'+day3_img+'">'+day3_tamp+'</p>'+weather+day4+'<img src="'+day4_img+'">'+day4_tamp+'</p>'+weather+day5+'<img src="'+day5_img+'">'+day5_tamp+'</p>'+weather+day6+'<img src="'+day6_img+'">'+day6_tamp+'</p>'+weather+day7+'<img src="'+day7_img+'">'+day7_tamp+'</p></pre><div></div>'
        else:
            feedback = '<p style="font-family:Microsoft Yahei;font:24px">当前网络不稳定，请稍后重试</p>'
    else:
        feedback = '<p style="font-family:Microsoft Yahei;font:24px">当前网络不稳定，请稍后重试</p>'
    return feedback
def local_weather():
    feedback = None
    url1='http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=js'
    page1=None
    try:
        page1=urllib2.urlopen(url1)
    except:
        feedback = '<p style="font-family:Microsoft Yahei;font:24px">请检查您的网络连接</p>'
    if page1:
        data1=page1.read()
        city_unicode=data1[data1.index('city')+7:data1.index('district')-3]
        city_code=None
        city_file=open("data/db/city2.txt","r")
        for i in range (0,2586):
            city_info=city_file.readline()
            if city_unicode in city_info:
                city_code=city_info[:9]
                break
        city_file.close
        if city_code:
            feedback=weather(city_code)
    return feedback
def city_weather(city_name):
    feedback = None
    city_code=None
    city_file=open("data/db/city1.txt","r")
    for i in range (0,2586):
        city_info=city_file.readline()
        if city_name in city_info :
            city_code=city_info[:9]
            break
    city_file.close
    if city_code:
        feedback=weather(city_code)      
    else:
        feedback = '<p style="font-family:Microsoft Yahei;font:24px">对不起，查不到此城市的天气信息。</p>'
    return feedback
if __name__=='__main__':
    info=str(raw_input('我能帮你做点什么？'))
    if '的天气'in info:
        info=info[:info.index('的天气')]
        print city_weather(info)
    if info=='天气':
        print local_weather()
    elif '天气'in info:
        if info[-4:]=='天气':
            info=info[:info.index('天气')]
            print city_weather(info)
        else:
            print weather()
