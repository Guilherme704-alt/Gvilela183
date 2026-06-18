from nodo import Nodo

class Fila ():
    def __init__(self):
        self.inicio = None
        self.final = None

    def vazia (self):
        return self.inicio == None

    def enfileirar (self,info):
        novo = Nodo(info)

        if not self.vazia ():
            self.final.prox = novo
            self.final = novo
        
        else:
            self.inicio = novo
            self.final = novo

        
    def desinfileirar (self):
         aux = self.inicio
         if not self.vazia ():
             if self.inicio != self.final:
                 self.inicio = self.inicio.prox  

             else:
                 self.inicio = None
                 self.final = None

             info = aux.info
             del aux
             return info  

    def primeiro(self):
        if not self.vazia ():
            return self.inicio.info
        
    def destruir(self):
        while not self.vazia():
            self.desinfileirar()
    
    def imprimir (self):
        aux = Fila()

        while not self.vazia():
            print(self.primeiro())
            aux.enfileirar(self.desinfileirar())

        while not aux.vazia():
            self.enfileirar(aux.desinfileirar())

    def imprimir_fila(self):
        self.imprimir()

    def buscar(self, info):
        aux = self.inicio
        while aux:
            if aux.info == info:
                return True
            aux = aux.prox
        return False

    def editar(self, info, novo_info=None):
        aux = self.inicio
        while aux:
            if aux.info == info:
                if novo_info is None:
                    novo_info = input(f"Novo valor para {info}: ")
                aux.info = novo_info
                return True
            aux = aux.prox
        return False

    def remover(self, info):
        aux = self.inicio
        anterior = None
        while aux:
            if aux.info == info:
                if anterior is None:
                    self.inicio = aux.prox
                else:
                    anterior.prox = aux.prox
                if aux == self.final:
                    self.final = anterior
                del aux
                return True
            anterior = aux
            aux = aux.prox
        return False

    def remover_repetidos(self):
        vistos = set()
        aux = self.inicio
        anterior = None
        while aux:
            if aux.info in vistos:
                anterior.prox = aux.prox
                if aux == self.final:
                    self.final = anterior
                temp = aux
                aux = aux.prox
                del temp
            else:
                vistos.add(aux.info)
                anterior = aux
                aux = aux.prox
            
