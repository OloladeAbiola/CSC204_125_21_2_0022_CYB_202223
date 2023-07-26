from nodes.node import Node

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")

    #Method to display the maximum and minimum data in the single linked list:
    def find_max(self):
        if not self.head:
            return None

        current = self.head
        max_data = current.data
        while current:
            if current.data > max_data:
                max_data = current.data
            current = current.next
        return max_data

    def find_min(self):
        if not self.head:
            return None

        current = self.head
        min_data = current.data
        while current:
            if current.data < min_data:
                min_data = current.data
            current = current.next
        return min_data

#Method that converts the single linked list into a binary search tree

    def convert_to_bst(self, lst):
        if not lst:
            return None

        mid = len(lst) // 2
        root_data = lst[mid]
        root = Node(root_data)

        root.left = self.convert_to_bst(lst[:mid])
        root.right = self.convert_to_bst(lst[mid + 1:])

        return root

