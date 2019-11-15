number = int(input())
val = number%100
if val > 10 and val < 20:
    print(number, u"программистов")
else:
    val = number%10
    if val == 1:
        print(number, u"программист")
    elif val > 1 and val < 5:
        print(number, u"программиста")
    else:
        print(number, u"программистов")
