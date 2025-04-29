expression = input()
expression = expression.split(" ")

a = int(expression[0])
b = expression[1]
c = int(expression[2])

if b == "+":
    print(a + c)
elif b == "-":
    print(a - c)
elif b == "*":
    print(a * c)
elif b == "/":
    print(a / c)