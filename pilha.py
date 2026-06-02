from nodo import Nodo

class Pilha():
    """
    Implementação de Pilha usando lista encadeada
    """

    def __init__(self):
         self.topo = None

    def Vazia(self):
        return self.topo == None
    
    def push(self, info):
        novo = Nodo(info)
        novo.prox = self.topo
        self.topo = novo

    def pop(self):
        if not self.Vazia():
            aux = self.topo
            self.topo = self.topo.prox
            info = aux.info
            del aux
            return info 

    def top(self):
        if not self.Vazia():
            return self.topo.info
        
    def imprimir(self):
        if not self.Vazia():
            #crio pilha aux Vazia
            aux = Pilha()
            while not self.Vazia():
                print (self.top())
                aux.push(self.pop())
            #Devolve para pilha principal
            
            while not aux.Vazia():
                self.push(aux.pop())
    
    
    def buscar(self, info):
        aux = self.topo

        while aux:
            if aux.info == info:
                return True

            aux = aux.prox

        return False

    def editar(self, antigo, novo):
        aux = self.topo

        while aux:
            if aux.info == antigo:
                aux.info = novo
                return True

            aux = aux.prox

        return False

    def remover(self, info):
        aux = self.topo
        ant = None

        while aux:
            if aux.info == info:

                if ant == None:
                    self.topo = aux.prox

                else:
                    ant.prox = aux.prox

                del aux
                return True

            ant = aux
            aux = aux.prox

        return False

    def remover_repetidos(self):
        aux = self.topo

        while aux:
            ant = aux
            atual = aux.prox

            while atual:
                if atual.info == aux.info:
                    ant.prox = atual.prox
                    atual = atual.prox

                else:
                    ant = atual
                    atual = atual.prox

            aux = aux.prox