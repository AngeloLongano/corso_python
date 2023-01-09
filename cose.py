class Stack:

    def __init__(self):
        self.values=[]
    def push(self,x):
        self.values.append(x)
    def pop(self):
        self.values.pop()
    def is_empty(self):
        return self.values.__len__()==0

a = Stack()
print(a.values)
print(a.is_empty())
a.push(10)
a.push(1)
a.push(3)
a.pop()
print(a.values)
print(a.is_empty())


class Ciao:
    def __init__(self, a,b):
        self.a = a
        self.b = b
    def __getattribute__(self, item):
        print("entro in getattribute")
        if item == "a" :
            return super().__getattribute__(item)
        else:
            return "paperino"
    def __getattr__(self, item):
        return "giumon"

