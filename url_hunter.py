def exibir_boas_vindas():
    print(r"""
             )    )            
   )  (   ( /( ( /(   )        
  /(( )\  )\()))\()| /(  (     
 (_))((_)((_)\((_)\)(_)) )\ )  
 _)((_|_)__  /__  ((_)_ _(_/(  
 \ V /| | / /  / // _` | ' \)) 
  \_/ |_|/_/  /_/ \__,_|_||_|  
                               
         por: VL
    """)

def abrir_arquivo():
    while True:
        arquivo_entrada = input("Qual o nome do arquivo com as URLs? (ex: db.txt): ").strip()

        try:
            with open(arquivo_entrada, 'r') as file:
                linhas = file.read().splitlines()
            return linhas
        except FileNotFoundError:
            print("Ei, não conseguimos encontrar esse arquivo!")
            if input("Quer tentar novamente? (s/n): ").strip().lower() != 's':
                print("Tudo bem, até mais!")
                return None

def filtrar_linhas(linhas, termo_busca):
    resultados = []
    for linha in linhas:
        partes = linha.rsplit(':', 2)
        if len(partes) == 3:
            dominio_atual, _, _ = partes
            if termo_busca in dominio_atual:
                resultados.append(linha)
    return resultados

def salvar_resultados(resultados, termo_busca):
    arquivo_saida = f"resultado_{termo_busca.replace('.', '_')}.txt"
    with open(arquivo_saida, 'w') as file:
        file.write('\n'.join(resultados))
    print(f"Prontinho! Os resultados estão no arquivo: '{arquivo_saida}'.")

def realizar_pesquisa(linhas):
    while True:
        termo_busca = input("Qual domínio ou parte do domínio você quer filtrar? (ex: insta): ").strip()
        resultados = filtrar_linhas(linhas, termo_busca)

        if resultados:
            salvar_resultados(resultados, termo_busca)
            break
        else:
            print(f"Vixe, não encontramos nada com '{termo_busca}'.")
            if input("Quer tentar novamente com outro termo? (s/n): ").strip().lower() != 's':
                print("Até mais! Esperamos que tenha dado certo!")
                return

def continuar_ou_encerrar():
    while True:
        continuar = input("Quer continuar fazendo pesquisas? (s para continuar, n para encerrar): ").strip().lower()
        if continuar == 's':
            return True
        elif continuar == 'n':
            print("Ok, até a próxima!")
            return False
        else:
            print("Por favor, digite 's' para continuar ou 'n' para encerrar.")

def main():
    exibir_boas_vindas()

    while True:
        linhas = abrir_arquivo()
        if linhas is None:
            break

        realizar_pesquisa(linhas)

        if not continuar_ou_encerrar():
            break

if __name__ == "__main__":
    main()
