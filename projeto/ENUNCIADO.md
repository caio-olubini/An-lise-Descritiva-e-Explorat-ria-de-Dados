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
  ser enviados para o diretório do grupo no Google Drive da disciplina.
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

## 3 · Segurança — ocorrências criminais por município

**Pergunta central:** a criminalidade aumentou no Brasil entre 2015 e 2025?

**Arquivo:** `seguranca_publica_municipio.csv` — [URL do CSV — a definir]

**Descrição.** Registros de ocorrências do **SINESP** (Sistema Nacional de
Estatísticas de Segurança Pública, do Ministério da Justiça), por município e
por ano: **667.559 linhas**, 5 colunas. Cada linha corresponde ao total de casos
de um indicador, em um município, em um ano. Cobre 5.297 municípios das 27
unidades da federação.

Os dados abrangem de 2015 a 2026, e **2026 está incompleto** — o ano ainda não
havia terminado quando a base foi extraída.

**Dicionário dos campos**

| coluna | o que é |
|---|---|
| `uf` | Estado (sigla) |
| `municipio` | Município |
| `ano` | Ano do registro (2015 a 2026) |
| `indicador` | Tipo de ocorrência — 10 valores, listados abaixo |
| `casos` | Número de casos registrados |

Os 10 indicadores: Feminicídio · Homicídio doloso · Lesão corporal seguida de
morte · Mandado de prisão cumprido · Morte no trânsito ou em decorrência dele
(exceto homicídio doloso) · Mortes a esclarecer (sem indício de crime) · Roubo
seguido de morte (latrocínio) · Suicídio · Tentativa de homicídio · Tentativa de
feminicídio.

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

## 5 · Desmatamento — alertas na Amazônia Legal

**Pergunta central:** o desmatamento na Amazônia aumentou em 2025?

**Arquivo:** `desmatamento_amazonia_alertas.csv` — [URL do CSV — a definir]

**Descrição.** Alertas de desmatamento e degradação do sistema **DETER**, do
INPE, na Amazônia Legal: **466.707 alertas**, 9 colunas. Cada linha corresponde a
um alerta — uma área detectada por satélite, com data, município e tipo de
alteração. Abrange de 2016 a 2026.

**Dicionário dos campos**

| coluna | o que é |
|---|---|
| `data` | Data do alerta |
| `ano` | Ano da data do alerta (2016 a 2026) |
| `mes` | Mês (1 a 12) |
| `ano_prodes` | Ano de referência do PRODES, que mede de agosto de um ano a julho do seguinte |
| `uf` | Estado (sigla), dentro da Amazônia Legal |
| `municipio` | Município |
| `codigo_municipio` | Código do município no IBGE |
| `classe` | Tipo de alteração detectada — 8 valores, listados abaixo |
| `area_km2` | Área do alerta, em km² |

As 8 classes: `DESMATAMENTO_CR` (corte raso, a área foi totalmente desmatada) ·
`DESMATAMENTO_VEG` (desmatamento com vegetação) · `DEGRADACAO` (floresta
degradada, não removida) · `CICATRIZ_DE_QUEIMADA` (marca de queimada) ·
`MINERACAO` (garimpo) · `CORTE_SELETIVO` (retirada de madeira) ·
`CS_DESORDENADO` e `CS_GEOMETRICO` (alertas com problema de geometria).

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
