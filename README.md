# Trabalho Fluxo
### Primeiro trabalho de back-end(Roberto Carletto)
O programa utiliza um sistema simples de interação com o usuário, bastando escolher as opções que as funções utilizam os métodos e atributos dos objetos
~~~Python
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
