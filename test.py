operator = input("Znak ")
a = int(input("A= "))
b = int(input("B= "))

if operator == "+":
    c = a + b
    print("otvet= ", c)
elif operator == "-":
    c = a - b
    print("otvet= ", c)
else:
    print("ERROR")

input()