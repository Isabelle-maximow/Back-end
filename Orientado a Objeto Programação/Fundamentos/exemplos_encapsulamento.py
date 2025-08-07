# encapsulamento simples:
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular # atributo comum
        # encapsulamento:
        # encapsulamento dos dados se usar dois underline
        self.__saldo = saldo # eh tipo ocultar o saldo

        # metodo de depositar:
    def depositar(self, valor):
        # ação de depositr um valor ao saldo
        # somar saldo + valor
        self.__saldo += valor
    
    # metodo mostrar o saldo:
    def exibir_saldo(self):
        print(f"olá {self.titular}")
        print(f"Seu saldo é R${self.__saldo}")
        
# criar um titular para teste:
conta_maria = ContaBancaria("Maria", 1000)
# exibir o valor:
conta_maria.exibir_saldo()

# Depositar valor:
conta_maria.depositar(500) 
conta_maria.exibir_saldo()

# SIMULAÇÃO DE ERRO DE ENCAPSULAMENTO:
print(conta_maria.__saldo) # erro de atributo