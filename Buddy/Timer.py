import calendar
import time


class Time(object):
    def __init__(self):
        self.current = None

    @ staticmethod
    def actual():
        return calendar.timegm(time.gmtime())

    @ staticmethod
    def date_time_format(epoch):
        return time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(epoch))
