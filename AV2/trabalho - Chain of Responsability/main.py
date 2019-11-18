from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, deposito) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, deposito: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(deposito)

        return None


class Deposito:
    __slots__ = ['banco','valor']

    def __init__(self, banco, valor):
        self.banco = banco
        self.valor = valor

class BBHandler(AbstractHandler):
    __slots__ = ['deposito']
    def handle(self, deposito: Any) -> str:
        if deposito.banco == "001":
            self.deposito = deposito.valor
            return f"\n Depósito realizado no banco: {deposito.banco} no valor: {deposito.valor}"
        else:
            return super().handle(deposito)


class SantanderHandler(AbstractHandler):
    __slots__ = ['deposito']
    def handle(self, deposito: Any) -> str:
        if deposito.banco == "033":
            self.deposito = deposito.valor
            return f"\n Depósito realizado no banco: {deposito.banco} no valor: {deposito.valor}"
        else:
            return super().handle(deposito)


class CaixaHandler(AbstractHandler):
    __slots__ = ['deposito']
    def handle(self, deposito: Any) -> str:
        if deposito.banco == "104":
            self.deposito = deposito.valor
            return f"\n Depósito realizado no banco: {deposito.banco} no valor: {deposito.valor}"
        else:
            return super().handle(deposito)

class BradescoHandler(AbstractHandler):
    __slots__ = ['deposito']
    def handle(self, deposito: Any) -> str:
        if deposito.banco == "237":
            self.deposito = deposito.valor
            return f"\n Depósito realizado no banco: {deposito.banco} no valor: {deposito.valor}"
        else:
            return super().handle(deposito)


def client_code(handler: Handler) -> None:
    continua = True
    while(continua):
        banco = input("\n Informe o Banco a ser depositado.")
        valor = input("\n Informe o valor a ser depositado.")
        deposito = Deposito(banco,valor)
        result = handler.handle(deposito)
        if result:
            continua = False
            print(f"\n {result}", end="\n")
        else:
            continua = True
            print(f"\n {deposito.banco} código do banco não encontrado.", end="\n")


if __name__ == "__main__":
    BB = BBHandler()
    Santander = SantanderHandler()
    Caixa = CaixaHandler()
    Bradesco = BradescoHandler()
    BB.set_next(Santander).set_next(Caixa).set_next(Bradesco)
    client_code(BB)
    