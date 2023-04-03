from downloader.youtube_downloader import *

if __name__ == "__main__":

    def exibir_menu():
        print("Escolha uma opção:")
        print("1. Youtube Downloader")
        print("2. File Converter")
        print("3. Sair")


    def tratar_opcao(opcao):
        if opcao == "1":
            print("Opção 1 selecionada")
            download()
        elif opcao == "2":
            print("Opção 2 selecionada")
        elif opcao == "3":
            print("Saindo...")
            exit()
        else:
            print("Opção inválida. Tente novamente.")


    while True:
        exibir_menu()
        opcao = input("Opção selecionada: ")
        tratar_opcao(opcao)
