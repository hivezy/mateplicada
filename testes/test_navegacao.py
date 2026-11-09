from enum import Enum


class Etapa(Enum):
    PRIMEIRONUM = "num1"
    OPERACAO = "operacao"
    SEGUNDONUM = "num2"


class Comando(Enum):
    VOLTAR = "voltar"
    SAIR = "sair"


etapa = Etapa.PRIMEIRONUM

while True:

    print(f"\nEtapa atual: {etapa.value}")

    comando = input("Digite um comando: ").strip().lower()

    if comando == Comando.SAIR.value:
        break

    elif comando == Comando.VOLTAR.value:

        if etapa == Etapa.SEGUNDONUM:
            etapa = Etapa.OPERACAO

        elif etapa == Etapa.OPERACAO:
            etapa = Etapa.PRIMEIRONUM

        else:
            print("\nVocê já está na primeira etapa.")

    elif comando == "avançar":

        if etapa == Etapa.PRIMEIRONUM:
            etapa = Etapa.OPERACAO

        elif etapa == Etapa.OPERACAO:
            etapa = Etapa.SEGUNDONUM

        else:
            print("\nVocê já está na última etapa.")

    else:
        print("\nComando inválido.")

print("\nMateplicada encerrada. Até logo!")