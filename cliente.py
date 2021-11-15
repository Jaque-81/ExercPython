
class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property #métodos que dão acesso ao objeto
    def nome(self):#get não precisará ser usado por causa da ciração da propriedade
        print("Chamando @property nome ()")
        return self.__nome.title()#o método title garante que a primeira letra esteja em caixa alta
    @nome.setter
    def nome(self, nome):
        print('Chamando setter nome()')
            self.__nome = nome
