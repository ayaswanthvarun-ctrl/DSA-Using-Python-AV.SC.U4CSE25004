
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.front is None:
            self.front = self.rear = new_node
            self.rear.next = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front

        print("Element inserted:", data)

    def dequeue(self):
        if self.front is None:
            print("Queue is Empty")
        elif self.front == self.rear:
            print("Deleted Element:", self.front.data)
            self.front = self.rear = None
        else:
            print("Deleted Element:", self.front.data)
            self.front = self.front.next
            self.rear.next = self.front

    def peek(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            print("Front Element:", self.front.data)

    def display(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            temp = self.front
            print("Circular Queue Elements:")
            while True:
                print(temp.data, end=" ")
                temp = temp.next
                if temp == self.front:
                    break
            print()


cq = CircularQueue()

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        data = int(input("Enter Element: "))
        cq.enqueue(data)
    elif ch == 2:
        cq.dequeue()
    elif ch == 3:
        cq.peek()
    elif ch == 4:
        cq.display()
    elif ch == 5:
        print("Exiting...")
        break
    else:
        print("Invalid Choice")
