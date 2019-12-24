# Define
def calculate(op, num1, num2):
    num1 = int(num1) #change type from str to int
    num2 = int(num2)
    return{
        op == "+" : num1 + num2,
        op == "-" : num1 - num2,
        op == "*" : num1 * num2,
        op == "/" : num1 / num2,
    }

n1 = input("Input first int: ")
if n1.isdigit():
    #print(n1)
    n2 = input("Input second int: ")
    if n2.isdigit(): #yes case
        op = input("Input the operator: ")
        if calculate(op, n1, n2).get(True) == None:
            print("Error with unknown operator")
        else:
            print(calculate(op, n1, n2).get(True))
    else:
        print("second number is not an int!")
else:
    print("first number is not an int!")