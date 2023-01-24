#Get the day by entering date

import calendar


DaysName = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
date = input()
spliteddate = date.split(" ")
year = int(spliteddate[2])
month = int(spliteddate[0])
day= int(spliteddate[1])

DayNumber = calendar.weekday(year, month, day)
print(DaysName[DayNumber])
    