figure = str(input())
if figure == "треугольник":
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a+b+c)/2
    print((p*(p-a)*(p-b)*(p-c))**0.5)
elif figure == "прямоугольник":
    a = float(input())
    b = float(input())
    print(a * b)
elif figure == "круг":
    r = float(input())
    print(3.14*(r**2))
