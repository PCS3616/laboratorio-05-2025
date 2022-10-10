# PCS3616 - Laboratório 5 - MVN 2

Nesta aula vamos continuar o trabalho da semana passada, hoje você deve
criar mais alguns programas em linguagem de máquina de MVN.

**Exercícios**

1.  Escrever um programa que determina, para três valores a, b e c se
    estes valores: não formam um triângulo, formam um triângulo
    retângulo, triângulo acutângulo ou triângulo obtusângulo (valores 0,
    1, 2, 3, respectivamente). Usar as posições 0x010, 0x012, 0x014 para
    os valores a, b e c e a posição 0x016 para o resultado.

**Entrega:** enviar um arquivo zip com nome **triangulos.zip** contendo
um único arquivo chamado **triangulos.mvn**.

2.  Desenvolva duas sub-rotinas (OP2MNEM e MNEM2OP), cujas finalidades
    são:

-   OP2MNEM (endereço inicial: 0x100) converte um número inteiro dado, 0
    ≤ n ≤ 15, localizado na posição de memória OPCODE (0x010) no
    mnemônico correspondente, formado por dois caracteres ASCII
    (consultar a tabela de mnemônicos fornecida adiante). O mnemônico
    deverá ser armazenado na posição de memória MNEM (0x012).

-   MNEM2OP (endereço inicial: 0x200) faz a conversão oposta,
    transformando um mnemônico válido localizado em MNEM, dado como dois
    caracteres ASCII, em um número inteiro correspondente, , 0 ≤ n ≤ 15,
    armazenado na posição de memória OPCODE, novamente conforme a tabela
    de mnemônicos fornecida.

-   Um pequeno programa principal (endereço inicial: 0x300) deve
    ilustrar o uso das duas sub-rotinas.

Observação: ambos os parâmetros, MNEM e OPCODE, são representados como
inteiros, ocupando, cada qual, dois bytes de memória.

Exemplo de operação:

-   Dado o OPCODE 0x0001, armazenado na posição OPCODE e OPCODE + 1 de
    memória, contendo respectivamente os bytes 00 e 01, a sub-rotina
    OP2MNEM retorna como resultado o par de letras JZ (*jump if zero*),
    cujos códigos ASCII são 4A e 5A, respectivamente. Em outras
    palavras, a posição de memória MNEM deverá conter o byte 0x4A e a
    posição MNEM+1 deverá conter o byte 0x5A.

-   Dado o mnemônico JZ em (MNEM, MNEM+1), ou seja, dado o par de bytes
    (0x4A, 0x5A), a sub-rotina MNEM2OP retornará em (OPCODE, OPCODE+1) o
    par de bytes (00, 01).

  ------------------------------------------------------------------------
  **Opcode (hexa)** **Mnemônico**   **Significado**
  ----------------- --------------- --------------------------------------
  0                 JP              Jump

  1                 JZ              Jump if zero

  2                 JN              Jump if negative

  3                 LV              Load value

  4                 AD              Add

  5                 SB              Subtract

  6                 ML              Multiply

  7                 DV              Divide

  8                 LD              Load

  9                 MM              Memory

  A                 SC              Subroutine Call

  B                 RS              Return from subroutine

  C                 HM              Halt Machine

  D                 GD              Get Data

  E                 PD              Put Data

  F                 OS              Operating System
  ------------------------------------------------------------------------

**Entrega:** enviar um arquivo zip com nome **op-mnem.zip** contendo um
único arquivo chamado **op-mnem.mvn**.

3.  Desenvolva um programa para a MVN que calcule e tabele, a partir da
    posição de memória 0x100, os quadrados perfeitos dos 64 primeiros
    números naturais (0x0, 0x1, 0x2, ..., 0x3F). O cálculo deverá ser
    realizado aplicando a seguinte interessante propriedade:

![n\^2=\\sum\_{i=0}\^{n-1}(2i+1)](./media/image2.gif){width="1.5833333333333333in"
height="0.6666666666666666in"}\*

Cada quadrado calculado deverá ser armazenado como um inteiro de dois
bytes, iniciando na posição de memória 0x100, ou seja, ao final da
execução, os valores das posições de memória serão:

  ------------------------------------------------------------------------
  **Posição (hexa)**      **Valor      **Valor         **N**
                          (hexa)**     (decimal)**     
  ----------------------- ------------ --------------- -------------------
  100                     0000         0               0

  102                     0001         1               1

  104                     0004         4               2

  \...                    \...                         \...

  1**??**                 0**???**     3969            63
  ------------------------------------------------------------------------

**Entrega:** enviar um arquivo zip com nome **quadrados-perfeitos.zip**
contendo um único arquivo chamado **quadrados-perfeitos.mvn**.

OBS.: caso você encontre problemas em algum exercício devido ao evitador
de loops infinitos, você pode mudar o valor do número máximo de passos
acionando a flag "-s \[valor\]" ou "\--max_step \[valor\]", trocando
"\[valor\]" pelo limite de passos que você queira definir, ao chamar o
módulo "mvnMonitor.py".

\*:mostração intuitiva da fórmula

![](./media/image1.png){width="2.375in" height="2.15625in"}
