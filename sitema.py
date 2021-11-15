class Sistema:
    def __init__(self):
        self.texto = ''

    def le_entrada(self):
        self.texto = input()

    def exibe_saida(self):
        print(self.texto)

sistema = Sistema()
sistema.le_entrada()
sistema.exibe_saida()