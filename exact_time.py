#!/usr/bin/env python
#-*- encoding: gbk -*-
import string
from shu2num import *
def translator(frm='',to='',delete='',keep=None):
    if len(to)==1:
        to=to*len(frm)
    trans=string.maketrans(frm,to)
    if keep is not None:
        allchars=string.maketrans('','')
        delete=allchars.translate(allchars,keep.translate(allchars,delete))
    def translate(s):
        return s.translate(trans,delete)
    return translate
digits_only=translator(keep=string.digits)
def exact_time(when):
    if ':' in when:
        _when=digits_only(when[:when.index(':')])
        when_=digits_only(when[when.index(':')+1:])
        if int(when_)>=60:
            _when=int(_when)+int(when_)/60
            when_=int(when_)%60
        if int(_when)>=24:
            exact_when='00:00'
        else:
            exact_when=str(_when)+':'+str(when_)
    elif '：' in when:
        _when=digits_only(when[:when.index('：')])
        when_=digits_only(when[when.index('：')+1:])
        exact_when=_when+':'+when_
    elif '点半' in when:
        if not digits_only(when[:when.index('点半')]):
            _when=str(shu2num(when[:when.index('点半')]))
        else:
            _when=digits_only(when[:when.index('点半')])
        exact_when=_when+':30'
    elif '点一刻' in when:
        if not digits_only(when[:when.index('点一刻')]):
            _when=str(shu2num(when[:when.index('点一刻')]))
        else:
            _when=digits_only(when[:when.index('点一刻')])
        exact_when=_when+':15'
    elif '点三刻' in when:
        if not digits_only(when[:when.index('点三刻')]):
            _when=str(shu2num(when[:when.index('点三刻')]))
        else:
            _when=digits_only(when[:when.index('点三刻')])
        exact_when=_when+':45'
    elif '点' in when:
        if not digits_only(when[:when.index('点')]):
            _when=str(shu2num(when[:when.index('点')]))
        else:
            _when=digits_only(when[:when.index('点')])
        if not when[when.index('点')+2:]:
            when_='00'
        else:
            if not digits_only(when[when.index('点')+2:]):
                when_=str(shu2num(when[when.index('点')+2:]))
            else:
                when_=digits_only(when[when.index('点')+2:])
        if int(when_)>=60:
            _when=int(_when)+int(when_)/60
            when_=int(when_)%60
        if int(_when)>=24:
            exact_when='00:00'
        else:
            exact_when=str(_when)+':'+str(when_)
    else:
        exact_when='00:00'
    return exact_when
