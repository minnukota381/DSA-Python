class Node:
    """A Node of the singly linked list."""
    def __init__(self, data):
        self.data = data  # Data to store in the node
        self.next = None  # Reference to the next node

class SinglyLinkedList:
    """A class to represent a singly linked list."""
    def __init__(self):
        self.head = None  # Initialize the head of the list as None

    def insert_at_beginning(self, data):
        """Insert a node at the beginning of the linked list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a node at the end of the linked list."""
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        current = self.head
        while current.next:  # Traverse to the last node
            current = current.next
        current.next = new_node

    def insert_at_position(self, position, data):
        """Insert a node at a specific position (1-based index)."""
        if position == 1:  # Special case for inserting at the beginning
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(position - 2):  # Traverse to the node before the position
            if not current:
                print("Position out of bounds.")
                return
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete_from_beginning(self):
        """Delete a node from the beginning of the linked list."""
        if not self.head:
            print("List is empty.")
            return
        self.head = self.head.next

    def delete_from_end(self):
        """Delete a node from the end of the linked list."""
        if not self.head:
            print("List is empty.")
            return
        if not self.head.next:  # If there is only one node
            self.head = None
            return
        current = self.head
        while current.next.next:  # Traverse to the second-last node
            current = current.next
        current.next = None

    def delete_at_position(self, position):
        """Delete a node at a specific position (1-based index)."""
        if position == 1:
            self.delete_from_beginning()
            return
        current = self.head
        for _ in range(position - 2):  # Traverse to the node before the position
            if not current or not current.next:
                print("Position out of bounds.")
                return
            current = current.next
        current.next = current.next.next

    def traverse(self):
        """Traverse the linked list and print all elements."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def search(self, key):
        """Search for an element in the linked list."""
        current = self.head
        position = 1
        while current:
            if current.data == key:
                print(f"Element {key} found at position {position}.")
                return
            current = current.next
            position += 1
        print(f"Element {key} not found in the list.")

# Create a linked list
ll = SinglyLinkedList()

# Insert elements
ll.insert_at_beginning(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_position(2, 15)  # Insert 15 at position 2

# Traverse the list
print("Linked List:")
ll.traverse()

# Search for an element
ll.search(15)
ll.search(40)

# Delete elements
ll.delete_from_beginning()
ll.delete_from_end()
ll.delete_at_position(2)

# Traverse after deletion
print("Linked List after deletion:")
ll.traverse()
