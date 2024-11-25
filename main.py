class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.start = None
        self.end = None

    def append(self, value):
        node = Node(value)

        if self.start is None:
            self.start = node

        if self.end is not None:
            self.end.next = node

        self.end = node

    def get(self, index):
        next = self.start

        for i in range(index):
            next = next.next

        return next.value

    def remove(self, index):
        next = self.start

        for i in range(index):
            if i == index - 1:
                next.next = next.next.next
                return

            next = next.next

    def print(self):
        next = self.start

        print("[", end="")

        while next is not None:
            print("'" + str(next.value) + "'", end="")

            if next.next is None:
                break
            else:
                next = next.next
                print(", ", end="")

        print("]")


l = LinkedList()
l.append("a")
l.append("b")
l.append(2)
l.append("gah gah")
l.remove(2)
l.print()
