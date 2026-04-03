num1 = float(input("Enter first number :"))
num2 = float(input("Enter second number : "))

operation = input("Enter a operation (+, -, *, /)")

if operation == "+":
    result = num1+num2

elif operation == "-":
    result = num1-num2

elif operation == "*":
    result = num1*num2

elif operation == "/":
    if num2 != 0:
        result = "erroe"
    result = num1/num2

else:
    result = "erroe"

print("result :" , result)