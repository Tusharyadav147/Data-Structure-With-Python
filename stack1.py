#Program for stack all operations

from collections import deque

def num_oper(funct_num):
    switch = {1:"append", 2:"pop", 3:"empty", 4:"push", 5:'stackSize', 6:'peek', 7:'replace', 8:"appendleft"}
    return switch.get(funct_num)

def stack_type(type_num):
    if type_num == 1:
        stack = []
    elif type_num == 2:
        from collections import deque
        stack = deque()
    value = input("\nEnter some values in stack\n(Note:- Mention space between each value): ")
    for i in value.split(" "):
            stack.append(i)
    print("\nYour stack = ",stack)
    return stack

def operations(stack, func):
    if func == "append":
        num = int(input("\nEnter how many number of value you want to append: "))
        print("\n")
        for i in range(num):
            value1 = input("Enter value: ")
            stack.append(value1)
        print("\n",stack)
    elif func == "pop":
        num = int(input("\nEnter how many value you want to remove: "))
        for i in range(num):
            if len(stack) == 0:
                print("----Your stack is already empty----")
            else:
               print("Popped value = ",stack.pop())
    elif func == "empty":
        if len(stack) == 0:
            print("----Your stack is empty----")
        else:
            print("\nStack has {} number of element".format(len(stack)))
    elif func == 'push':
        value = input("\nEnter value to push it: ")
        stack.append(value)
        print(stack)
    elif func == 'stackSize':
        print("\n", stack)
        print("\nStackSize = ", len(stack))
    elif func == 'peek':
        if len(stack) == 0:
            print("----Your stack is empty----")
        else:
            print("\nIn stack top most elemnt is '{}'".format(stack[-1]))
    elif func == 'replace':
        print('\n', stack)
        value = input("\nSelect value to replace: ")
        value1 = input("Enter new value: ")
        for i in range(len(stack)):
            if stack[i] == value:
                stack[i] = value1
        print("\nAfter Replacement = ", stack)
    elif func == "appendleft":
        if type(stack) == deque:
            value = input("\nEnter value: ")
            stack.appendleft(value)
            print(stack)
        else:
            print("\nList type stack has no attribute 'appendleft'")

if __name__ == "__main__":
    type_num = int(input("\n\nSelect Which Type Of Stack Your want to use \n 1) List type \n 2) Deque type \n Select any of one('Enter 1 or 2'): "))
    stack = stack_type(type_num)

    cont = "yes"
    while cont.lower() == 'yes':

        funct_num = int(input("\n\nSelect any function:-\n 1) Append\n 2) Pop\n 3) Empty\n 4) Push\n 5) StackSize\n 6) Peek\n 7) Replace\n 8) Appendleft\n Select any of one('Enter number'): "))
        func= num_oper(funct_num)

        operations(stack, func)
        cont = input("\nFor more changes type 'yes' else type 'no': ")
    print("\n")
