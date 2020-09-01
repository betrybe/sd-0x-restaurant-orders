# Boas vindas ao repositório do projeto Restaurant Orders!

Você já usa o GitHub diariamente para desenvolver os exercícios, certo? Agora, para desenvolver os projetos, você deverá seguir as instruções a seguir. Fique atento a cada passo, e se tiver qualquer dúvida, nos envie por _Slack_! #vqv 🚀

Aqui você vai encontrar os detalhes de como estruturar o desenvolvimento do seu projeto a partir desse repositório, utilizando uma branch específica e um _Pull Request_ para colocar seus códigos.

---

## Instruções para entregar seu projeto:

### ANTES DE COMEÇAR A DESENVOLVER:

1. Clone o repositório

- `git clone git@github.com:tryber/sd-0x-restaurant-orders.git`.
- Entre na pasta do repositório que você acabou de clonar:
  - `sd-0x-restaurant-orders`

2. Crie o ambiente virtual para o projeto

- `python3 -m venv .venv && source .venv/bin/activate`

3. Instale as dependências

- `python3 -m pip install -r requirements.txt`

4. Crie uma branch a partir da branch `master`

- Verifique que você está na branch `master`
  - Exemplo: `git branch`
- Se não estiver, mude para a branch `master`
  - Exemplo: `git checkout master`
- Agora crie uma branch à qual você vai submeter os `commits` do seu projeto
  - Você deve criar uma branch no seguinte formato: `nome-github-nome-do-projeto`
  - Exemplo: `git checkout -b exemplo-project-name`

5. Adicione as mudanças ao _stage_ do Git e faça um `commit`

- Verifique que as mudanças ainda não estão no _stage_
  - Exemplo: `git status` (deve aparecer listada a pasta _exemplo_ em vermelho)
- Adicione o novo arquivo ao _stage_ do Git
  - Exemplo:
    - `git add .` (adicionando todas as mudanças - _que estavam em vermelho_ - ao stage do Git)
    - `git status` (deve aparecer listado o arquivo _exemplo/README.md_ em verde)
- Faça o `commit` inicial
  - Exemplo:
    - `git commit -m 'iniciando o projeto project-name'` (fazendo o primeiro commit)
    - `git status` (deve aparecer uma mensagem tipo _nothing to commit_ )

6. Adicione a sua branch com o novo `commit` ao repositório remoto

- Usando o exemplo anterior: `git push -u origin exemplo-project-name`

7. Crie um novo `Pull Request` _(PR)_

- Vá até a página de _Pull Requests_ do [repositório no GitHub](https://github.com/tryber/sd-0x-restaurant-orders/pulls)
- Clique no botão verde _"New pull request"_
- Clique na caixa de seleção _"Compare"_ e escolha a sua branch **com atenção**
- Clique no botão verde _"Create pull request"_
- Adicione uma descrição para o _Pull Request_ e clique no botão verde _"Create pull request"_
- **Não se preocupe em preencher mais nada por enquanto!**
- Volte até a página de _Pull Requests_ do repositório e confira que o seu _Pull Request_ está criado

---

## Entregáveis

Para entregar o seu projeto você deverá criar um _Pull Request_ neste repositório. Este _Pull Request_ deverá conter os arquivos `analyse_orders.py` e `test_analyse_orders.py`,  que conterão seu código `Python` e seus testes, respectivamente.

### ⚠️ É importante que seus arquivos tenham exatamente estes nomes! ⚠️

Você pode adicionar outros arquivos se julgar necessário. Qualquer dúvida, procure a monitoria.

Lembre-se que você pode consultar nosso conteúdo sobre [Git & GitHub](https://course.betrybe.com/intro/git/) sempre que precisar!

---

## O que deverá ser desenvolvido

A lanchonete Pão Na Chapa atualmente possui um sistema de faturamento dos pedidos dos clientes que salva a nome da pessoa junto com o pedido realizado, bem como dia do atendimento.

A lanchonete quer promover ações de marketing, mas para isso a agência de publicidade precisa das informações abaixo:

* Qual o prato mais pedido por 'maria'?
* Quantas vezes 'arnaldo' pediu 'hamburguer'?
* Quais pratos 'joao' nunca pediu?
* Quais dias 'joao' nunca foi na lanchonete?

O seu projeto consiste em implementar um código que leia esses logs de compras anteriores e retorne cada uma das informações acima de maneira detalhada para que a gerência possa emitir emails de promoções direcionadas. A segunda parte do projeto será explicada após você concluir a primeira.

---

## Desenvolvimento e testes

No diretório `src/` você vai encontrar os arquivos onde devem ser implementados todas as classes e métodos que você considerar importantes para resolver o projeto. Os testes devem ser implementados no arquivo no diretório `tests/`.

Para executar os testes, lembre-se de primeiro **criar e ativar o ambiente virtual**, além de também instalar as dependências do projeto. Isso pode ser feito através dos comandos:

```bash
$ python3 -m venv .venv

$ source .venv/bin/activate

$ python3 -m pip install -r requirements.txt
```

O arquivo `requirements.txt` contém todos as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`. Com as dependências já instaladas, para executar os testes basta usar o comando:

```bash
$ python3 -m pytest
```

Se quiser saber mais sobre a instalação de dependências com `pip`, veja esse artigo: https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1

Para verificar se você está seguindo o guia de estilo do Python corretamente, execute o comando:

```bash
$ python3 -m flake8
```

---

## Orientações para execução do projeto

### Etapa 1 - Campanha de publicidade

#### 1.1 - Apresentação

* Utilize os arquivo `orders_1.csv`
* O histórico de pedidos é um arquivo csv com as informações de `cliente,pedido,dia` um por linha e sem nome das colunas (a primeira linha já é um pedido)
* Todas as informações são strings com letras minúsculas
* O histórico contém pedidos feitos em todos os dias da semana e de todos os pratos que a lanchonete oferece. Ou seja, é possível saber o cardápio completo.
* Os dias da semana estão no formato "...-feira", "sabado" ou "domingo".
* A lanchonete abre todos os dias da semana.

#### 1.2 - Implementação

* No arquivo `analyse_log.py`, escreva uma função que responda às seguintes perguntas abaixo:
  1. Qual o prato mais pedido por 'maria'?
  2. Quantas vezes 'arnaldo' pediu 'hamburguer'?
  3. Quais pratos 'joao' nunca pediu?
  4. Quais dias 'joao' nunca foi na lanchonete?

* As respostas devem ser impressas na tela. Fique à vontade com o texto da frase que será mostrada.

#### 1.3 Testes

* **NÃO** é necessário implementar testes para a primeira etapa
* Verifique se a saída do seu código apresenta as saídas corretas:
  * O prato mais pedido de Maria é: [todo]
  * Arnaldo comeu [todo] hamburguers
  * Joao nunca pediu: [todo]
  * Joao nunca foi na lanchonete nos dias [todo]

#### 1.4 - Requisitos obrigatórios

* No arquivo analyse_log.py deve haver pelo menos um função que imprima na tela os valores corretos
* Não é necessária a implementação de testes para a primeira etapa

#### 1.5 - As seguintes verificações serão feitas:

* Corretude das saídas do código
* Legibilidade do código
* Utilização dos conceitos vistos no módulo

---

### Etapa 2 - Análises contínuas

#### 2.1 - Apresentação

* A campanha de marketing foi um sucesso! A gerência agora deseja um sistema que mantenha um registro contínuo dessas informações.
* Mais especificamente, desejam que o sistema tenha controles que permitam a extração das seguintes informações:
  * Prato favorito por cliente
  * Quanto de cada prato cada cliente já pediu
  * Pratos nunca pedidos por cada cliente
  * Dia mais movimentado
  * Dia menos movimentado

* Para isso, você precisará implemetar uma classe que entregue as informações acima.

#### 2.2 Implementação

* No arquivo `track_orders.py`, implemente a classe TrackOrders, contendo, **no mínimo**, os métodos abaixo:

```Python
class TrackOrders:
  def add_new_order(self, costumer, order, day):
    raise NotImplementedError

  def get_most_ordered_dish_per_costumer(self, costumer):
    raise NotImplementedError

  def get_dish_quantity_per_costumer(self, costumer, order):
    raise NotImplementedError

  def get_never_ordered_per_costumer(self, costumer):
    raise NotImplementedError

  def get_busiest_day(self):
    raise NotImplementedError

  def get_least_busy_day(self):
    raise NotImplementedError
```

* Implemente o construtor com as atributos que você achar necessários para que a classe funcione corretamente.
* Sugestão: implemente um método por vez e garanta que o método funciona e passa nos testes antes de seguir para a próxima implementação. A cada novo método, faça as alterações necessárias.
* Você é livre para criar os atributos e métodos necessários. Lembre-se de criar uma classe legível e bem modularizada.

#### 2.3 Testes

* Implemente os testes no arquivo `test_track_orders.py`
* Garanta, no mínimo, 90% de cobertura.

#### 2.4 Requisitos obrigatórios:

* Classe TrackOrders implementada e com todos os testes passando
* Cobertura de testes de, pelo menos, 90%

#### 2.5 As seguintes verificações serão feitas:

* A classe está devidamente modularizada
* Os métodos fazem uso das técnicas de Dict e Set vistos no módulo
* Os métodos têm complexidade de, no máximo, O(n) e O(1) sempre que possível.

---

### [Bônus 3] Etapa 3 - Controle de estoque

#### 3.1 - Apresentação

* 

#### 3.2 Implementação

* 

#### 3.3 Testes

* 

#### 3.4 Requisitos obrigatórios:

* 

#### 3.5 As seguintes verificações serão feitas:

* 

---

#### [Bônus 2] Etapa 4 - Estoque pode acabar

#### 4.1 - Apresentação

* 

#### 4.2 Implementação

* 

#### 4.3 Testes

* 

#### 4.4 Requisitos obrigatórios:

* 

#### 4.5 As seguintes verificações serão feitas:

* 

---

### DURANTE O DESENVOLVIMENTO

- Faça `commits` das alterações que você fizer no código regularmente

- Lembre-se de sempre após um (ou alguns) `commits` atualizar o repositório remoto

- Os comandos que você utilizará com mais frequência são:
  1. `git status` _(para verificar o que está em vermelho - fora do stage - e o que está em verde - no stage)_
  2. `git add` _(para adicionar arquivos ao stage do Git)_
  3. `git commit` _(para criar um commit com os arquivos que estão no stage do Git)_
  4. `git push -u nome-da-branch` _(para enviar o commit para o repositório remoto na primeira vez que fizer o `push` de uma nova branch)_
  5. `git push` _(para enviar o commit para o repositório remoto após o passo anterior)_

---

### DEPOIS DE TERMINAR O DESENVOLVIMENTO (OPCIONAL)

Para sinalizar que o seu projeto está pronto para o _"Code Review"_ dos seus colegas, faça o seguinte:

- Vá até a página **DO SEU** _Pull Request_, adicione a label de _"code-review"_ e marque seus colegas:

  - No menu à direita, clique no _link_ **"Labels"** e escolha a _label_ **code-review**;

  - No menu à direita, clique no _link_ **"Assignees"** e escolha **o seu usuário**;

  - No menu à direita, clique no _link_ **"Reviewers"** e digite `students`, selecione o time `tryber/students-sd-0x`.

Caso tenha alguma dúvida, [aqui tem um video explicativo](https://vimeo.com/362189205).

---

### REVISANDO UM PULL REQUEST

Use o conteúdo sobre [Code Review](https://course.betrybe.com/real-life-engineer/code-review/) para te ajudar a revisar os _Pull Requests_.

#VQV 🚀
