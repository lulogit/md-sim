from .timing import as_clock

class StrLog(list):

    def log(self, time, by, msg):
        print("[%s|%s] %s" % (by,as_clock(time),msg))
        self.append((time,by,msg))

    def to_list(self):
        return self
