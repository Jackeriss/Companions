#!/usr/bin/env python
#-*- encoding: gbk -*-
import string,os,thread,math
from shell import shell
from shell import shellcon
windows_path = shell.SHGetPathFromIDList(shell.SHGetSpecialFolderLocation(0,shellcon.CSIDL_WINDOWS))
operator=['+','-','*','/','^','!','加','减','乘','除','次方','平方','立方','根号','阶乘','次幂','的正弦','的余弦','的正切','的余切','sin','cos','tan','cot','ln']
number=['0','1','2','3','4','5','6','7','8','9']
##def translator(frm='',to='',delete='',keep=None):
##    if len(to)==1:
##        to=to*len(frm)
##    trans=string.maketrans(frm,to)
##    if keep is not None:
##        allchars=string.maketrans('','')
##        delete=allchars.translate(allchars,keep.trancelate(allchars,delete))
##    def translate(s):
##        return s.translate(trans,delete)
##    return translate
def calc(a):
    feedback=None
    digits=['0','1','2','3','4','5','6','7','8','9','.']
    n_op=0
    NaN=False
    num1_id=None
    num2_id=None
    op_id=None
    end_id=None
    num1=None
    num2=None
    b=None
    length=len(a)
    for i in range(0,length):
        for j in range(0,len(number)):
            if number[j] == a[i]:
                num1_id=i
                break
        if num1_id != None:

            break
    for i in range(num1_id,length):
        digit=False
        for j in range(0,len(digits)):
            if digits[j] == a[i]:
                digit=True
                break
        if not digit:

            op_id=i
            break
    if op_id == None:
        op_id=length
    for i in range(op_id,length):
        for j in range(0,len(number)):
            if number[j] == a[i]:
                num2_id=i
    
                break
        if num2_id != None:

            break
    if num2_id != None:
        for i in range(num2_id,length):
            digit=False
            for j in range(0,len(digits)):
                if digits[j] == a[i]:
                    digit=True
        
                    break
            if not digit:
                end_id=i
    
                break
        if end_id == None:

            end_id=length
    if num1_id != None:
        num1=float(a[num1_id:op_id])
    if num2_id != None:
        num2=float(a[num2_id:end_id])
    if num1_id != None and num2_id != None:
        if '+' in a or '加' in a or '加上' in a:
            try:
                b=num1+num2
            except:
                NaN=True
                feedback = '这数字实在太大了，我也无能为力……'
            n_op+=1     
        if '-' in a or '减' in a or '减去' in a:
            try:
                b=num1-num2
            except:
                NaN=True
                feedback = '这数字实在太大了，我也无能为力……'
            n_op+=1
        if '*' in a or '乘' in a or '乘以' in a:
            try:
                b=num1*num2
            except:
                NaN=True
                feedback = '这数字实在太大了，我也无能为力……'
            n_op+=1
        if '/' in a or '除以' in a:
            if num2==0:
                feedback = '"0"不能作除数哦，你小学数学是看门的大爷教的吧？'
                NaN=True
            else:
                if "余" in a:
                    try:
                        b=num1%num2
                    except:
                        NaN=True
                        feedback = '这数字实在太大了，我也无能为力……'
                    n_op+=1
                else:
                    try:
                        b=num1/num2
                    except:
                        NaN=True
                        feedback = '这数字实在太大了，我也无能为力……'
                    n_op+=1
        elif '除' in a:
            if num1==0:
                feedback = '"0"不能作除数哦，你小学数学是看门的大爷教的吧？'
                NaN=True
            else:
                if "余" in a:
                    try:
                        b=num2%num1
                    except:
                        NaN=True
                        feedback = '这数字实在太大了，我也无能为力……'
                    n_op+=1
                else:
                    try:
                        b=num2/num1
                    except:
                        NaN=True
                        feedback = '这数字实在太大了，我也无能为力……'
                    n_op+=1
        if "次根号" in a:
            if num1==0:
                feedback = '根号下面的数字要大于等于0哦，你初中数学是教导主任教的吧？'
                NaN=True
            else:
                try:
                    b=num2**(1.0/num1)
                except:
                    NaN=True
                    feedback = '这数字实在太大了，我也无能为力……'
                n_op+=1
        if ("开" in a and "次方" in a) or ("的" in a and "次方根" in a):
            if num1==0:
                feedback = '根号下面的数字要大于等于0哦，你初中数学是教导主任教的吧？'
                NaN=True
            else:
                try:
                    b=num1**(1.0/num2)
                except:
                    NaN=True
                    feedback = '这数字实在太大了，我也无能为力……'
                n_op+=1
        elif "^" in a or ("的" in a and "次方" in a) or ("的" in a and "次幂" in a):
            try:
                b=num1**num2
            except:
                NaN=True
                feedback = '这数字实在太大了，我也无能为力……'
            n_op+=1
    elif num1_id != None:
        if "阶乘" in a or "!" in a:
            try:
                b=float(math.factorial(int(num1)))
            except:
                NaN=True
                feedback = '这数字实在太大了，我也无能为力……'
            n_op+=1
        if 'sin' in a or "正弦" in a:
            try:
                b=math.sin(num1)
            except:
                NaN=True
                feedback = '你给的这个数字不在sin函数的定义域内……'
            n_op+=1
        if 'cos' in a or "余弦" in a:
            try:
                b=math.cos(num1)
            except:
                NaN=True
                feedback = '你给的这个数字不在cos函数的定义域内……'
            n_op+=1
        if 'tan' in a or "正切" in a:
            try:
                b=math.tan(num1)
            except:
                NaN=True
                feedback = '你给的这个数字不在tan函数的定义域内……'
            n_op+=1
        if 'cot' in a or "余切" in a:
            try:
                b=math.tan(num1)
                if b == 0:
                    NaN=True
                    feedback='你给的这个数字不在cot函数的定义域内……'
                else:
                    b=1.0/b
            except:
                b=0
            n_op+=1
        if 'ln' in a:
            try:
                b=math.log1p(num1-1)
            except:
                NaN=True
                feedback = '你给的这个数字不在ln函数的定义域内……'
            n_op+=1
        if '平方根' in a or '根号' in a:
            try:
                b=num1**(1.0/2)
            except:
                NaN=True
                feedback = '这数字实在太大了，我也无能为力……'
            n_op+=1
        if '立方根' in a:
            try:
                b=num1**(1.0/3)
            except:
                NaN=True
                feedback = '这数字实在太大了，我也无能为力……'
            n_op+=1
        if '平方' in a:
            try:
                b=num1**2
            except:
                NaN=True
                feedback = '这数字实在太大了，我也无能为力……'
            n_op+=1
        if '立方' in a:
            try:
                b=num1**3
            except:
                NaN=True
                feedback = '这数字实在太大了，我也无能为力……'
            n_op+=1

    if n_op >= 2:
        thread.start_new_thread(os.system,("calc",))
        feedback = '我去，这么复杂！你还是用计算器自己算吧！'
    else:
        if b != None and not NaN:
            too_big=False
            if b > 10000000000000000:
                too_big=True
                feedback = "运算结果太大了，不好显示……"       
            c='%.2f'%b
            if '.00' in c:
                c=c[:-3]
            if not too_big:
                feedback = c
        elif not NaN:

            thread.start_new_thread(os.system,("calc",))
            feedback = '我去，这么复杂！你还是用计算器自己算吧！'
    return feedback
if __name__=='__main__':
    op=False
    nu=False
    info=raw_input('我能为你做些什么？')
    for i in range(0,12):
        if operator[i] in info:
            op=True
    for i in range(0,10):
        if number[i] in info:
            nu=True
    if op==True and nu==True:
        calc(info)
        
