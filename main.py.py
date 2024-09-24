import os
from datetime import datetime

def criar_diretorios():
    """Cria diretórios para armazenar evidências."""
    os.makedirs("evidencias/fotos", exist_ok=True)
    os.makedirs("evidencias/questionarios", exist_ok=True)
    os.makedirs("evidencias/anotacoes", exist_ok=True)
    os.makedirs("evidencias/relatorios", exist_ok=True)

def registrar_foto():
    """Registra uma nova foto."""
    try:
        foto_nome = input("Digite o nome da foto (com extensão): ")
        foto_path = f"evidencias/fotos/{foto_nome}"
        with open(foto_path, "w") as f:
            f.write("Registro de foto: " + foto_nome)
        print(f"Foto registrada: {foto_path}")
    except Exception as e:
        print(f"Erro ao registrar a foto: {e}")

def registrar_questionario():
    """Registra um novo questionário."""
    try:
        questao = input("Digite a pergunta do questionário: ")
        resposta = input("Digite a resposta do participante: ")
        questionario_nome = f"questionario_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        questionario_path = f"evidencias/questionarios/{questionario_nome}"
        with open(questionario_path, "w") as f:
            f.write(f"Pergunta: {questao}\nResposta: {resposta}\n")
        print(f"Questionário registrado: {questionario_path}")
    except Exception as e:
        print(f"Erro ao registrar o questionário: {e}")

def registrar_anotacao():
    """Registra uma nova anotação."""
    try:
        anotacao = input("Digite a anotação da roda de conversa: ")
        anotacao_nome = f"anotacao_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        anotacao_path = f"evidencias/anotacoes/{anotacao_nome}"
        with open(anotacao_path, "w") as f:
            f.write(anotacao)
        print(f"Anotação registrada: {anotacao_path}")
    except Exception as e:
        print(f"Erro ao registrar a anotação: {e}")

def registrar_relatorio():
    """Registra um novo relatório de participação."""
    try:
        participante = input("Digite o nome do participante: ")
        feedback = input("Digite o feedback do participante: ")
        relatorio_nome = f"relatorio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        relatorio_path = f"evidencias/relatorios/{relatorio_nome}"
        with open(relatorio_path, "w") as f:
            f.write(f"Participante: {participante}\nFeedback: {feedback}\n")
        print(f"Relatório registrado: {relatorio_path}")
    except Exception as e:
        print(f"Erro ao registrar o relatório: {e}")

def listar_evidencias(tipo):
    """Lista as evidências de um tipo específico."""
    try:
        caminho = f"evidencias/{tipo}/"
        arquivos = os.listdir(caminho)
        if arquivos:
            print(f"\nEvidências registradas em '{tipo}':")
            for arquivo in arquivos:
                print(f"- {arquivo}")
        else:
            print(f"Nenhuma evidência registrada em '{tipo}'.")
    except Exception as e:
        print(f"Erro ao listar evidências: {e}")

def main():
    criar_diretorios()
    while True:
        print("\nSistema de Registro de Evidências")
        print("1. Registrar Foto")
        print("2. Registrar Questionário")
        print("3. Registrar Anotação")
        print("4. Registrar Relatório")
        print("5. Listar Evidências")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            registrar_foto()
        elif escolha == "2":
            registrar_questionario()
        elif escolha == "3":
            registrar_anotacao()
        elif escolha == "4":
            registrar_relatorio()
        elif escolha == "5":
            print("Tipos de evidências disponíveis:")
            print("a. fotos")
            print("b. questionarios")
            print("c. anotacoes")
            print("d. relatorios")
            tipo = input("Escolha o tipo de evidência a listar (a/b/c/d): ").strip().lower()
            if tipo == 'a':
                listar_evidencias("fotos")
            elif tipo == 'b':
                listar_evidencias("questionarios")
            elif tipo == 'c':
                listar_evidencias("anotacoes")
            elif tipo == 'd':
                listar_evidencias("relatorios")
            else:
                print("Tipo inválido. Tente novamente.")
        elif escolha == "6":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
