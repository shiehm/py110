"""
Problem: Given a year yyyy, find how many 13ths fall on a Friday

Input: Year in strings
Output: Integer for how many Friday the 13ths there are 

Notes:
- Use the datetime module 

Algorithm:
- Create a datetime list of all 13ths from Jan-Dec datetime(yyyy, mm, 13)
- Find the weekdays of these dates using weekday method from datetime module
- Count the number of fridays (Note: 4 = Friday because Monday is 0)

"""
import datetime as dt

def friday_the_13ths(year):
    thirteenths = [dt.date(year, month, 13) for month in range(1, 13)] 
    weekdays = [date.weekday() for date in thirteenths]
    return weekdays.count(4)
    
print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True