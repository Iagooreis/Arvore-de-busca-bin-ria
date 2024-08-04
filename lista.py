class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Lista:
    def __init__(self):
        self.head = None

    def add(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
        else:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = new_node

    def remove(self):
        if self.head is None:
            return False
        no_atual = self.head
        self.head = self.head.next
        return no_atual.data

    def ordenar(self):
        if self.head is None or self.head.next is None:
            return
        trocou = True
        while trocou:
            trocou = False
            atual = self.head
            while atual.next is not None:
                if atual.data > atual.next.data:
                    atual.data, atual.next.data = atual.next.data, atual.data
                    trocou = True
                atual = atual.next

    def imprimir(self):
        atual = self.head
        while atual is not None:
            print(atual.data)
            atual = atual.next

   