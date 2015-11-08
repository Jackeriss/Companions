#!/usr/bin/env python
#-*- encoding: gbk -*-
import cookielib,urllib2,requests,string,webbrowser,thread,time,Image
from delete_pic import *
def neihan():
    feedback = None
    page1=None
    url='http://neihanshequ.com/pic'
    HEADERS = {"cookie":'uuid="w:d132301db48c4c8184be1d188c296f9b"; tt_webid=4370653838; __utmt=1; __utma=101886750.501576781.1434802321.1434875802.1434885355.5; __utmb=101886750.1.10.1434885355; __utmc=101886750; __utmz=101886750.1434871312.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E5%86%85%E6%B6%B5%E6%AE%B5%E5%AD%90; csrftoken=e6e30ca5623bce575755fad47ddb029d; Hm_lvt_773f1a5aa45c642cf87eef671e4d3f6a=1434810401,1434811107,1434811114,1434871312; Hm_lpvt_773f1a5aa45c642cf87eef671e4d3f6a=1434885357'}
    req = urllib2.Request(url, headers=HEADERS)
    try:
        page1 = urllib2.urlopen(req)
    except:
       feedback = '<p style="font-family:Microsoft Yahei;font:24px">请检查您的网络连接</p>'
    if page1:
        text=page1.read()
        if "<p>"in text and "</p>"in text:
            pic=text[text.index("</p>")+4:]
            text=text[text.index("<p>")+3:text.index("</p>")]
            while "<" in text and ">" in text :
                text=text[:text.index("<")]+text[text.index(">")+1:]
            text=text.decode("utf-8").encode("gbk")
            if "data-src" in pic:
                pic=pic[pic.index("data-src")+10:]
                pic=pic[:pic.index('"')]
            if pic:
                file_name="cache/"+time.strftime("%Y%m%d%H%M%S", time.localtime())
                image_info=requests.get(pic)
                with open(file_name+".jpg", "wb") as code:
                    code.write(image_info.content)
                    code.flush()
                    code.close()
                im = Image.open(file_name+".jpg")
                im = im.convert('RGB')
                w, h = im.size
                while w>360:
                    im.thumbnail((w//2, h//2))
                    w, h = im.size
                im.save(file_name+".png")
                thread.start_new_thread(delete_pic,(file_name,))
            feedback='<p style="font-family:Microsoft Yahei;font:24px">'+text+'</p><div align=center><img src="'+file_name+'.png"/></div>'
        else:
            feedback = '<p style="font-family:Microsoft Yahei;font:24px">请检查您的网络连接</p>'
    else:
        feedback = '<p style="font-family:Microsoft Yahei;font:24px">请检查您的网络连接</p>'
    return feedback
