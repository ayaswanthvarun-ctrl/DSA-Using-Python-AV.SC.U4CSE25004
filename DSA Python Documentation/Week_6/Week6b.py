
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

front = None
rear = None

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        x = int(input("Enter element: "))
        new = Node(x)

        if front is None:
            front = rear = new
        else:
            rear.next = new
            rear = new

        print("Element inserted")

    elif ch == 2:
        if front is None:
            print("Queue Underflow")
        else:
            print("Deleted element:", front.data)
            front = front.next

            if front is None:
                rear = None

    elif ch == 3:
        if front is None:
            print("Queue is Empty")
        else:
            print("Front element:", front.data)

    elif ch == 4:
        if front is None:
            print("Queue is Empty")
        else:
            temp = front
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next
            print()

    elif ch == 5:
        break

    else:
        print("Invalid choice")
