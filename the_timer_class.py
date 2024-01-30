"""
    Program implements class which will be called Timer. Its constructor accepts three arguments representing hours
    (a value from range [0..23]), minutes (from range [0..59]) and seconds (from range [0..59]). Zero is the default
    value for all of the above parameters. The class itself provides the following facilities:
    - objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings
    - the class is equipped with parameterless methods called next_second() and previous_second(),
      incrementing the time stored inside objects by +1/-1 second respectively.
"""

class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return f"{format_time(self.__hours)}:{format_time(self.__minutes)}:{format_time(self.__seconds)}"

    def next_second(self):
        self.__seconds += 1
        if self.__seconds > 59:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes > 59:
                self.__minutes = 0
                self.__hours += 1
                if self.__hours > 23:
                    self.__hours = 0

    def prev_second(self):
        self.__seconds -= 1
        if self.__seconds < 0:
            self.__seconds = 59
            self.__minutes -= 1
            if self.__minutes < 0:
                self.__minutes = 59
                self.__hours -= 1
                if self.__hours < 0:
                    self.__hours = 23

def format_time(time_part):
    time_part = str(time_part)
    if len(time_part) == 1:
        time_part = '0' + time_part
    return time_part

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
timer.next_second()
print(timer)
timer.next_second()
print(timer)
