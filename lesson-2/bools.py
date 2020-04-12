a = True # the day is sunny
b = True # the day is warm
c = False # the year is 1980

if (a and b):
    print("the day is sunny and warm!")

if (a and c):
    print("the day is sunny and the year is 1980!")

if (a or c):
    print("the day is sunny or its 1980!")

if (a and not c):
    print("the day is sunny and its not 1980!")
