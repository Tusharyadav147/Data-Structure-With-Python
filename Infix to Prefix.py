
#Infix to postfix conversion

equation = input("Enter Infix Expression: ")
precedence = {"^":5, "/":4, "*":4, "+":3, "-":3, ")":2, "(":1}
prefix = ""
stack = []

print("Stack", "Prefix")
try:
    for i in equation[::-1]:
        if i == " ":
            continue
        if i.isalpha():
            prefix += i
        elif i.isnumeric():
            print("Infix Expression never contain an integer")
            break
        elif i.isspace():
            pass
        else:
            if len(stack) !=0:
                if precedence[i] > precedence[stack[len(stack)-1]] and precedence[i] != 1 and precedence[i] != 2:
                    stack.append(i)
                elif precedence[i] <= precedence[stack[len(stack)-1]] and precedence[i] != 1 and precedence[i] != 2:
                    while precedence[i] <= precedence[stack[len(stack)-1]]:
                        prefix += stack.pop()
                        if len(stack) == 0:
                            break
                    stack.append(i)
                elif precedence[i] == 2:
                    stack.append(i)
                elif precedence[i] == 1:
                    while ")" in stack:
                        out = stack.pop()
                        if out != ")":
                            prefix += out
                        else:
                            pass
            else:
                stack.append(i)
        print(stack, prefix)
    while len(stack) != 0:
        prefix += stack.pop()
except:
    print("Please Enter A valued infix expression")

print("\nPostfix Expression: ", prefix[::-1])
