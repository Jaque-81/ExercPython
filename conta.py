class Conta:#dentro da classe Conta será criado os objetos.

        def __init__(self, numero, titular, saldo, limite):#função construtora/ slf é a referência que sabe encontrar o obejto criado.
            print("Construindo objeto ... {}".format(self))
            self.__numero = numero
            self.__titular = titular
            self.__saldo = saldo
            self.__limite = limite


        def extrato(self):
            print("Saldo de {} do titular{}".format(self.__saldo, self.__titular))

        def deposita(self, valor):
            self.__saldo += valor

        def saca(self, valor):
            self.__saldo -= valor

        def transfere(self, valor, destino):
            self.saca(valor)
            destino.deposita(valor)

        def get_saldo(self):
            return self._saldo

        def get_titular(self):
            return self._titular

        def get_limite(self):
            return self._limite

        def set_limite(self, limite):
            self._limite = limite


""" Se eu importar a classe:
    Conta()
Out[8]: <conta.Conta at 0x18391e82820>

os números representam o lugar na memporia 
    que foi armazenado o objeto. 
    Se eu criar:
        conta = Conta () /// objeto
   Saída: conta
Out[10]: <conta.Conta at 0x18391eaa490>
'conta' é uma variável/referencial  que armazena o 
objeto Conta()"""
