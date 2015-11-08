#!/usr/bin/env python
#-*- encoding: gbk -*-
import urllib2
def zhidao(Key):
    feedback = None
    page1=None
    key=Key.decode('gbk').encode('utf8')
    url1='http://zhidao.baidu.com/search?word='+key
    try:
        page1 = urllib2.urlopen(url1)
    except:
        feedback = '请检查您的网络连接'
    if page1:
        text=page1.read()
        if "推荐答案"in text and "</dd>"in text:
            text=text[text.index("推荐答案")+8:text.index("</dd>")]
            while "<" in text and ">" in text :
                text=text[:text.index("<")]+text[text.index(">")+1:]
            if "[详细]" in text:
                text=text[:text.index("[详细]")]
            text1=text
            if text1[-3:-2]==".":
                shenglue=False
                while "。" in text1:
                    shenglue=True
                    text1=text1[text1.index("。")+2:]
                if shenglue:
                    if text1 in text:
                        text=text[:text.index(text1)]
            feedback=text
    return feedback
if __name__=='__main__':
    info=raw_input('我能为你做些什么？')
    print zhidao(info)
