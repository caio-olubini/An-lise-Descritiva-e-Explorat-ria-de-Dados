"""Gera projeto/ENUNCIADO.pdf a partir do markdown.

Sem pandoc nem LaTeX na maquina: converte markdown -> HTML (lib `markdown`)
e usa o Chrome headless para imprimir em PDF. O anexo ganha quebra de pagina
antes de cada ficha, para cada dataset comecar numa pagina.

Uso: uv run --with markdown python -I gerar_pdf_enunciado.py <pasta_projeto>

O caminho do navegador pode ser trocado pela variavel de ambiente NAVEGADOR
(por padrao, o Chrome do macOS).
"""
import os
import subprocess
import sys
import tempfile

import markdown

CHROME = os.environ.get(
    "NAVEGADOR", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
)

CSS = """
@page { size: A4; margin: 18mm 16mm; }
* { box-sizing: border-box; }
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 10.5pt; line-height: 1.5; color: #1a1a1a; margin: 0;
}
h1 {
  font-size: 17pt; margin: 0 0 4pt; padding-bottom: 6pt;
  border-bottom: 2px solid #1a1a1a; page-break-after: avoid;
}
h1 + p { margin-top: 6pt; }
h2 {
  font-size: 12.5pt; margin: 20pt 0 6pt; padding-bottom: 3pt;
  border-bottom: 1px solid #c8c8c8; page-break-after: avoid;
}
h3 { font-size: 11pt; margin: 14pt 0 4pt; page-break-after: avoid; }
p { margin: 6pt 0; }
ul { margin: 6pt 0; padding-left: 18pt; }
li { margin: 3pt 0; }
strong { font-weight: 600; }
code {
  font-family: "SF Mono", Menlo, Consolas, monospace;
  font-size: 9pt; background: #f2f2f2; padding: 0.5pt 2.5pt; border-radius: 2pt;
}
table {
  border-collapse: collapse; width: 100%; margin: 8pt 0; font-size: 9.5pt;
}
th, td {
  border: 0.5pt solid #b8b8b8; padding: 4pt 6pt; text-align: left;
  vertical-align: top;
}
th { background: #ececec; font-weight: 600; }
tr { page-break-inside: avoid; }
blockquote {
  margin: 8pt 0; padding: 6pt 10pt; border-left: 2.5pt solid #b8b8b8;
  background: #f7f7f7; font-size: 9.5pt;
}
blockquote p { margin: 3pt 0; }
hr { border: 0; border-top: 0.5pt solid #d0d0d0; margin: 16pt 0; }
.anexo h1 { page-break-before: always; }
.anexo h2 { page-break-before: always; }
"""

PLANTILLA = """<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8">
<title>Projeto final - MATD39</title><style>{css}</style></head>
<body>{corpo}</body></html>
"""


def renderizar(texto):
    return markdown.markdown(texto, extensions=["tables", "sane_lists"])


def main():
    projeto = sys.argv[1] if len(sys.argv) > 1 else "."
    origem = os.path.join(projeto, "ENUNCIADO.md")
    destino = os.path.join(projeto, "ENUNCIADO.pdf")

    with open(origem, encoding="utf-8") as f:
        texto = f.read()

    # O anexo comeca no h1 "# Anexo"; separa para dar quebra de pagina por ficha.
    marcador = "\n# Anexo"
    corte = texto.index(marcador)
    principal = renderizar(texto[:corte])
    anexo = renderizar(texto[corte + 1:])

    corpo = principal + '<div class="anexo">' + anexo + "</div>"

    with tempfile.TemporaryDirectory() as pasta:
        html_caminho = os.path.join(pasta, "enunciado.html")
        with open(html_caminho, "w", encoding="utf-8") as f:
            f.write(PLANTILLA.format(css=CSS, corpo=corpo))

        if os.path.exists(destino):
            os.remove(destino)
        resultado = subprocess.run(
            [
                CHROME, "--headless", "--disable-gpu", "--no-sandbox",
                "--no-pdf-header-footer",
                "--print-to-pdf=" + destino,
                "file://" + html_caminho,
            ],
            capture_output=True, text=True,
        )

    if not os.path.exists(destino):
        print(resultado.stdout[-2000:])
        print(resultado.stderr[-2000:])
        raise SystemExit("O Chrome nao gerou o PDF.")

    tamanho_kb = round(os.path.getsize(destino) / 1024)
    print("PDF:", destino, "|", tamanho_kb, "KB")


if __name__ == "__main__":
    main()
