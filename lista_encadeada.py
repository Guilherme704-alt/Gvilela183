from nodo import Nodo

class Lista_encadeada():
    """
    Lista simplesmente encadeada
    """
    #Cria a lista vazia
    def __init__(self):
        print("Lista criada com sucesso")
        self.cabeca = None

    def vazia(self):
        if self.cabeca != None:
            return False
        else: 
            return True
        
    def inserir_inicio(self,info):
        """
        Insere no inicio da lista
        """
        novo = Nodo(info)
        novo.prox = self.cabeca
        self.cabeca = novo
    
    def imprimir(self):
        """
        percorre e imprime
        """
        aux = self.cabeca
        while aux:
            print(aux.info)
            aux = aux.prox

    def remover_inicio(self):
        if  not self.vazia():
            aux = self.cabeca
            self.cabeca = aux.prox
            del aux

    def inserir_final(self,info):
        """
        Insere no final
        """
        novo = Nodo(info)
        if not self.vazia():
            aux = self.cabeca
            while aux.prox:
                aux = aux.prox
            aux.prox = novo
        else:
            novo.prox = self.cabeca
            self.cabeca = novo
    
    def remover_final(self):
        if not self.vazia():
            aux = self.cabeca
            ant = None
            
            # Hipótese 1: Lista com mais de um elemento
            if aux.prox:
                while aux.prox:
                    ant = aux       # 'ant' guarda o atual antes de avançar
                    aux = aux.prox  # 'aux' avança para o próximo
                
                ant.prox = None     # O penúltimo agora vira o último (aponta para None)
                del aux             # Deleta o antigo último
                
            # Hipótese 2: Lista com apenas um elemento
            else:
                self.cabeca = None
                del aux

    def buscar(self, valor):
        aux = self.cabeca 
        while aux:
            if aux.info == valor:
                return True
            
            aux = aux.prox
            
        return False


    def min(self):
        aux = self.cabeca

        if aux:
            menor = aux.info

            while aux:
                if aux.info < menor:
                    menor = aux.info

                aux = aux.prox

            return menor

    def max(self):
        aux = self.cabeca

        if aux:
            maior = aux.info

            while aux:
                if aux.info > maior:
                    maior = aux.info

                aux = aux.prox

            return maior

    def sum(self):
        soma = 0
        aux = self.cabeca

        while aux:
            soma += aux.info
            aux = aux.prox

        return soma

    def len(self):
        qtd = 0
        aux = self.cabeca

        while aux:
            qtd += 1
            aux = aux.prox

        return qtd

    def avg(self):
        if not self.vazia():
            return self.sum() / self.len()

    def append(self, outra_lista):
        aux = outra_lista.cabeca

        while aux:
            self.inserir_final(aux.info)
            aux = aux.prox

    def reverse(self):
        ant = None
        atual = self.cabeca

        while atual:
            prox = atual.prox
            atual.prox = ant
            ant = atual
            atual = prox

        self.cabeca = ant  