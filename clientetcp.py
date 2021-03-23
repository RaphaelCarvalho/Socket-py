import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("**A conexão falhou**")
        print("Erro: {}".format(e))
        sys.exit()
    print("**Socket criado com sucesso**")

    HostAlvo = input("Digite o host ou IP a ser conectado: ")
    PortaAlvo = input("Digite a porta a ser conectada: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo))) #O s.conect não aceita string no parametro da porta
        print("Cliente TCP conectado com sucesso no host: " + HostAlvo + " e na porta: " + PortaAlvo)
        s.shutdown(2) #Limitar a 2 segundos de conexão e finaliza-la
    except socket.error as e:
        print("A conexao falhou")
        print("Erro: {}".format(e))
        sys.exit()

if __name__ == "__main__":
    main()