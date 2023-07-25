from Cliente_TCP import Cliente_TCP
import time
import pandas as pd

tamanho_pacotes = [100, 500, 1000]
HEADER_SIZE = 66 # Tamanho do cabeçalho em cada pacote

for tamanho in tamanho_pacotes: # Itera sobre os diferentes tamanho de pacotes de dados
    tempos = []
    sizes = []
    total_pacotes = []

    for i in range(10): # Executa 10 iterações de teste para cada tamanho de dados
        time.sleep(1)
        tempo, contador_pacotes = Cliente_TCP(tamanho, HEADER_SIZE) # Inicia a comunicação
        tempos.append(tempo)
        sizes.append(tamanho)
        total_pacotes.append(contador_pacotes)
        print(f"Iteração {i} feita para o tamanho: {tamanho}, em: {tempo} seg")
    time.sleep(1)

    resultados = pd.DataFrame({ # Armazena os resultados
            'Tamanho': sizes,
            'Tempos': tempos,
            'Pacotes': total_pacotes
    })

    if tamanho==100:
        resultados.to_csv("ResultadosTCP.csv",index=False)
    else:
        file_df = pd.read_csv("ResultadosTCP.csv")
        file_df = pd.concat([file_df,resultados], ignore_index=True)
        file_df.to_csv("ResultadosTCP.csv",index=False)