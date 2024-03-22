import time
import random
import matplotlib.pyplot as plt



def medir_tempo_execucao(algoritmo,lista):
    inicio = time.time()
    algoritmo(lista)
    fim = time.time()
    return fim - inicio

#montar lista de tuplas falando o número do algorítmo e em quanto tempo ele executa