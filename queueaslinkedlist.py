class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
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
            while temp.next.next is not none:
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
    value = int(input("\nSelect which operation your want to perform (1 to 8) \n 1) enqueue()\n 2) dequeue()\n 3) print()\n 4) isempty()\n 5) count()\nSelect one: "))
    return value
def perform(operation):
    if operation == 1:
        value = input("\nEnter value to Push: ")
        myqueue.en(value)
        myqueue.print()
    elif operation == 2:
        myqueue.print()
        myqueue.pop()
        myqueue.print()
    elif operation == 3:
        myqueue.print()
    elif operation == 4:
        print(myqueue.isempty())

myqueue = queue()
while myqueue.count() == 0:
    value = input("First Enter some values in Queue\n(Note:- Mention a space between each value): ")
    for i in value.split(" "):
        myqueue.enqueue(int(i))
cont = "Yes"
while cont.lower() == "yes":
    operation = function()
    try:
        perform(operation)
    except Exception as e:
        print(e)
    cont = input("If want to apply other operation type 'Yes' else enter any key to exit: ")