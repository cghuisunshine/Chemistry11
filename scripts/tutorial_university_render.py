"""HTML rendering for the university tutor layer; no runtime dependencies."""
from tutorial_university import NOTES, FOUNDATIONS

DIAGRAMS = {
'atoms-3': '''<figure class="university-figure"><svg viewBox="0 0 540 240" role="img" aria-labelledby="hydrogen-level-title"><title id="hydrogen-level-title">Hydrogen energy levels with emission from n equals 3 to n equals 2</title><defs><marker id="photon-arrow" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0L7 3.5L0 7" fill="#d46a43"/></marker></defs><path d="M55 210V15M55 24H370" fill="none" stroke="#a6b59d"/><g stroke="#235b47" stroke-width="3"><path d="M80 188H330M80 66H330M80 43H330"/></g><path d="M240 43V66" stroke="#d46a43" stroke-width="2" marker-end="url(#photon-arrow)"/><g font-family="system-ui,sans-serif" font-size="13" fill="#213e36"><text x="355" y="28">ionization limit · 0 eV</text><text x="355" y="48">n = 3 · −1.51 eV</text><text x="355" y="73">n = 2 · −3.40 eV</text><text x="355" y="193">n = 1 · −13.6 eV</text><text x="85" y="111" fill="#ad512f">3 → 2: a 1.89 eV photon</text><text x="85" y="132" fill="#ad512f">λ ≈ 656 nm</text><text x="12" y="17">E ↑</text></g></svg><figcaption>Energy differences determine photon energy. The bound-state zero and endpoint labels matter; the photon carries a positive energy while the atom’s energy decreases.</figcaption></figure>''',
'bonding-3': '''<figure class="university-figure"><svg viewBox="0 0 540 245" role="img" aria-labelledby="bond-well-title"><title id="bond-well-title">Schematic potential-energy well: steep repulsion at short separation and a stable minimum at equilibrium</title><path d="M55 15V208H510" fill="none" stroke="#879b80"/><path d="M60 65H500" stroke="#a6b59d" stroke-dasharray="5 5"/><path d="M88 20C105 80 123 180 166 180S255 105 330 84S450 68 500 65" fill="none" stroke="#235b47" stroke-width="3"/><path d="M166 180V208" stroke="#d46a43" stroke-dasharray="4 4"/><circle cx="166" cy="180" r="5" fill="#d46a43"/><g font-family="system-ui,sans-serif" font-size="12" fill="#213e36"><text x="15" y="17">U</text><text x="443" y="230">separation r →</text><text x="157" y="229">rₑ</text><text x="199" y="182">minimum: U′ = 0, U″ &gt; 0</text><text x="70" y="47">repulsion</text><text x="320" y="120">attractive region</text><text x="318" y="49">separated-atom reference</text></g></svg><figcaption>A schematic energy landscape, not a plot for a particular molecule. Slope gives force; curvature near the minimum sets a small-amplitude vibration scale; depth concerns dissociation.</figcaption></figure>''',
'bonding-4': '''<figure class="university-figure"><svg viewBox="0 0 540 150" role="img" aria-labelledby="oxygen-spin-title"><title id="oxygen-spin-title">Oxygen has one electron in each of two degenerate highest occupied antibonding pi orbitals</title><g fill="#eef3e8" stroke="#a9bca1"><rect x="120" y="50" width="100" height="55" rx="7"/><rect x="320" y="50" width="100" height="55" rx="7"/></g><g text-anchor="middle" font-family="system-ui,sans-serif" fill="#235b47"><text x="170" y="87" font-size="35">↑</text><text x="370" y="87" font-size="35">↑</text><text x="170" y="128" font-size="13">π* orbital</text><text x="370" y="128" font-size="13">π* orbital</text><text x="270" y="25" font-size="15">O₂ · highest occupied π* pair</text></g></svg><figcaption>Only the two relevant degenerate antibonding orbitals are shown. Their separate parallel-spin electrons explain O₂ paramagnetism; the full valence MO diagram also contains lower occupied orbitals.</figcaption></figure>'''
}


def reference(ref, e, pdf):
    path, label, page = ref
    if path.startswith('https://'):
        return f'<a href="{e(path)}" target="_blank" rel="noopener">{e(label)} ↗</a>'
    return pdf(path, label, page)


def foundation_links(keys, e, link):
    titles = {f['id']:f['title'] for f in FOUNDATIONS}
    return ' → '.join(link('foundation-'+key,titles[key]) for key in keys)


def render_guide(units, e, paragraphs, eq, pdf, link):
    count = sum(n['derivation'] for n in NOTES.values())
    result = f'''<section class="tutor-guide searchable" id="tutor-guide" aria-labelledby="guide-title"><div class="section-title"><h2 id="guide-title">The tutor’s explanation guide</h2><span>42 university connections · {count} worked derivations</span></div><p>Teach the Chemistry 11 idea first. Then use these university-level explanations to define the quantities, rebuild the reasoning, test a numerical or conceptual example, and identify where the model stops working. The local university textbooks provide the foundations; the derivations and classroom examples are written in original wording for this tutorial.</p><div class="tutor-actions"><button type="button" data-tutor-expand="true">Open all tutor explanations</button><button type="button" data-tutor-expand="false">Close tutor explanations</button><a href="#foundations">Start with shared foundations ↓</a></div><div class="foundations" id="foundations"><h3>Ten foundations connect the course</h3><p>Follow a definition as far back as needed. Each lesson links to the foundations it uses, then brings the definition back to the student-level problem. These extensions support explanation and further study; the assigned Chemistry 11 course still sets assessment expectations.</p>'''
    for f in FOUNDATIONS:
        refs = ' · '.join(reference(ref,e,pdf) for ref in f['refs'])
        result += f'<details class="foundation-note" id="foundation-{f["id"]}"><summary>{e(f["title"])}</summary><div class="foundation-body">{paragraphs(f["text"])}{eq(f["equation"])}{paragraphs(f["connection"])}<p class="source-links">Textbook basis: {refs}</p></div></details>'
    result += '</div><div class="derivation-map"><h3>Follow a worked derivation</h3><p>Each route names the symbols, builds the argument, checks a result, and states its assumptions.</p><ul>'
    for i,u in enumerate(units,1):
        for j,l in enumerate(u['lessons'],1):
            lid=f'{u["id"]}-{j}'
            if NOTES[lid]['derivation']:
                result += f'<li>{link("derive-"+lid,f"{i}.{j} · {NOTES[lid]["title"]}")}</li>'
    result += '</ul></div><h3 class="mini-title">Find the university explanation for a lesson</h3><div class="tutor-index">'
    for i,u in enumerate(units,1):
        result+=f'<div><h3>{i:02d} · {e(u["title"])}</h3><ul>'
        for j,l in enumerate(u['lessons'],1):
            lid=f'{u["id"]}-{j}'
            result+=f'<li>{link("tutor-"+lid,f"{i}.{j} {NOTES[lid]["title"]}")}</li>'
        result+='</ul></div>'
    return result+'</div></section>'


def render_tutor(lid, base, number, e, paragraphs, eq, pdf, link):
    n=NOTES[lid]
    terms=''.join(f'<tr><th scope="row">{e(symbol)}</th><td>{e(meaning)}</td><td>{e(units)}</td></tr>' for symbol,meaning,units in n['terms'])
    refs=' · '.join(reference(ref,e,pdf) for ref in n['refs'])
    steps=''.join(f'<li><strong>{e(title)}</strong> {e(text)}</li>' for title,text in n['steps'])
    diagram=DIAGRAMS.get(lid,'')
    if diagram:
        diagram=diagram.replace('<svg','<div class="university-diagram-scroll"><svg',1).replace('</svg>','</svg></div>',1)
    label='Worked derivation' if n['derivation'] else 'University reasoning'
    cls='derivation' if n['derivation'] else 'university-reasoning'
    return f'''<details class="tutor-note" id="tutor-{lid}"><summary><span class="tutor-badge">Tutor explanation {number}</span><span>{e(n['title'])}</span></summary><div class="tutor-body"><p class="tutor-say"><strong>Say to students</strong>{e(n['say'])}</p><h4>Bridge from Chemistry 11</h4>{paragraphs(base['why'])}<h4>Define the quantities before using the formula</h4><div class="table-scroll"><table class="study-table terms-table"><caption>Symbols and concepts for this explanation</caption><thead><tr><th scope="col">Symbol or term</th><th scope="col">Definition</th><th scope="col">Units or interpretation</th></tr></thead><tbody>{terms}</tbody></table></div><div class="textbook-basis"><h4>Back to the foundations</h4><p class="foundation-path">{foundation_links(n['foundations'],e,link)}</p><p>Use these definitions to explain the result below, then return to {link(lid,'the student-level lesson')} to connect the particle picture with the calculation.</p></div><section class="{cls}" id="derive-{lid}" aria-labelledby="derive-title-{lid}"><div class="eyebrow">{label} · {number}</div><h4 id="derive-title-{lid}">{e(n['title'])}</h4>{diagram}<ol class="reasoning-steps">{steps}</ol>{eq(n['equation'])}<div class="worked-check"><strong>Check the result</strong><p>{e(n['worked'])}</p></div></section><div class="university-note"><h4>University connection &amp; limits</h4><p>{e(n['limits'])}</p></div><div class="tutor-check"><strong>Ask, then explain</strong>{e(n['check'])}</div><p class="source-links"><strong>University textbook basis:</strong> {refs}. The reasoning and examples above are original adaptations and applications, rather than quoted textbook passages.</p><p class="source-links">Chemistry 11 connection: {pdf('chem11.pdf',f'BC Science Chemistry 11 · PDF page {base["page"]}',base['page'])}. {link('tutor-guide','Return to tutor guide ↑')}</p></div></details>'''


def render_reading_map(e, pdf):
    result='<h3>University foundations and further reading</h3><p>The tutor layer draws on Brown et al., <em>Chemistry: The Central Science</em>, 15th Global Edition in SI units; Oxtoby, Gillis and Butler, <em>Principles of Modern Chemistry</em>, 8th edition; and selected thermodynamic definitions from Atkins and de Paula, <em>Physical Chemistry</em>, 8th edition, already used in your Chemistry 12 tutorial. Local links open the supplied files at verified PDF viewer pages. Printed-page offsets differ between books, so use each link’s label.</p><div class="table-scroll"><table class="study-table"><caption>University reading map · definitions used by the tutor explanations</caption><thead><tr><th scope="col">Foundation</th><th scope="col">Read the source</th></tr></thead><tbody>'
    for f in FOUNDATIONS:
        result+=f'<tr><th scope="row">{e(f["title"])}</th><td>'+ ' · '.join(reference(ref,e,pdf) for ref in f['refs'])+'</td></tr>'
    return result+'</tbody></table></div><p class="lesson-intro">Every tutor explanation also gives its own section and page references. Additional algebraic deductions and original numerical examples are identified as applications of the cited definitions. The university layer is explanatory preparation, not an expanded Chemistry 11 memorization list.</p>'


def university_outline(units):
    out=['\n# University tutor explanations','\n## Shared foundations']
    for f in FOUNDATIONS:
        out += ['\n### '+f['title'],f['text'],'`'+f['equation']+'`',f['connection'],'Sources: '+'; '.join(r[1] for r in f['refs'])]
    for i,u in enumerate(units,1):
        out.append(f'\n## {i}. {u["title"]}')
        for j,l in enumerate(u['lessons'],1):
            n=NOTES[f'{u["id"]}-{j}']
            out += [f'\n### {i}.{j} {n["title"]}','Say to students: '+n['say']]
            out += [f'- {s}: {m} ({unit})' for s,m,unit in n['terms']]
            out += [f'{k}. {title} {text}' for k,(title,text) in enumerate(n['steps'],1)]
            out += ['`'+n['equation']+'`','Worked check: '+n['worked'],'Conditions: '+n['limits'],'Ask, then explain: '+n['check'],'Sources: '+'; '.join(r[1] for r in n['refs'])]
    return '\n\n'.join(out)
