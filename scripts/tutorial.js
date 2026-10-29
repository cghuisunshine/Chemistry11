'use strict';
const $ = id => document.getElementById(id);
const allDetails = [...document.querySelectorAll('details')];
const sections = [...document.querySelectorAll('.searchable')];
function toast(message) {
  $('toast').textContent = message;
  $('toast').hidden = false;
  clearTimeout(window.toastTimer);
  window.toastTimer = setTimeout(() => { $('toast').hidden = true; }, 2500);
}
const searchState = new Map();
function applySearch() {
  const query = $('search').value.trim().toLocaleLowerCase();
  if (query && !searchState.size) allDetails.forEach(d => searchState.set(d, d.open));
  let count = 0;
  sections.forEach(section => {
    section.hidden = !!query && !section.textContent.toLocaleLowerCase().includes(query);
    if (!section.hidden) count++;
    section.querySelectorAll('.lesson, .tutor-note, .formula-tree, .foundation-note').forEach(d => {
      const match = !!query && d.textContent.toLocaleLowerCase().includes(query);
      d.classList.toggle('search-hit', match && d.classList.contains('lesson'));
      if (match) d.open = true;
    });
  });
  $('overview').hidden = !!query;
  $('emptySearch').hidden = !query || count > 0;
  $('searchStatus').textContent = query ? `${count} matching section${count === 1 ? '' : 's'}. Clear search to restore the full course.` : '';
  if (!query) {
    searchState.forEach((open, detail) => { detail.open = open; });
    searchState.clear();
  }
}
$('search').addEventListener('input', applySearch);
function clearSearch() { if ($('search').value) { $('search').value = ''; applySearch(); } }
document.querySelectorAll('[data-expand]').forEach(button => button.addEventListener('click', () => {
  clearSearch(); allDetails.forEach(detail => { detail.open = button.dataset.expand === 'true'; });
}));
document.querySelectorAll('[data-tutor-expand]').forEach(button => button.addEventListener('click', () => {
  clearSearch();
  const open = button.dataset.tutorExpand === 'true';
  document.querySelectorAll('.tutor-note').forEach(note => {
    note.open = open;
    if (open) note.closest('.lesson').open = true;
  });
  toast(open ? 'Tutor explanations opened' : 'Tutor explanations closed');
}));
document.querySelectorAll('[data-tree-expand]').forEach(button => button.addEventListener('click', () => {
  clearSearch(); document.querySelectorAll('.formula-tree').forEach(tree => { tree.open = button.dataset.treeExpand === 'true'; });
}));
let printDetails = [], printHidden = [];
window.addEventListener('beforeprint', () => {
  printDetails = allDetails.map(detail => detail.open);
  printHidden = [...document.querySelectorAll('[hidden]')].filter(el => el.id !== 'toast' && el.id !== 'emptySearch' && !el.classList.contains('feedback'));
  printHidden.forEach(el => { el.hidden = false; });
  allDetails.forEach(detail => { detail.open = true; });
});
window.addEventListener('afterprint', () => {
  allDetails.forEach((detail, i) => { detail.open = printDetails[i] ?? detail.open; });
  printHidden.forEach(el => { el.hidden = true; });
});
$('printBtn').addEventListener('click', () => window.print());
const menu = $('menuBtn');
function closeMenu() { document.body.classList.remove('sidebar-open'); menu.setAttribute('aria-expanded', 'false'); }
menu.addEventListener('click', () => {
  const open = document.body.classList.toggle('sidebar-open'); menu.setAttribute('aria-expanded', String(open));
  if (open) document.querySelector('#sidebar a').focus();
});
$('backdrop').addEventListener('click', closeMenu);
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && document.body.classList.contains('sidebar-open')) { closeMenu(); menu.focus(); }
  if (event.key === 'Tab' && document.body.classList.contains('sidebar-open')) {
    const focusables = [...$('sidebar').querySelectorAll('a,button,input')];
    const first = focusables[0], last = focusables[focusables.length - 1];
    if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last.focus(); }
    else if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first.focus(); }
  }
});
function revealTarget(hash = location.hash) {
  let id; try { id = decodeURIComponent(hash.slice(1)); } catch { return; }
  const target = $(id); if (!target) return;
  if (target.closest('[hidden]')) clearSearch();
  let ancestor = target;
  while (ancestor) { if (ancestor.tagName === 'DETAILS') ancestor.open = true; ancestor = ancestor.parentElement; }
}
document.querySelectorAll('a[href^="#"]').forEach(anchor => anchor.addEventListener('click', () => { revealTarget(anchor.hash); closeMenu(); }));
window.addEventListener('hashchange', () => { revealTarget(); });
const complete = [...document.querySelectorAll('.complete')];
let saved = [];
try { const value = JSON.parse(localStorage.getItem('chem11-reviewed-v1') || '[]'); if (Array.isArray(value)) saved = value; } catch { /* Session progress works even if storage is disabled. */ }
function updateProgress() {
  const checked = complete.filter(input => input.checked);
  $('progressText').textContent = `${checked.length} of ${complete.length} chapters reviewed`;
  $('courseProgress').value = checked.length;
  try { localStorage.setItem('chem11-reviewed-v1', JSON.stringify(checked.map(input => input.dataset.unit))); }
  catch { $('storageNote').textContent = 'Progress is available for this session only.'; }
}
complete.forEach(input => { input.checked = saved.includes(input.dataset.unit); input.addEventListener('change', updateProgress); });
updateProgress();
$('resetProgress').addEventListener('click', () => { complete.forEach(input => { input.checked = false; }); updateProgress(); toast('Review progress reset'); });
document.querySelectorAll('.quiz').forEach(form => form.addEventListener('submit', event => {
  event.preventDefault(); let score = 0, answered = 0;
  const questions = quizData[form.dataset.unit];
  questions.forEach((question, i) => {
    const chosen = form.querySelector(`input[name="${form.dataset.unit}-q${i}"]:checked`);
    const feedback = $(`${form.dataset.unit}-feedback${i}`);
    feedback.hidden = false;
    if (!chosen) { feedback.className = 'feedback bad'; feedback.textContent = 'Choose an answer, then check again.'; return; }
    answered++;
    const correct = Number(chosen.value) === question.answer; if (correct) score++;
    feedback.className = 'feedback ' + (correct ? 'good' : 'bad');
    feedback.textContent = (correct ? 'Correct. ' : 'Try again. ') + question.explanation;
  });
  form.querySelector('.quiz-score').textContent = `${score}/${questions.length} correct` + (answered < questions.length ? ` · ${questions.length - answered} unanswered` : '');
}));
async function copyFormula(box) {
  const text = box.querySelector('span').textContent;
  try { await navigator.clipboard.writeText(text); toast('Formula copied'); }
  catch {
    const range = document.createRange(); range.selectNodeContents(box.querySelector('span'));
    const selection = window.getSelection(); selection.removeAllRanges(); selection.addRange(range);
    toast('Formula selected — use your browser’s Copy command');
  }
}
document.querySelectorAll('[data-copy]').forEach(box => {
  box.addEventListener('dblclick', () => copyFormula(box));
  box.querySelector('button').addEventListener('click', () => copyFormula(box));
});
function validNumbers(ids) { return ids.every(id => $(id).value.trim() !== '' && $(id).validity.valid && Number.isFinite(Number($(id).value))); }
function fixed(number) { return Number(number.toPrecision(4)).toLocaleString('en-US', { maximumSignificantDigits: 4 }); }
function sci(number) { return number === 0 ? '0' : number.toExponential(3).replace(/e\+?(-?)(\d+)/, (_, sign, power) => ` × 10^${sign === '-' ? '−' : ''}${power}`); }
function bind(ids, handler) { ids.forEach(id => $(id).addEventListener('input', handler)); handler(); }
bind(['densityMass','densityVolume'], () => {
  if (!validNumbers(['densityMass','densityVolume'])) { $('densityResult').textContent = 'Enter a nonnegative mass and a positive volume within the displayed limits.'; return; }
  const mass = Number($('densityMass').value), volume = Number($('densityVolume').value);
  $('densityResult').textContent = `ρ = ${mass} g ÷ ${volume} mL = ${fixed(mass / volume)} g mL⁻¹ = ${fixed(mass / volume * 1000)} kg m⁻³`;
});
const cations = [{formula:'Ca',charge:2,name:'calcium'}, {formula:'Al',charge:3,name:'aluminum'}, {formula:'Fe',charge:3,name:'iron(III)'}, {formula:'NH₄',charge:1,name:'ammonium',poly:true}];
const anions = [{formula:'Cl',charge:1,name:'chloride'}, {formula:'O',charge:2,name:'oxide'}, {formula:'SO₄',charge:2,name:'sulfate',poly:true}, {formula:'NO₃',charge:1,name:'nitrate',poly:true}];
const subs = value => String(value).replace(/\d/g, digit => '₀₁₂₃₄₅₆₇₈₉'[Number(digit)]);
function gcd(a,b) { return b ? gcd(b,a % b) : a; }
function group(ion,count) { return (ion.poly && count > 1 ? `(${ion.formula})` : ion.formula) + (count > 1 ? subs(count) : ''); }
bind(['cation','anion'], () => {
  const a = cations[Number($('cation').value)], b = anions[Number($('anion').value)];
  const divisor = gcd(a.charge,b.charge), x = b.charge / divisor, y = a.charge / divisor;
  $('ionicResult').textContent = `${group(a,x)}${group(b,y)} · ${a.name} ${b.name} · charge check: ${x}(+${a.charge}) + ${y}(−${b.charge}) = 0`;
});
const substances = [{mass:18.02,entity:'molecules',oxygen:1}, {mass:44.01,entity:'molecules',oxygen:2}, {mass:58.44,entity:'formula units',oxygen:0}, {mass:32,entity:'molecules',oxygen:2}];
bind(['moleMass','moleSubstance'], () => {
  if (!validNumbers(['moleMass'])) { $('moleResult').textContent = 'Enter a nonnegative sample mass up to 1,000,000 g.'; return; }
  const substance = substances[Number($('moleSubstance').value)], n = Number($('moleMass').value) / substance.mass;
  $('moleResult').textContent = `n = ${fixed(n)} mol · N = ${sci(n * 6.02214076e23)} ${substance.entity}` + (substance.oxygen ? ` · O atoms = ${sci(n * substance.oxygen * 6.02214076e23)}` : ' · Equal numbers of Na⁺ and Cl⁻ in the formula-unit count.');
});
bind(['hydrogen','oxygen'], () => {
  if (!validNumbers(['hydrogen','oxygen'])) { $('limitingResult').textContent = 'Enter each reactant amount from 0 to 100 mol.'; return; }
  const h = Number($('hydrogen').value), o = Number($('oxygen').value), extent = Math.min(h / 2,o);
  const limiting = h === 0 && o === 0 ? 'No reactants available' : Math.abs(h / 2 - o) < 1e-10 ? 'Exact stoichiometric amounts' : h / 2 < o ? 'H₂ limits' : 'O₂ limits';
  $('limitingResult').textContent = `${limiting} · H₂O formed: ${fixed(2 * extent)} mol · Remaining H₂: ${fixed(h - 2 * extent)} mol · Remaining O₂: ${fixed(o - extent)} mol`;
});
bind(['wavelength'], () => {
  const wavelength = Number($('wavelength').value), frequency = 299792458 / (wavelength * 1e-9), energy = 6.62607015e-34 * frequency;
  $('waveValue').value = wavelength;
  $('photonResult').textContent = `ν = ${sci(frequency)} s⁻¹ · E = ${sci(energy)} J per photon · ${fixed(energy * 6.02214076e23 / 1000)} kJ per mole of photons`;
  const points = Array.from({length:261},(_,i) => `${i ? 'L' : 'M'}${10 + i * 2},${48 - 27 * Math.sin(i * 2 * Math.PI / (wavelength / 9))}`).join(' ');
  $('wavePath').setAttribute('d',points);
  $('wavePath').setAttribute('stroke',`hsl(${Math.max(0,Math.min(275,(750 - wavelength) / 370 * 275))} 50% 43%)`);
});
const shapes = {
  CO2:{central:'C',outer:'O',positions:[[-150,0],[150,0]],name:'linear',geometry:'linear',domains:2,lone:0,angle:'180°',polar:false,double:true},
  BF3:{central:'B',outer:'F',positions:[[0,-80],[-105,65],[105,65]],name:'trigonal planar',geometry:'trigonal planar',domains:3,lone:0,angle:'120°',polar:false},
  CH4:{central:'C',outer:'H',positions:[[0,-80],[-100,65],[100,65],[0,70]],name:'tetrahedral',geometry:'tetrahedral',domains:4,lone:0,angle:'109.5°',polar:false,depth:true},
  NH3:{central:'N',outer:'H',positions:[[-105,45],[105,45],[0,85]],name:'trigonal pyramidal',geometry:'tetrahedral',domains:4,lone:1,angle:'about 107°',polar:true,depth:true},
  H2O:{central:'O',outer:'H',positions:[[-95,74],[95,74]],name:'bent',geometry:'tetrahedral',domains:4,lone:2,angle:'about 104.5°',polar:true},
  PCl5:{central:'P',outer:'Cl',positions:[[0,-90],[0,90],[-115,-35],[115,-35],[85,55]],name:'trigonal bipyramidal',geometry:'trigonal bipyramidal',domains:5,lone:0,angle:'90°, 120°, 180°',polar:false,depth:true},
  SF6:{central:'S',outer:'F',positions:[[0,-90],[0,90],[-115,-30],[115,30],[-90,55],[90,-55]],name:'octahedral',geometry:'octahedral',domains:6,lone:0,angle:'90°, 180°',polar:false,depth:true}
};
bind(['shape'], () => {
  const key = $('shape').value, s = shapes[key], cx = 270, cy = 120;
  let markup = '';
  s.positions.forEach(([x,y],i) => {
    const color = '#789775';
    if (s.depth && i === s.positions.length - 1) markup += `<path d="M${cx - 2} ${cy} L${cx + x - 9} ${cy + y} L${cx + x + 9} ${cy + y}Z" fill="${color}"/>`;
    else markup += `<line x1="${cx}" y1="${cy}" x2="${cx + x}" y2="${cy + y}" stroke="${color}" stroke-width="${s.double ? 8 : 3}" ${s.depth && i === s.positions.length - 2 ? 'stroke-dasharray="5 5"' : ''}/>`;
    if (s.double) markup += `<line x1="${cx}" y1="${cy}" x2="${cx + x}" y2="${cy + y}" stroke="#edf2e6" stroke-width="2"/>`;
    markup += `<circle cx="${cx + x}" cy="${cy + y}" r="21" fill="#e0e8c2"/><text x="${cx + x}" y="${cy + y + 5}" text-anchor="middle" font-size="15" fill="#235b47">${s.outer}</text>`;
  });
  markup += `<circle cx="${cx}" cy="${cy}" r="26" fill="#235b47"/><text x="${cx}" y="${cy + 6}" text-anchor="middle" font-size="19" fill="white">${s.central}</text>`;
  for (let i = 0; i < s.lone; i++) markup += `<ellipse cx="${cx + (s.lone === 2 ? (i ? 30 : -30) : 0)}" cy="${cy - 45}" rx="15" ry="23" fill="#d46a4320"/><text x="${cx + (s.lone === 2 ? (i ? 30 : -30) : 0)}" y="${cy - 43}" text-anchor="middle" fill="#b25130" font-size="18">••</text>`;
  $('shapeDrawing').innerHTML = markup;
  $('shapeGraphic').setAttribute('aria-label',`${key}: ${s.name}; ${s.lone} central lone pairs; ${s.polar ? 'polar' : 'nonpolar'}. Schematic projection.`);
  $('shapeResult').textContent = `${s.domains} electron domains · ${s.lone} central lone pair${s.lone === 1 ? '' : 's'} · Electron geometry: ${s.geometry} · Molecular shape: ${s.name} · Angles: ${s.angle} · ${s.polar ? 'Polar: dipoles do not cancel' : 'Nonpolar: symmetry cancels bond dipoles'}`;
});
bind(['stockConcentration','stockVolume','finalVolume'], () => {
  if (!validNumbers(['stockConcentration','stockVolume','finalVolume'])) { $('dilutionResult').textContent = 'Enter a nonnegative concentration and positive volumes within the displayed limits.'; return; }
  const c = Number($('stockConcentration').value), v = Number($('stockVolume').value), final = Number($('finalVolume').value);
  if (final < v) { $('dilutionResult').textContent = 'For dilution, final volume must be at least the aliquot volume. Enter a larger final volume.'; return; }
  $('dilutionResult').textContent = `Retained solute: ${fixed(c * v / 1000)} mol · c₂ = ${c} × ${v}/${final} = ${fixed(c * v / final)} mol L⁻¹ · Dilution factor: ${fixed(final / v)}`;
});
bind(['carbonCount'], () => {
  const n = Number($('carbonCount').value), names = ['methane','ethane','propane','butane','pentane','hexane','heptane','octane','nonane','decane'];
  $('carbonValue').value = n;
  $('organicResult').textContent = `${names[n - 1]} · C${n > 1 ? subs(n) : ''}H${subs(2 * n + 2)} · ${n - 1} C–C bonds · ${2 * n + 2} C–H bonds`;
  const gap = n > 1 ? Math.min(48,440 / (n - 1)) : 0, left = 270 - (n - 1) * gap / 2;
  let markup = '';
  for (let i = 0; i < n; i++) {
    const x = left + i * gap, y = n === 1 ? 55 : (i % 2 ? 75 : 35);
    if (i) markup += `<line x1="${x - gap}" y1="${i % 2 ? 35 : 75}" x2="${x}" y2="${y}" stroke="#789775" stroke-width="3"/>`;
    markup += `<circle cx="${x}" cy="${y}" r="13" fill="#235b47"/><text x="${x}" y="${y + 4}" text-anchor="middle" fill="white" font-size="12">C</text>`;
  }
  $('chainDrawing').innerHTML = markup;
  $('chainGraphic').setAttribute('aria-label',`${names[n - 1]}: a straight chain of ${n} carbon atoms with ${2 * n + 2} implicit hydrogens`);
});
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver(entries => {
    const visible = entries.filter(entry => entry.isIntersecting).sort((a,b) => a.boundingClientRect.top - b.boundingClientRect.top);
    if (visible.length) document.querySelectorAll('nav a').forEach(anchor => anchor.classList.toggle('active',anchor.hash === '#' + visible[0].target.id));
  }, {rootMargin:'-80px 0px -55% 0px'});
  [$('overview'),...sections].forEach(section => observer.observe(section));
}
revealTarget();
if (location.hash) requestAnimationFrame(() => { document.getElementById(decodeURIComponent(location.hash.slice(1)))?.scrollIntoView({behavior:'instant',block:'start'}); });
