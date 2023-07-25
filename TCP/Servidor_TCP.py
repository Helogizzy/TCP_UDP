import socket
import time

HOST = "192.168.100.10"  
PORT = 8080

def Servidor_TCP(tamanho, HEADER_SIZE, extra_sleep): # Recebe os dados do cliente e salva no arquivo
    f = open('teste_recebido.txt', 'wb')
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor: # Cria o socket usando o IPv4
        servidor.bind((HOST, PORT)) # Vincula socket ao endereço e porta
        servidor.listen() # Escuta conexões recebidas
        conexao, addr = servidor.accept() # Aceita a conexão
        print(addr)
        leitura = conexao.recv(tamanho - HEADER_SIZE) # Recebe bloco de dados

        while(leitura): # Continua até que não tenha mais dados do cliente
            f.write(leitura) # Dados gravados no arquivo
            leitura = conexao.recv(tamanho - HEADER_SIZE) # Recebe bloco de dados
        if extra_sleep:
            time.sleep(5) # Servidor faz uma pausa caso seja necessário
        f.close()
        conexao.close()
