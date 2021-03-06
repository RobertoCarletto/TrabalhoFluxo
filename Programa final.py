from random import randint
lutadores = []
lutas = []
class Lutador:

    vitorias = 0
    derrotas = 0
    empates = 0

    def __init__(self,nome,peso,forca):

        if not isinstance(peso,float):
            print("Peso inválido!")
            return None

        if not isinstance(forca,int) or forca < 0 or forca > 10:
            print("Força inválida!")
            return None

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

        if not isinstance(lutador1,Lutador) or not isinstance(lutador2,Lutador):
            print("Luta inválida!")
            return None

        if abs(lutador1.peso - lutador2.peso) > 5:
            print('Luta inválida, os combatentes são de categorias diferentes.')
            raise ValueError

        self.lutador1 = lutador1
        self.lutador2 = lutador2

    def combatentes(self):
        return self.lutador1.nome,self.lutador2.nome
    
    def apresentacao(self):
        print(self.lutador1.nome,'pesa',self.lutador1.peso,'e tem um cartel de:')
        self.lutador1.historico()
        print(self.lutador2.nome,'pesa',self.lutador2.peso,'e tem um cartel de:')
        self.lutador2.historico()
        
    def combate(self):
        a1 = self.lutador1.forca + randint(0,5)
        a2 = self.lutador2.forca + randint(0,5)
        print("O ataque do",self.lutador1.nome,"é de",a1)
        print("O ataque do",self.lutador2.nome,"é de",a2)

        if a1 > a2:
            self.lutador1.vitoria()
            self.lutador2.derrota()
            print(self.lutador1.nome,'venceu!')

        elif a1 < a2:
            self.lutador2.vitoria()
            self.lutador1.derrota()
            print(self.lutador2.nome,'venceu!')

        elif a1 == a2:
            self.lutador1.empate()
            self.lutador2.empate()
            print('Empate!')

def cadastra_lutador():

    try:
        nome = input("Insira o nome do lutador: ")

        for i in lutadores:
            if i.nome == nome:
                print("Este nome já está sendo utilizado!")
                return None
        peso = float(input("Insira o peso do lutador em quilos: "))
        forca = int(input("Insira a força do lutador numa escala de 0 a 10: "))

    except :
        print("Valor inválido!")
        return None

    lutadores.append(Lutador(nome,peso,forca))
    print('')
    print("Cadastro completo.")

def criar_luta():

    if len(lutadores) < 2:
        print("Não há lutadores suficentes cadastrados!")
        return None

    print("Escolha os números dos lutadores:")

    for i in range(len(lutadores)):
        print(i+1,'-',lutadores[i].nome)

    try:
        x = int(input("Primeiro lutador: "))
        y = int(input("Segundo lutador: "))

        if x <= 0 or y <= 0:
            raise ValueError

        lutador1 = lutadores[x-1]
        lutador2 = lutadores[y-1]
        lutas.append(Luta(lutador1,lutador2))
        print('')
        print("Luta agendada!")

    except :
        print("Número inválido!")
        return None

def apresentar():

    if len(lutas) == 0:
        print("Não há lutas agendadas!")
        return None

    print("Escolha o número da luta:")

    for i in range(len(lutas)):
        c1,c2 = lutas[i].combatentes()
        print(i+1,'-',c1,'VS',c2)

    try:
        x = int(input("Luta: "))
        if x <= 0:
            raise ValueError
        lutas[x-1].apresentacao()
    except:
        print("Número inválido!")
        return None


def combater():

    if len(lutas) == 0:
        print("Não há lutas agendadas!")
        return None

    print("Escolha o número da luta:")

    for i in range(len(lutas)):
        c1,c2 = lutas[i].combatentes()
        print(i+1,'-',c1,'VS',c2)

    try:
        x = int(input("Luta: "))
        if x <= 0:
            raise ValueError
        lutas[x-1].combate()
        del lutas[x-1]
    except:
        print("Número inválido!")
        return None
        
def mostrar_historico():

    if len(lutadores) == 0:
        print("Não há lutadores cadastrados!")
        return None

    print("Escolha o número do lutador:")

    for i in range(len(lutadores)):
        print(i+1,'-',lutadores[i].nome)

    try:
        x = int(input("-> "))
        if x <= 0:
            raise ValueError
        print("O hisórico do lutador",lutadores[x-1].nome,"é:")
        lutadores[x-1].historico()
    except:
        print("Número inválido!")
        return None


def main():
    print("Escolha uma opção:")
    print("1 - Cadastrar um lutador")
    print("2 - Agendar uma luta")
    print("3 - Apresentar uma luta")
    print("4 - Promover uma luta")
    print("5 - Ver o histórico de um lutador")
    print("6 - Sair")
    print('')

    try:
        entrada = int(input('-> '))
        if entrada > 6 or entrada < 1:
            raise ValueError
    except:
        print("Entrada inválida!")
        print('')
        return None

    print('')
    print('')

    if entrada == 1:
        cadastra_lutador()

    elif entrada == 2:
        criar_luta()

    elif entrada == 3:
        apresentar()

    elif entrada == 4:
        combater()       

    elif entrada == 5:
        mostrar_historico()

    elif entrada == 6:
        exit()

    print('')
    print('')
    print('')
    
while True:
    main()
