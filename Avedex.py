Login_Menu = 0
Cadastro_Ave = 0
Loop = 1
    
print("=" * 35)
print("             AVEDEX")
print("=" * 35)

Nome_Do_Usuario = input("Digite o seu nome: ").strip()
print(f"Olá, {Nome_Do_Usuario}!")

while (Loop == 1):


    print("-" * 35)
    print("             MENU")
    print("-" * 35)
    print("1- Fazer Login;")
    print("2- Conhecer uma ave;")
    print("3- Sobre o AVEDEX;")
    print("4- Cadastrar uma ave;")
    print("5- Ver ave cadastrada;")
    print("6- Fechar o programa;")
    Opcao_Menu = int(input("Digite uma opção válida: "))
    print(35*"-")
    
    if (Opcao_Menu == 1 and Login_Menu == 0):
        Cidade_Do_Usuario = input("Digite a sua cidade: ").strip()
        Ave_Favorita = input("Digite a sua ave favorita: ").strip()
        Login_Menu = 1
    
        print("=" * 35)
        print("         DADOS INICIAIS")
        print("=" * 35)
    
        print(f"Nome: {Nome_Do_Usuario}.")
        print(f"Cidade: {Cidade_Do_Usuario}.")
        print(f"Ave favorita:{Ave_Favorita}.")
        
    elif (Opcao_Menu == 1 and Login_Menu != 0):
        print("Você já fez o login.\n")
        print("=" * 35)
        print("         DADOS INICIAIS")
        print("=" * 35)
    
        print(f"Nome: {Nome_Do_Usuario}.")
        print(f"Cidade: {Cidade_Do_Usuario}.")
        print(f"Ave favorita:{Ave_Favorita}.")
        
    elif (Opcao_Menu == 2):
        print("Você escolheu Conhecer uma ave:")
        print("Nome da ave: Carcará.")
        print("Nome Científico: Caracara plancus.")
        print("Habitat: Cerrado.")
        print("Descrição: O carcará é facilmente reconhecível, quando pousado, pelo fato de ter um penacho\n preto sobre a cabeça parecido com um solidéu, assim como o bico adunco e alto, que\n se assemelha à lâmina de um cutelo; a face, chamada de cera, varia do vermelho ou\n laranja quando está calmo, ao amarelo quando está irritado, disputando território ou\n alimento.")
        print("Alimentação: Carniças, pequenos invertebrados e grãos.")
    
    
    elif (Opcao_Menu == 3):
        print(f"Olá {Nome_Do_Usuario}, seja bem-vindo ao AVEDEX!")
        print("Aqui construiremos um catálogo interativo sobre aves e aprenderemos sobre boas práticas de programação :D . ")
        
    elif (Opcao_Menu == 4):
        print("=" * 35)
        print("         CADASTRO DE AVE")
        print("=" * 35)
        Nome_Ave = (input("Digite o Nome da ave: "))
        Nome_Cientifico = (input("Digite o nome Científico da ave: "))
        Habitat = (input("Digite o Habitat da ave: "))
        Alimentação = (input("Digite a Alimentação da ave: "))
        Cadastro_Ave = 1
        print("Ave cadastrada com suscesso!\nVerifique a opção 5 para ver as informações!")
    
    elif (Opcao_Menu == 5 and Cadastro_Ave == 0):
        print("Nenhuma ave cadastrada, acesse a opção 4 para cadastrar uma ave!")
        
    elif (Opcao_Menu == 5 and Cadastro_Ave == 1):
        print("=" * 35)
        print("         AVE CADASTRADA")
        print("=" * 35)
        print(f"Nome da ave: {Nome_Ave}")
        print(f"Nome Científico: {Nome_Cientifico}")
        print(f"Habitat: {Habitat}")
        print(f"Alimentação: {Alimentação}")
        
    elif (Opcao_Menu == 6):
        print("Encerrando o programa.")
        Loop = 0
    
    else :
        print("Você digitou uma opção inválida.\nTente novamente.")