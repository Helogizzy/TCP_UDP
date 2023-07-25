# Multiplicação de Matrizes - OpenMP

>Colaboradoras: Ellen Bonafin ([GitHub Profile](https://github.com/EllenBonafin)) e Heloisa Alves ([Github Profile](https://github.com/Helogizzy))

## Descrição do Problema
O objetivo central é apresentar uma análise de desempenho de um algoritmo paralelizado de multiplicação de matrizes. Utilizaremos a linguagem C, que tem como suporte a biblioteca OpenMP para o modelo de programação paralela de memória compartilhada. 

## Ambiente de execução

Foi utilizado o supercomputador Santos Dumont (SDumont) por meio de uma VPN (rede privada virtual) para a execução do algoritmo. O SDumont está localizado na sede do Laboratório Nacional de Computação Científica (LNCC), em Petrópolis – RJ. 

Possui uma configuração híbrida de nós computacionais que são interligados por uma rede de interconexão Infiniband proporcionando alto rendimento e baixa latência tanto para comunicação entre os processos quanto para o acesso ao sistema de arquivos (SINAPAD, 2014).

## Código-fonte sequencial e paralelo
O código está submetido em sua versão paralela, para deixar sequencial será necessário comentar as linhas: 

22 
```
omp_set_num_threads(2);
```
24
```
#pragma omp parallel for private(aux,j,k) firstprivate(l,c) shared(i)
```

## Detalhes da paralelização
Para a realização dos testes utilizamos a versão 9.3 do gcc (compilador C) e adotamos a multiplicações de matrizes das seguintes dimensões: 1000x1000, 2000x2000, 4000x4000 e 8000x8000. A fim de avaliar o impacto no tempo de processamento do algoritmo paralelo, cada umas das dimensões receberam testes de 1, 2, 4, 8, 16 e 24 threads. 

Os resultados são apresentados em segundos por meio da função omp_get_wtime. A seguinte função “retorna um valor de precisão dupla igual ao número de segundos desde o valor inicial do relógio de tempo real do sistema operacional”.

## Análise de desempenho
Em andamento...

## Referências

BRASIL. Ministério da ciência, tecnologia e inovações. Projeto Sistema de Computação Petaflópica do SINAPAD. Configuração do SDumont. Laboratório Nacional de Computação Científica, 2014. Disponível em: < https://sdumont.lncc.br/machine.php?pg=machine >. Acesso em: 29/07/2022.

IBM. XL Fortran for AIX 15.1.0. 2021. Omp_get_wtime(). Disponível em: < https://www.ibm.com/docs/en/xl-fortran-aix/15.1.0?topic=openmp-omp-get-wtime>. Acesso em: 31/07/2022.
# TCP_UDP
