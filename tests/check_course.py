"""Structural integrity and independent exact arithmetic checks; stdlib only."""
from pathlib import Path
from fractions import Fraction as F
import json
import re

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / 'course.json').read_text())
activities = json.loads((ROOT / 'exercises/activities.json').read_text())
fixtures = json.loads((ROOT / 'tests/fixtures.json').read_text())
checks = 0

def check(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1

mods = manifest['modules']
check(len(mods) == 16, 'expected 16 modules')
check([m['id'] for m in mods] == [f'{i:02}' for i in range(1,17)], 'ordered unique modules')
check(len(activities) == 32, 'expected 32 activities')
check(len({a['id'] for a in activities}) == len(activities), 'unique activity IDs')
ids = {a['id']: a for a in activities}
objectives = {m['objective'] for m in mods}
check(set(manifest['critical_objectives']) <= objectives, 'critical objectives exist')
for i, m in enumerate(mods):
    check((ROOT / m['path']).is_file(), f'missing {m["path"]}')
    text = (ROOT / m['path']).read_text()
    for section in ['Observable goal','Opening scene','Exploration','Branch consequences',
                    'Mandatory explanation','Worked application','Misconception and feedback',
                    'Memory callback','Visual and text equivalent','If the learner says continue',
                    'Application and transition']:
        check('## ' + section in text, f'{m["id"]}: missing {section}')
    check('status: draft' in text, f'{m["id"]}: missing draft')
    check(m['next'] == (mods[i+1]['id'] if i+1 < len(mods) else None), 'next pointer')
    check(len(m['activities']) == 2, 'two activities per module')
    for aid in m['activities']:
        check(aid in ids, 'activity exists')
        a = ids[aid]
        check(a['module'] == m['id'] and a['objective'] == m['objective'], 'activity aligned')
        for key in ['prompt','rubric','misconception','feedback','reveal_fallback','callback']:
            check(bool(a.get(key)), f'{aid}: missing {key}')
        check(a['status'] == 'draft', 'activity status')
        check(len(a['rubric']) >= 2, 'substantive rubric')

for file in ROOT.rglob('*.md'):
    text = file.read_text()
    # Actual Markdown file links, independent of inline examples.
    for dest in re.findall(r'\]\(([^)]+)\)', text):
        if dest.startswith('#'):
            continue
        check('://' not in dest, f'external reference in {file.relative_to(ROOT)}')
        target = (file.parent / dest.split('#')[0]).resolve()
        check(target.is_relative_to(ROOT), 'link escapes repository')
        check(target.exists(), f'broken link {file.name}: {dest}')
    check('source_ids' not in text and 'source_id:' not in text, 'no citation fields')

final = (ROOT / 'exercises/FINAL.md').read_text()
for obj in manifest['critical_objectives']:
    check(obj in final, f'final coverage missing {obj}')
for file in ['AGENTS.md','START.md','pedagogy/FRAMEWORK.md','knowledge/SAFETY.md',
             'knowledge/GAS.md','knowledge/NAVIGATION.md','knowledge/COMPUTER.md',
             'knowledge/PREPARATION.md','glossary/TERMS.md','visuals/ROUTE.md','visuals/MODELS.md']:
    check((ROOT/file).is_file(), f'required runtime file {file}')
for term in ['primary reel','mainline','cookie','REM','TTS','RMV']:
    check(term in (ROOT/'glossary/TERMS.md').read_text(), f'glossary missing {term}')

# Exact rational arithmetic, independent of rounded decimal prose.
# Rounding is tested through conservation inequalities as well as explicit outputs.
for c in fixtures['matching']:
    budget = min(F(v)*p for v,p in zip(c['v'],c['p'])) / c['f']
    turns=[]
    for v,p in zip(c['v'],c['p']):
        step=5
        drop = (budget / v // step) * step
        turns.append(p-drop)
        check(v*drop <= budget < v*(drop+step), f'{c["label"]}: nonconservative rounding')
        check(0 <= drop <= p, 'invalid permitted use')
    check(turns == c['turn'], f'{c["label"]}: turn pressures {turns}')
for c in fixtures['fraction']:
    raw=F(c['p'],c['f'])
    drop=raw//5*5
    check(drop==c['drop'] and c['p']-drop==c['turn'], 'fraction threshold')
    check(drop<=raw<drop+5, 'fraction rounding bounds')
for c in fixtures['demand']:
    pressure=1+F(c['depth'],10)
    q=sum(c['rmv'])*pressure*(c['response']+c['travel'])
    check(q==c['demand'], f'{c["label"]}: emergency demand')
    check([v*p-q for v,p in zip(c['v'],c['p'])]==c['balance'], f'{c["label"]}: donor comparison')
for c in fixtures['rmv']:
    rmv=F(c['v']*c['drop'],c['time'])/(1+F(c['depth'],10))
    check(rmv==c['expected'], 'RMV normalization')
for c in fixtures['consumption']:
    q=c['rmv']*(1+F(c['depth'],10))*c['time']
    check(q==c['q'] and q/c['v']==c['drop'], 'consumption and pressure inversion')
for c in fixtures['mod']:
    oxygen=F(c['oxygen_percent'],100)
    depth=10*(F(c['limit'])/oxygen-1)
    check(depth//1==c['whole_depth'], 'MOD rounded no deeper')
    check(oxygen*(1+F(c['whole_depth'],10))<=F(c['limit']), 'MOD ppO2 bound')
# Diagnostic unequal-own-thirds example, tested independently of matching.
q_a,q_b=24*210,22*210
u_a,u_b=F(q_a,3),F(q_b,3)
check(u_a+u_b-(q_b-u_b)==140, 'own-thirds smaller donor shortfall')
# Critical prose anchors keep examples and their independent fixtures associated.
for path, phrases in {
    'modules/09.md':['Turn Mira=165 bar, Leon=135 bar'],
    'modules/10.md':['turn 170 bar','turn 140 bar'],
    'modules/12.md':['2100 L','3900 L','300 L'],
    'exercises/FINAL.md':['turn 140 bar','turn 175 bar','surplus 480','deficit 100','short 700']
}.items():
    body=(ROOT/path).read_text()
    for phrase in phrases:
        check(phrase in body, f'prose/fixture association: {path}: {phrase}')
# Boundary behaviour: 0 inventory never creates an inbound budget; exact steps remain exact.
check((F(0,3)//5)*5==0, 'zero budget arithmetic boundary')
check((F(70)//5)*5==70, 'exact increment preserved')
check(F(24*225-24*150,24)==75, 'inventory difference inversion')
check(11*200+11*180==4180, 'unequal independent-cylinder inventory')
print(f'PASS: {checks} checks; 16 modules; 32 activities; 31 arithmetic cases plus boundary/diagnostic checks.')
print('Not covered: expert factual approval, practical competency, rendered visuals, fresh ChatGPT/Claude delivery or retention.')
