from .timing import as_clock

def render(log):
    from colorama import init, deinit, Fore, Back, Style
    init()
    styles = [Fore.WHITE+bg+"%s"+Style.RESET_ALL for bg in [Back.RED, Back.BLUE]]
    objs = list({by for _t,by,_m in log})
    block = {o:s for o,s in zip(objs, styles)}
    for (time,by,msg) in log:
        print("[%s|%s] %s" % (block[by] % by, as_clock(time), msg))
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
