#!/usr/bin/env python3
"""Render ontwerp Markdown with Mermaid blocks to PDF via Kroki and WeasyPrint."""

from __future__ import annotations

import html
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MERMAID_RE = re.compile(r"```mermaid\n(.*?)```", re.DOTALL)
INIT = (
    "%%{init: {"
    "'theme':'neutral',"
    "'flowchart':{'htmlLabels':false,'nodeSpacing':28,'rankSpacing':32,'padding':8},"
    "'sequence':{'mirrorActors':false,'messageFontSize':12},"
    "'themeVariables':{'fontSize':'13px'}"
    "}}%%\n"
)


def kroki_svg(source: str) -> str:
    body = source if source.lstrip().startswith("%%{init:") else INIT + source
    request = urllib.request.Request(
        "https://kroki.io/mermaid/svg",
        data=body.encode("utf-8"),
        headers={"Content-Type": "text/plain", "User-Agent": "uwv-woo-ontwerp"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=90) as response:
        return response.read().decode("utf-8")


def inline_markdown(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    return escaped


def markdown_to_html(markdown: str, svg_dir: Path, stem: str) -> str:
    svg_dir.mkdir(parents=True, exist_ok=True)
    diagram_index = 0

    def replace_diagram(match: re.Match[str]) -> str:
        nonlocal diagram_index
        diagram_index += 1
        source = match.group(1).strip() + "\n"
        svg = kroki_svg(source).replace("container", f"diagram{diagram_index}")
        svg_path = svg_dir / f"{stem}-{diagram_index}.svg"
        svg_path.write_text(svg, encoding="utf-8")
        print(f"  diagram {diagram_index}: {svg_path.name} ({len(svg)} bytes)")
        return f"\n\n[[DIAGRAM:{svg_path}]]\n\n"

    text = MERMAID_RE.sub(replace_diagram, markdown)
    lines = text.splitlines()
    parts: list[str] = []
    i = 0

    def flush_paragraph(buf: list[str]) -> None:
        if buf:
            parts.append(f"<p>{inline_markdown(' '.join(buf))}</p>")
            buf.clear()

    paragraph: list[str] = []
    while i < len(lines):
        line = lines[i]
        if line.startswith("[[DIAGRAM:") and line.endswith("]]"):
            flush_paragraph(paragraph)
            path = line[len("[[DIAGRAM:") : -2]
            svg = Path(path).read_text(encoding="utf-8")
            parts.append(f'<figure class="diagram">{svg}</figure>')
            i += 1
            continue
        if line.startswith("#"):
            flush_paragraph(paragraph)
            level = len(line) - len(line.lstrip("#"))
            title = inline_markdown(line[level:].strip())
            parts.append(f"<h{level}>{title}</h{level}>")
            i += 1
            continue
        if line.startswith("|"):
            flush_paragraph(paragraph)
            rows: list[str] = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append(lines[i])
                i += 1
            cells = [
                [cell.strip() for cell in row.strip().strip("|").split("|")]
                for row in rows
                if not re.match(r"^\|\s*-+", row)
            ]
            if not cells:
                continue
            head, *body = cells
            table = ["<table><thead><tr>"]
            table.extend(f"<th>{inline_markdown(cell)}</th>" for cell in head)
            table.append("</tr></thead><tbody>")
            for row in body:
                table.append("<tr>")
                table.extend(f"<td>{inline_markdown(cell)}</td>" for cell in row)
                table.append("</tr>")
            table.append("</tbody></table>")
            parts.append("".join(table))
            continue
        if line.startswith("- "):
            flush_paragraph(paragraph)
            items: list[str] = []
            while i < len(lines) and lines[i].startswith("- "):
                items.append(f"<li>{inline_markdown(lines[i][2:].strip())}</li>")
                i += 1
            parts.append("<ul>" + "".join(items) + "</ul>")
            continue
        if not line.strip():
            flush_paragraph(paragraph)
            i += 1
            continue
        paragraph.append(line.strip())
        i += 1
    flush_paragraph(paragraph)
    return "\n".join(parts)


CSS = """
@page { size: A4; margin: 14mm 13mm 16mm; }
html { font-family: "DejaVu Sans", sans-serif; font-size: 10.5pt; line-height: 1.45; color: #1c1917; }
* { print-color-adjust: exact; -webkit-print-color-adjust: exact; }
h1 { font-size: 20pt; margin: 0 0 0.4em; line-height: 1.2; }
h2 { font-size: 14pt; margin: 1.3em 0 0.4em; page-break-after: avoid; }
h3 { font-size: 12pt; margin: 1em 0 0.3em; break-after: avoid-page; }
p { margin: 0.4em 0 0.7em; }
ul { margin: 0.3em 0 0.8em; padding-left: 1.2em; }
li { margin: 0.15em 0; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 0.86em; background: #f5f5f4; padding: 0 0.2em; }
table { border-collapse: collapse; width: 100%; margin: 0.4em 0 1em; page-break-inside: avoid; }
th, td { border: 1px solid #d6d3d1; padding: 4px 6px; vertical-align: top; text-align: left; }
th { background: #f5f5f4; }
.diagram { margin: 0.2em 0 0.8em; break-inside: avoid; text-align: center; }
.diagram svg { max-width: 100%; max-height: 225mm; height: auto; }
"""


def render(md_path: Path) -> None:
    print(f"Rendering {md_path.name}")
    body = markdown_to_html(md_path.read_text(encoding="utf-8"), ROOT / "diagrams", md_path.stem)
    html_path = ROOT / f"{md_path.stem}.html"
    pdf_path = ROOT / f"{md_path.stem}.pdf"
    html_path.write_text(
        "<!DOCTYPE html><html lang='nl'><head><meta charset='utf-8'>"
        f"<title>{html.escape(md_path.stem)}</title><style>{CSS}</style></head>"
        f"<body>{body}</body></html>",
        encoding="utf-8",
    )
    subprocess.run(
        [
            "chromium",
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            "--no-pdf-header-footer",
            f"--print-to-pdf={pdf_path}",
            html_path.as_uri(),
        ],
        check=True,
    )
    print(f"  wrote {pdf_path}")


def main() -> int:
    names = sys.argv[1:] or (
        "functioneel-ontwerp.md",
        "technisch-ontwerp.md",
        "business-case.md",
    )
    for name in names:
        render(ROOT / name)
    return 0


if __name__ == "__main__":
    sys.exit(main())
