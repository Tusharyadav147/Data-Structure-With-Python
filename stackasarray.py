class arraystack():
    def __init__(self):
        self.data = []

    def leng(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self,element):
        self.data.append(element)

    def pop(self):
        if self.is_empty() == True:
            return "stack is empty"
        return self.data.pop()

    def top(self):
        if self.is_empty() == True:
            return "stack is empty"
        return self.data[-1]

s = arraystack()
s.push(20)
s.push(50)
print('Stack:',s.data)
print("length :",len(s.data))
print("Is-empty:",s.is_empty())
print('popped:',s.pop())
print("stack:",s.data)
