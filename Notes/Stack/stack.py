class Stack():
    def __init__(self): # Constructor to initiate the object.
        self.items = []

    def push(self, items): # To Push the item in the empty stack list.
        self.items.append(items)

    def pop(self): # To Pop the last item pushed in stack list.
        return self.items.pop()

    def get_stack(self): # To Fetch the items in stack list.
        return self.items

    def is_empty(self): # To check is stack list is empty.
        return self.items == []

    def peek(self): # To Fetch the last item in stack list.
        if not self.is_empty():
            return self.items[-1]

objectStack = Stack() # Object of the Stack Class.

print(objectStack.is_empty()) 

objectStack.push("Rat")
objectStack.push("Cat")

print(objectStack.get_stack())
 
objectStack.push("Bat")

print(objectStack.get_stack())

objectStack.push("Hat")

print(objectStack.is_empty())

print(objectStack.get_stack())

print(objectStack.peek())

objectStack.pop()

print(objectStack.get_stack())
