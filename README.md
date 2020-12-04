# Trabalho Fluxo
### Primeiro trabalho de back-end(Roberto Carletto)
O programa utiliza um sistema simples de interação com o usuário, bastando escolher as opções que as funções utilizam os métodos e atributos dos objetos
~~~Python
def main():
    print("Escolha uma opção:")
    print("1 - Cadastrar um lutador")
    print("2 - Agendar uma luta")
    print("3 - Apresentar uma luta")
    print("4 - Promover uma luta")
    print("5 - Ver o histórico de um lutador")
    print("6 - Sair")
    
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
while True:
    main()
    
~~~
