queue = [None] * 5  # Initialize an empty queue with a fixed size (e.g., 5)
front = rear = -1

def enque(data):
    global front, rear  # Use the global keyword to modify global variables
    if rear == -1 and front == -1:
        front = 0
        rear = 0
        queue[rear] = data
    elif (rear == len(queue) - 1):
        print("Queue is full")  # Changed "queue is empty" to "Queue is full"
    else:
        rear += 1
        queue[rear] = data

def deque():
    global front, rear  # Use the global keyword to modify global variables
    if rear == -1 and front == -1:
        print('No elements in queue')
    elif rear == front:
        rear = front = -1
    else:
        print(f"Deleted {queue[front]}")
        front += 1

def display():
    if rear == -1 and front == -1:
        print("No data in Queue")
    else:
        for i in range(front, rear + 1):  # Include rear in the range
            print(f"{queue[i]}", end=" ")  # Use end=" " to print elements on the same line
        print()  # Print a newline at the end

def peek():
    if rear == -1 and front == -1:
        print("No data in Queue")
    else:
        print(f"{queue[front]}")

enque(10)
enque(20)
enque(30)
deque()
enque(40)
enque(50)
display()
peek()
