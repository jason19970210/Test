try:
    n1 = int(input("first input: "))
    try:
        n2 = int(input("second input: "))
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
    except:
        print("second input is not int")
    
except:
    print("first input is not int")