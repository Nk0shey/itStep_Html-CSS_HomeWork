"""Check local HTML/CSS references and basic page metadata; standard library only."""
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import urlsplit, unquote
import sys
ROOT = Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.refs=[]; self.title=False; self.viewport=False; self.lang=False
    def handle_starttag(self, tag, attrs):
        values=dict(attrs)
        if tag=="title": self.title=True
        if tag=="html" and values.get("lang"): self.lang=True
        if tag=="meta" and values.get("name", "").lower()=="viewport": self.viewport=True
        for key,value in attrs:
            if value and ((tag in ("img","script","iframe","source") and key=="src") or (tag in ("link","a") and key=="href")):
                self.refs.append(value)
def check():
    issues=[]; count=0; pages=0
    for path in sorted(ROOT.rglob("*")):
        if path.suffix.lower() not in (".html",".css"): continue
        source=path.read_text(encoding="utf-8")
        if path.suffix.lower()==".html":
            page=Page();page.feed(source);refs=page.refs;pages+=1
            for name,ok in (("title",page.title),("viewport",page.viewport),("lang",page.lang)):
                if not ok: issues.append(f"{path.relative_to(ROOT)}: missing {name}")
        else: refs=[value.strip(" \"'") for value in re.findall(r"url\(([^)]+)\)",source)]
        for ref in refs:
            parsed=urlsplit(ref)
            if parsed.scheme or parsed.netloc or not parsed.path: continue
            target=(path.parent / unquote(parsed.path)).resolve(); count+=1
            if not target.is_file(): issues.append(f"{path.relative_to(ROOT)}: missing {ref}")
    return pages,count,issues
if __name__=="__main__":
    pages,count,issues=check()
    for issue in issues: print(issue, file=sys.stderr)
    print(f"{pages} pages; {count} local references; {len(issues)} issues")
    raise SystemExit(bool(issues))
