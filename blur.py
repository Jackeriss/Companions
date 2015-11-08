#!/usr/bin/env python
#-*- encoding: gbk -*-
import string,random

def blur(key,question):
    feedback = None
    re_good=['谢谢夸奖！','嗯，其实我也没那么厉害了啦……','别夸我了，人家都不好意思了*^_^*']
    re_bad=['不许你说我坏话！','你再这样我生气了！','(╥﹏╥)呜……']
    ni_keyi=['不可以，绝对不行！','我不同意！']
    ni_neng=['怎么可能？！','我？你在开玩笑吧？','我不这么觉得……']
    ni_hui=['^_^|||不会……','我倒是想啊……','你教教我呗！']
    ni_xihuan=['一点都不喜欢……','这个嘛，我还是很喜欢的！','我怎么可能不喜欢？']
    ni_ai=['累觉不爱……','很爱，很爱！','爱！！！']
    ni_hen=['一点也不恨']
    ni_shi=['当然不是！','我怎么可能是……','你觉得我像吗？']
    ni_you=['对不起……没有……','有也不告诉你！','你觉得我会有那玩意儿吗？']
    ni_xiang=['当然想了！','做梦都在想呢！','']
    ni_unknown=['你猜啊！','这是个秘密！','你怎么什么都问啊！','这个真不知道','你知道的太多了！','这还用问吗？','你不是最了解人家了吗在？怎么会不知道？']
    if key[:2]=='你':
        good_time=bad_time=0
        good_file=open("data/db/good.txt","r")
        over=False
        while not over:
            good_info=good_file.readline().strip('\n')
            if good_info=='':
                over=True
            elif good_info in key:
                good_time_file=open("data/db/good_time.txt","r")
                good_time=int(good_time_file.readline().strip('\n'))
                feedback=re_good[good_time%len(re_good)]
                good_time+=1
                good_time_file.close
                good_time_file=open("data/db/good_time.txt","w")
                good_time_file.write('%d'%good_time)
                good_time_file.close
                over=True
        good_file.close
        if not feedback:
            bad_file=open("data/db/bad.txt","r")
            over=False
            while not over:
                bad_info=bad_file.readline().strip('\n')
                if bad_info=='':
                    over=True
                elif bad_info in key:
                    bad_time_file=open("data/db/bad_time.txt","r")
                    bad_time=int(bad_time_file.readline().strip('\n'))
                    feedback=re_bad[bad_time%len(re_bad)]
                    bad_time+=1
                    bad_time_file.close
                    bad_time_file=open("data/db/bad_time.txt","w")
                    bad_time_file.write('%d'%bad_time)
                    bad_time_file.close
                    over=True
            bad_file.close
        if not feedback:
            if key[-2:]=='吗' or key[-2:]=='么' or question==True:
                if key[-4:]=='是吗' or key[-4:]=='是么' :
                    if key[-6:]=='不是吗' or key[-6:]=='不是么' :
                        feedback ='是是是！当然！'
                    else:
                        feedback ='那可未必！'
                else:
                    if '可以' in key:
                        feedback = random.choice(ni_keyi)
                    elif '能' in key:
                        feedback = random.choice(ni_neng)
                    elif '会' in key:
                        feedback = random.choice(ni_hui)
                    elif '喜欢' in key:
                        feedback = random.choice(ni_xihuan)
                    elif '爱' in key:
                        feedback = random.choice(ni_ai)
                    elif '恨' in key:
                        feedback = random.choice(ni_hen)
                    elif '是' in key:
                        feedback = random.choice(ni_shi)
                    elif '有' in key:
                        feedback = random.choice(ni_you)
                    elif '想' in key:
                        feedback = random.choice(ni_xiang)
                    else:
                        feedback = random.choice(ni_unknown)
    elif key[:2]=='我':
        wo_keyi=['没门！','做梦吧你！','想都别想！']
        wo_neng=['如果你特别想这么做的话……','','']
        wo_shi=['欧巴别这么说自己！','我只能说，你和你想象的不一样……']
        wo_you=['你有没有我怎么知道……','','']
        wo_unknown=['']
        if key[-2:]=='吗' or key[-2:]=='么' or question==True:
            if key[-4:]=='是吗' or key[-4:]=='是么' :
                if key[-6:]=='不是吗' or key[-6:]=='不是么' :
                    feedback ='是是是！当然！'
                else:
                    feedback ='那可未必！'
            else:
                if '可以' in key:
                    feedback = random.choice(wo_keyi)
                elif '能' in key:
                    feedback = random.choice(wo_neng)
                elif '是' in key:
                    feedback = random.choice(wo_shi)
                elif '有' in key:
                    feedback = random.choice(wo_you)
                else:
                    feedback = random.choice(wo_unknown)
        if '可以不可以' in key:
            feedback = random.choice(wo_keyi)
        elif '能不能' in key:
            feedback = random.choice(wo_neng)
        elif '是不是' in key:
            feedback = random.choice(wo_shi)
        elif '有没有' in key:
            feedback = random.choice(wo_you)
    if '可以不可以' in key:
        feedback = random.choice(ni_keyi)
    elif '能不能' in key:
        feedback = random.choice(ni_neng)
    elif '会不会' in key:
        feedback = random.choice(ni_hui)
    elif '喜欢不喜欢' in key:
        feedback = random.choice(ni_xihuan)
    elif '爱不爱' in key:
        feedback = random.choice(ni_ai)
    elif '恨不恨' in key:
        feedback = random.choice(ni_hen)
    elif '是不是' in key:
        feedback = random.choice(ni_shi)
    elif '有没有' in key:
        feedback = random.choice(ni_you)
    elif '想不想' in key:
        feedback = random.choice(ni_xiang)
    return feedback
if __name__=='__main__':
    info=raw_input('我能为你做些什么？')
    print blur(info)
