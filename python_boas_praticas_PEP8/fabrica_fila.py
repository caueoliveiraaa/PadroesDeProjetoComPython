from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria
from constantes import TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA
from typing import Union


class FabricaFila:
    @staticmethod
    def pega_fila(tipo_fila) -> Union[FilaNormal, FilaPrioritaria]:
        if tipo_fila == 'normal':
            return FilaNormal()
        elif tipo_fila == 'prioritaria':
            return FilaPrioritaria()
        else:
            raise NotImplementedError('Tipo de fila não existe.')