#ask user what their speed is
spd = int(input('What is your current speed?: '))

#compare speed in an if else statement
if spd >= 24 and spd <= 56:
    #if speed is between 24 and 56 then speed is normal
    print('Speed is normal')

else:
    #if speed is outside 24 and 56 then speed is abnormal
    print('Speed is abnormal')
