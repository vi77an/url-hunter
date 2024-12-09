# url hunter 🕵️‍♀️

um script simples para filtrar credenciais de um domínio especifico numa lista de URLs. sem complicação.

## como funciona? 🤔
1. você fornece um arquivo `.txt` no formato `url:user:password` (uma por linha).
2. escolhe um domínio ou parte dele para buscar.
3. o script cria um novo arquivo com os resultados filtrados.

## requisitos 📋
- python 3 instalado no seu computador.

## como usar 🚀
1. baixe este arquivo [`url_hunter.py`](./url_hunter.py).
2. abra o terminal (prompt de comando) dentro da pasta onde você salvou o arquivo anterior.
3. rode o comando:

    ```bash
    python url_hunter.py
    ```

4. siga as instruções exibidas.

## exemplo de uso 🌟

- arquivo de entrada no formato `url:user:password` (`db.txt`):
    ```
    https://instagram.com/:usuarioX:senha1
    https://facebook.com/:usuarioY:senha2
    https://twitter.com/:usuarioZ:senha3
    ```
- filtrar por `insta`.
- resultado no arquivo `resultado_insta.txt`:
    ```
    https://instagram.com/:usuarioX:senha1
    ```

## dúvidas? 🛠️
se precisar de ajuda, me envie uma mensagem no [telegram](https://t.me/vi77an)! 😊
