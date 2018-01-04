---
title: Padrões de dados
layout: default
---

Esta página contém informações de como seguir o padrão dos dados.

Cada sessão se refere a um campo cadastral, em sua ordem e categoria.

## Editora

A especificação da editora é feita através de seu código, que está disponível na lista de opções. Você só pode inserir um mangá das editoras que estão disponíveis na lista, caso alguma editora nova surja, o utilitário será atualizado.

Atualmente, as editoras disponíveis são:

    1) Editora JBC
    2) Panini
    3) NewPOP Editora
    4) Nova Sampa
    5) DarkSide Books
    6) Devir
    7) L&PM
    8) Editora Draco

## Selo editorial

Algumas editoras possuem diferentes selos editoriais, tais como a Editora JBC, que possui o seu selo normal de mangás, os da *Ink Comics*, o de *Novels* e o de *Graphic Novels*. O mesmo se aplica a Panini, com o *Planet Manga*, por exemplo.

O utilitário já tem em sua base os selos editoriais de cada editora, então somente será listado nas opções os selos correspondentes.

Caso a editora possua apenas um selo editorial, como a Nova Sampa, com o *JENS*, este será selecionado automaticamente.

Exemplo de lista de opções de selos editoriais:

    1) Mangás
    2) Ink Comics
    3) Novels
    4) Graphic Novels

Caso algum selo novo surja, mesmo caso das Editoras.

## Informações

Esta categoria abrange informações simples do mangá.

### Nome

O nome da série, não confundir com o nome do volume. 

O nome usado **sempre** deverá ser o localizado, ou seja, o nome da série aqui no país, por exemplo, *A Voz do Silêncio*, e não *Koe no Katachi*, *A Silent Voice* etc.

### Data

A data de lançamento do mangá, ou seja, quando o mesmo começou a ser vendido.

O formato deve ser **sempre** `dd/mm/yyyy`, por exemplo, `04/01/2018`.

Este campo é um pouco impreciso, pois algumas editoras tem uma data específica para as bancas de jornal, outra para lojas especializadas etc. Tente optar sempre pela data das bancas de jornal.

### Subtítulo

Nome do volume. Alguns mangás, além de ter a própria numeração, tem um nome para cada volume.

Este campo **não** se destina ao subtítulo do mangá.

### Sinopse

Sinopse do mangá, de preferência a sinopse específica do volume.

Este campo deve ter um cuidado redobrado, pois ele aceita *tags* `HTML`. Cada parágrafo da sinopse deve ser envolvido em `<p></p>`, como pode-se observar no exemplo abaixo:

```html
<p>A Major Motoko Kusanagi volta atualizada na sequência da obra-prima de Shirow&nbsp;Masamune&nbsp;<strong>The Ghost in the Shell 2.0 – Manmachine Interface.</strong><br> Assim como o mangá original que apresentou ao mundo a Major Motoko Kusanagi, esta sequência chega ao Brasil em uma luxuosa edição. Ao todo serão quase 200 páginas totalmente coloridas, revelando cada detalhe da excepcional arte de Shirow.<br> Serializado no Japão na Revista Young Magazine, da Editora Kodansha, The Ghost in the Shell 2.0 foi publicado entre 1991 e 1997 para depois ter todas suas histórias em um volume único.</p>

<p>A história acontece em um mundo virtual onde quase tudo é possível, até mesmo controlar múltiplas personalidades. É neste momento que entra a “atualizada” Motoko que&nbsp;precisa rastrear e localizar uma nova inteligência artificial e, ao mesmo tempo, impedir que ela caia em mãos erradas. Qual será o desfecho desta incrível história? Confira em <strong>The Ghost in the Shell 2.0 – Manmachine Interface</strong>.</p>
```

A quebra de linha entre os parágrafos é apenas para fins demonstrativos e didáticos, **não** utilize quebra de linha dentro dos parágrafos e nem após eles.

Para copiar os parágrafos já formatados, você pode clicar com o botão direito do mouse no site, ir em `Inspecionar`. Você perceberá que cada parágrafo será listado, basta selecioná-lo (cada `<p></p>`) e dar `Ctrl + C` e colar no programa, mas cuidado, pode ser que as quebras de linha (*tags* `<br/>` ou simples quebras) façam como se você tivesse dado `Enter` na sinopse, pulando para o próximo campo.

A imagem abaixo ilustra o mesmo parágrafo do exemplo acima, no `Inspecionar` do navegador.

![Imgur](https://i.imgur.com/xiJAdVq.png)

## Dados da Edição

Esta categoria abrange os dados básicos da edição do mangá.

### Volume

Numeração do mangá. Caso o volume seja único, você pode entrar `-1` ou apenas dar `Enter`.

Geralmente o volume fica indicado após um sustenido (#), por exemplo:

    Fort of Apocalypse #10

O volume então, neste caso, seria `10`.

O campo aceita apenas números, **não** digite sustenidos ou letras.

### Autor(es)

Autor(es) do mangá. Caso haja mais de um, todos os nomes devem ser separados por `, ` (vírgula seguida de espaço).

Os nomes devem ser todos ocidentalizados, e romanizados. Geralmente, basta apenas copiar as informações da capa ou da lombada do mangá.

### Número de páginas

Número de páginas do mangá. Caso a informação seja desconhecida, digite `0`.

O campo aceita apenas números, **não** digite letras.

### Classificação etária

Classificação etária do mangá. Seguir o [Sistema de Classificação Indicativa Brasileiro](http://www.justica.gov.br/seus-direitos/classificacao).

Geralmente a classificação se localiza perto do código de barras. Quando este não está aparente, a classificação, geralmente, é `Livre`.

Opções aceitas: `Livre`, `10 anos`, `12 anos`, `14 anos`, `16 anos` ou `18 anos`.

## Edição impressa

Esta categoria abrange os dados e informações da edição impressa do mangá.

### Formato

Formato do mangá.

Deve seguir o padrão `<largura> x <altura> cm`. Caso algum dos números seja real, utilize vírgulas para indicar a parte fracionária.

Exemplos aceitos: `13,7 x 20 cm`, `13,5 x 20,5 cm`, `17 x 24 cm`.

### Preço

Preço *de capa* do mangá.

O campo aceita apenas números, **não** digite letras, nem a moeda. Caso o preço seja desconhecido, digite `0`.

Você pode usar vírgulas ou pontos para a parte fracionária.

Exemplos aceitos: `13.9`, `12,9`, `64.90`.

### ISBN

Código *ISBN* do mangá.

O ISBN geralmente é o mesmo valor do código de barras.

Opte **sempre** pelo valor do *ISBN-13*, porém, se a editora utiliza outro cadastro, como a Nova Sampa que utiliza o *ISSN*, utilize este. Caso o mangá não esteja cadastrado na Agência Brasileira do ISBN, utilize o código de barras, ou, caso este seja desconhecido, deixe o campo em branco.

Você pode entrar com ISBN com hífens, o utilitário os removerá automaticamente.

Exemplos aceitos: `978-85-457-0371-6`, `9788545703716`.

## Edição Digital

Algumas editoras, como a Editora JBC, recentemente começaram a disponibilizar edições digitais de seus mangás.

Caso o mangá possua uma edição digital, digite `S` na pergunta, caso contrário, apenas dê `Enter` para pular esta categoria.

    Edição Digital (S / N): S

### Formato

Formato de disponibilização da edição digital, ou seja, os tipos de arquivos.

Caso haja mais de um tipo de arquivo, estes devem ser separados por `/`.

Exemplos aceitos: `.mobi/.epub`.

### Preço

Preço *de capa* do mangá em sua edição digital.

O campo aceita apenas números, **não** digite letras, nem a moeda. Caso o preço seja desconhecido, digite `0`.

Você pode usar vírgulas ou pontos para a parte fracionária.

Exemplos aceitos: `13.9`, `12,9`, `64.90`.

### Disponível nas lojas

Lojas onde a edição digital está sendo vendida.

Caso haja mais de uma loja, estas devem ser separados por `, ` (vírgula seguida de espaço).

Exemplos aceitos: `Amazon, Livraria Cultura`.

### ISBN [.epub] e ISBN [.mobi]

Código *ISBN* do mangá em sua edição digital, para cada formato.

O ISBN geralmente é o mesmo valor do código de barras.

Opte **sempre** pelo valor do *ISBN-13*, porém, se a editora utiliza outro cadastro, como a Nova Sampa que utiliza o *ISSN*, utilize este. Caso o mangá não esteja cadastrado na Agência Brasileira do ISBN, utilize o código de barras, ou, caso este seja desconhecido, deixe o campo em branco.

Você pode entrar com ISBN com hífens, o utilitário os removerá automaticamente.

Exemplos aceitos: `978-85-457-0371-6`, `9788545703716`.

## Imagens

Esta categoria abrange as imagens do mangá.

### Capa

URL para a imagem da capa do mangá.

Opte **sempre** por utilizar imagens hospedadas no site da própria editora, e por imagens que tenham, pelo menos, `400px` de altura.

Alternativamente, você pode utilizar imagens hospedadas na Amazon.

Caso a capa não esteja disponível, ou não cumpra os critérios acima especificados, deixe o campo em branco, dando `Enter`.

Exemplo aceito: 

    https://jbchost.com.br/mangasjbc/wp-content/uploads/2017/11/The-Ghost-in-the-Shell-2-Sobrecapa_p-300x421.jpg`

Você pode obter o URL da imagem clicando com o botão direito do mouse nela e indo em `Copiar o endereço da imagem`.

### Cabeçalho

URL para a imagem de cabeçalho (*header*) do mangá.

Exemplo de cabeçalho:

![Cabeçalho](https://jbchost.com.br/mangasjbc/wp-content/uploads/2017/12/site_header-gits_2.0.jpg)

Caso não exista uma imagem **oficial** de cabeçalho, deixe o campo em branco, dando `Enter`.

Exemplo aceito:

    https://jbchost.com.br/mangasjbc/wp-content/uploads/2017/12/site_header-gits_2.0.jpg

### URL

URL para a página do mangá no site da editora.

Caso a editora não possua um site apenas para informações, como a Editora JBC possui, você *pode* utilizar a URL para o mangá na loja **oficial** da editora, caso aplica-se.

Caso não exista uma URL, deixe o campo em branco, dando `Enter`.

Exemplos aceitos: 

    https://mangasjbc.com.br/death-note-black-edition-how-to-read-07/
    https://loja.panini.com.br/panini/produto/Manga-The-Legend-of-Zelda-Ocarina-of-Time-Perfect-Edition.aspx