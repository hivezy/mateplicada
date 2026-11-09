from enum import Enum

class Etapa(Enum):
    """As etapas básicas da calculadora."""

    PRIMEIRONUM = "num1"
    SEGUNDONUM = "num2"
    OPERACAO = "operacao"

class Comando(Enum):
    "Os comandos da calculadora."

    VOLTAR = "voltar"
    SAIR = "sair"

class Navegacao:
    """Navegação da Mateplicada."""

    def voltar(etapa_atual):
        """Retorna a etapa anterior da calculadora."""

        if etapa_atual == Etapa.SEGUNDONUM:
            return Etapa.OPERACAO

        elif etapa_atual == Etapa.OPERACAO:
            return Etapa.PRIMEIRONUM

        return etapa_atual

    def sair():
        """Solicita o encerramento da calculadora."""
        return True