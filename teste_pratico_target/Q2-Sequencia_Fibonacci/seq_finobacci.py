#função da sequencia de Fibonacci.
def verifica_fibonacci(num):   #define a função e o parametro 'num' sendo o que posteriormente receberá a entrada.
    
    a, b = 0, 1    #duas variáveis que recebem a sequência inicial.
    
 # estrutura de repetição utilizando os valores iniciais e o parametro, 
 # que enquanto o primeiro valor for menor que o valor dado, 'a' se tornará 'b', e 'b' se tornará 'a' + 'b',
 # se dando a sequencia de fibonacci.
    while a < num:
        a, b = b, a + b  
# retorna TRUE ou FALSE se  o numero pertence ou não à sequência. 
    return a == num                 

# Utilizando a função recebendo um valor para o parâmetro 'num' usando a variável 'numero' e por fim
# utilizando condicional simples para imprimir a mensagem nas situações em que a função retorna TRUE e FALSE.
numero = int(input("Informe um número: "))

if verifica_fibonacci(numero):  
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")