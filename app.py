import os
def exibir_nome_do_programa():
      print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")
def finaliza_app():
      os.system('cls')
      print ('finalizado o app\n')

def exibir_opcoes():
      print("1.Cadastrar restaurante")
      print("2.Lista restaurante")
      print("3.Ativar restaurante")
      print("4.sai\n")

Opcao_escolha= int(input("Escolha uma opção"))

def escolher_opcao():
      if Opcao_escolha == 1 :
       print('Cadastrar restaurante')
      elif Opcao_escolha == 2:
            print('Lista restaurante')
      elif Opcao_escolha == 3:
            print('Ativar restaurante')
      else :
       print('Encerrado o programa')

      finaliza_app()

def main():
      exibir_nome_do_programa()

if __name__ == '__main__':
    main()