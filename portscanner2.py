import sys
import socket

argumentos = sys.argv
#arg[1] = method (if via terminal)
#arg[2] = port
#arg[3] = host

def ajuda():
    print("\n\t\t\t\t--- PortScanner ---\n\nPara iniciar o programa pela entrada de comandos, basta utilizar o seguinte escopo\n\nEntrada via argumentos (terminal or term):\nPorta desejada e em seguida Host na qual deseja fazer a varredura.\nExemplo:\n$ python portscanner2.py scan 80 www.site.com\n\nUtilizacao via console, para uma varredura de varias portas. Para iniciar o programa via console basta iniciar como: python portscanner2.py main\n\nCaso tenha duvidas contate meu GitHub: github.com/slackbot115\n\n#METODO MAIN EM MANUTENCAO, NAO UTILIZAVEL#")

#----------------------- METHODS -----------------------#

def scan(portas, host):
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.settimeout(0.5)
        codigo = cliente.connect_ex((host, int(portas)))
        if codigo == 0:
            print(portas, 'OPEN')
        else:
            print('Porta',portas,'fechada/recusada')

def main():
    host = input('Digite o host na qual deseja fazer a varredura: ')
    while True:
        portas = input('Digite a porta para fazer a verificacao: ')
        scan(portas, host)
        op = input('Deseja continuar a verificar portas?:\n'
                   '[S]im ou [N]ao: ')
        if op == 's' or op == 'S':
            scan(portas, host)
        else:
            print('Saindo do programa...')
    exit()
    
ajuda()
try:
    if argumentos[1] == "terminal" or argumentos[1] == "term":
        scan(argumentos[2], argumentos[3])
    #elif argumentos[1] == "main":
     #   main()
except Exception as error:
    if error == "list index out of range":
        print("")
        