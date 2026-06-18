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
        
    def buscar(self, info):
        aux = self.topo
        while aux:
            if aux.info == info:
                return True
            aux = aux.prox
        return False

    def editar(self, info, novo_info=None):
        aux = self.topo
        while aux:
            if aux.info == info:
                if novo_info is None:
                    novo_info = input(f"Novo valor para {info}: ")
                aux.info = novo_info
                return True
            aux = aux.prox
        return False

    def remover(self, info):
        aux = self.topo
        anterior = None
        while aux:
            if aux.info == info:
                if anterior is None:
                    self.topo = aux.prox
                else:
                    anterior.prox = aux.prox
                del aux
                return True
            anterior = aux
            aux = aux.prox
        return False

    def remover_repetidos(self):
        vistos = set()
        aux = self.topo
        anterior = None
        while aux:
            if aux.info in vistos:
                anterior.prox = aux.prox
                temp = aux
                aux = aux.prox
                del temp
            else:
                vistos.add(aux.info)
                anterior = aux
                aux = aux.prox

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
    
