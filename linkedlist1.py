class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.start = None

    def print_ll(self):
        temp = self.start
        if temp is None:
            print("Linked List Is Empty")
        else:
            while temp is not None:
                print(temp.data, end=", ")
                temp = temp.next
            print("\n")

    def add_begin(self, value):
        newnode = node(value)
        newnode.next = self.start
        self.start = newnode

    def add_end(self,value):
        newnode = node(value)
        if self.start is None:
            self.start = newnode
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = newnode
    
    def add_position(self, value, position):
        newnode = node(value)
        if position < 1:
            print("Position should be 1 or greater than 1")
        elif position == 1:
            self.add_begin(value)
        else:
            temp = self.start
            for i in range(1, position-1):
                if temp is not None:
                    temp = temp.next
                elif temp is None:
                    print("Position Is Out of Range", "\nYour linked list have only {} element".format(i))
            newnode.next = temp.next
            temp.next = newnode

    def remove_first(self):
        if self.start == None:
            print("Your linked list is already empty")
        else:
            temp = self.start
            self.start = temp.next
    
    def remove_last(self):
        if self.start == None:
            print("Your linked list is already empty")
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
    
    def remove_position(self, position):
        temp = self.start
        if position < 1:
            print("Position should be 1 or greater than 1")
        elif position == 1:
            self.remove_first()
        elif position > 1:
            for i in range(1, position-1):
                if temp.next.next is not None:
                    temp = temp.next
                elif temp.next.next == None :
                    print("There is no value in such position ")
                    break
            if temp.next is not None:
                temp.next = temp.next.next

    def search(self, value):
        temp = self.start
        if temp is None:
            print("linked list is Empty")
        else:
            count = 1
            while temp is not None:
                if temp.data == value:
                    print("The value at {} position".format(count))
                    break
                elif temp.next == None:
                    print("Value don't exist")
                    break
                else:
                    temp = temp.next
                    count = count + 1
    
    def count(self):
        temp = self.start
        count = 0
        while temp is not None:
            temp = temp.next
            count = count + 1
        #print("The total number of element in linked list is {}".format(count))
        return count

def function():
    value = int(input("\nSelect which operation your want to perform (1 to 8) \n 1)add_begin()\n 2)add_end()\n 3)add_position()\n 4)remove_first()\n 5)remove_last()\n 6)remove_position()\n 7)count()\n 8)search()\n 9)print()\nSelect one: "))
    return value
def perform(operation):
    if operation == 1:
        value = input("\nEnter value to add at begin: ")
        mylist.add_begin(value)
        mylist.print_ll()
    elif operation == 2:
        value = input("\nEnter value to add at end: ")
        mylist.add_end(value)
        mylist.print_ll()
    elif operation == 3:
        value = input("\nEnter value: ")
        position = int(input("\nEnter position: "))
        mylist.add_position(value, position)
        mylist.print_ll()
    elif operation == 4:
        mylist.print_ll()
        mylist.remove_first()
        mylist.print_ll()
    elif operation == 5:
        mylist.print_ll()
        mylist.remove_last()
        mylist.print_ll()
    elif operation == 6:
        mylist.print_ll()
        position = int(input("\nEnter Position to remove that value: "))
        mylist.remove_position(position)
        mylist.print_ll()
    elif operation == 7:
        print("The Total number of element is {}".format(mylist.count()))
    elif operation == 8:
        value = input("\nEnter value to search in linkedlist: ")
        mylist.search(value)
    elif operation == 9:
        mylist.print_ll()

mylist = linkedlist()
while mylist.count() == 0:
    value = input("Enter some values in Linked List\n(Note:- Mention a space between each value): ")
    for i in value.split(" "):
        mylist.add_end(int(i))
cont = "Yes"
while cont.lower() == "yes":
    operation = function()
    try:
        perform(operation)
    except Exception as e:
        print(e)
    cont = input("If want to apply other operation type 'Yes' else enter any key to exit: ")