from datetime import datetime 


class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def formatar_data(self):
        return f"{self.dia}/{self.mes}/{self.ano}"
    

if __name__ == "__main__":
    d = Data(25, 10, 2010)
    print(d.formatar_data())
        