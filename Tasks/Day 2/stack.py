class Node:
    def __init__(self, value, link_node = None):
        #to initialize the object constructure is used.
        self.value=value
        self.link_node=link_node

    def get_value(self):
        return self.value

    def get_link_node(self):
        return self.link_node

    def set_link_node(self, link_node):
        self.link_node=link_node

class Stack(Node):
    def __init__(self, size, limit = 1000):
        self.size = 0
        self.limit = limit
        self.top_item = None

    def has_space(self):
        return self.limit > self.size

    def push(self, value):
        if self.has_space():
            super.__init__(value)
            self.set_link_node(self.top_item)
            self.top_item = value
            self.size += 1
        else:
            print("Out Of Space")

    def is_empty(self):
        return self.size <= 0

    def poo(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            top_item = self.get_link_node()
            self.size -= 1
            return item_to_remove
        else:
            print("Stack Empty")