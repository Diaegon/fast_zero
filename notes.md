# 1. anotações importantes: 

- Poetry ajuda na criação do ambiente virtual e criar todo o versionamento do código e controlar variáveis importantes
- importante instalar as ferramentas de desenvolvimento com (poetry add --group **ferramenta**) porque ai instalaremos ela e ela não vai ser instalada no ambiente do código quando for ser feito o deploy.

>Ferramentas utilizadas: 
>
>-**ruff** mostra os erros de linha de código e formata eles. ([ poetry run ruff format . ] formata as linhas fora da formatação convencionada no pyproject.toml.)
>- **pytest** O Pytest é uma framework de testes, que usaremos para escrever e executar nossos testes. 
>- **taskipy** O taskipy é um executor de tarefas, onde a gente pega os comandos grandes e complicados que usamos no terminal e transformamos em tasks mais simples EX: task comand (onde comand é algo como: "poetry run ruff format .")
>


>**Comandos do taskipy**
>
>Os comandos definidos fazem o seguinte:
>
>-lint: Faz a checagem de boas práticas do código python
>-pre_format: Faz algumas correções de boas práticas automaticamente
>-format: Executa a formatação do código em relação às convenções de estilo de código
>-run: executa o servidor de desenvolvimento do FastAPI
>-pre_test: executa a camada de lint antes de executar os testes
>-test: executa os testes com pytest de forma verbosa (-vv) e adiciona nosso código como base de cobertura
>-post_test: gera um report de cobertura após os testes
>

## 1. Entendendo os testes

>Utilizando o comando task test, conseguimos o retorno de quantas linhas tem escritas no 
>proejto como um todo, e mostra que nosso código tem 5 linhas escritas (stmts) e 5 linhas 
>não cobertas por teste (miss) e a cobertura (cover) 0%, rodando o task post_test
>a gente recebe um relatório de cobertura de testes em formato HTML. nesse relatório 
>podemos ver em vermelho as linhas que não foram testadas, significa que precisaremos testar todas. 

>Método AAA para estruturar um teste. (arrange, act, assert)
>-**Arrange** cria um ambiente para o teste ser executado, no nosso caso criou um client
>-**ACT** Etapa de executar a ação principal do teste, que basicamente o código de teste executa o código de produção que está sendo testado.
>-**Assert** confirma se tudo ocorreu como o esperado
> os tags estão comentados no código test_app.py

## 2. Criar repositório no git

>Finalizando a primeira aula a gente cria um arquivo .gitignore para não subir arquivos desnecessários no versionamento do código.
> o código utilizado no terminal foi (pipx run ignr -p python > .gitignore) O comando pipx run vai baixar o ignr vai executar o comando e vai desinstalar. 
>Não existe a necessidade de termos ele instalado no sistema, pois só será executado dessa vez.