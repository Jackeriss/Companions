#!/usr/bin/env python
#-*- encoding: gbk -*-
import urllib2
def iciba(key):
    feedback = None
    page1=None
    url='http://dict.baidu.com/s?wd='+key
    try:
        page = urllib2.urlopen(url)
    except:
        feedback = '请检查您的网络连接'
    if page:
        text=page.read()
        if 'explain: "'in text:
            text=text[text.index('explain: "'.decode("gbk").encode("utf8"))+10:]
            text=text[:text.index('"')]
            if text:
                text="<br/>"+text
            text=text.replace(" ","").replace("\t","").replace("&nbsp;","").replace("\n","")
            feedback=text.decode("utf8").encode("gbk")
    return feedback
if __name__=='__main__':
    info=raw_input('我能为你做些什么？')
    print iciba(info)
