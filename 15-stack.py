class Stack:
    def __init__(self):
        self.stack = []
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Error: Pop from an empty stack")
            return None
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Nothing to Peek from an empty stack") 
    
    def size(self):
        return len(self.stack)
    
    def display(self):
        return self.stack
    

    def menu(self):
        
        while True:
            print("\nChoose an option:")
            print("1. Push item to the stack")
            print("2. Pop item from the stack")
            print("3. Peek (Top item)")
            print("4. Size of the stack")
            print("5. Display the stack")
            print("6. Check if the stack is empty")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                item = input("Enter item to push: ")
                self.push(item)
                print("Item pushed successfully.\n")

            elif choice == '2':
                item = self.pop()
                if item is not None:
                    print(f"Popped item: {item}\n")

            elif choice == '3':
                item = self.peek()
                if item is not None:
                    print(f"Peeked item: {item}\n")

            elif choice == '4':
                print(f"Current Size: {self.size()}\n")

            elif choice == '5':
                print(f"Stack Elements: self.display()\n")

            elif choice == '6':
                if self.is_empty():
                    print("The stack is empty.\n")
                else:
                    print("The stack is not empty.\n")

            elif choice == '7':
                print("Exiting the program. Goodbye!\n")
                break

            else:
                print("Invalid choice. Please select a valid option. \n")

stack = Stack()
stack.menu()

