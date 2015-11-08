#!/usr/bin/env python
#-*- encoding: gbk -*-
import cookielib,urllib2
def xiaohua():
    feedback = None
    page1=None
    url='http://neihanshequ.com/'
    HEADERS = {"cookie":'uuid="w:d132301db48c4c8184be1d188c296f9b"; tt_webid=4370653838; csrftoken=e6e30ca5623bce575755fad47ddb029d; __utma=101886750.501576781.1434802321.1434871312.1434875802.4; __utmb=101886750.12.10.1434875802; __utmc=101886750; __utmz=101886750.1434871312.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E5%86%85%E6%B6%B5%E6%AE%B5%E5%AD%90; Hm_lvt_773f1a5aa45c642cf87eef671e4d3f6a=1434810401,1434811107,1434811114,1434871312; Hm_lpvt_773f1a5aa45c642cf87eef671e4d3f6a=1434876948'}
    req = urllib2.Request(url, headers=HEADERS)
    try:
        page1 = urllib2.urlopen(req)
    except:
        feedback = '<p style="font-family:Microsoft Yahei;font:24px">请检查您的网络连接</p>'
    if page1:
        text=page1.read()
        if "<p>"in text and "</p>"in text:
            text=text[text.index("<p>")+3:text.index("</p>")]
            while "<" in text and ">" in text :
                text=text[:text.index("<")]+text[text.index(">")+1:]
            feedback=text
            feedback=feedback.decode("utf-8").encode("gbk")
        else:
            feedback = '请检查您的网络连接</p>'
    else:
        feedback = '请检查您的网络连接</p>'
    return feedback

