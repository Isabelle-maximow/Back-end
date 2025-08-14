from cadastroalunosClass import CadastroAluno
def main():
    print("Cadastro de alunos...")
    sistema = CadastroAluno()
    sistema.cadastrar_aluno()
    sistema.exibir_alunos()

if __name__ == "__main__":
    main()