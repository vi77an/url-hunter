import os
#================##================#
cor_reset = "\033[0m"     
cor_vermelho = "\033[38;5;198m"  
cor_p_roxo = "\033[38;5;135m"
cor_p_azul = "\033[38;5;81m"
cor_p_verde = "\033[38;5;119m"
#================##================#

def vulgo_bloody():
    print(rf"""
{cor_p_verde} ==* coded by *== {cor_p_roxo}

 ██▒   █▓ ██▓ ██▓     ██▓    ▄▄▄       ███▄    █ 
▓██░   █▒▓██▒▓██▒    ▓██▒   ▒████▄     ██ ▀█   █ 
 ▓██  █▒░▒██▒▒██░    ▒██░   ▒██  ▀█▄  ▓██  ▀█ ██▒
  ▒██ █░░░██░▒██░    ▒██░   ░██▄▄▄▄██ ▓██▒  ▐▌██▒
   ▒▀█░  ░██░░██████▒░██████▒▓█   ▓██▒▒██░   ▓██░
   ░ ▐░  ░▓  ░ ▒░▓  ░░ ▒░▓  ░▒▒   ▓▒█░░ ▒░   ▒ ▒ 
   ░ ░░   ▒ ░░ ░ ▒  ░░ ░ ▒  ░ ▒   ▒▒ ░░ ░░   ░ ▒░
     ░░   ▒ ░  ░ ░     ░ ░    ░   ▒      ░   ░ ░ 
      ░   ░      ░  ░    ░  ░     ░  ░         ░ 
     ░                                           
      {cor_p_verde} ==*  {cor_vermelho}VL{cor_reset} ~ {cor_vermelho}villanelle{cor_reset} | {cor_vermelho}t.me/vi77an{cor_p_verde} *=={cor_reset}
""")

def abrir_arquivo():
    # Listar arquivos .txt no diretório atual
    txt_files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.txt')]

    if not txt_files:
        print(f"{cor_vermelho}[💔] Nenhum arquivo .txt foi encontrado no diretório atual.{cor_reset}")
        exit(1)

    print(f"{cor_p_roxo}[💌] Arquivos disponíveis:{cor_reset}")
    for i, file in enumerate(txt_files, 1):
        print(f"  [{i}] {file}")
    print("  [0] Cancelar e sair")

    while True:
        try:
            choice = int(input(f"{cor_p_roxo}[*] Selecione o número do arquivo desejado: {cor_p_verde}"))
            if choice == 0:
                print(f"{cor_p_roxo}[👋] Operação cancelada. Até mais!{cor_reset}")
                exit(0)
            elif 1 <= choice <= len(txt_files):
                input_file = txt_files[choice - 1]
                with open(input_file, 'r') as file:
                    linhas = file.read().splitlines()
                return linhas
            else:
                print(f"{cor_vermelho}[💔] Escolha inválida. Tente novamente.{cor_reset}")
        except ValueError:
            print(f"{cor_vermelho}[💔] Entrada inválida. Digite um número correspondente a um arquivo.{cor_reset}")

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
    output_file = f"resultado_{termo_busca.replace('.', '_')}.txt"
    with open(output_file, 'w') as file:
        file.write('\n'.join(resultados))
    print(f"{cor_p_roxo}[💚] CONFIRA >> {cor_p_verde}{output_file}{cor_reset}.")

def realizar_pesquisa(linhas):
    while True:
        termo_busca = input(f"{cor_p_roxo}[*] Domínio ou parte do domínio (ex: insta): {cor_reset}").strip()
        resultados = filtrar_linhas(linhas, termo_busca)

        if resultados:
            salvar_resultados(resultados, termo_busca)
            break
        else:
            print(f"{cor_vermelho}[!] Vixe, não encontramos nada com '{termo_busca}'.")
            if input(f"{cor_p_roxo}[?] Tentar novamente com outro termo? (s/n): ").strip().lower() != 's':
                print(f"\n{cor_p_roxo}[👋] Até mais!")
                return exit()

def continuar_ou_encerrar():
    while True:
        continuar = input(f"{cor_p_roxo}[?] Continuar? (s/n): ").strip().lower()
        if continuar == 's':
            return True
        elif continuar == 'n':
            print(f"{cor_p_roxo}[👋] Ok, até a próxima!")
            return False
        else:
            print(f"{cor_vermelho}[!] Por favor, digite 's' para continuar ou 'n' para encerrar.")

def main():
    vulgo_bloody()
    print('+-+-+-+-+-++-+-+-+-+-++-+-+-+')
    print(f'.:|| {cor_p_roxo}URL:LOG:PASS HUNTER {cor_reset}||:.')
    print('+-+-+-+-+-++-+-+-+-+-++-+-+-+\n')

    while True:
        linhas = abrir_arquivo()
        if linhas is None:
            break

        realizar_pesquisa(linhas)

        if not continuar_ou_encerrar():
            break

if __name__ == "__main__":
    main()