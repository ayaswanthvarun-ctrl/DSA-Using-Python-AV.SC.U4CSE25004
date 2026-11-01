
queue = []
size = 5

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        if len(queue) == size:
            print("Queue is Full")
        else:
            x = int(input("Enter element: "))
            queue.append(x)
            print("Element inserted")

    elif ch == 2:
        if len(queue) == 0:
            print("Queue is Empty")
        else:
            print("Deleted element:", queue.pop(0))

    elif ch == 3:
        if len(queue) == 0:
            print("Queue is Empty")
        else:
            print("Front element:", queue[0])

    elif ch == 4:
        if len(queue) == 0:
            print("Queue is Empty")
        else:
            print("Queue:", queue)

    elif ch == 5:
        break

    else:
        print("Invalid choice")
