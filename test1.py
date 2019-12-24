n1 = input("first input: ")
if n1.isdigit():
    n1 = int(n1)
    n2 = input("second input: ")
    if n2.isdigit():
        n2 = int(n2)
        op = input("operator: ")
        if op == '+':
            print(n1 + n2)
        elif op == '-':
            print(n1 - n2)
        elif op == '*':
            print(n1 * n2)
        elif op == '/':
            try:
                print(n1 / n2)
            except ZeroDivisionError:
                print("ZeroDivisionError")
        else:
            print('unknown operator')
    else:
        print("second input is not int")
else:
    print("first input is not int")