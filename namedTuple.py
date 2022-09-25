# Dr. John Wesley has a spreadsheet containing a list of student's , ,  and .
# Your task is to help Dr. Wesley calculate the average marks of the students.
# Note:
# 1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
# 2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)

from collections import namedtuple

n = int(input())
TotalMarks = 0

for i in range(n+1):     
    if i == 0:
        s = " ".join(input().split())
        students = namedtuple('students',s)
    else:
        ID, MARKS, NAME, CLASS = input().split()
        spreadsheet = students(ID, MARKS, NAME, CLASS)
        TotalMarks += int(spreadsheet.MARKS)
    
print('%.2f' % (TotalMarks/n))