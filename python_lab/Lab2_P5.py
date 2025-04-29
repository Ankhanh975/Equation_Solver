a = input()
a = True if a == "True" else False

b = input()
b = True if b == "True" else False

c = input()
c = True if c == "True" else False

print(f"{not a} {a and b} {a or b} {a and (b or c)}")