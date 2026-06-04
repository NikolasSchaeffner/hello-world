#!/usr/bin/env python3
"""
Direct docx generator — no external dependencies needed.
This script reads hausarbeit_final.md and produces
Hausarbeit_Softwaremodellierung_final.docx using only Python stdlib.

Usage: python3 /home/user/hello-world/generate_docx_direct.py
"""
import re, zipfile, io, os, sys

MD   = '/home/user/hello-world/hausarbeit_final.md'
DOCX = '/home/user/hello-world/Hausarbeit_Softwaremodellierung_final.docx'

# ─── XML helpers ──────────────────────────────────────────────────────────

def x(s):
    """XML-escape."""
    return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('"','&quot;')

def run(text, bold=False, italic=False, sz=22):
    rpr = f'<w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:sz w:val="{sz}"/><w:szCs w:val="{sz}"/>'
    if bold:   rpr += '<w:b/><w:bCs/>'
    if italic: rpr += '<w:i/><w:iCs/>'
    return f'<w:r><w:rPr>{rpr}</w:rPr><w:t xml:space="preserve">{x(text)}</w:t></w:r>'

INLINE = re.compile(r'\*\*(.+?)\*\*|\*(.+?)\*|([^*]+)', re.DOTALL)

def inline_runs(text, sz=22):
    out = ''
    for m in INLINE.finditer(text):
        if m.group(1): out += run(m.group(1), bold=True,   sz=sz)
        elif m.group(2): out += run(m.group(2), italic=True, sz=sz)
        elif m.group(3): out += run(m.group(3), sz=sz)
    return out

def para(text, style='Normal', sz=22, space_after=120, line=280):
    ppr = (f'<w:pStyle w:val="{style}"/>'
           f'<w:spacing w:after="{space_after}" w:line="{line}" w:lineRule="auto"/>')
    return f'<w:p><w:pPr>{ppr}</w:pPr>{inline_runs(text, sz)}</w:p>'

def heading(text, lvl):
    sizes = {1:32, 2:28, 3:24, 4:22}
    sz = sizes.get(lvl, 22)
    before = {1:280, 2:240, 3:200, 4:160}[lvl]
    ppr = (f'<w:pStyle w:val="Heading{lvl}"/>'
           f'<w:spacing w:before="{before}" w:after="80"/>')
    runs = ''
    for m in INLINE.finditer(text):
        t = m.group(1) or m.group(2) or m.group(3) or ''
        runs += run(t, bold=True, sz=sz)
    return f'<w:p><w:pPr>{ppr}</w:pPr>{runs}</w:p>'

BORDER_SIDES = ('top','left','bottom','right','insideH','insideV')
TBL_BORDERS = ''.join(
    f'<w:{s} w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
    for s in BORDER_SIDES)

def table(rows):
    ncols = max(len(r) for r in rows)
    out = (f'<w:tbl>'
           f'<w:tblPr>'
           f'<w:tblW w:w="0" w:type="auto"/>'
           f'<w:tblBorders>{TBL_BORDERS}</w:tblBorders>'
           f'</w:tblPr>')
    for ri, row in enumerate(rows):
        out += '<w:tr>'
        for ci in range(ncols):
            txt  = row[ci] if ci < len(row) else ''
            fill = 'D9D9D9' if ri == 0 else 'FFFFFF'
            tcpr = f'<w:tcPr><w:shd w:val="clear" w:color="auto" w:fill="{fill}"/></w:tcPr>'
            bold = ri == 0
            cell_runs = ''
            for m in INLINE.finditer(txt):
                t = m.group(1) or m.group(2) or m.group(3) or ''
                cell_runs += run(t, bold=bold or bool(m.group(1)),
                                  italic=bool(m.group(2)), sz=20)
            out += (f'<w:tc>{tcpr}'
                    f'<w:p><w:pPr><w:spacing w:after="60"/></w:pPr>{cell_runs}</w:p>'
                    f'</w:tc>')
        out += '</w:tr>'
    out += '</w:tbl><w:p><w:pPr><w:spacing w:after="60"/></w:pPr></w:p>'
    return out

# ─── table parser ─────────────────────────────────────────────────────────

def parse_table(lines, start):
    rows, i = [], start
    while i < len(lines):
        s = lines[i].strip()
        if not s or not s.startswith('|'): break
        if re.match(r'^\|[-|: ]+\|$', s): i += 1; continue
        rows.append([c.strip() for c in s.strip('|').split('|')])
        i += 1
    return rows, i

# ─── body builder ─────────────────────────────────────────────────────────

def build_body(lines):
    body = ''
    i = 0
    while i < len(lines):
        s = lines[i].strip()
        if not s: i += 1; continue

        if re.match(r'^-{3,}$', s):
            body += ('<w:p><w:pPr>'
                     '<w:pBdr><w:bottom w:val="single" w:sz="6" w:space="1" w:color="AAAAAA"/></w:pBdr>'
                     '<w:spacing w:before="120" w:after="120"/>'
                     '</w:pPr></w:p>')
            i += 1; continue

        m = re.match(r'^(#{1,4})\s+(.*)', s)
        if m:
            body += heading(m.group(2).strip(), len(m.group(1)))
            i += 1; continue

        if s.startswith('|'):
            rows, i = parse_table(lines, i)
            if rows: body += table(rows)
            continue

        body += para(s)
        i += 1
    return body

# ─── package components ────────────────────────────────────────────────────

CONTENT_TYPES = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
<Override PartName="/word/settings.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml"/>
</Types>'''

ROOT_RELS = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>'''

WORD_RELS = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/settings" Target="settings.xml"/>
</Relationships>'''

SETTINGS = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:settings xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:defaultTabStop w:val="720"/>
</w:settings>'''

STYLES = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:docDefaults><w:rPrDefault><w:rPr>
  <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:cs="Calibri"/>
  <w:sz w:val="22"/><w:szCs w:val="22"/>
  <w:lang w:val="de-DE"/>
</w:rPr></w:rPrDefault></w:docDefaults>
<w:style w:type="paragraph" w:styleId="Normal" w:default="1">
  <w:name w:val="Normal"/>
  <w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:sz w:val="22"/></w:rPr>
</w:style>
<w:style w:type="paragraph" w:styleId="Heading1">
  <w:name w:val="heading 1"/><w:basedOn w:val="Normal"/>
  <w:pPr><w:outlineLvl w:val="0"/><w:spacing w:before="280" w:after="80"/></w:pPr>
  <w:rPr><w:b/><w:sz w:val="32"/><w:szCs w:val="32"/></w:rPr>
</w:style>
<w:style w:type="paragraph" w:styleId="Heading2">
  <w:name w:val="heading 2"/><w:basedOn w:val="Normal"/>
  <w:pPr><w:outlineLvl w:val="1"/><w:spacing w:before="240" w:after="80"/></w:pPr>
  <w:rPr><w:b/><w:sz w:val="28"/><w:szCs w:val="28"/></w:rPr>
</w:style>
<w:style w:type="paragraph" w:styleId="Heading3">
  <w:name w:val="heading 3"/><w:basedOn w:val="Normal"/>
  <w:pPr><w:outlineLvl w:val="2"/><w:spacing w:before="200" w:after="60"/></w:pPr>
  <w:rPr><w:b/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr>
</w:style>
<w:style w:type="paragraph" w:styleId="Heading4">
  <w:name w:val="heading 4"/><w:basedOn w:val="Normal"/>
  <w:pPr><w:outlineLvl w:val="3"/><w:spacing w:before="160" w:after="40"/></w:pPr>
  <w:rPr><w:b/><w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr>
</w:style>
</w:styles>'''

# ─── main ─────────────────────────────────────────────────────────────────

def main():
    print(f'Reading {MD} ...')
    with open(MD, encoding='utf-8') as f:
        lines = f.read().split('\n')

    print('Building document XML ...')
    body_xml = build_body(lines)

    doc_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'
        ' xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">\n'
        '<w:body>\n'
        + body_xml
        + '\n<w:sectPr>'
        '<w:pgSz w:w="11906" w:h="16838"/>'
        '<w:pgMar w:top="1134" w:right="1417" w:bottom="1134" w:left="1417"'
        ' w:header="709" w:footer="709" w:gutter="0"/>'
        '</w:sectPr>\n'
        '</w:body>\n'
        '</w:document>'
    )

    print(f'Packaging as .docx ...')
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.writestr('[Content_Types].xml',         CONTENT_TYPES.strip())
        zf.writestr('_rels/.rels',                  ROOT_RELS.strip())
        zf.writestr('word/_rels/document.xml.rels', WORD_RELS.strip())
        zf.writestr('word/document.xml',            doc_xml)
        zf.writestr('word/styles.xml',              STYLES.strip())
        zf.writestr('word/settings.xml',            SETTINGS.strip())

    with open(DOCX, 'wb') as f:
        f.write(buf.getvalue())

    size = os.path.getsize(DOCX)
    print(f'[OK] Written {DOCX}  ({size:,} bytes)')
    return True

if __name__ == '__main__':
    ok = main()
    if ok:
        print()
        print('FERTIG')
        print()
        print('Erstellte Dateien:')
        print(f'  {MD}')
        print(f'  {DOCX}')
        print(f'  /home/user/hello-world/convert_to_docx.py')
