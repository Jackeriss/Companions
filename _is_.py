#!/usr/bin/env python
#-*- encoding: gbk -*-
def _is_(key):
    feedback=None
    _is_file=open("cache/_is_.txt","r")
    while 1:
        _is_info=_is_file.readline().strip('\n')
        if not _is_info:
            break
        _is=_is_info[:_is_info.index('是')]
        is_=_is_info[_is_info.index('是')+2:]
        if key == _is :
            for i in range(0,len(_is_info)/2,2):
                if _is_info[i:i+2]=='我':
                    _is_info=_is_info[0:i]+'你'+_is_info[i+2:]
                elif _is_info[i:i+2]=='你':
                    _is_info=_is_info[0:i]+'我'+_is_info[i+2:]
            feedback = _is_info
            break
        elif key == is_:
            for i in range(0,len(_is)/2,2):
                if _is[i:i+2]=='我':
                    _is=_is[0:i]+'你'+_is[i+2:]
                elif _is[i:i+2]=='你':
                    _is=_is[0:i]+'我'+_is[i+2:]
            feedback = _is
            break
    _is_file.close
    return feedback
if __name__=='__main__':
    info=raw_input('我能为你做些什么？')
    if info[:4]=='啥是' or info[:6]=='什么是' or info[:4]=='谁是':
        info=info[info.index('是')+1:]
        _is_(info)
    elif info[-4:]=='是啥' or info[-6:]=='是什么' or info[-4:]=='是谁':
        info=info[:info.index('是')]
        _is_(info)
