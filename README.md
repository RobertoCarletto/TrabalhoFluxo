# Trabalho Fluxo
### Primeiro trabalho de back-end(Roberto Carletto)
Segue o código:
~~~Python
from random import randint
lutadores = []
class Lutador:
    vitorias = 0
    derrotas = 0
    empates = 0
    def __init__(self,nome,peso,forca):
        self.nome = nome
        self.peso = peso
        self.forca = forca
    def vitoria(self):
        self.vitorias += 1
    def derrota(self):
        self.derrotas += 1
    def empate(self):
        self.empates += 1
    def historico(self):
        print(self.vitorias,'vitórias')
        print(self.derrotas,'derrotas')
        print(self.empates,'empates')

class Luta:
    def __init__(self,lutador1,lutador2):
        if abs(lutador1.peso - lutador2.peso) > 5:
            print('Luta inválida, os combatentes são de categorias diferentes.')
            return None
        a1 = lutador1.forca + randint(0,5)
        a2 = lutador2.forca + randint(0,5)
        print("O ataque do",lutador1.nome,"é de",a1)
        print("O ataque do",lutador2.nome,"é de",a2)
        if a1 > a2:
            lutador1.vitoria()
            lutador2.derrota()
            print(lutador1.nome,'venceu!')
        elif a1 < a2:
            lutador2.vitoria()
            lutador1.derrota()
            print(lutador2.nome,'venceu!')
        elif a1 == a2:
            lutador1.empate()
            lutador2.empate()
            print('Empate!')

def cadastra_lutador():
    nome = input("Insira o nome do lutador: ")
    peso = int(input("Insira o peso do lutador em quilos: "))
    forca = int(input("Insira a força do lutador numa escala de 0 a 10: "))
    lutadores.append(Lutador(nome,peso,forca))
    print('')
    print("Cadastro completo.")

def criar_luta():
    lutador1 = input("Insira o nome de um lutador cadastrado: ")
    lutador2 = input("Insira o nome de outro lutador cadastrado: ")
    luta = []
    for i in lutadores:
        if i.nome == lutador1 or i.nome == lutador2:
            luta.append(i)
    try:
        Luta(luta[0],luta[1])
    except:
        print("Lutador não encontrado!")

def mostrar_historico():
    lutador = input("Insira o nome do lutador: ")
    try:
        lutador.historico()
    except:
        print("Lutador não encontrado!")

def main():
    print("Escolha uma opção:")
    print("1 - Cadastrar um lutador")
    print("2 - Criar uma luta")
    print("3 - Ver o histórico de um lutador")
    print("4 - Sair")
    print('')
    entrada = int(input('-> '))
    print('')
    print('')
    if entrada == 1:
        cadastra_lutador()
    elif entrada == 2:
        criar_luta()
    elif entrada == 3:
        mostrar_historico()
    elif entrada == 4:
        exit()
    print('')
    print('')
    print('')
    
while True:
    main()
    
~~~
