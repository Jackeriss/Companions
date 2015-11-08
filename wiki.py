#!/usr/bin/env python
#-*- encoding: gbk -*-
import urllib,urllib2,requests,string,webbrowser,thread,time,Image
from delete_pic import *
def wiki(Key):
    feedback = None
    page1=None
    key=Key.decode('gbk').encode('utf8')
    url1='http://www.baike.com/wiki/'+key+'?prd=so_1_doc'
    try:
        page1 = urllib2.urlopen(url1)
    except:
        feedback = '<p style="font-family:Microsoft Yahei;font:24px">请检查您的网络连接</p>'
    if page1:
        url2=""
        text=page1.read()
        if "开放分类".decode('gbk').encode('utf8') in text and "编辑摘要".decode('gbk').encode('utf8') in text:
            text=text[text.index("开放分类".decode('gbk').encode('utf8')):text.index("编辑摘要".decode('gbk').encode('utf8'))]
            text1=text
            if "<p>".decode('gbk').encode('utf8') in text and "</p>".decode('gbk').encode('utf8') in text:
                text=text[text.index("<p>".decode('gbk').encode('utf8'))+3:text.index("</p>".decode('gbk').encode('utf8'),text.index("<p>".decode('gbk').encode('utf8')))]
            while "<".decode('gbk').encode('utf8') in text and ">".decode('gbk').encode('utf8') in text :
                text=text[:text.index("<".decode('gbk').encode('utf8'))]+text[text.index(">".decode('gbk').encode('utf8'))+1:]
            if text=="":
                if key in text1 and "。".decode('gbk').encode('utf8') in text1:
                    text1=text1[text1.index(key,text1.index(key)):text1.index("。".decode('gbk').encode('utf8'),text1.index(key))]
                    text1=text1+"。".decode('gbk').encode('utf8')
                    while key in text1[2:] and "。".decode('gbk').encode('utf8') in text1:
                        text1=text1[text1.index(key,text1.index(key)+2):text1.index("。".decode('gbk').encode('utf8'),text1.index(key))]
                        text1=text1+"。".decode('gbk').encode('utf8')
                    text=text1
            feedback = text.decode('utf8').encode('gbk')
            while "<" in feedback and ">" in feedback :
                feedback=feedback[:feedback.index("<")]+feedback[feedback.index(">")+1:]
            if "》" in feedback :
                if feedback[:len(Key)+2] == Key+"》":
                    feedback="《"+feedback
            url2='http://tupian.baike.com/doc/'+key+'/tctupian/1/0'
            page2=None
            try:
                page2 = urllib2.urlopen(url2)
            except:
                feedback = '<p style="font-family:Microsoft Yahei;font:24px">请检查您的网络连接</p>'
            if page2:
                url3=""
                url3=page2.read()
                if "imageUrl".decode('gbk').encode('utf8') in url3:
                    url3=url3[url3.index("imageUrl".decode('gbk').encode('utf8')):]
                    if "value".decode('gbk').encode('utf8') in url3 and ".jpg".decode('gbk').encode('utf8') in url3[:100]:
                        url3=url3[url3.index("value".decode('gbk').encode('utf8'))+7:url3.index(".jpg".decode('gbk').encode('utf8'))+4]
                    else:
                        url3=""
                else:
                    url3=""
                if url3:
                    page3=None
                    try:
                        page3 = urllib2.urlopen(url3)
                    except:
                        feedback = '<p style="font-family:Microsoft Yahei;font:24px">请检查您的网络连接</p>'
                    if page3:
                        file_name="cache/"+time.strftime("%Y%m%d%H%M%S", time.localtime())
                        # urllib.urlretrieve(url3, file_name+".jpg")
                        image_info=requests.get(url3)
                        with open(file_name+".jpg", "wb") as code:
                            code.write(image_info.content)
                            code.flush()
                            code.close()
                        im = Image.open(file_name+".jpg")
                        w, h = im.size
                        while w>360:
                            im.thumbnail((w//2, h//2))
                            w, h = im.size
                        im.save(file_name+'1.png')
                        thread.start_new_thread(delete_pic,(file_name,))
            if url3:
                feedback='<div align=center><img src="'+file_name+'1.png"/><p style="font-family:Microsoft Yahei;font:24px">'+Key+'</p></div><p style="font-family:Microsoft Yahei;font:15px">'+feedback+'</p>'
            else:
                feedback='<p style="font-family:Microsoft Yahei;font:15px">'+feedback+'</p>'
            if "互动百科" in feedback:
                feedback = None
        else:
            feedback = None
    return feedback
if __name__=='__main__':
    info=raw_input('我能为你做些什么？')
    print wiki(info)
