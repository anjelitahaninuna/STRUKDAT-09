class QueueList:
    def __init__(self):
        self.queue_data = []
    
    def enqueue(self, value):
        self.queue_data.append(value)
    
    def dequeue(self):
        return self.queue_data.pop(0)

    def front(self):
        return self.queue_data[0]
    
    def clear(self):
        self.queue_data = []
    
    def __len__(self):
        return len(self.queue_data)

    def __str__(self):
        output = ""
        for item in self.queue_data:
            output = output + str(item)+" "
        return output

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLNC:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def delete_head(self):
        hapus = self.head
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.size -= 1
        del hapus
    
    def insert_tail(self, value):
        new_node = Node(value)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

class QueueLinkedList:
    def __init__(self):
        self.queue_data = SLNC()

    def enqueue(self, value):
        self.queue_data.insert_tail(value)

    def dequeue(self):
        value = self.queue_data.head.data
        self.queue_data.delete_head()
        return value

    def front(self):
        return self.queue_data.head.data

    def clear(self):
        self.queue_data = SLNC()

    def __len__(self):
        return len(self.queue_data.size)

    def __str__(self):
        output = ""
        helper = self.queue_data.head
        while helper != None:
            output = output + str(helper.data)+" "
            helper = helper.next
        return output

queue = QueueLinkedList()
queue.enqueue(30)
queue.enqueue(50)
queue.enqueue(10)
print(queue) #30 50 10
queue.dequeue()
queue.dequeue()
queue.enqueue(70)
queue.enqueue(20)
print(queue) #10 70 20
print(queue.dequeue()) #10
print(queue.dequeue()) #70