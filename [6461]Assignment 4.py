from abc import ABCMeta, abstractclassmethod
import random


class Node():
    def __init__(self, data, next=None):
        self.name = data['n']
        self.priority = data['p']
        self.next = next

    def __repr__(self):
        return self.name


class Queue():
    # Abstract Class
    __metaclass__ = ABCMeta

    @abstractclassmethod
    def enqueue(self, d):
        pass

    @abstractclassmethod
    def dequeue(self):
        pass

    @abstractclassmethod
    def empty(self):
        pass


class ImplQueue(Queue):

    def __init__(self):
        self.head = None

    def initlist(self, data):
        if data:
            self.head = Node(data[0])
        p = self.head
        for i in data[1:]:
            p.next = Node(i)
            p = p.next

    def enqueue(self, data):
        q = Node(data[0])
        if not self.head:
            self.head = q
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = q

    def dequeue(self):
        p, q = self.head, self.head
        m = p.priority
        i, j, idx = 0, 0, 0
        # p = p.next
        while p:
            if p.priority > m:
                m = p.priority
                idx = i
            p = p.next
            i += 1
        if idx != 0:
            while j != idx - 1:
                q = q.next
                j += 1
            q.next = q.next.next
        else:
            self.head = self.head.next

    def empty(self):
        self.head = None

    def print(self):
        p = self.head
        if not p:
            print('This queue is empty!')
            return 0
        while p and p.next:
            print('(' + p.name + ',' + str(p.priority) + ')', end=';')
            p = p.next
        print('(' + p.name + ',' + str(p.priority) + ')')


a = ImplQueue()
print('The original queue:')
a.initlist([{'n': 'a', 'p': random.randint(0, 100)}, {'n': 'b', 'p': random.randint(0, 100)},
            {'n': 'c', 'p': random.randint(0, 100)},
            {'n': 'd', 'p': random.randint(0, 100)}, {'n': 'e', 'p': random.randint(0, 100)},
            {'n': 'f', 'p': random.randint(0, 100)}])
a.print()
print('Start inserting element to the queue:')
a.enqueue([{'n': 'g', 'p': random.randint(0, 100)}])
a.print()
a.enqueue([{'n': 'h', 'p': random.randint(0, 100)}])
a.print()
a.enqueue([{'n': 'i', 'p': random.randint(0, 100)}])
a.print()
a.enqueue([{'n': 'j', 'p': random.randint(0, 100)}])
a.print()
print('Start dequeue element from the queue:')
a.dequeue()
a.print()
a.dequeue()
a.print()
a.dequeue()
a.print()
a.dequeue()
a.print()
print('Empty the queue:')
a.empty()
a.print()
