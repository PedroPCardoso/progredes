__author__ = 'Pedro Cardoso'
# -.- coding: utf-8 -.-
from threading import Thread

class minhaThread(Thread):
    # sobrescrevendo o metodo __init__()
    def __init__(self, meu_argumento):
        # o metodo __init__ da superclasse
        # deve ser chamado para proceder
        # com a inicializacao
        Thread.__init__(self)
        self.atributo=meu_argumento

    # sobrescrevendo o metodo run()
    def run(self):
        for e in range (0,10):
            print 'patata'
            print e
            tr = minhaThread("ola")
            tr.start()

tr = minhaThread("ola")
tr.start()