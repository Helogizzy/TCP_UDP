import sys
import pandas
from udp import Cliente, Servidor

HOST = "192.168.100.151"
PORTA = 8080
NUMERO_DE_TESTES = 10
TAMANHOS = [100, 500, 1000]
PLANILHA = "res.csv"

class CSV:
    testes = []
    tamanhos = []
    tempos = []
    pacotes = []
    reenvios = []

    def __init__(self):
        pass
        
    def adicionar(self, teste, tamanho, tempo, pacotes, reenvios):
        print(str(tamanho) + ": " + str(teste) + " levou " + str(tempo) + " segundos.")
        self.testes.append(teste)
        self.tamanhos.append(tamanho)
        self.tempos.append(tempo)
        self.pacotes.append(pacotes)
        self.reenvios.append(reenvios)
    
    def gravar(self):
        resultados = pandas.DataFrame({
            "Testes": self.testes,
            "Tamanhos": self.tamanhos,
            "Tempos": self.tempos,
            "Pacotes": self.pacotes,
            "Reenvios": self.reenvios,
        })
        resultados.to_csv(PLANILHA, index=False)


# Verifica se foram fornecidos argumentos na linha de comando
if len(sys.argv) > 2:
    garantia = False

    # O primeiro argumento da linha de comando (caminho do arquivo)
    primeiro_argumento = sys.argv[1]
    
    # O terceiro argumento da linha de comando
    if len(sys.argv) > 3:
        terceiro_argumento = sys.argv[3]
        if terceiro_argumento == "garantia":
            garantia = True
        else:
            print("Terceiro argumento incorreto.")
            exit(-1)
    
    # O segundo argumento da linha de comando
    segundo_argumento = sys.argv[2]

    # Instancia classes de acordo com o tipo de execução
    # e rodar os testes

    # Caso o usuário escolha rodar como cliente
    if segundo_argumento == "cliente":
        for tamanho in TAMANHOS:
            for i in range(NUMERO_DE_TESTES):
                cliente = Cliente(primeiro_argumento, HOST, PORTA, garantia)
                tempo, pacotes, reenvios = cliente.enviar_arquivo(tamanho)
                csv = CSV()
                csv.adicionar(i, tamanho, tempo, pacotes, reenvios)
                csv.gravar()

    # Caso o usuário escolha rodar como servidor
    elif segundo_argumento == "servidor":
        for tamanho in TAMANHOS:
            for i in range(NUMERO_DE_TESTES):
                servidor = Servidor(primeiro_argumento, HOST, PORTA, garantia)
                servidor.receber_arquivo(tamanho)
    
    else:
        print("Segundo argumento incorreto.")
        exit(-1)
else:
    print("Faltando argumentos.")
    exit(-1)

