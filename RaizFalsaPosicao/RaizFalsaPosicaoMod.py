import math

# Definição de variáveis
a = -8             # Inicio do intervalo
b = 0            # Final do intervalo
e = 1e-10          # Indicador de precisão
x = 0              # A variável x é zerada
E = abs(b-a)       # E recebe o tamanho absoluto do intervalo
iteracoes = 0      # Contador de iterações é zerado
cont_a = 0         # Contador de 'cortes' na esquerda
cont_b = 0         # Contador de 'cortes' na direita

def funcao(x):
    #y = math.pow(x, 10) + 1 # 0, 1.3
    y = x + 5 #-8, 0
    #y = math.sqrt(9.81*x/0.25) * math.tanh(4 * math.sqrt(9.81 * 0.25 / x)) -36 #50, 200
    return y

# São impressos a equação e o intervalo
print("Função y = x + 5")
print("Intervalo: [", a, ",", b, "]\n")

# Loop Principal
while (E > e):
    # Incremento no contador de iterações
    iteracoes += 1
    
    # E é atualizado
    E = abs(b-a)
    
    # São calculados os valores de x, f(a), f(b), e f(x)
    y_a = funcao(a)
    y_b = funcao(b)
    if cont_a > 1:
        y_a = y_a / 2
    if cont_b > 1:
        y_b = y_b / 2
    
    x = b - (y_b * (b-a))/(y_b - y_a)
    y_x = funcao(x)
    
    # É testado se algum dos limites, a, b, ou x, é a raiz
    if y_a == 0:
        print(a, "é zero\n")
        break
    
    if y_b == 0:
        print(b, "é zero\n")
        break
    
    if y_x == 0:
        print(x, "é zero\n")
        break
    
    # Os limites do intervalo são reestabelecidos
    if y_x*y_b < 0:
        a = x 
        cont_a += 1
    else:
        b = x
        cont_b += 1
print("Número de Iterações: ", iteracoes)