class Node:
    def __init__(self, data):
      self.data = data
      self.ref = None

class LinkedList:
    def __init__(self):
      self.head = None
    def print_LL(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
    def addbegin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

link1 = LinkedList()
link1.addbegin(10)
link1.addbegin(20)
link1.addbegin(30)
link1.print_LL()