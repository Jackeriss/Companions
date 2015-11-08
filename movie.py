#!/usr/bin/env python
#-*- encoding: gbk -*-
import urllib2,requests,string,webbrowser,time,thread,Image
from urllib2 import Request, urlopen
from delete_pic import *
def movie(Key):
    page1=None
    feedback = None
    point=None
    juqing=False
    key=Key.decode('gbk').encode('utf8')
    url1='http://movie.douban.com/subject_search?search_text='+Key+'&cat=1002'
    try:
        page1 = urllib2.urlopen(url1)
    except:
        feedback = '<p style="font-family:Microsoft Yahei;font:24px">请检查您的网络连接</p>'
    if page1:
        url2=page1.read()
        if "问答".decode('gbk').encode('utf8') in url2 and "评价".decode('gbk').encode('utf8') in url2:
            url2=url2[url2.index("问答".decode('gbk').encode('utf8')):url2.index("评价".decode('gbk').encode('utf8'))]
            if key in url2:
                url2=url2[:url2.index(key)]
                if 'nbg" href='.decode('gbk').encode('utf8') in url2 and "onclick".decode('gbk').encode('utf8') in url2:
                    url2=url2[url2.index('nbg" href='.decode('gbk').encode('utf8'))+11:url2.index("onclick".decode('gbk').encode('utf8'))-2]
                    url2=url2.decode('utf8').encode('gbk')
                    page2=None
                    try:
                        page2 = urllib2.urlopen(url2)
                    except:
                        feedback = '<p style="font-family:Microsoft Yahei;font:24px">请检查您的网络连接</p>'
                    if page2:
                        text=page2.read()
                        text2=text
                        if "<title>".decode('gbk').encode('utf8') in text and "</title>".decode('gbk').encode('utf8') in text:
                            title=text[text.index("<title>".decode('gbk').encode('utf8'))+7:text.index("</title>".decode('gbk').encode('utf8'))].replace(" (豆瓣)".decode('gbk').encode('utf8'),"")
                        if "问答".decode('gbk').encode('utf8') in text and "评价".decode('gbk').encode('utf8') in text:
                            text=text[text.index("问答".decode('gbk').encode('utf8')):text.index("评价".decode('gbk').encode('utf8'))]
                            if "点击看更多海报".decode('gbk').encode('utf8') in text:
                                url3=text[text.index("点击看更多海报".decode('gbk').encode('utf8')):text.index("点击看更多海报".decode('gbk').encode('utf8'),text.index("点击看更多海报".decode('gbk').encode('utf8'))+1)]
                                if "src=".decode('gbk').encode('utf8') in url3 and "title=".decode('gbk').encode('utf8') in url3:
                                    url3=url3[url3.index("src=".decode('gbk').encode('utf8'))+5:url3.index("title=".decode('gbk').encode('utf8'))-2]      
                            if "评价人数不足".decode('gbk').encode('utf8')in text:
                                point=None
                            elif "v:votes".decode('gbk').encode('utf8') in text:
                                votes=text[text.index("v:votes".decode('gbk').encode('utf8'))+9:-10]
                                if int(votes)<=10000:
                                    point=None
                                elif "v:average".decode('gbk').encode('utf8') in text and "</strong>".decode('gbk').encode('utf8') in text:
                                    point=text[text.index("v:average".decode('gbk').encode('utf8'))+11:text.index("</strong>".decode('gbk').encode('utf8'))]
                            if point:
                                if "导演".decode('gbk').encode('utf8') in text:
                                    if "IMDb".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("导演".decode('gbk').encode('utf8')):text.index("IMDb".decode('gbk').encode('utf8'))]
                                    elif "又名".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("导演".decode('gbk').encode('utf8')):text.index("又名".decode('gbk').encode('utf8'))]
                                    elif "片长".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("导演".decode('gbk').encode('utf8')):text.index("片长".decode('gbk').encode('utf8'))]
                                    elif "集数".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("导演".decode('gbk').encode('utf8')):text.index("集数".decode('gbk').encode('utf8'))]
                                    elif "首播".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("导演".decode('gbk').encode('utf8')):text.index("首播".decode('gbk').encode('utf8'))]
                                elif "编剧".decode('gbk').encode('utf8') in text:
                                    if "IMDb".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("编剧".decode('gbk').encode('utf8')):text.index("IMDb".decode('gbk').encode('utf8'))]
                                    elif "又名".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("编剧".decode('gbk').encode('utf8')):text.index("又名".decode('gbk').encode('utf8'))]
                                    elif "片长".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("编剧".decode('gbk').encode('utf8')):text.index("片长".decode('gbk').encode('utf8'))]
                                    elif "集数".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("编剧".decode('gbk').encode('utf8')):text.index("集数".decode('gbk').encode('utf8'))]
                                    elif "首播".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("编剧".decode('gbk').encode('utf8')):text.index("首播".decode('gbk').encode('utf8'))]
                                elif "主演".decode('gbk').encode('utf8') in text:
                                    if "IMDb".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("主演".decode('gbk').encode('utf8')):text.index("IMDb".decode('gbk').encode('utf8'))]
                                    elif "又名".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("主演".decode('gbk').encode('utf8')):text.index("又名".decode('gbk').encode('utf8'))]
                                    elif "片长".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("主演".decode('gbk').encode('utf8')):text.index("片长".decode('gbk').encode('utf8'))]
                                    elif "集数".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("主演".decode('gbk').encode('utf8')):text.index("集数".decode('gbk').encode('utf8'))]
                                    elif "首播".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("主演".decode('gbk').encode('utf8')):text.index("首播".decode('gbk').encode('utf8'))]
                                elif "类型".decode('gbk').encode('utf8') in text:
                                    if "IMDb".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("类型".decode('gbk').encode('utf8')):text.index("IMDb".decode('gbk').encode('utf8'))]
                                    elif "又名".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("类型".decode('gbk').encode('utf8')):text.index("又名".decode('gbk').encode('utf8'))]
                                    elif "片长".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("类型".decode('gbk').encode('utf8')):text.index("片长".decode('gbk').encode('utf8'))]
                                    elif "集数".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("类型".decode('gbk').encode('utf8')):text.index("集数".decode('gbk').encode('utf8'))]
                                    elif "首播".decode('gbk').encode('utf8') in text:
                                        text=text[text.index("类型".decode('gbk').encode('utf8')):text.index("首播".decode('gbk').encode('utf8'))]
                                if "剧情简介".decode('gbk').encode('utf8') in text2:
                                    if "&copy;豆瓣".decode('gbk').encode('utf8') in text2:
                                        juqing=True
                                        text2=text2[text2.index("剧情简介".decode('gbk').encode('utf8')):text2.index("&copy;豆瓣".decode('gbk').encode('utf8'))]
                                    else:
                                        if "的预告片和图片".decode('gbk').encode('utf8') in text2:
                                            juqing=True
                                            text2=text2[text2.index("剧情简介".decode('gbk').encode('utf8')):text2.index("的预告片和图片".decode('gbk').encode('utf8'))-len(key)]
                                        elif "的图片".decode('gbk').encode('utf8') in text2:
                                            juqing=True
                                            text2=text2[text2.index("剧情简介".decode('gbk').encode('utf8')):text2.index("的图片".decode('gbk').encode('utf8'))-len(key)]
                                        elif "的电视剧图片".decode('gbk').encode('utf8') in text2:
                                            juqing=True
                                            text2=text2[text2.index("剧情简介".decode('gbk').encode('utf8')):text2.index("的电视剧图片".decode('gbk').encode('utf8'))-len(key)]
                                if juqing:
                                    if "(展开全部)".decode('gbk').encode('utf8') in text2:
                                        text2="剧情简介:".decode('gbk').encode('utf8')+text2[text2.index("(展开全部)".decode('gbk').encode('utf8'))+14:]
                                
                                if juqing:
                                    text=text+text2
                                while "<".decode('gbk').encode('utf8') in text and ">".decode('gbk').encode('utf8') in text :
                                    text=text[:text.index("<".decode('gbk').encode('utf8'))]+text[text.index(">".decode('gbk').encode('utf8'))+1:]
                                text=text.replace(" ","").replace("&nbsp;".decode('gbk').encode('utf8'),"").replace("······".decode('gbk').encode('utf8'),":").replace("&copy;豆瓣".decode('gbk').encode('utf8'),"").replace("\n\n","\n").replace("\n\n","\n").replace("\n\n","\n").replace("\n\n","\n").replace("\n\n","\n").strip("\n").replace("\n","<br>")
                                text=text.decode('utf8').encode('gbk')
                                url3=url3.decode('utf8').encode('gbk')
                                title=title.decode('utf8').encode('gbk')
                                page3=None
                                try:
                                    page3 = urllib2.urlopen(url3)
                                except:
                                    feedback = '<p style="font-family:Microsoft Yahei;font:24px">请检查您的网络连接</p>'
                                if page3:
                                    file_name="cache/"+time.strftime("%Y%m%d%H%M%S", time.localtime())
                                    image_info=requests.get(url3)
                                    with open(file_name+".jpg", "wb") as code:
                                        code.write(image_info.content)
                                        code.flush()
                                        code.close()
                                    im=Image.open(file_name+".jpg")
                                    im.save(file_name+".png")
                                    thread.start_new_thread(delete_pic,(file_name,))
                                style_path_file=open("data/settings/style_path.txt","r")
                                style_path=style_path_file.read()
                                style_path_file.close()
                                href_file=open(style_path+"href.txt","r")
                                href=href_file.read()
                                href_file.close()
                                if point:
                                    feedback='<div align=center><p style="font-family:Microsoft Yahei;font:24px">'+title+'</p></div><br><img src="'+file_name+'.png" style="float:left"/><div align=right><span style="font-family:Microsoft Yahei;font:20px;color:#'+href+'">豆瓣评分：</span><span style="font-family:Microsoft Yahei;font:40px;color:#'+href+'">'+point+'</span></div><p style="font-family:Microsoft Yahei;font:15px">'+text+'<div align=right><a style="text-decoration:none;color:#'+href+'" href="'+url2+'">到豆瓣看</a></p></div><div align=left><a></a></div>'
                                else:
                                    feedback='<div align=center><p style="font-family:Microsoft Yahei;font:24px">'+title+'</p></div><br><img src="'+file_name+'.png" style="float:left"/><p style="font-family:Microsoft Yahei;font:15px">'+text+'<div align=right><a style="text-decoration:none;color:#'+href+'" href="'+url2+'">到豆瓣看</a></p></div><div align=left></div>'
    return feedback
if __name__=='__main__':
    info=raw_input('我能为你做些什么？')
    print movie(info)
