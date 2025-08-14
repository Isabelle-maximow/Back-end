
class Aluno:
    def __init__(self, nome):
        self.notas = []
        self.nome = nome
        self.media = 0.0  # média
        self.situacao = ""  # aprovado ou reprovado

    def add_notas(self):
        for i in range(1,4):
            while True:
                try:
                    nota = float(input(f"Digite a nota {i}: "))
                    if 0 <= nota <= 10:
                        self.notas.append(nota)
                        break
                    else:
                        print("Valor inexistente. Digite uma nota entre 0 e 10.")
                except ValueError:
                    print("Erro: digite um número válido.")

    def calculo_media(self):
        if self.notas:
            self.media = sum(self.notas) / len(self.notas)
            self.situacao = "Aprovado" if self.media >= 6 else "Reprovado"
        else:
            self.media = 0.0
            self.situacao = "Sem notas"

    def exibir_dados(self):
        print(f"""
            Nome: {self.nome}
            Notas: {self.notas}
            Média: {self.media:.2f}
            Situação: {self.situacao}
        """)