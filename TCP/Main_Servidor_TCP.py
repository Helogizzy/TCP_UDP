from Servidor_TCP import Servidor_TCP
import time

tamanho_pacotes = [100, 500, 1000]
HEADER_SIZE = 66 #Tamanho do cabeçalho em cada pacote

for tamanho in tamanho_pacotes: # Itera sobre os diferentes tamanhos de pacotes de dados
    for i in range(10): # Executa 10 iterações de teste para cada tamanho de dados
        Servidor_TCP(tamanho, HEADER_SIZE, (i==9 and tamanho==1000))
        print(f"Iteração {i} feita para o tamanho: {tamanho}")
        time.sleep(0.1) # Pausa para a próxima iteração
    time.sleep(0.3) # Pausa para o próximo tamanho de pacotes