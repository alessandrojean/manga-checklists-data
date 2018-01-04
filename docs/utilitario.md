---
title: Utilitário
layout: default
---

Esta página contém informações de como colaborar com as informações através do utilitário.

## Instalando o Python

Para o utilitário funcionar, você precisa ter o [Python](https://python.org) instalado em sua máquina. Seu processo de instalação é simples, apenas seguir as etapas. Não se preocupe, o instalador não contém adware. Opte por sempre baixar a versão `3.x.x`.

**É importante deixar a opção *Add Python 3.x to PATH* marcada durante a instalação.**

## Executando o utilitário

Primeiramente, é necessário fazer o download do mesmo. Baixe o [zip](https://github.com/alessandrojean/manga-checklists-data/archive/master.zip) com o repositório e o extraia em algum lugar.

Para executá-lo, basta abrir o arquivo `run.bat`, ou `run.sh`, dependendo do seu sistema operacional.

## Utilizando o utilitário

Quando você executá-lo, o mesmo lhe pedirá que você especifique o mês e o ano que você pretende gerenciar. Utilize somente números, o programa não aceita nomes de meses.

Se você não digitar nada, pressionando `Enter`, serão utilizados o mês e ano da data atual.

Se algum arquivo já existir com a data especificada, as informações serão carregadas e exibidas em uma tabela, senão, será informado que a lista está vazia.

### Opções

Existem, atualmente, quatro opções básicas. Ao final de cada operação, o arquivo será salvo automaticamente.

Caso a lista esteja vazia, nenhum arquivo será criado. Se você editou um arquivo e removeu todas as entradas dele, o mesmo será deletado.

#### 1. Adicionar novo item a lista manualmente

Utilize essa opção se quiser inserir um novo mangá ao checklist selecionado. Para mais informações, veja a página [Padrões de dados](padroes.md).

#### 2. Editar item da lista

Utilize essa opção se quiser editar um mangá já existente na lista. Lhe será pedido o índice do mesmo, que você pode encontrar na primeira coluna da tabela.

Se quiser manter o valor atual de cada campo, basta apenas deixar em branco, pressionando `Enter`, mas, caso queira limpar o valor, digite `*`.

#### 3. Remover item da lista

Utilize essa opção se quiser remover um mangá já existente da lista. Lhe será pedido o índice do mesmo, que você pode encontrar na primeira coluna da tabela.

#### Q. Salvar alterações e sair

Utilize essa opção quando quiser encerrar o utilitário. Você pode encerrar a qualquer momento, inclusive fora da seleção de opções, pressionando `Ctrl + C`.

## Enviando os dados

Você pode enviar os arquivos criados/editados, que estarão disponíveis na pasta `docs/checklists/br`, através do e-mail `<e-mail>`, com o assunto `[DATA] Checklists` e os arquivos `.json` anexados. 

Se você já tiver familiaridade com Git, sinta-se a vontade para dar um *fetch* no repositório, criar/editar as informações, e mandar um *pull request*.

Se quiser que seu nome seja citado na parte de colaboradores, especifique no e-mail, ou *pull request*, como gostaria que fosse mencionado.