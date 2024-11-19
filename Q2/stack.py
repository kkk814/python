class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    def __len__(self):
        return self.size()

    def __str__(self):
        items = []
        current_item = self.top

        while current_item is not None:
            items.append(str(current_item.value))
            current_item = current_item.next

        return ', '.join(items)
        

    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

        self.size += 1

    def pop(self):
        if self.top is None:
            raise ValueError("stack is empty")
        
        pop_value = self.top.value
        self.top = self.top.next

        self.size -= 1

        return pop_value

    def peek(self):
        if self.top is None:
            raise ValueError("stack is empty")
        return self.top.value

    def is_Empty(self):
        return self.top is None


if __name__ == '__main__':
    stack = Stack()

    # stack.push(10)
    # stack.push(2)
    # stack.push(40)
    # stack.push(8)
    # stack.push(19)
    # stack.push(22)

    x = int(input("enter the size of the stack\n"))
    for i in range(x):
        print(f"enter the {i+1}th element")
        y = int(input())
        stack.push(y)

    print(stack.peek())
    print(stack)

    print(stack.pop())
    print(stack)
