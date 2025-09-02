# 1. anotações importantes: 

- Poetry ajuda na criação do ambiente virtual e criar todo o versionamento do código e controlar variáveis importantes
- importante instalar as ferramentas de desenvolvimento com (poetry add --group **ferramenta**) porque ai instalaremos ela e ela não vai ser instalada no ambiente do código quando for ser feito o deploy.

>Ferramentas utilizadas: 
>
>- **ruff** mostra os erros de linha de código e formata eles. ([ poetry run ruff format . ] formata as linhas fora da formatação convencionada no pyproject.toml.)
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

>
>Utilizando o comando task test, conseguimos o retorno de quantas linhas tem escritas no 
>proejto como um todo, e mostra que nosso código tem 5 linhas escritas (stmts) e 5 linhas 
>não cobertas por teste (miss) e a cobertura (cover) 0%, rodando o task post_test
>a gente recebe um relatório de cobertura de testes em formato HTML. nesse relatório 
>podemos ver em vermelho as linhas que não foram testadas, significa que precisaremos testar todas. 
>

>
>Método AAA para estruturar um teste. (arrange, act, assert)
>-**Arrange** cria um ambiente para o teste ser executado, no nosso caso criou um client
>-**ACT** Etapa de executar a ação principal do teste, que basicamente o código de teste executa o código de produção que está sendo testado.
>-**Assert** confirma se tudo ocorreu como o esperado
> os tags estão comentados no código test_app.py
>

## 2. Criar repositório no git
>
>Finalizando a primeira aula a gente cria um arquivo .gitignore para não subir arquivos desnecessários no versionamento do código.
> o código utilizado no terminal foi (pipx run ignr -p python > .gitignore) O comando pipx run vai baixar o ignr vai executar o comando e vai desinstalar. 
>Não existe a necessidade de termos ele instalado no sistema, pois só será executado dessa vez.
>

## 3. Introdução ao desenvolvimento WEB

>
>**modelo cliente-servidor** a partir dele conseguimos nos comunicar com outra máquina(geralmente semelhante a nossa) que oferece um serviço. 
> o que difrencia o cliente de um servidor é o software que ele está rodando. ao construir um servidor, precisamos de uma biblioteca que consiga "servir" nossa aplicação. 
> É aí que entra o Uvicorn, responsável por servir nossa aplicação com FastAPI. o Uvicorn é um servidor ASGI e ele é o que permite o python se conectar com a rede. 
>- **HTTP** - protocolo de tranferência de hipertextom, basicamente o protocolo de comunicação da internet.
>- **URL**  - endereço das páginas
>- **HTML** - linguagem de estrutura das páginas WEB
>
>O protocolo HTTP define oito métodos (GET, HEAD, POST, PUT, DELETE, TRACE, OPTIONS e CONNECT)
>
> A URL é composta de diversas partes: (protocolo, endereço do host, porta/opcional, caminho ) quando o caminho não é especificado ele é substituido pelo caminho (/) que leva direto pra raiz.
>

>
>**Transferência de dados via JSON** As páginas web trocam informações por meio da linguagem HTML mas nesse momento vamos entender o conceito de 
>API's que trocam dados pelo formato JSON, que é uma forma leve e fácil de ler.
>-**API** Application programming interface,  é uma interface definida para a comunicação entre aplicações por meio do protocolo http.
>o cliente se comunica com o servidor enviando as requisições para uma **endpoint** que nada mais é que um endereço URL onde o servidor ou API está ativo 
>e pronto para responder requisições
>-**documentação** Ao disponibilizar uma API para o público, precisamos informar todos os endpoints dela e informar todo o funcionamento da API, como um manual.
> A melhor forma de escrever esse manual é seguindo as especificações da OpenAPI specification. no nosso app conseguimos ver fazendo um "task run" no terminal  e clicando no link gerado/doc
>

>
>-**contratos em apis json**
>trafegar os dados em JSON é simples, porém precisamos entender que precisamos seguir um padrão na estrutura dos dados na hora da troca
>e sabendo disso definimos um schema, que é basicamente um contrato que define a forma e o conteúdo dos dados trafegados.
>usaremos o **pydantic** que criará os schemas de dados e a validação dos dados, o pydantic é uma dependência do fastAPI e não precisa ser instalado
>



