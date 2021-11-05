class Conta: #dentro da classe Conta será criado os objetos.
    def __init__(self, numero, titular, saldo, limite): #função construtora/ slf é a referência que sabe encontrar o obejto criado.
        print("Criando objeto...{}",format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato (self):
        print("Saldo de {} do titular {} ".format(self.saldo, self.titular))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor
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