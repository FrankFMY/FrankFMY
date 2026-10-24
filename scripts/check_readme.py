"""Check the profile's Markdown structure, local links and contact targets."""
from pathlib import Path
import re
from urllib.parse import urlsplit, unquote

root = Path(__file__).resolve().parents[1]
text = (root / "README.md").read_text(encoding="utf-8")
assert len(re.findall(r"^# ", text, re.M)) == 1, "Use one main heading"
assert len(re.findall(r"^```", text, re.M)) % 2 == 0, "Unclosed code fence"
assert text.count("<details>") == text.count("</details>"), "Unclosed details block"
assert "Permission is hereby granted" in (root / "LICENSE").read_text(), "MIT license is missing"
required = {
    "https://t.me/FrankFMY",
    "https://frankfmy.com",
    "https://www.linkedin.com/in/frankfmy/",
    "https://x.com/FrankFMY",
    "https://github.com/FrankFMY",
    "https://www.npmjs.com/~frankfmy",
    "mailto:frankfmy@proton.me",
    "mailto:Pryanishnikovartem@gmail.com",
}
links = re.findall(r"\[[^\]]+\]\(([^\s)]+)\)", text)
assert required <= set(links), "A professional contact target is missing"
for link in links:
    parts = urlsplit(link)
    assert parts.scheme in {"", "https", "mailto"}, f"Unexpected link scheme: {link}"
    if not parts.scheme and parts.path:
        target = (root / unquote(parts.path)).resolve()
        assert target.is_relative_to(root) and target.is_file(), f"Broken local link: {link}"
assert "<your-" not in text and "TODO" not in text, "Unfinished profile text"
print(f"Profile checks passed: {len(links)} links; all professional contacts; balanced structure; MIT license")
