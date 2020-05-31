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
        start = self.head_node
        while start:
            string += str(start.get_value())+"\n"
            start = start.next_node
        return string

    def remove_node(self, value_to_remove):
        current_node = self.head_node
        if current_node == value_to_remove:
            self.head_node = current_node.next_node
        else:
            while current_node:
                if (current_node.get_next_node()).get_next_node() == value_to_remove:
                    current_node = current_node.next_node.get_next_node()
                    current_node.next_node = None
                current_node = current_node.next_node


myNode = Node(44)

print(myNode.get_value())