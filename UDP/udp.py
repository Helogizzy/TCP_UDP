import socket
import time

ACK = 0
NACK = -1
ESPERA = 0.5
MAX_FALHAS = 10

class Cliente:
    def __init__(self, arquivo, host, porta, garantia):
        self.arquivo = arquivo
        self.host = host
        self.porta = porta
        self.garantia = garantia

        # Cria um socket UDP
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def enviar_arquivo(self, tamanho):
        numero_de_reenvios = 0

        # Armazena o tempo inicial
        tempo_inicial = time.time()

        # Lê o arquivo e envia os pacotes para o servidor
        with open(self.arquivo, 'rb') as arquivo:
            numero_de_pacotes = 0
            
            while True:
                # Incrementa número de pacotes enviados
                numero_de_pacotes += 1

                # Lê os dados do arquivo em um pacote de tamanho fixo
                dados = arquivo.read(tamanho)

                # Encerra o loop quando todos os dados foram lidos do arquivo
                # e manda mensagem sinalizando o fim do envio dos pacotes
                if not dados:
                    dados = str.encode("CRm0W>W?;GQ4AP.sSg") # Converte a string em uma sequência de bytes
                    self.enviar(dados, tamanho)
                    break
                
                # Envia os dados para o servidor
                numero_de_reenvios += self.enviar(dados, tamanho)

        # Fecha o socket
        self.sock.close()

        # Armazena o tempo final
        tempo_final = time.time()
        
        # Retorna tempo de execução, número de pacotes e número de pacotes reenviados
        return tempo_final - tempo_inicial, numero_de_pacotes, numero_de_reenvios

    def enviar(self, dados, tamanho):
        if self.garantia:
            reenvios = 0
            tentativas = 1
            
            while True:
                # Define o quanto o servidor deve esperar
                self.sock.settimeout(ESPERA)

                try:
                    # Envia os pacotes para o servidor
                    self.sock.sendto(dados, (self.host, self.porta))

                    # Aguarda resposta do servidor
                    resposta = self.sock.recvfrom(tamanho)
                    mensagem = resposta[0]

                    # Reenvia se a mensagem não for ACK
                    if mensagem != b'ACK':
                        reenvios += 1
                        print("A resposta não foi ACK. Reenvinando...")
                        continue
                    
                    #print("A resposta foi ACK!!!")
                    tentativas = 1
                    break
                except:
                    tentativas += 1
                    reenvios += 1

                    print("Tempo limite atingido. Reenvinando...")
                    
                    # Interrompe em caso de muitas falhas
                    if tentativas > MAX_FALHAS:
                        print("Muitas falhas consecutivas. Parando...")
                        break

            return reenvios
        
        else:
            # Envia os pacotes para o servidor
            self.sock.sendto(dados, (self.host, self.porta))

            return 0


class Servidor:
    def __init__(self, arquivo, host, porta, garantia):
        self.arquivo = arquivo
        self.host = host
        self.porta = porta
        self.garantia = garantia

        # Cria um socket UDP
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.host, self.porta))

    def receber_arquivo(self, tamanho):
        print(tamanho)
        # Abre o arquivo para escrita
        with open(self.arquivo, 'wb') as arquivo:
            while True:
                # Recebe os pacotes do cliente
                recebido = self.sock.recvfrom(tamanho)
                dados = recebido[0]
                endereco = recebido[1]

                if self.garantia:
                    # Envia ACK para o cliente
                    if dados != b'ACK':
                        self.sock.sendto(str.encode('ACK'), endereco)
                
                # Encerra o loop quando todos os dados foram recebidos
                if dados == str.encode("CRm0W>W?;GQ4AP.sSg"):
                    break

                # Escreve os dados recebidos no arquivo
                arquivo.write(dados)

        # Fecha o socket
        self.sock.close()

