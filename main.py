from pilhas_encadeamento import Stack

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0
       
    def push(self, valor):
        node = Node(valor)
        
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node

        if self.first is None:
            self.first = node

        self._size = self._size + 1
        
    def pop(self):
        if self.first is not None:
            value = self.first.data
            self.first = self.first.next
            self._size -= 1
            return value
        
        raise IndexError('The queue is empty!')
     
    def peek(self):
        if self._size > 0:
            value = self.first.data
            return value
        
        raise IndexError("The queue is empty")
        
    def destroy(self):
        self.first = None
        self.last = None
        self._size = 0

    def __len__(self):
        return self._size

    def __repr__(self):
        if self._size > 0:
            
            r = ""
            pointer = self.first

            while pointer:
                r = r + str(pointer.data) + " "
                pointer = pointer.next

            return r
        
        return 'The queue is empty!'

    def __str__(self):
        return self.__repr__()
    
    def __getitem__(self, index):
        pointer = self.first
        
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError('Index out of range.')
        if pointer:
            return pointer.data
        else:
            raise IndexError('Index out of range.')
            
            
    def sort_queue(self):
        stack1 = Stack()
        
        stack2 = Stack()
        
        pointer = self.first
        stack1.push(pointer.data)
        
        pointer = pointer.next
        
        while pointer:
            if pointer.data > stack1.peek():
                while stack1.peek() < pointer.data:
                    stack2.push(stack1.peek())
                    stack1.pop()

                    if len(stack1) == 0:
                        break

                stack1.push(pointer.data)

                while stack2:
                    stack1.push(stack2.peek())
                    stack2.pop()
            else:
                stack1.push(pointer.data)

            pointer = pointer.next
        
        self.destroy()
        
        while stack1:
            self.push(stack1.peek())
            stack1.pop()
        
        return True

if __name__ == '__main__':
    # strings
    queue = Queue()

    queue.push('dado')
    queue.push('aula')
    queue.push('fila')
    queue.push('zorra')
    queue.push('carro')
    queue.push('xis')

    queue

    queue.sort_queue()

    queue

    # valores numericos
    queue2 = Queue()

    queue2.push(4210)
    queue2.push(4)
    queue2.push(250)
    queue2.push(100)
    queue2.push(0)
    queue2.push(1552)
    queue2.push(2634)

    print(queue2)

    queue2.sort_queue()

    print(queue2)