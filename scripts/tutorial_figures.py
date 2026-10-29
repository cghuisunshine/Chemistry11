"""Original, accessible SVG teaching diagrams embedded in the standalone page."""
from html import escape
from math import cos, sin, pi

GREEN='#235b47'; ORANGE='#c05d38'; BLUE='#416b9b'; INK='#213e36'
FIGURES={}
def text(x,y,s,size=15,fill=INK,anchor='start'):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}">{escape(s)}</text>'
def line(x,y,x2,y2,color=GREEN,width=2,dash=''):
    return f'<path d="M{x} {y}L{x2} {y2}" fill="none" stroke="{color}" stroke-width="{width}"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>'
def circle(x,y,r=10,fill=GREEN,label=''):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"/>'+(text(x,y+5,label,14,'white','middle') if label else '')
def panel(x,y,w,h,title):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#fff" stroke="#cbd8c3"/>'+text(x+15,y+26,title,16)
def arrow(x,y,x2,y2,color=ORANGE):
    angle=__import__('math').atan2(y2-y,x2-x)
    pts=' '.join(f'{x2-9*cos(angle+a):.1f},{y2-9*sin(angle+a):.1f}' for a in (-.5,.5))
    return line(x,y,x2,y2,color)+f'<polygon points="{x2},{y2} {pts}" fill="{color}"/>'
def add(lid,title,body,caption,height=280):
    FIGURES[lid]=(title,body,caption,height)
def molecule(x,y,kind='water'):
    if kind=='water':
        return line(x,y,x-23,y+25,BLUE,4)+line(x,y,x+23,y+25,BLUE,4)+circle(x,y,14,ORANGE,'O')+circle(x-23,y+25,10,BLUE,'H')+circle(x+23,y+25,10,BLUE,'H')
    return line(x-20,y,x+20,y,GREEN,4)+circle(x-20,y,12,BLUE,'H')+circle(x+20,y,12,BLUE,'H')

# Reading a measured volume.
b=panel(25,20,250,225,'Eye level avoids parallax')
b+='<path d="M100 65V207H180V65M102 138Q140 160 178 138" fill="none" stroke="#416b9b" stroke-width="3"/>'
for y,n in [(100,'20'),(140,'21'),(180,'22')]: b+=line(163,y,180,y)+text(187,y+5,n,13)
b+=line(140,150,245,150,ORANGE,2,'5 4')+text(40,235,'Read the bottom of the meniscus.',13)
b+=panel(300,20,295,225,'Burette: numbers increase down')+text(325,89,'Initial reading: 12.30 mL',17)+text(325,129,'Final reading: 28.65 mL',17)+arrow(332,150,332,182)+text(355,184,'Delivered = 16.35 mL',17)
add('skills-1','Read a burette at the meniscus',b,'For a clear aqueous liquid with a concave meniscus, read its bottom at eye level. Delivered volume is the final reading minus the initial reading.')

b=''
for x,title,pts in [(20,'Solid',[(i*28,j*28) for i in range(4) for j in range(3)]),(220,'Liquid',[(5,3),(34,10),(68,0),(95,18),(12,37),(43,45),(78,34),(101,62),(20,77),(57,76),(80,91),(3,107)]),(420,'Gas',[(8,0),(95,10),(45,52),(6,105),(96,119),(63,143)])]:
    b+=panel(x,20,180,220,title)
    for dx,dy in pts: b+=circle(x+36+dx,80+dy,8)
b+=text(310,268,'Same particles; different arrangement and motion.',15,anchor='middle')
add('matter-1','Particle arrangements in three states',b,'Schematic snapshots: solid particles vibrate around positions; liquid particles remain close but rearrange; gas particles are widely separated. Sizes and separations are not to scale.')

b=line(65,225,65,32)+line(65,225,570,225)+text(22,28,'T',18)+text(410,258,'Energy supplied →',14)
points=[(75,205),(165,160),(265,160),(365,95),(485,95),(558,43)]
b+='<polyline points="'+' '.join(f'{x},{y}' for x,y in points)+'" fill="none" stroke="#235b47" stroke-width="4"/>'
for x,y,s in [(85,187,'solid warms'),(175,145,'melting'),(292,134,'liquid warms'),(384,80,'boiling'),(465,33,'gas warms')]:b+=text(x,y,s,13)
b+=text(165,191,'solid + liquid',12)+text(380,125,'liquid + gas',12)
add('matter-2','Heating a pure substance at constant pressure',b,'Slopes raise temperature within one phase. Idealized plateaus change the phase at constant temperature: energy changes intermolecular potential energy. The widths are schematic.')

b=panel(20,20,275,215,'Mixture before filtration')+panel(320,20,275,215,'Filtrate: dissolved solute passes')
for x,y in [(60,85),(125,115),(230,95),(80,190),(220,180),(160,165)]: b+=circle(x,y,5,BLUE)
for x,y in [(75,125),(195,85),(245,145)]: b+=circle(x,y,15,ORANGE)
b+=line(355,105,558,105,INK,4)+text(376,86,'filter holds large solid particles',12)
for x,y in [(380,151),(445,182),(530,161),(400,207),(490,220)]: b+=circle(x,y,5,BLUE)
for x in [380,440,520]: b+=circle(x,100,13,ORANGE)
b+=text(42,264,'Orange: insoluble solid    Blue: dissolved solute (water omitted)',14)
add('matter-3','Filtration separates suspended solid from solution',b,'A filter does not remove dissolved ions or small solute molecules. Recover dissolved solid by a suitable evaporation or crystallization procedure.')

b=panel(20,20,275,200,'Ionic: MgCl₂')+panel(320,20,275,200,'Molecular: CO₂')
for x,y,label,col in [(95,105,'Mg²⁺',GREEN),(202,80,'Cl⁻',ORANGE),(202,158,'Cl⁻',ORANGE)]:b+=circle(x,y,25,col)+text(x,y+5,label,14,'white','middle')
b+=text(55,194,'+2 + 2(−1) = 0',17)
b+=line(386,115,525,115,GREEN,6)+circle(386,115,24,ORANGE,'O')+circle(455,115,24,GREEN,'C')+circle(525,115,24,ORANGE,'O')+text(350,194,'One C atom, two O atoms',16)
add('matter-4','Formula ratios versus discrete molecules',b,'MgCl₂ specifies the 1:2 ion ratio in an extended ionic solid, not an isolated three-ion molecule. CO₂ is a discrete molecule with covalent bonds.',250)

b=''
for x,title,neut,mass in [(20,'Carbon-12',6,12),(320,'Carbon-14',8,14)]:
    b+=panel(x,20,275,215,title)
    for i in range(6+neut):b+=circle(x+77+(i%4)*31,90+(i//4)*31,12,GREEN if i<6 else ORANGE,'+' if i<6 else '')
    b+=text(x+20,219,f'6 protons + {neut} neutrons; A = {mass}',14)
add('mole-1','Isotopes have the same proton count',b,'Green + circles are protons; orange circles are neutrons. These are schematic nucleus inventories, not a measured nuclear arrangement. Neutral atoms of either isotope have six electrons.',260)

b=panel(20,30,170,190,'Count particles')+panel(225,30,170,190,'Convert to moles')+panel(430,30,170,190,'Convert to mass')
b+=text(105,111,'N',34,anchor='middle')+text(310,111,'n',34,anchor='middle')+text(515,111,'m',34,anchor='middle')+text(105,178,'entities',14,anchor='middle')+text(310,178,'mol',14,anchor='middle')+text(515,178,'g',14,anchor='middle')+arrow(174,130,237,130)+arrow(379,130,442,130)+text(205,103,'÷ Nₐ',14,anchor='middle')+text(410,103,'× M',14,anchor='middle')
add('mole-2','Particles to amount to mass',b,'Specify the entity: atoms, molecules, ions, or formula units. Nₐ is the Avogadro constant and M is the molar mass of that entity.',245)

b=''
for x,title,rad in [(20,'Same n, same pressure',78),(320,'Higher temperature → larger volume',98)]:
    b+=panel(x,20,275,225,title if x==20 else 'Higher T at the same n and p')
    b+=f'<rect x="{x+136-rad}" y="65" width="{rad*2}" height="{rad*1.45}" rx="12" fill="#eef3e8" stroke="#235b47"/>'
    for dx,dy in [(-36,25),(22,55),(-13,88),(42,103)]:b+=circle(x+136+dx,65+dy,7)
b+=text(310,270,'Ideal-gas model: V = nRT / p',16,anchor='middle')
add('mole-3','Gas volume depends on temperature and pressure',b,'At fixed amount and pressure, heating an ideal gas increases volume. The sketches represent equal particle counts; they are not to scale.')

b=panel(20,20,580,215,'2 H₂ + O₂ → 2 H₂O')+molecule(82,115,'hydrogen')+molecule(82,180,'hydrogen')+line(210,135,255,135,GREEN,4)+circle(210,135,17,ORANGE,'O')+circle(255,135,17,ORANGE,'O')+arrow(300,137,375,137)+molecule(445,100)+molecule(530,165)
b+=text(310,264,'Before: 4 H, 2 O             After: 4 H, 2 O',16,anchor='middle')
add('reactions-1','Balancing conserves atoms',b,'Each coefficient counts whole molecules in this particle picture. Bonds rearrange while the numbers of H and O atoms are conserved.')

b=panel(20,20,270,205,'Before: freely moving ions')+panel(315,20,285,205,'After: AgCl precipitates')
for x,y,col,s in [(70,92,GREEN,'Ag⁺'),(152,158,ORANGE,'Cl⁻'),(234,90,BLUE,'Na⁺'),(228,180,'#74736a','NO₃⁻')]: b+=circle(x,y,24,col)+text(x,y+5,s,13,'white','middle')
for i in range(6):b+=circle(359+(i%3)*34,145+(i//3)*34,16,GREEN if i%2 else ORANGE)
b+=text(358,213,'AgCl(s)',14)+circle(505,90,24,BLUE)+text(505,95,'Na⁺',13,'white','middle')+circle(550,167,24,'#74736a')+text(550,172,'NO₃⁻',13,'white','middle')
add('reactions-3','Precipitation and spectator ions',b,'Ag⁺(aq) + Cl⁻(aq) → AgCl(s). Na⁺ and NO₃⁻ remain dissolved spectators. Water and most particles are omitted; the cluster represents a growing ionic lattice.',250)

b=panel(20,20,260,205,'Oxidation: electron loss')+panel(330,20,270,205,'Reduction: electron gain')+text(150,115,'Zn → Zn²⁺ + 2e⁻',22,anchor='middle')+text(465,115,'Cu²⁺ + 2e⁻ → Cu',22,anchor='middle')+arrow(220,172,399,172)+text(310,157,'2 electrons transferred',13,anchor='middle')+text(310,262,'Zn + Cu²⁺ → Zn²⁺ + Cu',19,anchor='middle')
add('reactions-4','Match electron loss with electron gain',b,'The two half-reactions conserve charge and exchange equal numbers of electrons. The electron arrow summarizes transfer; it is not a picture of the complete cell apparatus.')

# All five atomic lessons receive a dedicated figure.
b=''
for x,title in [(15,'Dalton'),(165,'Thomson'),(315,'Rutherford'),(465,'Quantum')]:b+=panel(x,20,140,215,title)
b+=circle(85,118,42,GREEN)
b+=circle(235,118,46,'#dfeab7')
for x,y in [(214,100),(252,107),(228,141)]:b+=circle(x,y,7,BLUE,'−')
b+=circle(385,118,8,ORANGE,'+')
for x,y in [(349,90),(416,144)]:b+=circle(x,y,6,BLUE)
b+='<ellipse cx="385" cy="118" rx="48" ry="33" fill="none" stroke="#a6b59d" stroke-dasharray="4 4"/>'
for r in range(48,4,-3):b+=f'<circle cx="535" cy="118" r="{r}" fill="#416b9b" opacity=".035"/>'
b+=circle(535,118,6,ORANGE)
for x,s in [(85,'solid sphere'),(235,'embedded e⁻'),(385,'small nucleus'),(535,'probability')]:b+=text(x,204,s,12,anchor='middle')
add('atoms-1','How atomic models changed',b,'Each model answered new evidence. Rutherford established a compact positive nucleus; the quantum picture describes electron probability rather than a definite orbit. Illustrations are schematic, with the nucleus greatly enlarged.',260)

b=panel(20,20,275,205,'²³₁₁Na: neutral atom')+panel(320,20,275,205,'²³₁₁Na⁺: positive ion')
for x,counts in [(20,('11 protons','12 neutrons','11 electrons')),(320,('11 protons','12 neutrons','10 electrons'))]:
    for j,(s,col) in enumerate(zip(counts,[GREEN,ORANGE,BLUE])):b+=circle(x+36,85+j*45,9,col)+text(x+57,90+j*45,s,17)
b+=text(310,263,'Ionization changes electrons; the nucleus stays the same.',15,anchor='middle')
add('atoms-2','Mass number, atomic number and ionic charge',b,'A = 23 counts protons + neutrons; Z = 11 counts protons. Losing one electron makes Na⁺. The plus charge does not mean that a proton was added.')

b=panel(20,20,245,220,'Bohr model: hydrogen only')+panel(290,20,310,220,'An emission line has a fixed energy')
for r in [28,53,80]:b+=f'<circle cx="142" cy="130" r="{r}" fill="none" stroke="#a6b59d"/>'
b+=circle(142,130,7,ORANGE,'+')+circle(142,50,6,BLUE)+arrow(147,54,147,98)+text(178,71,'n = 3',12)+text(178,105,'n = 2',12)
b+=line(325,83,562,83)+line(325,168,562,168)+arrow(373,86,373,163)+text(419,110,'ΔE = hν = hc/λ',17)+text(419,145,'photon emitted',14)+text(330,209,'3 → 2: red light, λ ≈ 656 nm',15)
add('atoms-3','From a hydrogen level change to an emission line',b,'The shell sketch is a historical Bohr model, not a literal electron trajectory. The electron’s lower final energy corresponds to the positive energy carried away by a photon.',265)

b=panel(20,20,275,210,'s orbital: spherical symmetry')+panel(320,20,275,210,'p orbital: two lobes, one orbital')
for r in range(65,3,-3):b+=f'<circle cx="157" cy="132" r="{r}" fill="#416b9b" opacity=".045"/>'
b+=circle(157,132,4,ORANGE)+f'<ellipse cx="414" cy="132" rx="38" ry="53" fill="{BLUE}" opacity=".7"/><ellipse cx="498" cy="132" rx="38" ry="53" fill="{ORANGE}" opacity=".7"/>'+circle(456,132,4,GREEN)+line(456,69,456,195,INK,1,'4 4')+text(414,137,'+',20,'white','middle')+text(498,137,'−',20,'white','middle')+text(450,215,'nodal plane through nucleus',12,anchor='middle')
add('atoms-4','Orbitals describe wavefunctions and probability',b,'The s shading suggests probability density; the p lobes are a schematic orbital boundary. The two colours and ± signs show opposite wavefunction phases, not positive and negative charge. A single orbital holds at most two electrons.',285)

b=text(25,37,'Nitrogen: 1s² 2s² 2p³',20)+text(25,72,'Energy increases upward (spacing is schematic).',13)
for x,y,label,spin in [(120,200,'1s','↑↓'),(120,145,'2s','↑↓'),(320,90,'2p','↑'),(385,90,'','↑'),(450,90,'','↑')]:
    b+=f'<rect x="{x}" y="{y}" width="55" height="43" fill="white" stroke="#235b47"/>'+text(x+27,y+30,spin,26,anchor='middle')+text(x-37,y+29,label,16)
b+=text(295,166,'Hund: occupy equal-energy',15)+text(295,189,'orbitals singly before pairing.',15)+text(295,229,'Pauli: paired spins are opposite.',15)
add('atoms-5','Electron configurations as orbital boxes',b,'Each box is one orbital; each arrow is one electron’s spin projection. Three p orbitals hold up to six electrons. Arrows do not show electrons moving up or down.')

b=panel(20,20,275,205,'Across a period →')+panel(320,20,275,205,'Down a group ↓')
for x,r,s in [(90,39,'Na'),(210,23,'Cl')]:b+=circle(x,116,r,GREEN)+text(x,121,s,16,'white','middle')
b+=arrow(125,180,227,180)+text(50,208,'radius generally decreases',14)
b+=circle(390,88,18,GREEN)+circle(390,166,35,GREEN)+arrow(460,73,460,174)+text(486,112,'more shells',13)+text(486,141,'larger radius',13)
add('bonding-2','Two competing periodic size trends',b,'Within a period, stronger effective nuclear attraction generally contracts the occupied shell. Down a group, additional shells usually increase radius. These are qualitative trends for comparable atomic-radius definitions.',250)

b=panel(20,20,275,210,'Resonance: two contributors')+panel(320,20,275,210,'One delocalized ion')
b+=text(45,110,'[ O=N–O⁻ ] ↔ [ ⁻O–N=O ]',18)+text(48,156,'Same atoms and connectivity',14)+text(48,183,'Electron placement differs',14)
b+=text(354,111,'O — N — O',25)+line(358,120,445,120,ORANGE,2,'4 4')+line(458,120,550,120,ORANGE,2,'4 4')+text(349,164,'NO₂⁻: equivalent N–O bonds',14)+text(350,191,'Sketch straightened for clarity',12)
add('bonding-4','Resonance contributors versus the real ion',b,'These are skeletons of nitrite resonance contributors; lone pairs are omitted. The real ion is bent and has delocalized bonding. It does not flip between two molecules.',260)

b=panel(20,20,275,210,'CO₂: linear and nonpolar')+panel(320,20,275,210,'H₂O: bent and polar')
b+=text(57,133,'O=C=O',30)+arrow(138,88,68,88)+arrow(148,88,218,88)+text(55,199,'Equal bond dipoles cancel.',14)
b+=molecule(455,102)+arrow(425,143,447,118)+arrow(485,143,463,118)+arrow(455,91,455,61)+text(489,77,'net dipole',13)+text(351,199,'Bent geometry prevents cancellation.',13)
add('bonding-5','Molecular shape determines dipole cancellation',b,'Arrows point toward the more electronegative oxygen. The two C=O bond dipoles cancel in linear CO₂; the O–H bond dipoles add to a nonzero resultant in bent water.',260)

b=molecule(150,105)+molecule(260,170)+line(173,130,248,164,ORANGE,2,'5 4')+text(320,104,'O–H: covalent bond',17)+text(320,153,'O···H: hydrogen bond',17)+text(320,192,'between molecules',14)+arrow(306,110,168,114)+arrow(306,155,211,146)
add('bonding-6','Within a molecule versus between molecules',b,'The solid O–H bonds hold each water molecule together. The dashed contact illustrates hydrogen bonding between an H bonded to O and a neighbouring oxygen lone-pair region. Lone pairs and the full three-dimensional network are omitted.',240)

b=panel(20,20,580,200,'Hydration: water orients around ions')
for x,label,col in [(170,'Na⁺',GREEN),(450,'Cl⁻',ORANGE)]:
    b+=circle(x,129,25,col)+text(x,135,label,17,'white','middle')
    for dx in [-75,75]:
        # oxygen faces cation; hydrogen faces anion
        ox=x+dx; oy=129
        direction=1 if (label=='Na⁺' and dx>0) or (label=='Cl⁻' and dx<0) else -1
        for dy in [-17,17]:b+=line(ox,oy,ox+direction*24,oy+dy,BLUE,3)+circle(ox+direction*24,oy+dy,8,BLUE,'H')
        b+=circle(ox,oy,13,ORANGE,'O')
b+=text(310,254,'Oδ− faces cations; Hδ+ faces anions.',16,anchor='middle')
add('solutions-2','Water’s polarity explains ion hydration',b,'Orientation is a dynamic preference, not a rigid arrangement. The oxygen end is partially negative; hydrogen ends are partially positive. Only two waters per ion are drawn; actual hydration shells contain more.')

b=panel(20,20,245,205,'Dissolve CaCl₂')+panel(310,20,290,205,'Count aqueous ions')+text(142,125,'CaCl₂(s)',26,anchor='middle')+arrow(245,129,330,129)
for x,y,label,col in [(387,124,'Ca²⁺',GREEN),(510,85,'Cl⁻',ORANGE),(510,167,'Cl⁻',ORANGE)]:b+=circle(x,y,27,col)+text(x,y+5,label,15,'white','middle')
b+=text(310,261,'[Ca²⁺] = c       [Cl⁻] = 2c',19,anchor='middle')
add('solutions-3','Formula-unit ratios determine ion concentrations',b,'For complete dissociation, each mole of CaCl₂ supplies one mole of Ca²⁺ and two moles of Cl⁻. Here c is the analytical molarity of dissolved CaCl₂; water is omitted.')

b=''
for x,title,w in [(20,'Before dilution',120),(320,'After dilution',210)]:
    b+=panel(x,20,275,210,title)+f'<rect x="{x+35}" y="65" width="{w}" height="130" rx="6" fill="#e5eef6" stroke="#416b9b"/>'
    for dx,dy in [(15,20),(55,25),(30,65),(80,85),(10,108),(95,40)]:b+=circle(x+40+dx*(w/120),70+dy,6,GREEN)
b+=text(310,264,'Same amount of solute; larger final solution volume.',15,anchor='middle')
add('solutions-4','Dilution spreads the same solute through more solution',b,'Six dots represent the same solute inventory before and after adding solvent. With no solute loss or reaction, c₁V₁ = c₂V₂. Volumes refer to the solutions, not just the added water.')

b=panel(20,20,270,210,'Ethane: single bond')+panel(320,20,275,210,'Ethene: double bond')+text(155,132,'H₃C—CH₃',29,anchor='middle')+text(457,132,'H₂C=CH₂',29,anchor='middle')+text(55,192,'σ bond; rotation is accessible',14)+text(352,192,'σ + π; rotation disrupts π overlap',13)
add('organic-1','Carbon bonding controls molecular geometry',b,'Carbon has four bonds in both structures. Single-bond rotation changes conformation; double-bond rotation has a much higher barrier because it disrupts π bonding.',260)

b=panel(20,20,275,210,'Butane')+panel(320,20,275,210,'2-methylpropane')+text(48,119,'CH₃–CH₂–CH₂–CH₃',20)+text(365,130,'CH₃–CH–CH₃',23)+line(447,105,447,80)+text(447,68,'CH₃',20,anchor='middle')+text(310,263,'Both C₄H₁₀; different carbon connectivity.',17,anchor='middle')
add('organic-2','Constitutional isomers have different connectivity',b,'These structures have the same molecular formula but different atom connections. Rotating a drawing cannot turn one connectivity into the other.')

b=''
for x,y,title,formula in [(20,20,'Alcohol','R–OH'),(320,20,'Carboxylic acid','R–C(=O)–OH'),(20,138,'Ester','R–C(=O)–O–R′'),(320,138,'Amide','R–C(=O)–NH₂')]:b+=panel(x,y,275,102,title)+text(x+137,y+73,formula,23,ORANGE,'middle')
add('organic-3','Recognize the functional group first',b,'R and R′ stand for carbon-containing groups in these examples. A carbonyl C=O next to O or N changes the functional group and its chemistry. C(=O) explicitly shows the double-bonded oxygen.',275)

b=panel(20,20,580,215,'Addition polymerization: keep track of the carbon backbone')+text(68,106,'n CH₂=CH₂',27)+arrow(253,99,340,99)+text(369,106,'[–CH₂–CH₂–]ₙ',27)+text(62,160,'Many ethene monomers',16)+text(351,160,'One chain; a repeating unit',16)+text(62,204,'The π bond is replaced as new C–C σ bonds connect the units.',14)
add('organic-4','A monomer becomes a repeating unit',b,'This is a net structural picture for ethene addition polymerization. The brackets identify the repeat unit; the subscript n represents many units. Initiator and chain ends are omitted.',265)

b=panel(20,20,275,215,'Start: 3 H₂ and 1 O₂')+panel(320,20,275,215,'Finish: 2 H₂O and 1 H₂')
for y in [85,140,195]:b+=molecule(82,y,'hydrogen')
b+=line(208,137,250,137,GREEN,4)+circle(208,137,16,ORANGE,'O')+circle(250,137,16,ORANGE,'O')
b+=molecule(390,90)+molecule(510,90)+molecule(450,190,'hydrogen')+text(310,269,'O₂ runs out first. One H₂ molecule remains.',16,anchor='middle')
add('reactions-7','A limiting reactant leaves some excess reactant unused',b,'By 2 H₂ + O₂ → 2 H₂O, one O₂ reacts with two H₂. Starting with three H₂ leaves one H₂ unused. This particle inventory illustrates complete conversion by the stated reaction.')

def render_figure(lid):
    if lid not in FIGURES:return ''
    title,body,caption,height=FIGURES[lid]
    tid='picture-'+lid
    return f'<figure class="lesson-picture"><div class="picture-heading">Picture the idea · {escape(title)}</div><div class="picture-scroll" tabindex="0" role="region" aria-label="{escape(title)} diagram"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 {height}" role="img" aria-labelledby="{tid}-title {tid}-desc" style="font-family:system-ui,sans-serif"><title id="{tid}-title">{escape(title)}</title><desc id="{tid}-desc">{escape(caption)}</desc>{body}</svg></div><figcaption>{escape(caption)}</figcaption></figure>'
