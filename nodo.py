class Nodo():
    """
    Nó de lista encadeada
    """
    #Construtor
    def __init__(self, info):
        self.info = info
        self.prox = None

    def __str__(self):
        return str(self.info)