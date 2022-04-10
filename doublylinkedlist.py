class node:
    def __init__(self, data):
        self.pre = None
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.start = None

    def print_ll(self):
        temp = self.start
        if temp == None:
            print("The Linked list is empty")
        else:
            while temp is not None:
                print(temp.data, end = ",")
                temp = temp.next
            print("\n")
    def add(self, data):
        new_node = node(data)
        if self.start is None:
            self.start  = new_node
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.pre = temp

    def delete_first(self):
        temp = self.start
        if temp == None:
            print("List is already empty")
        else:
            self.start.next.pre = None
            self.start = self.start.next
    def delete_last(self):
        temp = self.start
        if temp == None:
            print("List is already empty")
        else:
            while temp.next is not None:
                temp = temp.next
            temp.pre.next = None
            temp.pre = None
    def count(self):
        temp = self.start
        count = 0
        while temp is not None:
            temp = temp.next
            count = count + 1
        #print("The total number of element in linked list is {}".format(count))
        return count

def function():
    value = int(input("\nSelect which operation your want to perform (1 to 8) \n 1) add()\n 2) remove_first()\n 3) remove_last()\n 4) print()\n 5) count()\nSelect one: "))
    return value
def perform(operation):
    if operation == 1:
        value = input("\nEnter value to add: ")
        mylist.add(value)
        mylist.print_ll()
    elif operation == 2:
        mylist.print_ll()
        mylist.delete_first()
        mylist.print_ll()
    elif operation == 3:
        mylist.print_ll()
        mylist.delete_last()
        mylist.print_ll()
    elif operation == 4:
        mylist.print_ll()
    elif operation == 5:
        print("The Total number of element in Doubly linked list is {}".format(mylist.count()))

mylist = linkedlist()
while mylist.count() == 0:
    value = input("Enter some values in Doubly Linked List\n(Note:- Mention a space between each value): ")
    for i in value.split(" "):
        mylist.add(int(i))
cont = "Yes"
while cont.lower() == "yes":
    operation = function()
    try:
        perform(operation)
    except Exception as e:
        print(e)
    cont = input("If want to apply other operation type 'Yes' else enter any key to exit: ")