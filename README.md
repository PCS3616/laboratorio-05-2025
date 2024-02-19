# PCS3616 - Laboratório 5 - MVN 3

Nesta aula vamos continuar o trabalho da semana passada, hoje você deve
criar mais alguns programas em linguagem de máquina de MVN.

## 1. `quadrados-perfeitos.mvn`
Desenvolva um programa para a MVN que calcule e tabele, a partir da
posição de memória 0x100, os quadrados perfeitos dos 64 primeiros
números naturais (0x0, 0x1, 0x2, ..., 0x3F). O cálculo deverá ser
realizado aplicando a seguinte interessante propriedade:

$$n^2=\sum_{i=0}^{n-1}(2i+1)$$

Cada quadrado calculado deverá ser armazenado como um inteiro de dois
bytes, iniciando na posição de memória 0x100, ou seja, ao final da
execução, os valores das posições de memória serão:

 |Posição (hexa)         |Valor (hexa)|Valor (decimal)|N                 |
 |-----------------------|------------|---------------|------------------|
 |100                    |0000        |0              |0                 |
 |102                    |0001        |1              |1                 |
 |104                    |0004        |4              |2                 |
 |...                    |...         |               |...               |
 |1??                    |0???        |3969           |63                |

OBS.: caso você encontre problemas em algum exercício devido ao evitador
de loops infinitos, você pode mudar o valor do número máximo de passos
acionando a flag "-s \[valor\]" ou "\--max_step \[valor\]", trocando
"\[valor\]" pelo limite de passos que você queira definir, ao chamar o
módulo "mvnMonitor.py".

\*:mostração intuitiva da fórmula

![](./media/image1.png)

## 2. `io.mvn`
Escrever um programa que lê dois números do teclado
(`x` e `y`), e imprime o valor de `x+y`. Observações:

- `0 <= x`, `y <= 99`

- Os números devem ser lidos do teclado, em uma única linha, no
formato `<x-d1><x-d2><s><s><y-d1><y-d2>`, onde:

  - `<x-d1>` é o primeiro dígito de x. Se `x < 10`, o dígito
  informado deve ser `0`.

  - `<x-d2>` é o segundo dígito de `x`.

  - `<s>` é um espaço em branco

  - `<y-d1>` é o primeiro dígito de `y`. Se `y < 10`, o dígito
  informado deve ser `0`.

  - `<x-d2>` é o segundo dígito de `y`.

Por exemplo, \"07 54\" é uma entrada válida, e o programa deve imprimir
\"61\" na saída. Lembrando que em ASCII 07 é 0x3037 e 54 é 0x3534, enquanto 61 é 0x3631.

Para realizar esse exercício, utilize o seguinte algoritmo:

- Subtraia 0x3030 de ambos os números obtidos pelo teclado.
- Some esses números.
- Caso o dígito menos significativo do número resultante da soma, seja maior ou igual a A, subtraia 0x000A e some 0x0100 para realizar o "vai-um".
- Soma 0x3030 ao número resultante do passo anterior.
- Imprima esse número no monitor.

OBS.: Consulte a [tabela ASCII](http://ascii.cl/)