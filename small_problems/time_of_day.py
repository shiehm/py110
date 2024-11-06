"""
Problem: Represent integer representing minutes after or before midnight 
as times "hh:mm"

Requirements:
- The time loops (i.e. if 50 hours, then that's 2+ days ahead)

Input: int
Output: str in the form of "hh:mm"

Algorithm:
1. Use the sign to signify whether we go backwards or forwards
2. Calculate how many hours and minutes the integer represents
3. Get only the remainder of any 24 hour period (i.e. if +50 hrs, it's +2 hrs)
"""

HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
MINUTES_PER_DAY = MINUTES_PER_HOUR * HOURS_PER_DAY

def time_of_day(total_mins):
    days = abs(total_mins) // (HOURS_PER_DAY * MINUTES_PER_HOUR)
    hours = abs(total_mins) // MINUTES_PER_HOUR
    mins = abs(total_mins) % MINUTES_PER_HOUR
    if days > 1:
        hours = hours - (days * HOURS_PER_DAY)
    if total_mins < 0:
        return f'"{HOURS_PER_DAY - hours:02d}:{MINUTES_PER_HOUR - mins:02d}"'
    else:
        return f'"{hours:02d}:{mins:02d}"'

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True

"""
Problem: Write 2 functions that takes a string "hh:mm" and gives you the 
number of minutes before and the number of minutes after midnight. 

Input: String in the format "hh:mm"
Output: integer representing amount of minutes before or after midnight

Data Structure: 
- We have a 24 hour clock 
- 00:00 and 24:00 are the same time but represented differently 
- 24:00 as an input should show up as 0 as an output 
- Edge cases: 00:00 and 24:00 
- We can calculate the raw number of minutes first before dealing with outliers

Algorithm:
after_midnight:
1. Calculate the number of hours after midnight by stripping out the first 2 digits
    a. Multiply that by 60 to get number of minutes
2. Calculate the number of minutes by stripping out the last 2 digits as integers
3. Add 1a to 2 to get total number of minutes
    a. If the result is greater than or equal to 1440, subtrack 1440

before_midnight: 
1. Use the after midnight function
2. Subtrack that from 1440 

"""

HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
MINUTES_PER_DAY = MINUTES_PER_HOUR * HOURS_PER_DAY

def after_midnight(time):
    hours = int(time[:2]) 
    mins = int(time[-2:])
    
    total_mins = hours * MINUTES_PER_HOUR + mins
    
    if total_mins >= 1440:
        total_mins -= (total_mins // MINUTES_PER_DAY) * MINUTES_PER_DAY
    
    return total_mins

def before_midnight(time): 
    mins_after_midnight = after_midnight(time)
    return 0 if mins_after_midnight == 0 else MINUTES_PER_DAY - mins_after_midnight

# print(after_midnight("00:00"))
# print(before_midnight("00:00"))
# print(after_midnight("12:34"))
# print(before_midnight("12:34"))
# print(after_midnight("24:00"))
# print(before_midnight("24:00"))

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True