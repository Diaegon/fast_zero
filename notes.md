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

>
>**estruturando projetos e criando CRUD** a CRUD é basicamente as quatro operações que podemos fazer em um banco de dados
> Create, Read, update e delete, no protocolo HTTP temos quatro verbos que fazem a mesma coisa. POST, GET, PUT e DELETE.
>
>>criamos uma função para o cadastro de usuário e é imprescindível que tenhamos uma resposta de confirmação quando a conta for criada por meio do status_code.
>>definiremos o modelo de entrada de dados, para que o app e o cliente tenham a certeza de que usarão os mesmos dados, para isso >>criamos uma classe do pydantic no arquivo schemas. o ponto forte do pydantic é que ele cuida da parte de validação dos dados
>>quando o usuario coloca dados que não estão de acordo com o schema definido, o sistema retorna erro 422, e caso a resposta 
>>do servidor não siga o schema é levantado o erro 500, sendo assim uma segurança de duas vias
>>
>

>
>Apos criar um db falso(simulando o db em uma lista) para continuar a escrita do código, vamos criar um test para o método post.
>criamos o teste do post de um novo usuário e percebemos que existe uma parte no test se repetindo, a parte do arrange que cria um
>cliente para rodar o teste, percebendo essa repetição vamos estudar uma funcionalidade do pytest chamada fixture para resolver esse problema.
>Vamos criar uma fixture que retorna nosso client, criando um arquivo novo na pagina de testes chamado conftest.py. feito o client no conftest
>podemos somente passar ele no parametro de cada teste e não precisamos mais criar um cliente toda vez. com o método POST finalizado, agora partimos
>para o método Read
>

>
>Partimos para implementar a rota GET, que está associada a operação Read e tem que retornar o status 200. 
>feito o schema agora vamos configurar o endpoint e por sua vez o teste. configurando esse endpoint ficou claro que o modelo de resposta padrão do 
>fastAPI é o json. Outra boa observação é que aprendemos muito sobre programação e funcionamento do python quando testamos.
>

>
>O proximo passo é implementar a rota PUT, que é equivalente a operação update. se a solicitação for bem sucedida deve retornar 200, 
>se o usuario não for encontrado deve retornar 404. como vamos alterar os dados de um usuário precisamos achaar ele pelo identificador, no nosso caso > o id. então o Endpoint que vamos construir deve receber o id de quem será alterado. para fazer essa identificação do recurso na URL usamos a 
>seguinte combinação /caminh/recurso mas como o recurso é dinâmico, ele deve ser enviado pelo cliente. fazendo com que o valor tenha q ser uma
>variável. Dentro do FastAPI, as variáveis de recursos são descritas dentro de {}, como {user_id}.
> com o endpoint definido agora implementamos a rota de teste.
>

>
>passamos para a operação delete e foi implementada tanta a operção quanto os testes, vale ressaltar que 
>a resposta da operação delete é uma escolha pessoal, alguns não ligam para o tipo de resposta. 

>
>**configurando o banco de dados** para gerenciar as configurações do código usaremos o pydantic-settings
>ele nos permite configurar de uma forma segura e simplificada a parte sensível dos nossos dados na criação
> do código. para gerenciar as alterações no banco de dados usaremos o SQLALCHEMY que nos ajuda a estruturar
> a ORM. A ORM é object-relational-mapper é uma técnica que facilita a comunicação entre um código orientado 
> a objeto e um banco de dados relacional, com elas conseguios manipular banco de dados utilizando classes 
> e objetos python.
>e o CORE que disponibiliza uma interface SQL abstrata que permite a gente se comunicar com um BD de maneira
>segura e alinhada com as convenções python
>
>alem desses dois temos também a Engine e a Session, onde a Engine fica encarregada de fazer a conexão com os 
>BD's e gerencia-las e a session é a encarregada das transações, mediada pela engine ela faz a conexão do python
>com o BD.

>
>montando nosso ORM vamos usar o registrador de tabelas para converter automáticamente as classes em dataclasses 
>podemos também usar por herança. no arquivos models.py vamos encontrar que Cada classe que é registrada pelo 
>objeto registry é automaticamente mapeada para uma tabela no banco de dados.
> criando a tabela no no moedels.py vemos que existem alguns valores que precisam ser alterados pelo o próprio
>bd, como id e created_at, para isso usamos uma função chamada mapped_column, nela conseguimos definir valores
> como unique, primary_key, etc. temos também valores passados como parametro que não conhecemos do SQL, como
>é o caso do init que indica que aquele atributo não precisa ser passado pelo usuário, ele será adicionado 
>pelo próprio banco, que é o caso do id e do created_at.
>


>com o banco de dados montado é interessante a gente criar uma fixture para testar ele, essa fixture 
>vai criar um db em memoria toda vez que a chamarmos e após realizar os testes vai apagar ele.
>com essa fixture feita agora criamos um arquivo test_db.py no diretorio test, ele deve criar um usuario
>e logo apos pesquisar um usuario para ver se o usuario foi criado com sucesso.


>
>**execução de testes é uma parte vital do desenvolvimento de qualquer aplicação. Os testes nos ajudam a identificar e corrigir problemas antes que eles se tornem mais sérios. Eles também fornecem a confiança de que nossas mudanças não quebraram nenhuma funcionalidade existente.**
>
>

>
>**Eventos do ORM** podemos validar os objetos inseridos por meio do teste, como nome, password e email, porém
>existem objetos que fogem do mecanismo de criação da tabela (init=false), para podemos validar os campos
> que fogem do nosso controle, podemos usar o sistema de eventos do sqlalchemy
>os eventos são blocos de códigos que podem ser inseridos ou retirados antes e depois de uma operação.
>Ao escrever testes a restrição init=false pode nos trazer algumas dificuldades no momento das validações
>
> escrevemos uma função para que ela apareça e insira um dado "fake" toda vez que aparecer uma restrição
>chamamos isso de gerenciador de contexto(assunto interessante para procurar entender),
> 
>A ideia por trás dessa função é ser um gerenciador de contexto (para ser chamado em um bloco with). 
>Toda vezes que um registro de model for inserido no banco de dados, se ele tiver o campo created_at, por
>padrão, o campo será cadastrado com a sua data pré-fixada '01/01/2024'. Facilitando a manutenção dos testes
>que precisam da comparação de data, pois será determinística. como agora todos os dados são deterministicos
>podemos agora passar para a fase de configuração de bd e gerenciamento de migrações.
>

>
>criamos uma arquivo settings para ser criada uma classe de settings, e a partir dele sempre que ela for
>chamada temos um modelo padrão de configs. também criaremos um arquivo de variaveis de ambiente e colocaremos
> o database no gitignore pois é uma pratica ruim colocar o db no versionamento do código.  
>com o database definido precisamos usar uma ferramenta que migre o banco de dados entre versões do código
>enquanto o código evolui, os metadados do banco possa evoluir de acordo com a versão do código.
>usaremos o alembic.
>

>
>com o alembic instalado vamos gerar nossa primeira migração, mas antes temos que garantir que o alembic consiga 
>acessar nossas configurações e modelos corretamente. para isso faremos as seguintes alterações no arquivo
>migrations/env.py
>- **Importar as Settings do nosso arquivo settings.py e a table_registry dos nossos modelos.**
>-**Configurar a URL do SQLAlchemy para ser a mesma que definimos em Settings.**
>-**Verificar a existência do arquivo de configuração do Alembic e, se presente, lê-lo.**
>-**Definir os metadados de destino como table_registry.metadata, que é o que o Alembic utilizará para gerar automaticamente as migrações.**
>Feitas essas alterações, estamos prontos para gerar nossa primeira migração automática. O Alembic é capaz de gerar migrações a 
> partir das mudanças detectadas nos nossos modelos do SQLAlchemy.
>> para criar a migração usamos o comando no terminal
>> alembic revision --autogenerate -m "create users table"
>
> No arquivo de migração é criado um arquivo chamado migrations/versions/(??????)
>Esse arquivo descreve as mudanças a serem feitas no banco de dados. Ele usa a linguagem core do SQLAlchemy, que é mais baixo nível que o ORM.
>As funções upgrade e downgrade definem, respectivamente, o que fazer para aplicar e para desfazer a migração. No nosso caso, a função upgrade
>cria a tabela 'users' com os campos que definimos em fast_zero/models.pye a função downgrade a remove.
>

>
>começaremos agora a integração do banco de dados com a API, a primeira coisa é definir a sessão, que é o canal lógico de 
>trabalho entre o cliente e o BD. Nesse parte da aula vamos aprender a manipular as dependências do código e deixar ele
>o menos acoplado o possível manuseando a injeção de dependências.  utilizaremos a função do FASTAPI depends.
>Agora que temos a nossa sessão de banco de dados gerenciada por meio do FastAPI e da injeção de dependências,
>atualizaremos nossos endpoints para poderem tirar proveito disso. Começaremos com a rota de POST para a criação de usuários.
>

>
>Quandon eu passo uma função dentro da Depends() ela faz com que a função passada dentro da depends seja inicialida antes da função
>na qual ela foi chamada, nesse caso passando a função get_session dentro da depends, garante que todo operação no BD só se inicie
>após uma sessão ser criada. 
>apos o banco de dados real ser conectado ao sistema, vamos para a parte das autenticações.
>

>
>A autenticação é o processo que confirmamos quem o usuário é, e a autorização é o processo para verificar o que ele pode fazer.
>Usaremos o JSON Web Token para (JWT) para implementar a autenticação, e adicionaremos lógica de autorização nos endpoints.
>Usaremos a biblioteca pwdlib  para encripitar as senhas.
>criamos um arquivo security.py para ser o arquivo que gera os tolkens jwt e por finalidade didática criaremos um test pra ele.
>

>
>Modificaremos os endpoins para encripitar as senhas passadas pelo usuario antes de jogar elas no banco.
>após os endpoints de create e update estarem modificados para a senha ser colocada em hash no banco de dados
>vamos fazer um endpoin para criação de token de autenticação do usuário e seu teste.
>com a criação do token e seu teste, a gente parte para criar uma função que valide esse token que estará no head da requisição
>criamos a função get_current_user() no arquivo security.py e a partir dele podemos proteger os endpoints.
>

>
>chegamos na fase de reestruturação do código, usaremos uma ferramenta do fastaPI chamada routers, que separa as atribuições
>semelhantes e melhora a legibilidade e organização do código.
> o primeiro passo é tirar todos os endpoints do app que possuem o mesmo contexto e passar para o subapp users da pasta routers.
>muito da nossa estrutura vai depender de qual filosofia de arquitetura a gente segue. nessa aula fizemos a atualização
> de estrutura e os testes necessários para que o projeto consiga avançar
>

>
>Com o projeto refatorado e melhorada a legibilidade e manutenção, vamos tornar ele um projeto assincrono
>a importância de tornar um projeto assincrono é fazer com que ele consiga ter diversas requisições simultaneas
>quando um projeto é sincrono ele espera uma requisição terminar para iniciar outra e isso pode acabar gerando
>um gargalo que fará a aplicação ficar lenta.
>usaremos a biblioteca asyncio do sqlachemy para manusear as orm do bd, e temos que baixar o aiosqlite para informar
>ao sqlite que estamos lidando com um bd assincrono.
>
>>O comportamento padrão do SQLAlchemy é expirar o cache de objetos após um commit, o que pode causar problemas em operações
>> assíncronas, pois o objeto pode ser descartado enquanto estamos aguardando em outra corrotina. 
>> outra coisa é que o pytest não lida muito bem com programação assincrona então temos que instalar uma extensão
>> poetry add --group dev pytest-asyncio
>

>justando a sessão de testes, passaamos para o ajuste da sessão de teste do bd.

