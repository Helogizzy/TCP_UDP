import socket
import time 
import sys

def Cliente_TCP(tamanho, HEADER_SIZE):
    servidor = socket.socket()         
    host = "192.168.100.151"    
    port = 8080
    f = open('teste.txt','rb')
    cont_pacotes = 0

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor: # Cria o socket usando o IPv4
        tempo_inicial = time.time()
        servidor.connect((host, port)) # Conexão com o servidor
        leitura = f.read(tamanho-HEADER_SIZE) 

        while (leitura):
            servidor.send(leitura) # Cada parte dos dados é enviado para o servidor
            cont_pacotes+=1
            time.sleep(sys.float_info.min) # Pausa para pacotes não se atropelarem
            leitura = f.read(tamanho-HEADER_SIZE) 

        servidor.shutdown(socket.SHUT_WR) # Encerra a conexão
        servidor.close()
        tempo_final = time.time()
        f.close()

    return tempo_final-tempo_inicial, cont_pacotes # Tempo total de comunicação e o nº total de pacotes
