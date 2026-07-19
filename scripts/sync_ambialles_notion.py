#!/usr/bin/env python3
"""
Script de coleta diária das páginas públicas do Notion da Ambialles.
Atualiza /opt/data/AgenteBruno-local/projects/Ambialles.md
"""
import json, os, sys, subprocess
from datetime import datetime, timezone
from pathlib import Path
import urllib.request

# Config
NOTION_PAGES = {
    "estrategia": {
        "id": "d1439030-a925-45be-801b-461224858f73",
        "url": "https://trapezoidal-aragon-9fc.notion.site/Estrat-gia-Produto-Ambialles-d1439030a92545be801b461224858f73",
        "name": "Estratégia & Produto",
        "type": "page"
    }
}

NOTION_DATABASES = {
    "desenvolvimento": {
        "id": "38e22450-071d-8025-b854-000b3b958559",
        "url": "https://trapezoidal-aragon-9fc.notion.site/38e22450071d80c7bd2fd24488c1853a?v=38e22450071d8019a84b000c59782153",
        "name": "Desenvolvimento (Projetos)",
        "type": "data_source",
        "token_key": "NOTION_API_KEY_AMB"
    }
}

# Tokens
TOKENS = {
    "NOTION_API_KEY": os.environ.get("NOTION_API_KEY", ""),
    "NOTION_API_KEY_AMB": "ntn_b91991590698IUaePbhdDAiueRJDMADKDHFgyvFnmzsg4x"
}

BRUNOOS_DIR = Path("/opt/data/AgenteBruno-local")
PROJECT_FILE = BRUNOOS_DIR / "projects" / "Ambialles.md"
DATA_DIR = BRUNOOS_DIR / "projects" / "ambialles_data"
SCRIPTS_DIR = BRUNOOS_DIR / "scripts"

def notion_api(method, endpoint, data=None, token_key="NOTION_API_KEY"):
    """Call Notion API with specified token."""
    token = TOKENS.get(token_key, "")
    url = f"https://api.notion.com/v1/{endpoint}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Notion-Version": "2025-09-03",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
    }
    
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        return {"_error": f"HTTP {e.code}: {e.read().decode()[:200]}"}

def extract_text(props):
    if not props: return ''
    parts = []
    for key, val in props.items():
        if isinstance(val, list):
            for item in val:
                if isinstance(item, list):
                    for sub in item:
                        if isinstance(sub, str):
                            parts.append(sub)
                        elif isinstance(sub, dict):
                            t = sub.get('text', {}) if isinstance(sub.get('text'), dict) else {}
                            parts.append(t.get('content', ''))
    return ''.join(parts)

def fetch_page_markdown(page_id):
    """Fetch page content via Notion public API v3."""
    url = "https://www.notion.so/api/v3/loadPageChunk"
    data = json.dumps({
        "pageId": page_id, "limit": 200,
        "cursor": {"stack": []}, "chunkNumber": 0, "verticalColumns": False
    }).encode()
    req = urllib.request.Request(url, data=data,
        headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())

def blocks_to_markdown(page_id, blocks_raw):
    """Convert Notion blocks to Markdown."""
    blocks = {}
    for bid, block in blocks_raw.items():
        raw = block.get('value') or block
        while isinstance(raw, dict) and 'value' in raw and isinstance(raw['value'], dict) and 'id' in raw['value']:
            raw = raw['value']
        if isinstance(raw, dict) and 'id' in raw:
            blocks[bid] = raw

    page_val = None
    for bid, val in blocks.items():
        if val.get('type') in ('page', 'collection_view_page') and val.get('id') == page_id:
            page_val = val
            break
    if not page_val:
        for bid, val in blocks.items():
            if val.get('type') in ('page', 'collection_view_page'):
                page_val = val
                break
    if not page_val:
        return "\n*>(Esta página não possui conteúdo textual extraível via API pública)*\n"

    lines = []
    def walk(val, indent=0):
        p = '  ' * indent
        btype = val.get('type', '?')
        props = val.get('properties', {})
        text = extract_text(props)
        
        if btype == 'page':
            lines.append(f'{p}# {text or "(sem título)"}\n')
        elif btype == 'header' and text: lines.append(f'{p}## {text}\n')
        elif btype == 'sub_header' and text: lines.append(f'{p}### {text}\n')
        elif btype == 'sub_sub_header' and text: lines.append(f'{p}#### {text}\n')
        elif btype == 'text' and text.strip(): lines.append(f'{p}{text}\n')
        elif btype == 'bulleted_list' and text.strip(): lines.append(f'{p}* {text}\n')
        elif btype == 'numbered_list' and text.strip(): lines.append(f'{p}1. {text}\n')
        elif btype == 'to_do':
            ck = (val.get('format') or {}).get('checked', False)
            lines.append(f'{p}- [{"x" if ck else " "}] {text}\n')
        elif btype == 'divider': lines.append(f'{p}---\n')
        elif btype in ('callout', 'quote') and text.strip():
            for line in text.split('\n'):
                lines.append(f'{p}> {line}\n')
            lines.append('\n')
        elif btype not in ('collection_view',) and text.strip():
            lines.append(f'{p}[{btype}] {text[:200]}\n')
        
        for cid in (val.get('content') or []):
            cid_s = cid if isinstance(cid, str) else str(cid)
            if cid_s in blocks:
                walk(blocks[cid_s], indent)
    
    walk(page_val, 0)
    return ''.join(lines)

def fetch_database(data_source_id, token_key="NOTION_API_KEY"):
    """Fetch all records from a Notion database/data_source."""
    # Get schema
    schema = notion_api("GET", f"data_sources/{data_source_id}", token_key=token_key)
    if '_error' in schema:
        return {"_error": schema['_error']}
    
    # Get records
    data = json.dumps({"page_size": 100}).encode()
    records = notion_api("POST", f"data_sources/{data_source_id}/query", data=data, token_key=token_key)
    
    return {"schema": schema, "records": records}

def database_to_markdown(db_data):
    """Convert database records to Markdown table."""
    if '_error' in db_data:
        return f"\n> Erro ao acessar database: {db_data['_error']}\n"
    
    records = db_data.get('records', {})
    results = records.get('results', []) if isinstance(records, dict) else []
    
    if not results:
        return "\n*(Database vazia ou sem registros acessíveis)*\n"
    
    lines = [f"\n**Total: {len(results)} registros**\n"]
    
    for r in results:
        props = r.get('properties', {})
        
        # Extract all properties
        fields = {}
        for k, v in props.items():
            ptype = v.get('type')
            val = ''
            if ptype == 'title':
                val = ''.join([p.get('text',{}).get('content','') for p in v.get('title',[])])
            elif ptype == 'status': val = (v.get('status') or {}).get('name','')
            elif ptype == 'select': val = (v.get('select') or {}).get('name','')
            elif ptype == 'multi_select': val = ', '.join([s.get('name','') for s in v.get('multi_select',[])])
            elif ptype == 'rich_text': val = ''.join([t.get('text',{}).get('content','') for t in v.get('rich_text',[])])
            elif ptype == 'date': val = (v.get('date') or {}).get('start','')[:10] if v.get('date') else ''
            elif ptype == 'checkbox': val = '✅' if v.get('checkbox') else ''
            elif ptype == 'url': val = v.get('url','')
            elif ptype == 'number': val = str(v.get('number',''))
            elif ptype == 'email': val = v.get('email','')
            elif ptype == 'phone_number': val = v.get('phone_number','')
            if val:
                fields[k] = val
        
        title = fields.pop('Feature', fields.pop('Name', 'Sem título'))
        
        # Determine status emoji
        status = fields.get('Status', '')
        status_emoji = {'Completed': '✅', 'In progress': '🔄', 'Backlog': '📋', 'Cancelled': '❌'}.get(status, '📋')
        
        # Build the item line
        parts = [f"**{title}**"]
        if status: parts.append(f"[{status_emoji} {status}]")
        if 'Priority' in fields: parts.append(f"(🎯 {fields['Priority']})")
        if 'Responsável' in fields: parts.append(f"👤 {fields['Responsável']}")
        if 'Date' in fields and fields['Date']: parts.append(f"📅 {fields['Date']}")
        
        lines.append(f"\n* {' · '.join(parts)}")
        
        # Secondary fields on sub-line
        extras = []
        for k in ('Category', 'Ajuda a Vender/Implantar/Reter'):
            if k in fields:
                extras.append(f"{k}: {fields[k]}")
        if extras:
            lines.append(f"  └ {', '.join(extras)}")
    
    return '\n'.join(lines)

def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    
    page_results = {}
    db_results = {}
    errors = []
    
    # Fetch pages
    for key, cfg in NOTION_PAGES.items():
        print(f"Fetching page: {cfg['name']}...")
        try:
            raw = fetch_page_markdown(cfg['id'])
            blocks_raw = raw.get('recordMap', {}).get('block', {})
            md = blocks_to_markdown(cfg['id'], blocks_raw)
            page_results[key] = md
            
            # Save raw data
            (DATA_DIR / f"{key}_raw.json").write_text(json.dumps(raw, ensure_ascii=False, indent=2))
            print(f"  ✅ Markdown: {len(md)} chars")
        except Exception as e:
            print(f"  ❌ Error: {e}")
            page_results[key] = f"\n> *Erro ao coletar: {e}*\n"
            errors.append(f"{cfg['name']}: {e}")
    
    # Fetch databases
    for key, cfg in NOTION_DATABASES.items():
        print(f"Fetching database: {cfg['name']}...")
        try:
            db_data = fetch_database(cfg['id'], cfg.get('token_key', 'NOTION_API_KEY'))
            md = database_to_markdown(db_data)
            db_results[key] = md
            
            # Save raw data
            if isinstance(db_data, dict) and '_error' not in db_data:
                (DATA_DIR / f"{key}_raw.json").write_text(json.dumps(db_data, ensure_ascii=False, indent=2))
            print(f"  ✅ Done ({len(md)} chars)")
        except Exception as e:
            print(f"  ❌ Error: {e}")
            db_results[key] = f"\n> *Erro ao coletar: {e}*\n"
            errors.append(f"{cfg['name']}: {e}")
    
    # Build Ambialles.md
    estrategia = page_results.get('estrategia', '')
    desenvolvimento = db_results.get('desenvolvimento', '')
    
    content = f"""# Ambialles

**Status:** 🟢 Ativo
**Área:** Negócio / SaaS — gestão de licenciamento ambiental
**Última sincronização:** {timestamp}
**Fontes:** Notion público (Estratégia & Produto, Desenvolvimento)

---

## ℹ️ Sobre

Empresa de gestão de licenciamentos ambientais. Produto principal: plataforma SaaS de licenciamento ambiental (MVP em andamento). Time: Bruno, Douglas e Wilson.

**Repositório GitHub:** [fullcontent/ambialles](https://github.com/fullcontent/ambialles)
**Workspace local:** `/opt/data/workspaces/ambialles`

---

## 📋 Infra & Tech Stack

- **Stack:** Laravel + Blade + Alpine.js + Tailwind + Vite + Pest
- **Branch principal:** `main`
- **Documentação:** `README.md`, `CLAUDE.md`, `docs/`

---

## 📄 Estratégia & Produto

{estrategia}

---

## 📋 Desenvolvimento — Database de Tarefas

{desenvolvimento}

---

## ⚙️ Automação

Este arquivo é atualizado automaticamente 1x/dia via script de coleta do Notion.
Última coleta: {timestamp}

*Fontes: [Notion Público Ambialles](https://trapezoidal-aragon-9fc.notion.site)*
"""
    
    PROJECT_FILE.write_text(content)
    print(f"\n✅ {PROJECT_FILE} atualizado ({len(content)} chars)")
    
    if errors:
        print(f"\n⚠️ Erros: {', '.join(errors)}")

if __name__ == '__main__':
    main()
