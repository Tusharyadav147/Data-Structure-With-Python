class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class stack:
    def __init__(self):
        self.start = None
    def isempty(self):
        if self.start == None:
            return True
        else:
            return False  
    def push(self,data):
        if self.start==None:
            self.start=Node(data)
        else:
            newnode=Node(data)
            newnode.next=self.start
            self.start=newnode
    def pop(self):
        if self.isempty():
            print("stack is already empty")
        else:
            popnode=self.start
            self.start=self.start.next
            popnode.next=None
    def print(self):
        temp=self.start
        if self.isempty():
            print("stack is underflow")
        else:
            while(temp!= None):
                print(temp.data,end=",")
                temp=temp.next
            print("\n")
    def count(self):
        temp = self.start
        count = 0
        while temp is not None:
            temp = temp.next
            count = count + 1
        return count

class queue:
    def __init__(self):
        self.start = None
    def isempty(self):
        if self.start == None:
            return True
        else:
            return False  
    def enqueue(self,data):
        if self.start==None:
            self.start=Node(data)
        else:
            newnode=Node(data)
            newnode.next=self.start
            self.start=newnode
    def dequeue(self):
        if self.isempty():
            print("Queue is already empty")
        else:
            temp=self.start
            while temp.next.next is not None:
                temp =temp.next
            temp.next=None
    def print(self):
        temp=self.start
        if self.isempty():
            print("queue is underflow")
        else:
            while(temp!= None):
                print(temp.data,end=",")
                temp=temp.next
            print("\n")
    def count(self):
        temp = self.start
        count = 0
        while temp is not None:
            temp = temp.next
            count = count + 1
        return count


def function():
    value = int(input("\nSelect which operation your want to perform (1 to 8) \n 1) push()\n 2) pop()\n 3) print()\n 4) isempty()\nSelect one: "))
    return value
def perform(operation):
    if operation == 1:
        value = input("\nEnter value to Push: ")
        mystack.push(value)
        mystack.print()
    elif operation == 2:
        mystack.print()
        mystack.pop()
        mystack.print()
    elif operation == 3:
        mystack.print()
    elif operation == 4:
        print(mystack.isempty())

def function1():
    value = int(input("\nSelect which operation your want to perform (1 to 8) \n 1) enqueue()\n 2) dequeue()\n 3) print()\n 4) isempty()\n 5) count()\nSelect one: "))
    return value
def perform1(operation):
    if operation == 1:
        value = input("\nEnter value to Push: ")
        myqueue.enqueue(value)
        myqueue.print()
    elif operation == 2:
        myqueue.print()
        myqueue.dequeue()
        myqueue.print()
    elif operation == 3:
        myqueue.print()
    elif operation == 4:
        print(myqueue.isempty())
    elif operation == 5:
        print(myqueue.count())

linked_type = int(input("\n 1)Queue\n 2)Stack \nSelect Type:"))
if linked_type == 2:
    mystack = stack()
    while mystack.count() == 0:
        value = input("First enter some values in Stack \n(Note:- Mention a space between each value): ")
        for i in value.split(" "):
            mystack.push(int(i))
    cont = "Yes"
    while cont.lower() == "yes":
        operation = function()
        try:
            perform(operation)
        except Exception as e:
            print(e)
        cont = input("If want to apply other operation type 'Yes' else enter any key to exit: ")
if linked_type == 1:
    myqueue = queue()
    while myqueue.count() == 0:
        value = input("First enter some values in Queue\n(Note:- Mention a space between each value): ")
        for i in value.split(" "):
            myqueue.enqueue(int(i))
    cont = "Yes"
    while cont.lower() == "yes":
        operation = function1()
        try:
            perform1(operation)
        except Exception as e:
            print(e)
        cont = input("If want to apply other operation type 'Yes' else enter any key to exit: ")