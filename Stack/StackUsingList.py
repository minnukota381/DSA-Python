class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            print("Stack Underflow: The stack is empty.")
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            print("The stack is empty.")
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def display(self):
        print("Stack:", self.stack)

# Test the Stack
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print("After pushing elements:")
s.display()

print("Top element (peek):", s.peek())

print("Popped element:", s.pop())
print("After popping one element:")
s.display()

print("Is stack empty?", s.is_empty())
