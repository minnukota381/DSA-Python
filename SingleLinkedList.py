class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
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

    def insert_at_position(self, position, data):
        if position == 1:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(position - 2):
            if not current:
                print("Position out of bounds.")
                return
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete_from_beginning(self):
        if not self.head:
            print("List is empty.")
            return
        self.head = self.head.next

    def delete_from_end(self):
        if not self.head:
            print("List is empty.")
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def delete_at_position(self, position):
        if position == 1:
            self.delete_from_beginning()
            return
        current = self.head
        for _ in range(position - 2):
            if not current or not current.next:
                print("Position out of bounds.")
                return
            current = current.next
        current.next = current.next.next

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def search(self, key):
        current = self.head
        position = 1
        while current:
            if current.data == key:
                print(f"Element {key} found at position {position}.")
                return
            current = current.next
            position += 1
        print(f"Element {key} not found in the list.")

ll = SinglyLinkedList()
ll.insert_at_beginning(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_position(2, 15)
print("Linked List:")
ll.traverse()
ll.search(15)
ll.search(40)
ll.delete_from_beginning()
ll.delete_from_end()
ll.delete_at_position(2)
print("Linked List after deletion:")
ll.traverse()
