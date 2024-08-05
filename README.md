# calculator_python

Esse código representa uma calculadora simples em Python que permite ao usuário realizar as operações básicas de adição, subtração, multiplicação e divisão.

** **Funções** **
1. add(x, y): Retorna a soma de x e y.
2. subtract(x, y): Retorna a subtração de y de x.
3. multiply(x, y): Retorna o produto de x e y.
4. divide(x, y): Retorna a divisão de x por y, mas antes verifica se y é igual a zero para evitar uma divisão por zero, retornando uma mensagem de erro se for o caso.

** **Função calculator()** **
* Esta função interage com o usuário para selecionar a operação desejada e executar o cálculo correspondente.
* Primeiramente, apresenta um menu com as operações disponíveis: adição, subtração, multiplicação e divisão.
* Em um loop while, a função solicita ao usuário a escolha de uma operação e os dois números para o cálculo.
* O programa trata entradas inválidas com uma verificação de erros ao tentar converter as entradas para float.
* Para cada operação, é chamada a função correspondente, e o resultado é exibido ao usuário.
* Após a exibição do resultado, o usuário é questionado se deseja realizar outra operação. Caso contrário, o loop é encerrado, e a função finaliza com uma mensagem de agradecimento.
  
** **Observações** **
* A função divide inclui uma verificação para divisão por zero, evitando assim uma exceção de runtime.
* O loop principal permite que o usuário realize múltiplas operações sem reiniciar o programa.
* O código é simples e eficaz para operações básicas de calculadora, proporcionando uma interface de texto interativa.
