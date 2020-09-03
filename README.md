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

Para entregar o seu projeto você deverá criar um _Pull Request_ neste repositório. Este _Pull Request_ deverá conter os arquivos do diretório src dvidamente preenchidos de acordo com as instruções, que conterão seu código `Python` e seus testes, respectivamente.

### ⚠️ É importante que seus arquivos tenham exatamente estes nomes! ⚠️

Você pode adicionar outros arquivos se julgar necessário. Qualquer dúvida, procure a monitoria.

Lembre-se que você pode consultar nosso conteúdo sobre [Git & GitHub](https://course.betrybe.com/intro/git/) sempre que precisar!

---

## O que deverá ser desenvolvido

A lanchonete Pão Na Chapa atualmente possui um sistema de faturamento dos pedidos dos clientes que salva a nome da pessoa junto com o pedido realizado, bem como dia do atendimento. O projeto consiste de ajudar a lanchonete a melhorar esse sistema para que ele possibilite extração de relatórios e num segundo momento, a controlar seu estoque.

O projeto está estruturado em duas etapas obrigatórias, e a tarefa bônus, também em duas etapas, totalizando 4. Foque nas etapas obrigatórias e com o mesmo cuidado que teria com um cliente real: código limpo, com boa manutenção e legibilidade. As tarefas não são complexas nem longas. Por isso, queremos ver um código bonito e testes bem pensados.

---

## Desenvolvimento e testes

**Estrutura do repositório**  

* No diretório `src/` você vai encontrar os arquivos onde devem ser implementadas todas as classes e métodos que você considerar importantes para resolver cada etapa do projeto. 
* No diretório `data/` você encontra os arquivos de log que deverão ser utilizados em cada etapa.
* Os testes devem ser implementados nos arquivos do diretório `tests/`.

**Testes**  

* Para executar os testes, lembre-se de primeiro **criar e ativar o ambiente virtual**, além de também instalar as dependências do projeto. Isso pode ser feito através dos comandos:

```bash
$ python3 -m venv .venv

$ source .venv/bin/activate

$ python3 -m pip install -r requirements.txt
```

**Instalação de Dependências**  
* O arquivo `requirements.txt` contém todos as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`. Com as dependências já instaladas, para executar os testes basta usar o comando:

```bash
$ python3 -m pytest
```

* Se quiser saber mais sobre a instalação de dependências com `pip`, veja esse artigo: https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1

**Estilo**  
* Para verificar se você está seguindo o guia de estilo do Python corretamente, execute o comando:

```bash
$ python3 -m flake8
```

---

## Orientações para execução do projeto

### Etapa 1: Campanha de publicidade

#### 1.1 Apresentação

A lanchonete quer promover ações de marketing e, para isso, a agência de publicidade precisa exatamente das informações abaixo:

  1. Qual o prato mais pedido por 'maria'?
  2. Quantas vezes 'arnaldo' pediu 'hamburguer'?
  3. Quais pratos 'joao' nunca pediu?
  4. Quais dias 'joao' nunca foi na lanchonete?

**Dados**  

* O atual sistema guarda os logs de todos os pedidos feitos em um arquivo csv no formato `cliente,pedido,dia` um por linha e sem nome das colunas (a primeira linha já é um pedido)
* O log a ser utilizado é o arquivo `data/orders_1.csv`
* Todas as informações são strings com letras minúsculas
* O histórico contém pedidos feitos em todos os dias da semana e de todos os pratos que a lanchonete oferece. Ou seja, é possível saber o cardápio completo.
* Os dias da semana estão no formato "...-feira", "sabado" ou "domingo".

#### 1.2 Implementação

* No arquivo `analyse_log.py`, escreva uma função que responda às seguintes perguntas abaixo:
  1. Qual o prato mais pedido por 'maria'?
  2. Quantas vezes 'arnaldo' pediu 'hamburguer'?
  3. Quais pratos 'joao' nunca pediu?
  4. Quais dias 'joao' nunca foi na lanchonete?

* As respostas devem ser salvas no arquivo `data/mkt_campaign.txt` na mesma ordem que acima.
* Assinatura da função:
  ```Python
  def analyse_log(path_to_file)
  ```
* Retorno: nenhum

#### 1.3 Testes

* No arquivo `tests/test_analyse_log.py`, implemente um teste que verifique a corretude da sua saída:
* Saída correta:
  * [todo] (O prato mais pedido de Maria)
  * [todo] (Quantos hamburguers Arnaldo comeu)
  * [todo] (Pratos que Joao nunca pediu)
  * [todo] (Dias que Joao nunca foi na lanchonete

#### 1.4 Commit

* Faça commits sempre que achar que faz sentido. Porém não se esqueça de realizar o commit obrigatório abaixo, pois facilitará a correção:
* **Ao terminar a implementação e testes, faça um commit com a mensagem** `"Finished stage 1"`

#### 1.5 Requisitos obrigatórios

* No arquivo analyse_log.py deve estar implementada a função `def analyse_log(path_to_file)`. 
* A função deve realizar a leitura do log e salvar um arquivo txt com as informações solicitadas.
* O teste deve estar implementados no arquivo `tests/test_analyse_log.py`.

#### 1.6 As seguintes verificações serão feitas:

* Código implementado e passando no teste.
* código legível e modularizado, quando for o caso.
* Utilização correta dos conceitos vistos no módulo.

---

### Etapa 2: Análises contínuas

#### 2.1 Apresentação

* A campanha de marketing foi um sucesso! A gerência agora deseja um sistema que mantenha um registro contínuo dessas informações.
* Mais especificamente, desejam que o sistema permita a extração das seguintes informações a qualquer momento:
  * Prato favorito por cliente
  * Quanto de cada prato cada cliente já pediu
  * Pratos nunca pedidos por cada cliente
  * Dia mais movimentado
  * Dia menos movimentado

* Para isso, você deverá implementar uma classe que entregue as informações acima.
* Você modularizou seu código da etapa 1? Se sim, essa etapa será bem rápida :)

#### 2.2 Implementação

* O arquivo `src/main.py` faz a leitura do arquivo csv passado e envia a informação de cada pedido para as classes `TrackOrders` e para a classe `StockControl` que será implementada caso você realize as etapas bônus.
* Após a leitura completa do arquivo csv, algumas informações são impressas na tela para que você observe o comportamento das suas classes.
* Abra o arquivo `main.py` e complete a variável path com `orders_2.csv`.
* Rode o arquivo `main.py`. Observe que as informções são impressas de maneira incompleta.
* No arquivo `track_orders.py`, implemente a classe `TrackOrders`, contendo, **no mínimo**, os métodos abaixo:

```Python
class TrackOrders:
  def add_new_order(self, costumer, order, day):
    pass

  def get_most_ordered_dish_per_costumer(self, costumer):
    pass

  def get_dish_quantity_per_costumer(self, costumer, order):
    pass

  def get_never_ordered_per_costumer(self, costumer):
    pass

  def get_busiest_day(self):
    pass

  def get_least_busy_day(self):
    pass
```

* Você é livre para criar os atributos e métodos necessários. Lembre-se de criar uma classe legível e bem modularizada.
* Lembre-se de não incorrer em otimização prematura. Ou seja, não implemente funcionalidades que ainda não são necessárias, nem coloque atributos do tipo "vai que um dia precisa".
* Rode o arquivo `main.py` para verificar o comportamento da sua classe.

#### 2.3 Testes

* Elabore uma suíte de testes que garanta, no mínimo, 90% de cobertura da sua classes.
* Implemente os testes no arquivo `test_track_orders.py`

#### 2.4 Commit

* Faça commits sempre que achar que faz sentido. Mas não se esqueça de realizar o commit obrigatório abaixo, pois facilitará a correção:
* **Ao terminar a implementação e testes, faça um commit com a mensagem** `"Finished stage 2"`

#### 2.5 Requisitos obrigatórios:

* Classe `TrackOrders` implementada e com todos os testes passando
* Cobertura de testes de, pelo menos, 90%.

#### 2.6 As seguintes verificações serão feitas:

* A classe está devidamente modularizada.
* Os métodos fazem uso das técnicas de Dict e Set vistos no módulo.
* Os métodos atingem complexidade ótima (geralmente O(1) ou O(n) em alguns métodos que usam Set).

---

### [Bônus parte 1] Etapa 3: Controle de estoque

#### 3.1 Apresentação

* Atualmente o controle de estoque de ingredientes é feito no caderninho. Ao final da semana, uma pessoa conta quantas unidades de cada ingredientes ainda restam no estoque e anota quantos precisam ser comprados para completar o estoque mínimo de cada ingrediente.
* A lanchonete deseja automatizar esse controle: No final da semana, a gerência irá imprimir uma lista de compras com as respectivas quantidades. 

#### 3.2 Implementação

* No arquivo `stock_control.py` você deve implementar a classe `StockControl` que retorna a lista de compras da semana a partir da informação de cada.
* É importante que a lista seja atualizada a cada pedido, e não apenas ao final de semana, pois a gerência quer a liberdade de imprimir a lista de compras a qualquer momento.
* A estrutura básica da classe está demonstrada abaixo e já contém as informações dos ingredientes bem como o estoque mínimo de cada um.]
* O método `get_shopping_list`deve retornar um Dict que mapeia o ingrediente para a quantidade a ser comprada.

```Python
class StockControl:
  def __init__(self):
    self.ingredients = {
        'hamburguer': ['pao', 'hamburguer', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho', 'tomate'],
        'queijo-quente': ['pao', 'queijo', 'queijo'],'misto-quente': ['pao', 'queijo', 'presunto'],
        'bauru': ['pao', 'queijo', 'presunto', 'tomate'],
        'coxinha': ['massa', 'frango'],
    }
  
    self.minimum_stock = {
        'pao': 50,
        'hamburguer': 35,
        'queijo': 100,
        'massa': 20,
        'molho': 30,
        'tomate': 35,
        'presunto': 20,
        'frango': 10,
    }
  
  def add_new_order(self, costumer, order, _):
    pass

  def get_shopping_list(self):
    pass

```

* Utilize o arquivo `orders_2.csv`. O arquivo representa os pedidos feitos em uma semana típica e contém mais pedidos que o arquivo 1.
* É garantido que os pedidos da semana não irão zerar nenhum dos estoques.


#### 3.3 Testes

* Crie testes para o método `get_shopping_list`.
* Garanta que todos os ingredientes e pratos foram testados.

#### 3.4 Commit

* Não se esqueça de realizar o commit obrigatório abaixo, pois facilitará a correção:
* **Ao terminar a implementação e testes, faça um commit com a mensagem** `"Finished stage 3"`

#### 3.5 Requisitos obrigatórios:

* Classe `StockControl`implementada e com todos os testes passando.
* Testes implementados do método `get_shopping_list` com cobertura de, no mínimo, 90%.

#### 3.6 As seguintes verificações serão feitas:

* A classe está devidamente modularizada e legível.
* Os métodos fazem uso das técnicas de Dict e Set vistos no módulo
* Os métodos atingem complexidade ótima (geralmente O(1) ou O(n) em alguns métodos que usam Set).

---

#### [Bônus parte 2] Etapa 4: Estoque pode acabar

#### 4.1 Apresentação

* As campanhas de marketing atraíram muitos novos clientes para a lanchonete. Se antes os estoques mínimos eram sempre suficientes para uma semana, agora não são mais...
* O cardápio do lanchonete é mostrado em um painel eletrônico de forma sempre atualizada. Suponha os seguintes estoques:
  * Pao: 1
  * Queijo: 5
  * Presunto: 3
* Se a pessoa pedir um misto-quente, será possível atendê-lo. Porém o pão irá acabar. Se a próxima pessoa pedir hamburguer, não será possível atendê-lo.
* Sua missão é implementar um código que, caso algum ingrediente acabe, todos os pratos que usam aquele ingrediente devem ser imediatamente removidos do painel, evitando clientes frustrados.

#### 4.2 Implementação

* Implemente as alterações que julgar necessárias para implementar a lógica do Painel.
* Fique à vontade para criar classes ou alterar o arquivo `main.py`.

#### 4.3 Testes

* Caso tenha tempo, implemente testes para as novas classes ou métodos que você criou.

#### 4.4 Commit

* Faça commits sempre que achar que faz sentido. Porém não se esqueça de realizar o commit obrigatório abaixo, pois facilitará a correção:
* **Ao terminar a implementação e testes, faça um commit com a mensagem** `"Finished stage 4"`

#### 4.4 Requisitos obrigatórios:

* Lógica implementada corretamente
* Testes passando, caso existam.

#### 4.5 As seguintes verificações serão feitas:

* As classes/métodos estão devidamente modularizados
* Os métodos fazem uso das técnicas de Dict e Set vistos no módulo

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
