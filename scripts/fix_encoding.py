"""Restore UTF-8 HTML from last good git commit and re-apply favicon."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REV = "30b76e6"
HTML_FILES = [
    "index.html",
    "sobre.html",
    "servicos.html",
    "portfolio.html",
    "produtos.html",
    "blog.html",
    "contacto.html",
    "faq.html",
    "privacidade.html",
]


def restore_html() -> None:
    for name in HTML_FILES:
        data = subprocess.check_output(["git", "show", f"{REV}:{name}"], cwd=ROOT)
        path = ROOT / name
        path.write_bytes(data)
        text = data.decode("utf-8")
        ok = any(ch in text for ch in "çãáéíóúõ")
        bad = "Ã§" in text or "Ã¡" in text
        print(f"restored {name}: good_accents={ok} mojibake={bad}")


def apply_favicon() -> None:
    for name in HTML_FILES:
        path = ROOT / name
        text = path.read_text(encoding="utf-8")
        new_text, n = re.subn(
            r'(<link rel="icon" href=")[^"]+(")',
            r'\1assets/images/logo.png\2',
            text,
            count=1,
        )
        if n:
            path.write_text(new_text, encoding="utf-8", newline="\n")
            print(f"favicon updated: {name}")
        else:
            print(f"favicon NOT updated: {name}")


def verify() -> None:
    print("\n=== VERIFY ===")
    for name in HTML_FILES:
        text = (ROOT / name).read_text(encoding="utf-8")
        print(
            f"{name}: accents_ok={any(ch in text for ch in 'çãáéíóúõ')} "
            f"mojibake={'Ã§' in text} charset={'charset=\"UTF-8\"' in text}"
        )
    title = next(
        line for line in (ROOT / "index.html").read_text(encoding="utf-8").splitlines() if "<title>" in line
    )
    print("title:", title)


if __name__ == "__main__":
    restore_html()
    apply_favicon()
    verify()
