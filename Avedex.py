catalogo_aves = [

{

"codigo": "1",

"nome_popular": "Bem-te-vi",

"nome_cientifico": "Pitangus sulphuratus",

"habitat": "Áreas abertas, cidades e bordas de florestas",

"alimentacao": "Insetos, frutos e pequenos animais",

"curiosidade": "Seu canto lembra a expressão bem-te-vi."

},

{

"codigo": "2",

"nome_popular": "Canário-da-terra",

"nome_cientifico": "Sicalis flaveola",

"habitat": "Campos, áreas abertas e ambientes rurais",

"alimentacao": "Sementes e pequenos insetos",

"curiosidade": "O macho possui plumagem amarela intensa."

},

{

"codigo": "3",

"nome_popular": "João-de-barro",

"nome_cientifico": "Furnarius rufus",

"habitat": "Campos, cidades e áreas rurais",

"alimentacao": "Insetos e outros pequenos invertebrados",

"curiosidade": "Constrói um ninho de barro característico."

}

]

def Fazer_Login(Login_Menu, Nome_Do_Usuario):
    if (Login_Menu == 0):
        Cidade_Do_Usuario = input("Digite a sua cidade: ").strip()
        Ave_Favorita = input("Digite a sua ave favorita: ").strip()
        Login_Menu = 1

        print("=" * 35)
        print("         DADOS INICIAIS")
        print("=" * 35)

        print(f"Nome: {Nome_Do_Usuario}.")
        print(f"Cidade: {Cidade_Do_Usuario}.")
        print(f"Ave favorita: {Ave_Favorita}.")

        return Login_Menu, Cidade_Do_Usuario, Ave_Favorita

    else:
        print("Você já fez o login.\n")
        print("=" * 35)
        print("         DADOS INICIAIS")
        print("=" * 35)

        print(f"Nome: {Nome_Do_Usuario}.")
        print(f"Cidade: {Cidade_Do_Usuario}.")
        print(f"Ave favorita: {Ave_Favorita}.")

        return Login_Menu, Cidade_Do_Usuario, Ave_Favorita


def Conhecer_Ave():
def Conhecer_Ave():
    print("=" * 35)
    print("         CATÁLOGO DE AVES")
    print("=" * 35)

    for ave in catalogo_aves:
        print(f"Código: {ave['codigo']}")
        print(f"Nome popular: {ave['nome_popular']}")
        print(f"Nome científico: {ave['nome_cientifico']}")
        print(f"Habitat: {ave['habitat']}")
        print(f"Alimentação: {ave['alimentacao']}")
        print(f"Curiosidade: {ave['curiosidade']}")
        print("-" * 35)


def Sobre_Avedex(Nome_Do_Usuario):
    print(f"Olá {Nome_Do_Usuario}, seja bem-vindo ao AVEDEX!")
    print("Aqui construiremos um catálogo interativo sobre aves")
    print("e aprenderemos sobre boas práticas de programação :D.")


def Cadastrar_Ave():
    print("=" * 35)
    print("         CADASTRO DE AVE")
    print("=" * 35)

    Nome_Ave = input("Digite o Nome da ave: ")
    Nome_Cientifico = input("Digite o nome Científico da ave: ")
    Habitat = input("Digite o Habitat da ave: ")
    Alimentação = input("Digite a Alimentação da ave: ")

    print("Ave cadastrada com sucesso!")
    print("Verifique a opção 5 para ver as informações!")

    return Nome_Ave, Nome_Cientifico, Habitat, Alimentação


def Ver_Ave(Cadastro_Ave, Nome_Ave, Nome_Cientifico, Habitat, Alimentação):
    if (Cadastro_Ave == 0):
        print("Nenhuma ave cadastrada, acesse a opção 4 para cadastrar uma ave!")

    else:
        print("=" * 35)
        print("         AVE CADASTRADA")
        print("=" * 35)
        print(f"Nome da ave: {Nome_Ave}")
        print(f"Nome Científico: {Nome_Cientifico}")
        print(f"Habitat: {Habitat}")
        print(f"Alimentação: {Alimentação}")


# =====================================
# PROGRAMA PRINCIPAL
# =====================================

Login_Menu = 0
Cadastro_Ave = 0
Loop = 1

# Variáveis da ave cadastrada
Nome_Ave = ""
Nome_Cientifico = ""
Habitat = ""
Alimentação = ""

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

    print(35 * "-")

    if (Opcao_Menu == 1):

        Login_Menu, Cidade_Do_Usuario, Ave_Favorita = Fazer_Login(
            Login_Menu,
            Nome_Do_Usuario
        )

    elif (Opcao_Menu == 2):

        Conhecer_Ave()

    elif (Opcao_Menu == 3):

        Sobre_Avedex(Nome_Do_Usuario)

    elif (Opcao_Menu == 4):

        Nome_Ave, Nome_Cientifico, Habitat, Alimentação = Cadastrar_Ave()
        Cadastro_Ave = 1

    elif (Opcao_Menu == 5):

        Ver_Ave(
            Cadastro_Ave,
            Nome_Ave,
            Nome_Cientifico,
            Habitat,
            Alimentação
        )

    elif (Opcao_Menu == 6):

        print("Encerrando o programa.")
        Loop = 0

    else:

        print("Você digitou uma opção inválida.\nTente novamente.")