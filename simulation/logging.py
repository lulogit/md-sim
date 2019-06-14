# -*- coding: utf-8 -*-
from .timing import as_clock

def emojify(s):
    return s.replace("PV_","🚴").replace("TV_","🚚").replace("MH_","🛅").replace("WHS", "🏭").replace("PC_","📦").replace("SUP_","🛒")

def render(log, emoji=False):
    from colorama import init, deinit, Fore, Back, Style
    init()
    styles = [Fore.WHITE+bg+"%s"+Style.RESET_ALL for bg in [Back.RED, Back.BLUE,Back.GREEN]]
    objs = list({by for _t,by,_m in log})
    block = {o:s for o,s in zip(objs, styles)}
    for (time,by,msg) in log:
        line = "[%s|%s] %s" % (block[by] % by, as_clock(time), msg)
        print(emojify(line) if emoji else line)
    deinit()


class StrLog:

    def __init__(self):
        self._log = []
    
    def log(self, time, by, msg):
        self._log.append((time,by,msg))

    def to_list(self):
        return self._log

#def __log__(self, pre=None,post=None):
#        'experimental feature, not to use'
#        def get_wrapper(func):
#            @wraps(func)
#            def wrapper(*args, **kwargs):
#                # This is the actual wrapper
#                # Call "pre" callback
#                if pre:
#                    #print("[%s|%s] %s" % (by,as_clock(time),msg))
#                    self._log.append(pre(*args))
#
#                # Perform actual operation
#                ret = func(*args, **kwargs)
#
#                # Call "post" callback
#                if post:
#                    #print("[%s|%s] %s" % (by,as_clock(time),msg))
#                    self._log.append(post(*args))
#
#                return ret
#            return wrapper
#        return get_wrapper
