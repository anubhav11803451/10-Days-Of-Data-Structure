class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.next_node = self.head_node
        self.head_node = new_node

    def stringify_list(self):
        string = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node


myNode = Node(44)

print(myNode.get_value())

L1 = LinkedList(8)
L1.insert_beginning(25)
L1.insert_beginning(85)
L1.insert_beginning(110)

print(L1.stringify_list())

L1.remove_node(85)

print(L1.stringify_list())