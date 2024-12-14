class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def delete_from_beginning(self):
        if not self.head:
            print("List is empty.")
            return
        if not self.head.next:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    def delete_from_end(self):
        if not self.head:
            print("List is empty.")
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next:
            current = current.next
        current.prev.next = None

    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def traverse_backward(self):
        current = self.head
        if not current:
            print("List is empty.")
            return
        while current.next:
            current = current.next
        while current:
            print(current.data, end=" -> ")
            current = current.prev
        print("None")

# Test the DLL
dll = DoublyLinkedList()
dll.insert_at_beginning(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
print("Traverse Forward:")
dll.traverse_forward()
print("Traverse Backward:")
dll.traverse_backward()
dll.delete_from_beginning()
dll.delete_from_end()
print("After Deletions:")
dll.traverse_forward()
