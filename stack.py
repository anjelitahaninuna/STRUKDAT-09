class StackList:
    def __init__(self):
        self._data = []
    
    def push(self, value):
        self._data.append(value)
    
    def pop(self):
        value = self._data[len(self._data)-1]
        del self._data[len(self._data)-1]
        return value
    
    def top(self):
        return self._data[len(self._data)-1]
    
    def print(self):
        for item in self._data:
            print(item, end=' ')
        print()

class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

class SingleLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def insertHead(self, value):
        newNode = Node(value)
        if self._size == 0:
            self._head = newNode
            self._tail = newNode
        else:
            newNode._next = self._head
            self._head = newNode
        self._size += 1

    def deleteHead(self):
        delNode = self._head
        if self._size == 1:
            self._head = None
            self._tail = None
        else:
            self._head = self._head._next
        del delNode
        self._size -= 1
    
    def print(self):
        helper = self._head
        while helper != None:
            print(helper._value, end=' ')
            helper = helper._next
        print()

class StackLinkedList:
    def __init__(self):
        self._data = SingleLinkedList()
    
    def push(self, value):
        self._data.insertHead(value)

    def pop(self):
        value = self._data._head._value
        self._data.deleteHead()
        return value

    def top(self):
        return self._data._head._value
    
    def print(self):
        self._data.print()

stack = StackLinkedList()
stack.push(5)
stack.push(70)
stack.push(34)
stack.push(11)
stack.push(98)
stack.print()
stack.pop()
stack.pop()
stack.print()
print(stack.top())
stack.print()
