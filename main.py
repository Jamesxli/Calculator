num1 = float(input("Enter first number: "))
op = input("Enter an operator (type + - /  or *) ")
num2 = float(input("Enter second number: "))

if op == "+":
  print(num1 + num2)
elif op == "-":
  print(num1 - num2)
elif op == "/":
  print(num1 / num2)
elif op == "*":
  print(num1 * num2)
else:
    print("invalid operator, must type \" +, - * or /\" ")
