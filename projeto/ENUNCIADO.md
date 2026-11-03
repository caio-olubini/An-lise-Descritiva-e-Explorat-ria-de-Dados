# Projeto final — MATD39

**Análise Descritiva e Exploratória de Dados A**

Grupos de 5 integrantes · Entrega do relatório: **15/12/2026** · Linguagem: Python ou R

---

## 1 · Objeto

O projeto final consiste na análise descritiva e exploratória de um conjunto de
dados públicos brasileiros, a partir de uma pergunta central definida para cada
conjunto. A resposta deve se apoiar nas medidas, tabelas e gráficos produzidos.

Serão entregues um **relatório** e uma **arguição oral**.

---

## 2 · Organização

- São **seis conjuntos de dados**, um por grupo. Cada grupo tem **5 integrantes**.
  A ordem de escolha é sorteada, e cada grupo escolhe o seu quando chegar a sua
  vez.
- A linguagem é livre: **Python ou R**.
- Os seis arquivos são publicados junto com este enunciado e ficam disponíveis
  em **URL fixa** durante todo o projeto. O arquivo deve ser lido diretamente do
  link — `read.csv` em R, `pd.read_csv` em Python.
- **Entrega do relatório:** 15 de dezembro de 2026. O relatório e o código devem
  ser enviados para um diretório em serviço de nuvem (Google Drive ou
  equivalente), cujo link será divulgado no AVA da disciplina.
- **Arguição oral:** realizada remotamente, com horário agendado previamente com
  cada grupo.
- **Não há entregas intermediárias.**

---

## 3 · Conteúdo do relatório

O relatório deve conter as dez saídas abaixo, comuns aos seis grupos. Análises
adicionais são permitidas.

| # | saída |
|---|---|
| 1 | Dimensão da tabela (linhas e colunas), tipos das variáveis e percentual de valores faltantes |
| 2 | Média, mediana, quartis, desvio padrão, coeficiente de variação e IQR de **uma** variável numérica |
| 3 | Frequência e proporção de **uma** variável categórica, com gráfico de barras |
| 4 | Histograma **e** boxplot da **mesma** variável |
| 5 | A mesma medida calculada em **dois ou mais subgrupos** |
| 6 | Assimetria de Pearson e curtose |
| 7 | Quantos casos têm \|z\| > 2 e **quais são** — as linhas devem ser nomeadas |
| 8 | Correlação entre **duas ou mais** variáveis numéricas |
| 9 | Dois achados escritos, sendo **um deles não previsto** |
| 10 | Resposta à pergunta central em **um parágrafo** |

Os itens 9 e 10 referem-se à interpretação dos resultados; os demais, ao cálculo
e à apresentação.

O **código** que gerou os resultados (notebook ou script, executável) deve ser
entregue junto com o relatório.

---

## 4 · Avaliação

| componente | peso |
|---|---|
| relatório | 60% |
| arguição oral | 40% |

A arguição oral é realizada por grupo, com duração de 30 minutos e perguntas
sorteadas no momento. Cada integrante responde sobre a parte que lhe couber. A
nota individual é obtida do cruzamento entre a nota do grupo e o desempenho na
arguição.

Critérios:

- **Suficiente** — as dez saídas do item 3 foram entregues.
- **Ótimo** — além das saídas, o grupo apresenta análise crítica dos resultados:
  interpretação, verificação e justificativa do que os dados mostram.

---

## 5 · Uso de inteligência artificial

O uso de ferramentas de inteligência artificial (ChatGPT, Claude, Copilot ou
equivalentes) é permitido, sem restrição de ferramenta. **É obrigatório declarar
esse uso.**

O relatório deve conter uma seção **"Uso de IA"**, informando:

- em que **etapa** a ferramenta foi utilizada;
- com que **finalidade**;
- qual foi o **aproveitamento** da resposta — utilizada, corrigida ou
  descartada.

> Exemplo: "A ferramenta foi utilizada na redação do código do boxplot por
> região, por não sabermos separar as cores por grupo; a resposta foi utilizada
> sem alteração. Foi utilizada também na interpretação do coeficiente de
> variação, cujo resultado estava incorreto — confundia o coeficiente com o
> desvio padrão; a interpretação foi refeita."

**O uso de IA não substitui o que o grupo precisa saber responder na arguição.**
Ainda que trechos do código tenham sido gerados com auxílio de IA, a arguição
pode incluir perguntas sobre qualquer parte do trabalho — o que determinada
função ou comando faz, como se lê um resultado, por que uma medida foi escolhida.

As perguntas da arguição são sorteadas no momento, e cada integrante responde
sobre a parte que lhe couber. Por esse motivo, **todos os membros da equipe
devem estar aptos a responder sobre qualquer parte do trabalho**.

---

# Anexo — os seis conjuntos de dados

Cada ficha apresenta a pergunta central, o link do arquivo, a descrição do
conjunto e o dicionário das colunas. Todos os arquivos estão em CSV e podem ser
lidos diretamente do link.

Os conjuntos são provenientes de fontes oficiais brasileiras e foram previamente
tratados. A descrição do conteúdo de cada arquivo integra o item 1 do relatório.

---

## 1 · Transporte — acidentes em rodovias federais

**Pergunta central:** acidentes em rodovia federal são mais perigosos de dia ou
de noite?

**Arquivo:** `acidentes_prf_2024.csv` — [URL do CSV — a definir]

**Descrição.** Acidentes registrados pela Polícia Rodoviária Federal nas
rodovias federais do país em 2024: **73.201 acidentes**, 29 colunas. Cada linha
corresponde a um acidente, com data, hora, local, causa, tipo e resultado
(mortos, feridos, ilesos).

**Dicionário dos campos**

| coluna | o que é |
|---|---|
| `id` | Identificador do acidente |
| `data_inversa` | Data do acidente |
| `dia_semana` | Dia da semana |
| `horario` | Hora do acidente, no formato HH:MM:SS |
| `uf` | Estado (sigla) |
| `br` | Número da rodovia federal (ex.: 101, 116) |
| `km` | Quilômetro da rodovia onde ocorreu |
| `municipio` | Município |
| `causa_acidente` | Causa provável registrada (69 valores, ex.: "Reação tardia ou ineficiente do condutor") |
| `tipo_acidente` | Tipo de acidente (17 valores, ex.: "Colisão traseira", "Saída de leito carroçável") |
| `classificacao_acidente` | Gravidade: Sem Vítimas, Com Vítimas Feridas ou Com Vítimas Fatais |
| `fase_dia` | Momento do dia: Pleno dia, Plena Noite, Anoitecer, Amanhecer |
| `sentido_via` | Sentido da via: Crescente, Decrescente, Não Informado |
| `condicao_metereologica` | Clima no momento: Céu Claro, Nublado, Chuva, Sol, Garoa/Chuvisco, Nevoeiro/Neblina, Vento, Granizo, Neve, Ignorado |
| `tipo_pista` | Simples, Dupla ou Múltipla |
| `tracado_via` | Traçado da via (Reta, Curva, Aclive, Declive; pode combinar mais de um) |
| `uso_solo` | Sim se o trecho está em área urbana, Não se rural |
| `pessoas` | Total de pessoas envolvidas |
| `mortos` | Pessoas mortas |
| `feridos_leves` | Feridos leves |
| `feridos_graves` | Feridos graves |
| `ilesos` | Pessoas ilesas |
| `ignorados` | Pessoas sem estado informado |
| `feridos` | Feridos leves + graves *(derivada)* |
| `veiculos` | Veículos envolvidos |
| `latitude` | Coordenada geográfica |
| `longitude` | Coordenada geográfica |
| `hora` | Hora do dia em número decimal (03:56 corresponde a 3,93) *(derivada)* |
| `total_vitimas` | Feridos + mortos *(derivada)* |

---

## 2 · Trabalho — salários por ocupação em São Paulo

**Pergunta central:** quais ocupações pagam melhor em São Paulo?

**Arquivo:** `caged_sp_2024_01.csv` — [URL do CSV — a definir]

**Descrição.** Admissões registradas no **Novo CAGED** (registro oficial de
emprego do Ministério do Trabalho) no estado de São Paulo em janeiro de 2024:
**633.990 admissões**, 10 colunas. Cada linha corresponde a uma pessoa
contratada, com ocupação, escolaridade, idade e salário.

**Dicionário dos campos**

| coluna | o que é |
|---|---|
| `municipio` | Município do estabelecimento (644 municípios) |
| `ocupacao` | Nome da ocupação (2.045 ocupações distintas) |
| `categoria` | Tipo de vínculo: Geral, Temporário, Aprendiz, Intermitente, Prazo determinado, Rural de pequeno prazo |
| `secao` | Seção da atividade econômica (21 seções, ex.: Comércio, Construção, Indústria de transformação) |
| `grau_instrucao` | Escolaridade (12 níveis, de Analfabeto a Doutorado) |
| `raca_cor` | Raça/cor declarada (Branca, Parda, Preta, Amarela, Indígena, Não informada, Não Identificado) |
| `sexo` | Homem, Mulher, Não Identificado |
| `idade` | Idade em anos (14 a 88) |
| `horas_contratuais` | Jornada semanal contratada |
| `salario` | Salário mensal, em reais |

---

## 3 · Educação — cursos de ensino superior por município

**Pergunta central:** o ensino a distância domina o ensino superior brasileiro?

**Arquivo:** `educacao_superior_curso_2023.csv` — [URL do CSV — a definir]

**Descrição.** Cursos de graduação ofertados no **Censo da Educação Superior
2023**, do INEP: **660.571 cursos ofertados**, 15 colunas. Cada linha
corresponde a um curso de uma instituição em um município — 3.495 municípios,
27 unidades da federação, 2.580 instituições e 46.248 cursos distintos. As
contagens de alunos (`ingressantes`, `matriculas`, `concluintes`) são as do ano
de 2023.

Um mesmo curso aparece em várias linhas quando a instituição o oferece em mais
de um município.

**Dicionário dos campos**

| coluna | o que é |
|---|---|
| `cod_ies` | Código da instituição de ensino superior |
| `cod_curso` | Código do curso dentro da instituição |
| `curso` | Nome do curso (ex.: Pedagogia, Direito, Enfermagem) |
| `cod_municipio` | Código do município no IBGE |
| `municipio` | Município onde o curso é ofertado |
| `uf` | Estado (sigla) |
| `regiao` | Norte, Nordeste, Sudeste, Sul, Centro-Oeste |
| `capital` | Capital ou Interior |
| `categoria` | Natureza administrativa: Pública federal, Pública estadual, Pública municipal, Privada com fins lucrativos, Privada sem fins lucrativos, Especial |
| `organizacao` | Universidade, Centro universitário, Faculdade, Instituto Federal de Educação, Ciência e Tecnologia, Centro Federal de Educação Tecnológica |
| `grau` | Bacharelado, Licenciatura, Tecnológico, Bacharelado e licenciatura, Não informado |
| `modalidade` | Presencial ou A distância |
| `ingressantes` | Alunos que ingressaram no curso em 2023 |
| `matriculas` | Alunos matriculados no curso em 2023 |
| `concluintes` | Alunos que concluíram o curso em 2023 |

---

## 4 · Saúde — mortalidade infantil por município

**Pergunta central:** a mortalidade infantil é maior no interior ou nas
capitais?

**Arquivo:** `mortalidade_infantil_municipio_2022.csv` — [URL do CSV — a definir]

**Descrição.** Nascimentos e óbitos de crianças menores de 1 ano em 2022, por
município, a partir do **SINASC** (registro de nascidos vivos) e do **SIM**
(registro de óbitos): **3.299 municípios**, 11 colunas. Foram mantidos os
municípios com pelo menos 100 nascidos vivos no ano.

**Dicionário dos campos**

| coluna | o que é |
|---|---|
| `codigo_ibge` | Código do município no IBGE |
| `municipio` | Nome do município |
| `uf` | Estado (sigla) |
| `regiao` | Nordeste, Sudeste, Sul, Norte, Centro-Oeste |
| `capital` | Capital ou Interior |
| `populacao` | População do município |
| `nascidos_vivos` | Nascidos vivos em 2022 |
| `obitos_infantis` | Óbitos de crianças menores de 1 ano em 2022 |
| `taxa_mortalidade_infantil` | Óbitos por mil nascidos vivos |
| `peso_medio_nascer` | Peso médio ao nascer, em gramas |
| `proporcao_baixo_peso` | Proporção de nascidos com menos de 2.500 g |

---

## 5 · Agricultura — produção agrícola por município

**Pergunta central:** qual estado tem a agricultura mais produtiva?

**Arquivo:** `producao_agricola_municipio_2023.csv` — [URL do CSV — a definir]

**Descrição.** Produção das lavouras temporárias em 2023, da **Produção
Agrícola Municipal** (PAM), do IBGE: **35.919 lavouras**, 11 colunas. Cada
linha corresponde a uma lavoura — a combinação de um município com um produto —
em 5.484 municípios e 30 produtos, somando 90,2 milhões de hectares colhidos e
R$ 690,9 bilhões em valor de produção.

**Dicionário dos campos**

| coluna | o que é |
|---|---|
| `cod_municipio` | Código do município no IBGE |
| `municipio` | Nome do município |
| `uf` | Estado (sigla) |
| `uf_nome` | Nome do estado |
| `regiao` | Norte, Nordeste, Sudeste, Sul, Centro-Oeste |
| `produto` | Lavoura (30 produtos, ex.: Soja (em grão), Cana-de-açúcar, Mandioca, Feijão (em grão)) |
| `area_plantada_ha` | Área plantada, em hectares |
| `area_colhida_ha` | Área efetivamente colhida, em hectares |
| `quantidade_t` | Quantidade produzida, em toneladas |
| `rendimento_kg_ha` | Rendimento médio da lavoura, em kg por hectare |
| `valor_mil_reais` | Valor da produção, em milhares de reais |

O **rendimento** é a razão entre a quantidade produzida e a área colhida. Ele é
calculado pelo IBGE para cada lavoura de cada município — não existe um
rendimento do município nem do estado na tabela.

---

## 6 · Moradia — saneamento básico por município

**Pergunta central:** qual região do Brasil tem mais domicílios com esgoto
adequado?

**Arquivo:** `saneamento_municipio_2022.csv` — [URL do CSV — a definir]

**Descrição.** Domicílios particulares permanentes ocupados, por tipo de
esgotamento sanitário, do **Censo Demográfico 2022** (IBGE): **5.570
municípios**, 16 colunas. Cada linha corresponde a um município, com a contagem
de domicílios em cada destino do esgoto e a proporção de esgoto adequado.

**Dicionário dos campos**

| coluna | o que é |
|---|---|
| `cod_municipio` | Código do município no IBGE |
| `municipio` | Nome do município |
| `uf` | Estado (sigla) |
| `uf_nome` | Nome do estado |
| `regiao` | Norte, Nordeste, Sudeste, Sul, Centro-Oeste |
| `total_domicilios` | Domicílios particulares permanentes ocupados |
| `dom_adequado` | Domicílios com esgotamento adequado *(derivada)* |
| `dom_rede_geral_pluvial` | Domicílios com esgoto na rede geral ou pluvial |
| `dom_fossa_septica_ligada` | Domicílios com fossa séptica ou filtro ligado à rede |
| `dom_fossa_septica_nao_ligada` | Domicílios com fossa séptica ou filtro não ligado à rede |
| `dom_fossa_rudimentar` | Domicílios com fossa rudimentar ou buraco |
| `dom_vala` | Domicílios que lançam o esgoto em vala |
| `dom_rio` | Domicílios que lançam o esgoto em rio, lago, córrego ou mar |
| `dom_outra` | Domicílios com outra forma de esgotamento |
| `dom_sem_banheiro` | Domicílios sem banheiro nem sanitário |
| `pct_adequado` | Domicílios com esgotamento adequado, em % do total *(derivada)* |

O esgotamento **adequado** é a classificação do IBGE: rede geral ou pluvial, ou
fossa séptica ou filtro ligado à rede. As duas parcelas aparecem separadas nas
colunas acima, e `dom_adequado` é a soma delas.
