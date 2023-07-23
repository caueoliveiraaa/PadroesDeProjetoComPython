
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero: int = numero
        self.__titular: str = titular
        self.__saldo: float = saldo
        self.__limite: float = limite
        print('Objeto criado com sucesso.')
        
    def deposita(self, valor) -> None:
        print(f"$ {valor} depositado para: {self.__titular}")
        self.__saldo += valor
        
    def __pode_sacar(self, valor_saque):
        valor_disponivel = (self.__saldo + self.__limite)
        return valor_saque <= valor_disponivel
        
    def saca(self, valor) -> None:
        if self.__pode_sacar(valor):
            print(f"Saque de {self.__titular}: $ {valor}")
            self.__saldo -= valor
        else:
            print(f"O valor {valor} passou o limite")
        
    def transfere(self, valor, destino) -> None:
        self.saca(valor)
        destino.deposita(valor)
        print(f"Transferência de $ {valor} de {self.__titular} para {destino.__titular}")
    
    @property
    def saldo(self) -> float:
        return self.__saldo
        
    @property
    def titular(self) -> str:
        return self.__titular
        
    @property
    def limite(self) -> float:
        return self.__limite
    
    @property
    def numero(self) -> int:
        return self.__numero
    
    @limite.setter
    def limite(self, limite) -> None:
        self.__limite = limite
        print(f"Atualizou limite: $ {self.__limite} ({self.__titular})")
        
    @staticmethod
    def codigo_banco() -> str:
        return "001"
    
    @staticmethod
    def codigo_bancos() -> dict:
        return {"BB":"001", "Caixa":"104", "Bradesco":"237"}
        