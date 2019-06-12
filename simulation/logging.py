
class StrLog(list):

    def log(self, msg):
        self.append(msg)

    def to_list(self):
        return self
