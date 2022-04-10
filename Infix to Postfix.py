
#Infix to postfix conversion

equation = input("Enter Infix Expression: ")
precedence = {"^":5, "/":4, "*":4, "+":3, "-":3, "(":2, ")":1}
postfix = ""
stack = []

print("Stack", "Postfix")
try:
    for i in equation:
        if i == " ":
            continue
        if i.isalpha():
            postfix += i
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
                        postfix += stack.pop()
                        if len(stack) == 0:
                            break
                    stack.append(i)
                elif precedence[i] == 2:
                    stack.append(i)
                elif precedence[i] == 1:
                    while "(" in stack:
                        out = stack.pop()
                        if out != "(":
                            postfix += out
                        else:
                            pass
            else:
                stack.append(i)
        print(stack, postfix)
    while len(stack) != 0:
        postfix += stack.pop()
except:
    print("Please Enter A valued infix expression")

print("\nPostfix Expression: ", postfix)
