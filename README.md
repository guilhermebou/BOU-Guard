# SBSeg2023
Repositório com o código fonte submetido ao Salão de Ferramentas do SBSeg 2023.

## 📌 Overview
Nesta pasta, encontram-se todo o código-fonte necessários para rodar a aplicação.

## **🏷️ Nota** 
Nesta implementacao utilizamos o python em sua versao 3.10.4, a biblioteca python BeautifulSoup em sua versao 4.12.2 ela é utilizada para realizar a raspagem de dados (web scraping), tambem utlizado a a Interface de Programação de aplicação (API) GPT-3.5-Turbo para realizar a analise, identificação e listagem das expressões desejadas, por ultimo, utilizado a biblioteca Requests 2.31.0 para realizar a requisicao nos sites obtendo o "Hypertext Transfer Protocol(HTTP). O desenvolvimento foi realizado em uma máquina com sistema operacional de 64 bit- Windows 10 Home.

## **📝 Requisitos/Instalação ⚙️** 

Python 3.10.4: Download no site oficial do Python.
(https://www.python.org).

Biblioteca Beautiful Soup 4.12.2: Para a instalação da biblioteca é necessário utilizar o gerenciador de pacotes 'pip'. Abra o terminal ou prompt de comando e execute o seguinte comando: 

```python
# pip install beautifulsoup4==4.12.2
```

API GPT-3.5 Turbo: Para a API, é preciso obter as credenciais de API da OpenAI, realizando cadastro e emissão da chave de acesso "API-KEY" 
(https://www.openai.com).

Biblioteca Requests 2.31.0: Para a instalação da biblioteca é necessário utilizar o gerenciador de pacotes 'pip'. Abra o terminal ou prompt de comando e execute o seguinte comando: 

```python
# pip install requests==2.31.0
``` 

## **🌐 Sites Avaliados**
 👀 observação: HyperLinks referenciados leva direto para a página avaliada. 

| Machismo | Racismo | Homofobia |
| -------- | ------- | --------- |
| [Pure Break](https://www.purebreak.com.br/noticias/10-frases-machistas-que-passam-despercebidas-no-dia-a-dia/91117) | [Direito Humanos ES](https://sedh.es.gov.br/Not%C3%ADcia/novembro-negro-conheca-algumas-expressoes-racistas-e-seus-significados) | [Revista Marie Claire](https://revistamarieclaire.globo.com/Comportamento/noticia/2019/06/nao-parece-mas-e-homofobia-20-frases-que-ofendem-e-devem-ser-abolidas.html) |
| [Espaço Viveka](https://www.espacoviveka.com.br/frases-machistas-que-precisamos-parar-de-usar/) | [Governo de Tocantins](https://www.to.gov.br/cidadaniaejustica/noticias/conheca-algumas-expressoes-racistas-e-por-que-moldar-o-vocabulario-e-uma-forma-de-combater-o-preconceito-racial/43yj0wrg7pzv) | [Governo de Tocantins](https://www.to.gov.br/cidadaniaejustica/noticias/10-frases-homofobicas-que-devemos-tirar-do-nosso-cotidiano/3e7k47m8fy9l#:~:text=1%20%2D%20%E2%80%9CQuando%20voc%C3%AA%20virou%20gay,outros%2C%20tem%20crian%C3%A7a%20aqui!%E2%80%9D) |
| [Lab. de Educação](https://labedu.org.br/12-frases-que-nao-devem-ser-ditas-aos-meninos/) | [VAGAS](https://www.vagas.com.br/profissoes/frases-racistas/) | [Hypeness](https://www.hypeness.com.br/2021/06/11-frases-homofobicas-que-voce-precisa-tirar-agora-do-seu-vocabulario/) |
| [Revista Marie Claire](https://revistamarieclaire.globo.com/Comportamento/noticia/2019/06/nao-parece-mas-e-machismo-20-frases-para-nao-repetir-mais.html) | [Revista Marie Claire](https://revistamarieclaire.globo.com/Comportamento/noticia/2019/07/nao-parece-mas-e-racismo-20-frases-para-extinguir-do-seu-vocabulario.html) | [Gazeta](https://www.agazeta.com.br/revista-ag/comportamento/10-frases-que-ofendem-e-devem-ser-abolidas-0620) |
| [Catho](https://www.catho.com.br/carreira-sucesso/8-de-marco-8-frases-que-mulheres-ouvem-no-trabalho/) | [JusBrasil](https://www.jusbrasil.com.br/noticias/13-expressoes-racistas-que-precisam-sair-do-seu-vocabulario/191503582) | [Uol](https://www.uol.com.br/universa/noticias/redacao/2018/02/14/7-frases-que-sao-homofobicas-e-as-pessoas-falam-sem-perceber.htm) |
| [Uol](https://www.uol.com.br/universa/noticias/redacao/2018/03/14/12-comentarios-rotineiros-que-reforcam-o-machismo-no-dia-a-dia.htm) | [APPSindicato](https://appsindicato.org.br/racismo-sutil-confira-algumas-expressoes-que-devem-ser-banidas-do-vocabulario/) | [Amo Direito](https://www.amodireito.com.br/2022/06/homofobia-20-frases-ofendem-devem-abolidas.html) |
| [CIEE](https://portal.ciee.org.br/institucional/palavras-que-ofendem-termos-machistas-para-pararmos-de-usar-ja/) | [Estado De Minas](https://www.em.com.br/app/noticia/diversidade/2022/12/11/noticia-diversidade,1432124/veja-40-expressoes-racistas-que-o-tse-sugere-banir-do-vocabulario.shtml) | [Catraca Livre](https://catracalivre.com.br/cidadania/10-frases-homofobicas-que-voce-provavelmente-ja-falou/) |
| [Leia Já](https://m.leiaja.com/cultura/2020/03/03/16-frases-machistas-repetidas-ao-redor-do-mundo/) | [Leiturinha](https://leiturinha.com.br/blog/7-expressoes-racistas-para-nao-ensinar-para-sua-crianca/) | [CIEE](https://portal.ciee.org.br/diversos/palavras-que-ofendem-termos-homofobicos-para-pararmos-de-usar-ja/) |
| [Alto Astral](https://www.altoastral.com.br/estido-de-vida/frases-machistas/) | [BBC](https://www.bbc.com/portuguese/geral-59366676) | [Exame](https://exame.com/pop/dia-internacional-contra-a-homofobia-confira-10-frases-para-celebrar-a-data/) |
| [Ne10 - Uol](https://ne10.uol.com.br/mundobit/2020/03/05/dia-da-mulher-frases-machistas-que-ainda-marcam-12-paises/index.html) | [Geledes](https://www.geledes.org.br/12-frases-racistas-que-todo-negro-ja-ouviu-na-vida/) | [Ibahia](https://www.ibahia.com/fervodascores/veja-expressoes-homofobicas-para-tirar-de-vez-do-vocabulario-293522) |
