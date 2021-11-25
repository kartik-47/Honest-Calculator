# Kat's code
"""while True:

    calc = input("Enter an equation: ")

    x, oper, y = calc.split(' ')

    x = x.replace(".", "") if "." in x  else x
    y = y.replace(".", "") if "." in y  else y
    x = calc[0]
    oper = calc[2]
    y = calc[-1]
    
    check_float_x = isinstance(x, float)
    check_float_y = isinstance(y, float)

    if not x.isdigit() or not y.isdigit() or check_float_x==False or check_float_y==False:
        print("Do you even know what numbers are? Stay focused!")
        continue

    elif oper not in "+-*/":
        print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
        continue

    

    if oper == '+':
        result = int(x) + int(y)
        print(float(result))
        break
    elif oper == '-':
        result = int(x) - int(y)
        print(float(result))
        break
    elif oper == '*':
        result = int(x) * int(y)
        print(float(result))
        break
    elif oper == '/':
        if y == '0':
            print("Yeah... division by zero. Smart move...")
        else:
            result = int(x) / int(y)
            print(float(result))
            break
    else:
        break"""

# Kat's code
"""while True:

    calc = input("Enter an equation ")

    x, oper, y = calc.split(' ')

    x = x.replace(".", "") if "." in x  else x
    y = y.replace(".", "") if "." in y  else y 
    
    if not x.isdigit() or not y.isdigit():
        print("Do you even know what numbers are? Stay focused!")
        continue

    elif oper not in "+-*/":
        print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
        continue

    x = x.replace("", ".",0) if "" in x  else x
    y = y.replace("", ".",0) if "" in y  else y 

    if oper == '+':
        result = int(x) + int(y)
        print(float(result))
        break
    if oper == '-':
        result = int(x) - int(y)
        print(float(result))
        break
    if oper == '*':
        result = int(x) * int(y)
        print(float(result))
        break
    if oper == '/' and y != '0':
        result = int(x) / int(y)
        print(float(result))
        break
    else:
        print("Yeah... division by zero. Smart move...")
"""

# Someone's else + kat's(just a little part) code

memory = 0
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Do you want to store the result? (y / n):" 
msg_4 = "Do you want to continue calculations? (y / n):"
msg_5 = " ... lazy"
msg_6 = " ... very lazy"
msg_7 = " ... very, very lazy"
msg_8 = "You are"
msg_9 = "Are you sure? It is only one digit! (y / n)"
msg_10 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_11 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_index = [msg_9, msg_10, msg_11]
def is_one_digit(v):
    v = str(v)
    if ("0" + v.strip('-').rstrip('.0')).isdigit() and abs(int(float(v))) < 10:
        output = True
    else:
        output = False
    return output

def check(x, y, oper):
    
    msg = ""
    if is_one_digit(x) and is_one_digit(y):
        msg = msg + msg_5
    if (x == 1 or y == 2) and oper == '*':
        msg = msg + msg_6
    if (x == 0 or y == 0) and (oper == '*' or oper == '+' or oper == '-'):
        msg = msg + msg_7
    if msg != "":
        msg = msg_8 + msg
    print(msg)

while True:
    print(msg_0)
    x, oper, y = input().split()
    if x == 'M':
        x = str(memory)
    if y == 'M':
        y = str(memory)
    if (x.isdigit() or '.' in x) and (y.isdigit() or '.' in y):
        x = int(x) if x.isdigit() else float(x)
        y = int(y) if y.isdigit() else float(y)
    else:
        print(msg_1)
        continue
    if oper not in '+-*/':
        print(msg_2)
        continue

    check(x, y, oper)

    if oper == '+':
        result = x + y
        print(float(result))
    elif oper == '-':
        result = x - y
        print(float(result))
    elif oper == '*':
        result = x * y
        print(float(result))
    elif oper == '/' and (y != 0):
        result = x / y
        print(float(result))   
    else:
        print("Yeah... division by zero. Smart move...")
        continue
    loop_run = True
    while loop_run:
        response = input(msg_3)
        if response == 'y':
            if is_one_digit(result):
                index = 0
                while True:
                    print(msg_index[index])
                    response = input()
                    if response == 'y':
                        if index < 3:
                            index = index + 1
                            if index == 3:
                                memory = result
                                loop_run = False
                                break
                        else:
                            memory = result
                            loop_run = False
                            break
                    elif response == 'n':
                        loop_run = False
                        break
                    else:
                        continue
            else:
                memory = result
                break

        elif response == 'n':
            break
    response = input(msg_4)
    if response == 'y':
        continue
    if response == 'n':
        break

        