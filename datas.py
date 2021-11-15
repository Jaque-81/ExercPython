class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def mostraData(self):
        print(f"{self.dia:2d}/{self.mes:2d}/{self.ano}")
