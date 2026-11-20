import csv,json
from pathlib import Path
base=Path(__file__).parent
with (base/'vocabulary.csv').open(encoding='utf-8-sig',newline='') as f: rows=list(csv.DictReader(f))
assert len({r['id'] for r in rows})==len(rows), 'Duplicate IDs'
for r in rows:
 r['level']=int(r['level']);assert 1<=r['level']<=12 and all(r[k] for k in ('id','term','translation','category'))
(base/'data.js').write_text('window.GEMARA_DATA = '+json.dumps(rows,ensure_ascii=False,indent=2)+';',encoding='utf-8')
