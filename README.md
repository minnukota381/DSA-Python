# **Complete Data Structures Tutorial**

This document provides a comprehensive overview of data structures, including their definitions, operations, and examples in Python. It is designed as a tutorial for understanding and implementing these essential components of computer science.

---

## **Table of Contents**
1. [Introduction to Data Structures](#introduction-to-data-structures)
2. [Arrays](#arrays)
3. [Linked Lists](#linked-lists)
4. [Stacks](#stacks)
5. [Queues](#queues)
6. [Hash Tables](#hash-tables)
7. [Trees](#trees)
8. [Graphs](#graphs)
9. [Heaps](#heaps)
10. [Tries (Prefix Trees)](#tries-prefix-trees)
11. [Complexity Analysis](#complexity-analysis)

---

## **Introduction to Data Structures**

### **Definition**
A **data structure** is a way of organizing and storing data in a computer so that it can be accessed and modified efficiently.

### **Types of Data Structures**
1. **Linear Data Structures**: Data is organized sequentially.
   - Arrays
   - Linked Lists
   - Stacks
   - Queues
2. **Non-Linear Data Structures**: Data is organized hierarchically.
   - Trees
   - Graphs
   - Heaps
3. **Hash-Based Data Structures**:
   - Hash Tables
   - Dictionaries

---

## **Arrays**

### **Definition**
An **array** is a collection of elements stored in contiguous memory locations. Each element is identified by an index.

### **Key Operations**
- **Access**: O(1)
- **Search**: O(n)
- **Insertion**: O(n)
- **Deletion**: O(n)

### **Example**
```python
arr = [10, 20, 30, 40, 50]
print(arr[2])  # Access element at index 2
```

### **Use Cases**
- Storing data that needs constant-time access.
- Implementing other data structures.

---

## **Linked Lists**

### **Definition**
A **linked list** is a linear data structure where each element (node) contains:
1. Data
2. Pointer to the next node

### **Types**
1. **Singly Linked List**: Nodes point to the next node only.
2. **Doubly Linked List**: Nodes point to both the next and previous nodes.
3. **Circular Linked List**: The last node points to the first node.

### **Example**
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
```

### **Key Operations**
- **Insertion**: O(1) at the beginning, O(n) at the end.
- **Deletion**: O(n)
- **Traversal**: O(n)

---

## **Stacks**

### **Definition**
A **stack** is a linear data structure that follows the **LIFO** (Last In, First Out) principle.

### **Key Operations**
1. **Push**: Add an element to the top of the stack.
2. **Pop**: Remove the top element.
3. **Peek**: View the top element without removing it.

### **Example**
```python
stack = []
stack.append(10)  # Push
stack.pop()       # Pop
```

### **Use Cases**
- Undo operations.
- Expression evaluation.

---

## **Queues**

### **Definition**
A **queue** is a linear data structure that follows the **FIFO** (First In, First Out) principle.

### **Types**
1. **Simple Queue**
2. **Circular Queue**
3. **Priority Queue**

### **Key Operations**
1. **Enqueue**: Add an element to the rear.
2. **Dequeue**: Remove an element from the front.

### **Example**
```python
from collections import deque
queue = deque()
queue.append(10)  # Enqueue
queue.popleft()   # Dequeue
```

### **Use Cases**
- Task scheduling.
- Breadth-First Search (BFS).

---

## **Hash Tables**

### **Definition**
A **hash table** is a data structure that maps keys to values using a hash function.

### **Key Operations**
- **Insertion**: O(1) on average.
- **Search**: O(1) on average.
- **Deletion**: O(1) on average.

### **Example**
```python
hash_table = {}
hash_table['key'] = 'value'
print(hash_table['key'])
```

### **Use Cases**
- Caching.
- Databases.

---

## **Trees**

### **Definition**
A **tree** is a hierarchical data structure consisting of nodes, with a root node and children nodes forming subtrees.

### **Types**
1. **Binary Tree**
2. **Binary Search Tree (BST)**
3. **AVL Tree**
4. **B-Trees**

### **Key Operations**
1. **Traversal**: Inorder, Preorder, Postorder
2. **Insertion**: O(log n) for balanced trees
3. **Search**: O(log n) for balanced trees

### **Example**
```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

---

## **Graphs**

### **Definition**
A **graph** is a collection of nodes (vertices) and edges connecting them.

### **Types**
1. **Directed Graph**
2. **Undirected Graph**
3. **Weighted Graph**

### **Key Operations**
1. **Traversal**: BFS, DFS
2. **Shortest Path**: Dijkstra’s Algorithm

### **Example**
```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
```

---

## **Heaps**

### **Definition**
A **heap** is a specialized tree-based data structure satisfying the heap property:
1. **Max-Heap**: Parent nodes are greater than child nodes.
2. **Min-Heap**: Parent nodes are smaller than child nodes.

### **Key Operations**
- **Insertion**: O(log n)
- **Deletion**: O(log n)

### **Use Cases**
- Priority queues.
- Heap Sort.

---

## **Tries (Prefix Trees)**

### **Definition**
A **trie** is a tree-like data structure used for storing strings in a way that facilitates fast retrieval.

### **Use Cases**
- Autocomplete.
- Spell checking.

### **Example**
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
```

---

## **Complexity Analysis**

### **Time Complexity**
1. **O(1)**: Constant time
2. **O(log n)**: Logarithmic time
3. **O(n)**: Linear time
4. **O(n log n)**: Log-linear time
5. **O(n^2)**: Quadratic time
6. **O(2^n)**: Exponential time

### **Space Complexity**
- Memory usage by algorithms.

---

This tutorial serves as a reference and foundation for mastering data structures. Dive into practice problems to solidify your understanding!

