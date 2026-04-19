class Queue:
    def __init__(self):
        self.queue = []
        
    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, item):
        self.queue.append(item)
        
    def dequeue(self):
        
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Error: Dequeue from an empty queue")
           
    
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Nothing to Peek from an empty queue")
            
    

    def display(self):
        print (self.queue)

    def size(self):
        return len(self.queue)
    

    def main(self):
        while True:
            print("\nChoose an option:")
            print("1. Enqueue item to the queue")
            print("2. Dequeue item from the queue")
            print("3. Peek (Front item)")
            print("4. Size of the queue")
            print("5. Display the queue")
            print("6. Check if the queue is empty")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                item = input("Enter item to enqueue: ")
                self.enqueue(item)
                print("Item enqueued successfully.\n")

            elif choice == '2':
                item = self.dequeue()
                if item is not None:
                    print(f"Dequeued item: {item}\n")

            elif choice == '3':
                item = self.peek()
                if item is not None:
                    print(f"Peeked item: {item}\n")

            elif choice == '4':
                print(f"Current Size: {self.size()}\n")

            elif choice == '5':
                print(f"Queue Elements: {self.display()}\n")

            elif choice == '6':
                if self.is_empty():
                    print("The queue is empty.\n")
                else:
                    print("The queue is not empty.\n")

            elif choice == '7':
                print("Exiting the program. Goodbye!\n")
                break

            else:
                print("Invalid choice. Please select a valid option.")

queue = Queue()
queue.main()
