class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        new_node.next = self.head
        current.next = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head

    def delete_from_beginning(self):
        if not self.head:
            print("List is empty.")
            return
        if self.head.next == self.head:
            self.head = None
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        self.head = self.head.next
        current.next = self.head

    def delete_from_end(self):
        if not self.head:
            print("List is empty.")
            return
        if self.head.next == self.head:
            self.head = None
            return
        current = self.head
        while current.next.next != self.head:
            current = current.next
        current.next = self.head

    def traverse(self):
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(head)")

# Test the CLL
cll = CircularLinkedList()
cll.insert_at_beginning(10)
cll.insert_at_end(20)
cll.insert_at_end(30)
print("Circular Linked List after insertions:")
cll.traverse()
cll.delete_from_beginning()
print("After deleting from the beginning:")
cll.traverse()
cll.delete_from_end()
print("After deleting from the end:")
cll.traverse()
