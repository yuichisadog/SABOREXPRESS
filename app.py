import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo':False},
                {'nome':'Pizza suprema', 'categoria' : 'Pizza', 'ativo':True},
                 {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo':False}]


def exibir_nome_do_programa():
     '''exibe o nome do programa, como já dito'''
     print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░█████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░██║░░██║
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗██║░░██║
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝╚█████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░░╚════╝░
      
      """)
def exibir_opcoes():
      '''exibe todas as opçoes na tela do usuario'''
      print('1. cadastrar restaurante')
      print('2. listar restaurante')
      print('3. alternar estado do restaurante')
      print('4. Sair\n')

def finalizar_app():
    '''Responsável por exibir o subtitulo de finalizacao do app e pela tecla de retorno ao escolher qualquer uma das opçoes e fazer o output'''
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    '''Responsável pela tecla de retorno ao escolher qualquer uma das opçoes e fazer o output'''
    input('Digite uma tecla para voltar ao menu')
    main()



def opcao_invalida():
    '''Quando o usuário faz um output que não é esperado pelo programa'''
    print('opçao invalida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Exibe o subtitulo ao escolher uma das opçoes'''
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa funçao é responsavel por cadastrar um novo restaurante
    
    Inputs:
    - NOME DO RESTAURANTE
    - CATEGORIA

    Output:
    -Adiciona um novo restaurante a lista de restaurantes

    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input ('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante,'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadatrado com sucesso!')

    voltar_ao_menu_principal()

def listar_restaurantes():
    ''' Essa funçao é responsavel por mostrar o nome, categoria e se o restaurante está ativo ou desativado'''

    exibir_subtitulo('listando restaurantes')
#para cada restaurante na lista restaurantes:
    for restaurante in restaurantes:
          nome_restaurante = restaurante['nome']
          categoria = restaurante['categoria']
          ativo = 'ativo' if restaurante['ativo'] else 'desativado'
          print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    '''Alterar o estado do restaurante de ativo para desativado ou vice-versa
    '''
    exibir_subtitulo('Alterando estado restaurante\n') 
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado =True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f' O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
          print('o restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
    '''O menu onde você escolhe as opções com funções que foram descritas anteriormente'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
            #opcao_escolhida = int(opcao_escolhida)_

        if opcao_escolhida == 1:
                cadastrar_novo_restaurante()
                print('Cadastrar restaurante')
        elif opcao_escolhida == 2:
                listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
                finalizar_app()
        else:
                opcao_invalida()
    except:
           opcao_invalida()

def main():
       '''Essa funçao é responsavel por limpar a tela quando você escolhe uma das funções'''
       os.system('cls')
       exibir_nome_do_programa()
       exibir_opcoes()
       escolher_opcao()
   
if __name__ =='__main__':
            main()


