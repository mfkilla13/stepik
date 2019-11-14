a = float(input())
b = float(input())
op = str(input())
if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/' and b == 0:
    print("0!")
elif op == '/' and b != 0:
    print(a / b)
elif op == 'mod' and b == 0:
    print('0!')
elif op == 'mod' and b != 0:
    print(a % b)
elif op == 'pow':
    print(a ** b)
elif op == 'div' and b == 0:
    print('0!')
elif op == 'div' and b != 0:
    print(a // b)
