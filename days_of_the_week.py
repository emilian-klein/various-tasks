"""
Task:
    Implement a class called Weeker. This name comes from the fact that objects of that class will be able to store and
    to manipulate the days of the week. The class constructor accepts one argument – a string. The string represents the
    name of the day of the week and the only acceptable values must come from the following set:
    - Mon Tue Wed Thu Fri Sat Sun.
    Invoking the constructor with an argument from outside this set should raise the WeekDayError exception.
    The class should provide the following facilities:
    - objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings
      of the same form as the constructor arguments,
    - the class should be equipped with one-parameter methods called add_days(n) and subtract_days(n), with n being an
      integer number and updating the day of week stored inside the object in the way reflecting the change of date by
      the indicated number of days, forward or backward,
    - all object's properties should be private.
"""


class WeekDayError(Exception):
    pass


class Weeker:
    __names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def __init__(self, day):
        try:
            self.__current = Weeker.__names.index(day)
        except ValueError:
            raise WeekDayError

    def __str__(self):
        return Weeker.__names[self.__current]

    def add_days(self, n):
        self.__current = (self.__current + n) % 7

    def subtract_days(self, n):
        self.__current = (self.__current - n) % 7


if __name__ == "__main__":
    try:
        weekday = Weeker("Mon")
        print(weekday)
        weekday.add_days(1)
        print(weekday)
        weekday.subtract_days(23)
        print(weekday)
        weekday = Weeker("Monday")
    except WeekDayError:
        print("Sorry, I can't serve your request.")