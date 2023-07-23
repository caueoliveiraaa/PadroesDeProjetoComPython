from fabrica_fila import FabricaFila
import os
from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida


def main():
    os.system('cls')
    teste_fabrica = FabricaFila.pega_fila('normal')
    teste_fabrica.atualiza_fila()
    teste_fabrica.atualiza_fila()
    teste_fabrica.atualiza_fila()
    print(teste_fabrica.chama_cliente(10))
    print(teste_fabrica.chama_cliente(1))

    teste_fabrica_2 = FabricaFila.pega_fila('prioritaria')
    teste_fabrica_2.atualiza_fila()
    teste_fabrica_2.atualiza_fila()
    teste_fabrica_2.atualiza_fila()
    print(teste_fabrica_2.chama_cliente(5))
    print(teste_fabrica_2.estatistica(EstatisticaResumida('10/01/1973', 198)))
    print(teste_fabrica_2.estatistica(EstatisticaDetalhada('19/03/1983', 249)))


if __name__ == '__main__':
    main()