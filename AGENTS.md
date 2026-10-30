# AGENTS.md — contexto do lab

Contexto para quem continuar iterando nestes notebooks (pessoa ou agente).
Se você só tem tempo para ler uma seção, leia **Convenções do notebook** e
**Regras pedagógicas**.

## O que é este projeto

Lab de análise exploratória de dados em Python, dado em duas aulas para uma
turma que **já sabe estatística descritiva e vem de R**. O objetivo não é
ensinar estatística — é trocar a ferramenta. Por isso todo conceito novo de
Python é ancorado num equivalente em R (`data.frame`, `aggregate()`,
`table()`, `ggplot2`, `dim()`).

A turma roda no **Google Colab**, e isso é restrição de projeto: nada de
arquivo local, os dados vêm de URL e as dependências se resolvem com
`%pip install` na primeira célula. O mesmo notebook precisa rodar do zero,
no navegador, a qualquer momento.

## Arquivos

| arquivo | papel |
|---|---|
| `01_python_basico.ipynb` | aula 1 — tipos, listas, NumPy, abrir o CSV, uma variável e uma por grupo |
| `01_python_basico_gabarito.ipynb` | mesma aula, células preenchidas (para projetar) |
| `02_eda_spotify.ipynb` | aula 2 — EDA completa (uma e duas variáveis) |
| `02_eda_spotify_gabarito.ipynb` | gabarito da aula 2 |
| `03_posicao_dispersao_terror.ipynb` | aula 3 — medidas de posição e dispersão (filmes de terror) |
| `03_posicao_dispersao_terror_gabarito.ipynb` | gabarito da aula 3 |
| `tools/gerar_aula03.py` | fonte única do par da aula 3 — edite aqui e regenere |
| `ementa/matd39_analise_descritiva_exploratoria_a.pdf` | programa oficial da disciplina (MATD39, UFBA) — documento de referência |
| `ementa/matd39_analise_descritiva_exploratoria_a.md` | transcrição do mesmo programa, para leitura e grep |

Regra: **todo notebook de aula tem um par `_gabarito`**. Os dois têm
exatamente as mesmas células, na mesma ordem. O que muda:

- **turma**: células "SUA VEZ" vazias (`# SUA VEZ — digite aqui o código do
  texto acima`) ou com lacunas `____`;
- **gabarito**: as mesmas células preenchidas, mais uma célula de aviso no
  topo (`> **VERSÃO GABARITO** — ...`).

Ao editar um, edite o outro na mesma passada. Detalhe operacional: os dois
arquivos têm as **mesmas células com ids diferentes** — o gabarito é a turma
deslocada em uma célula. Scripts que editam os dois devem mapear por posição,
não por id.

A aula 3 é gerada, não editada à mão. Mexeu em conteúdo? Edite
`tools/gerar_aula03.py` e rode:

```bash
uv run --with pandas python -I tools/gerar_aula03.py .
```

Isso reescreve os dois notebooks de uma vez, com o mapeamento por posição
já resolvido. Editar os `.ipynb` direto funciona, mas aí o gerador fica
desatualizado e a próxima regeração desfaz seu trabalho — escolha um dos
dois caminhos, não os dois. As aulas 1 e 2 não têm gerador: são editadas
nos dois arquivos na mesma passada.

## A ementa da disciplina (MATD39)

O lab é material de apoio da disciplina **MATD39 — Análise Descritiva e
Exploratória de Dados A** (UFBA, Departamento de Estatística, 2010; 68 h,
51 teóricas + 17 práticas). O programa oficial está em `ementa/` — o PDF é o
documento original, o `.md` ao lado é a transcrição para consulta.

A ementa é a referência de **escopo**: ela lista os tópicos que a disciplina
deve cobrir, e o lab cobre uma parte deles. Antes de acrescentar conteúdo,
confira ali se o tópico é da disciplina (e evite duplicar o que a aula
presencial já dá).

| tópico da ementa | onde está no lab |
|---|---|
| 2.2 Medidas de posição (médias, separatrizes, quartis) | aula 3 §3; aula 1 §4; aula 2 §2 |
| 2.3 Dispersão (desvio padrão, variância, CV) | aula 3 §4 (desvio padrão e CV); o IQR entra no lugar do desvio médio |
| 2.4 Variável reduzida | aula 3 §4, bloco opcional de z-score |
| 4.1 Fase exploratória × confirmatória | é o fio da aula 2 e da aula 3 |
| 4.3.5 Valores atípicos + 4.4 Boxplot | aula 3 §4 (boxplot e cerca do IQR) e §2/§5 (corte por `vote_count`) |

**Ainda não cobertos por nenhuma aula** (candidatos naturais a aula 4+):
cálculo com somatórios (1); médias geométrica, harmônica e quadrática,
decis e percentis (2.2); desvio médio (2.3.1); **momentos, assimetria e
curtose (3)** — o bloco mais largo da ementa sem nenhuma cobertura;
ramo-e-folhas (4.2); juntas, oitavos e trimédia (4.3.2–4.3.3); e
**proporções, taxas e índices (5)**, incluindo números-índices,
Laspeyres/Paasche/Fisher e deflacionamento.

## Convenções do notebook

Estrutura de uma aula:

- célula de título com a **pergunta da aula** e a fonte dos dados;
- seção "Como usar este notebook" (Shift + Enter, o que é "SUA VEZ", ler a
  última linha do erro);
- seções numeradas `## N · Título  \`⏱️ X–Y min\`` — o orçamento de tempo é
  explícito no cabeçalho e precisa ficar monotonicamente crescente;
- fechamento com "De volta à pergunta", "Para onde isso leva" e um bloco
  "Para brincar depois" (nunca obrigatório).

Marcadores de interação, sempre com estes nomes:

- `### SUA VEZ — digite você mesmo` — a célula de código está vazia e o
  código completo aparece no texto acima;
- `### SUA VEZ — preencha as lacunas` — a célula tem `____` para completar;
- `### SUA VEZ — troque a variável` / `— troque a coluna` / `— troque o par`
  — pede para reusar código mudando um parâmetro;
- `opcional / se der tempo` no cabeçalho — válvula de escape se a aula
  atrasar. Use com parcimônia: é o que permite cortar sem perder o fio.

Estilo de escrita:

- português, segunda pessoa ("você"), tom direto, sem exclamação;
- negrito no termo que importa (`**DataFrame**`), não para ênfase solta;
- tabelas comparando Python e R sempre que um conceito novo aparece;
- emoji só no `⏱️` dos cabeçalhos e nos checkboxes do fechamento;
- o texto **interpreta** o output antes da célula seguinte — não descreve o
  código, diz o que o resultado significa;
- achados estatísticos são afirmados com número (ex.: "nenhuma correlação
  passa de 0,15 em módulo"), não com "parece que".

Estilo do código:

- **`print()` nunca calcula.** O argumento do `print()` recebe texto e
  nomes que já existem — nunca uma chamada (`.sum()`, `.mean()`,
  `len()`, `round()`, `.quantile()`, `.nlargest()`, `.tolist()`,
  `.to_string()`), uma comparação (`== 0`) ou uma conta
  (`q75 - q25`, `100 * n / total`). Calcule numa variável nomeada na
  linha de cima e imprima a variável:

  ```python
  # não
  print("IQR:", q75 - q25)

  # sim
  iqr = q75 - q25
  print("IQR:", iqr)
  ```

  Motivo didático, não estético: a turma lê a linha e não vê de onde o
  número veio, nem consegue reusar aquele valor na célula seguinte. Com
  a variável separada, `iqr` vira vocabulário. Vale para o markdown dos
  "SUA VEZ" também — o código de referência mostrado no texto segue a
  mesma regra, senão a turma copia a versão ruim. `print(filmes.shape)`
  e `print(pd.__version__)` passam: atributo simples não é cálculo.

## Regras pedagógicas (aprendidas na prática)

- **Toda ferramenta ensinada ganha uma variação.** Ensinar só o uso mínimo
  (criar lista, acessar um elemento) deixa a turma sem vocabulário para o
  passo seguinte. Inclua uma variação pequena do **mesmo** recurso — um uso
  vizinho, não um tópico novo, e não um desafio de verdade. Exemplos já
  aplicados: `agg()` com várias medidas (`["mean", "median", "std"]` numa
  lista só), `corr()` aplicado a várias colunas de uma vez, `quantile` numa
  lista e `quantile` por grupo, média de coluna booleana como proporção, e
  `nlargest()`. Candidatos ainda não usados: fatia de lista (`valores[1:3]`)
  e índice negativo, `range()`, matrizes especiais (`np.zeros` / `np.ones` /
  `np.eye` / `np.arange`), fatia de linhas com `iloc`,
  `value_counts(normalize=True)`, `groupby` com duas colunas,
  `corr(method="spearman")`, filtro booleano com duas condições (`&`).
- **Os achados são o fio condutor.** Na aula 2, "características de áudio
  descrevem gênero, mas não popularidade" é o ponto da aula — ajustes de
  conteúdo não podem diluí-lo nem antecipá-lo. Na aula 3, o ponto é que a
  dispersão aparente das notas ao longo das décadas é artefato de
  composição da tabela: a leitura ingênua precisa aparecer **primeiro**, e
  só então ser desmontada pelo corte de `vote_count`. Antecipar o corte
  (limpando antes de mostrar o problema) mata a aula.

## Stack e dados

- Python 3.12, gerenciado com **uv** (`pyproject.toml`, `uv.lock`). Não edite
  `uv.lock` à mão — rode `uv lock`.
- Dependências: `numpy`, `pandas`, `seaborn`, `matplotlib` (+ `jupyter` e
  `ipykernel` para rodar local).
- Dados, sempre TidyTuesday, com a URL fixa na célula de `read_csv`:
  - aulas 1 e 2 — *Spotify Songs*, 2020-01-21;
  - aula 3 — *Horror Movies* (TMDB), 2022-11-01: 32.540 filmes, ~14 MB.
    Carrega em alguns segundos no Colab; a aula depende de três recortes
    nomeados (`terror`, `terror_votado`, `terror_bilheteria`), e o texto
    sempre diz de qual deles cada número veio.

## Verificação

A versão da turma tem `____` e células vazias, então **não executa inteira —
isso é esperado**. Valide rodando o gabarito ponta a ponta:

```bash
uv run jupyter nbconvert --to notebook --execute <aula>_gabarito.ipynb --output /tmp/check.ipynb
```

Depois confira, na versão da turma, que toda célula "SUA VEZ" tem a
correspondente preenchida no gabarito e que os `⏱️` continuam crescentes.

Como o texto interpreta o output antes da célula seguinte, vale conferir
que cada número afirmado na prosa bate com a saída real da execução — é o
erro mais fácil de cometer e o mais difícil de ver relendo o markdown.
Conferir número por número contra o output, e não relendo: na aula 3 duas
afirmações sobreviveram a várias releituras e só caíram na conferência
mecânica (um empate de quantis atribuído ao par errado e "11.602 filmes
sem nota" quando o certo era 11.590).

Vale também um `grep -n 'print(' ` no notebook: qualquer chamada,
comparação ou operador dentro do argumento do `print()` é violação da
regra de estilo do código, e aparece fácil assim.
