def dms(num):
    DEGREE = "\u00B0"
    degs = int(num // 1)
    decimal_mins = divmod(num, 1)[1]
    mins = int((decimal_mins * 60) // 1)
    decimal_secs = divmod(decimal_mins * 60, 1)[1]
    secs = int(decimal_secs * 60)
    return f'{degs:01.0f}{DEGREE}{mins:02.0f}\'{secs:02.0f}\"'

print(dms(30))
print(dms(76.73))
print(dms(254.6))
print(dms(93.034773))
print(dms(0))
print(dms(360))

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

print(dms(-1))   # -1°00'00"
print(dms(400))  # 400°00'00"
print(dms(-40))  # -40°00'00"
print(dms(-420)) # -420°00'00"

"""
Modify it such that it shows up to 360 and then continues forward 
(or back if negative) to the next (or prior) 360. 

Algortithm, incorporating existing dms function:
1. for positive numbers, take the remainder of division by 360 into dms()
2. for negative numbers, take the remainder of division by -360, 
subtract from 360 and put into dms()
"""

def dms_360(num):
    if num >= 0:
        new_num = divmod(num, 360)[1]
    else:
        new_num = 360 + divmod(num, -360)[1]
    return dms(new_num)

print(dms_360(-1))   # 359°00'00"
print(dms_360(400))  # 40°00'00"
print(dms_360(-40))  # 320°00'00"
print(dms_360(-420)) # 300°00'00"