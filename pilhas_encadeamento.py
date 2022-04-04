# criar pilha vazia
# inserir na pilha
# excluir da pilha
# consultar topo da pilha
# destruir a pilha

# ENCADEAMENTO
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, valor):
        node = Node(valor)
        node.next = self.top
        self.top = node
        self._size = self._size + 1
     
    def pop(self):
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return node.data
        
        raise IndexError('Cannot remove from empty stack.')

    def peek(self):
        if self._size > 0:
            return self.top.data
        
        raise IndexError('Cannot remove from empty stack.')
        
    def destroy(self):
        if self._size > 0:
            while self.top != None:
                pointer = self.top
                self.top = self.top.next
                self._size = self._size - 1
                pointer = None
            return True
        
        raise IndexError('Cannot destroy an empty stack.')

    def __len__(self):
        return self._size

    def __repr__(self):
        r = ""
        pointer = self.top
        
        while pointer:
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        
        return r

    def __str__(self):
        return self.__repr__()
    
    def __getitem__(self, index):
        pointer = self.top
        
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError('Index out of range.')
        if pointer:
            return pointer.data
        else:
            raise IndexError('Index out of range.')


if __name__ == '__main__':
    
    def is_equal(stack1, stack2):
        flag = True
        
        if (len(stack1) != len(stack2)):
            flag = False
            return flag
     
        while (len(stack1)):
            if (stack1[0] == stack2[0]):
                stack1.pop()
                stack2.pop()
            else:
                flag = False
                break
        
        return flag


    pilha = Stack()

    pilha.push(12)
    pilha.push(18)
    pilha.push('Python')
    pilha.push('Carro')
    pilha.push(61.5)

    # print(pilha[2])

    pilha2 = Stack()

    pilha2.push(12)
    pilha2.push(18)
    pilha2.push('Python')
    pilha2.push('Carro')
    pilha2.push(61.5)

    print(is_equal(pilha, pilha2))