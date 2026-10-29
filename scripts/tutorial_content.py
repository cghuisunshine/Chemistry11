"""Original Chemistry 11 teaching notes; PDF page numbers refer to chem11.pdf."""
def lesson(title, page, idea, equation, trap, why, check):
    return dict(title=title, page=page, idea=idea, equation=equation, trap=trap, why=why, check=check)
def unit(id, title, subtitle, question, symbol, lessons, examples, quiz, tree):
    return dict(id=id,title=title,subtitle=subtitle,question=question,symbol=symbol,lessons=lessons,examples=examples,quiz=quiz,tree=tree)
UNITS = [
unit('skills','Skills & processes','Measure carefully. Make evidence useful.','How can a measurement support a scientific claim?','±',[
lesson('Laboratory safety & choosing equipment',8,
'''A safe investigation starts with knowing the hazards, the procedure, and where the eyewash, safety shower, fire equipment, and exits are. Wear splash goggles and the protective clothing required by your teacher; tie back hair, keep food away, and report spills, injuries, and broken glass immediately. Never taste a chemical or pipette by mouth. Follow the instructor’s disposal directions rather than assuming a sink is suitable.

Choose equipment for its purpose. A beaker holds and mixes; a graduated cylinder measures approximate volumes; a volumetric pipette transfers a specified volume accurately; a volumetric flask makes a solution to one final volume; a burette measures a variable delivered volume. Read a clear liquid’s meniscus at eye level to avoid parallax.''',
'Volume delivered by a burette = final reading − initial reading',
'A beaker’s volume marks do not make it a substitute for a volumetric flask. Follow the teacher’s procedure for heating and dilution.',
'''Accuracy depends on calibration and on how the apparatus is used. A pipette marked “to deliver” is calibrated for its intended drainage procedure. Rinsing it with the solution prevents a residual water film from diluting that solution. A burette tip bubble makes the recorded volume larger than the volume actually delivered to the flask: part of the apparent delivery fills the tip. Connect each technique to its effect on the result rather than memorizing a ritual.''',
'Why read the meniscus at eye level? A tilted line of sight creates parallax and shifts the apparent reading.'),
lesson('Scientific method, observations & lab reports',22,
'''An observation records what was measured or noticed; an inference proposes an explanation. “A blue solid formed” is an observation; “a new copper compound formed” is an inference that needs chemical evidence. Qualitative observations describe a property; quantitative observations include a number and a unit.

State a testable question and a hypothesis with a reason. Change the independent variable, measure the dependent variable, and control other relevant conditions. Record raw data before calculating. A useful lab report gives the purpose, relevant theory, enough procedure to understand the investigation, labelled observations, calculations, and a conclusion tied to the evidence. Discuss specific sources of uncertainty and explain their likely effect. A graph puts the independent variable on x and the dependent variable on y, with units on both axes.''',
'Slope = Δy/Δx; percent error = |experimental − accepted|/|accepted| × 100%',
'“Human error” does not identify a cause or predict its effect. State what happened and how it changes the measured quantity.',
'''The claim–evidence–reasoning pattern separates a conclusion from its support. For a density experiment, the claim identifies the material, the evidence gives mass and volume or a graph slope, and the reasoning links those measurements to characteristic density. Repeated trials estimate variability but do not automatically remove a calibration bias. A best-fit line uses the overall data pattern; forcing it through the origin needs a physical justification and compatible uncertainties.''',
'Is a constant balance offset random? No. It is a systematic effect; repeating the same measurement does not average it away.'),
lesson('Significant figures, uncertainty & scientific notation',38,
'''A measurement includes the digits supported by the instrument and an estimated final digit where appropriate. Nonzero digits are significant. Zeros between them are significant; leading zeros locate the decimal point; trailing zeros after a decimal point indicate precision. Thus 0.00450 has three significant figures. Scientific notation makes the intended precision explicit: 4.50 × 10⁻³.

For multiplication and division, round to the fewest significant figures among measured inputs. For addition and subtraction, round to the least precise decimal place. Keep extra digits in intermediate work. Counted quantities, defined unit conversions, and stoichiometric coefficients are exact and do not limit significant figures. Accuracy describes closeness to a reference value; precision describes the spread of repeated measurements.''',
'12.11 g + 0.3 g = 12.4 g; 2.50 cm × 3.2 cm = 8.0 cm²',
'Decimal places and significant figures are different rules. A calculator display does not establish measurement precision.',
'''The rounding rules are practical ways to avoid claiming information the measurements do not contain. If a ruler supports millimetres, reporting a length to a millionth of a metre needs additional evidence. For an explicit uncertainty, quote the central value to a matching decimal place. Relative uncertainty compares Δx with |x|; a small absolute uncertainty can still be a large fraction of a tiny measurement. Exact factors such as 1000 mL per litre change the unit, not the underlying precision.''',
'How many significant figures are in 0.03040? Four: 3, the internal zero, 4, and the final zero.'),
lesson('Dimensional analysis, density & conversions',51,
'''A conversion factor is a ratio of two equivalent quantities, so multiplying by it changes the unit without changing the physical amount. Write the starting measurement, multiply by factors, cancel units, and check that only the requested unit remains. Convert numerator and denominator units separately for rates and densities. Square or cube the entire length conversion factor when converting area or volume.

Density is mass per volume. Rearrange its definition before substituting: m = ρV and V = m/ρ. For an irregular solid that does not dissolve or react, displaced liquid can provide its volume. Temperature and composition matter when comparing densities. Use kelvin for gas-law calculations: a change of 1 K equals a change of 1 °C, but the absolute zero points differ.''',
'ρ = m/V; 1.00 g cm⁻³ = 1.00 × 10³ kg m⁻³; T/K = t/°C + 273.15',
'1 cm³ = 10⁻⁶ m³. A cubic unit conversion uses the cube of the length factor.',
'''Density is intensive: doubling a uniform sample doubles m and V, so their ratio is unchanged. On a mass-versus-volume graph, m = ρV has slope ρ. If a constant container mass is accidentally included, m = ρV + m(container) has the same slope but a nonzero intercept. Unit analysis catches many setup mistakes, but it cannot prove the chosen physical model is valid.''',
'A metal has mass 27.0 g and volume 10.0 cm³. Its density is 2.70 g cm⁻³, not 270 g cm⁻³.')
], [
('Convert a density','Convert 2.70 g cm⁻³ to kg m⁻³.', ['Write 2.70 g/cm³ × (1 kg/1000 g) × (100 cm/1 m)³.','The cubic factor is 10⁶ cm³/m³; units reduce to kg/m³.','Result: 2.70 × 10³ kg m⁻³ (three significant figures).']),
('Use a best-fit line','A mass–volume line passes through (5.0 mL, 13.5 g) and (15.0 mL, 40.5 g). Find its slope and meaning.', ['Slope = (40.5 − 13.5) g/(15.0 − 5.0) mL = 2.70 g mL⁻¹.','The slope gives the material’s density when measured mass is proportional to sample volume.','The points should be points on the best-fit line, sufficiently far apart to reduce reading uncertainty.'])
], [
('Which instrument prepares an accurate final solution volume?',['Beaker','Volumetric flask','Test tube'],1,'A volumetric flask is calibrated to contain one specified volume at its calibration temperature.'),
('0.00560 has how many significant figures?',['Two','Three','Five'],1,'Leading zeros are placeholders; 5, 6, and the final zero are significant.'),
('Doubling a homogeneous sample doubles its mass. Its density…',['doubles','halves','stays the same'],2,'Volume doubles too, so the mass-to-volume ratio is unchanged.')
], ('Density from a proportional relationship','A uniform sample has m = ρV. Divide by V to get ρ = m/V; multiply by V to get m = ρV. Solve for V to get V = m/ρ.','For ρ = 2.70 g mL⁻¹ and V = 8.00 mL, m = 21.6 g.','The sample must be homogeneous and the density must correspond to the relevant temperature.','skills-4')),
unit('matter','The nature of matter','Classify, separate, and name substances.','What changes when ice melts, salt dissolves, or iron rusts?','◌',[
lesson('Properties, particles & physical or chemical change',66,
'''Matter has mass and occupies space. A physical property can be examined without changing chemical identity: density, melting point, conductivity, and state. A chemical property describes the ability to form different substances, such as flammability or reaction with acid. Extensive properties depend on sample size; intensive properties do not for a homogeneous material under specified conditions.

In a physical change the substance’s chemical identity remains; in a chemical change atoms rearrange into different substances. Melting ice changes the arrangement and motion of H₂O molecules, while electrolysis produces H₂ and O₂. Colour change, bubbles, light, or a temperature change can suggest reaction, but each also has possible physical causes. Interpret several observations together with the chemical context.''',
'Physical change: H₂O(s) → H₂O(l) | Chemical change: 2H₂O(l) → 2H₂(g) + O₂(g)',
'Boiling produces bubbles without forming a new substance. Dissolving is not automatically a chemical reaction.',
'''The particle model connects visible behaviour to invisible structure. Solids have particles localized around positions; liquids have close particles able to move past one another; gases have widely separated particles and fill their container. A molecular particle does not expand to fill a gas container; the distances between particles increase. Dissolving an ionic solid separates and hydrates pre-existing ions, so it needs a more careful particle description than “the salt disappears.”''',
'When water boils, does each water molecule become larger? No; molecular spacing increases as gas forms.'),
lesson('Energy, phase changes & heating curves',66,
'''Temperature measures thermal condition and is related to average particle kinetic energy in a simple particle model. Heat is energy transferred because of a temperature difference. On a heating curve at constant pressure, sloping portions describe warming within one phase; flat portions describe phase change of a pure substance at its transition temperature.

During melting or boiling, added energy changes particle interactions while the temperature remains approximately constant until the transition is complete. Freezing and condensation release energy to the surroundings; melting, vaporization, and sublimation absorb energy. The reverse paths undo those energy changes. Mixtures and changing pressure can shift or broaden transition temperatures. Use the axes: a curve plotted against time assumes a roughly constant heating power if time is to represent added energy.''',
'Within one phase: q = mcΔT | During a transition: q = nΔH_transition',
'A flat region does not mean no energy enters. It means added energy is supporting phase change rather than increasing temperature.',
'''Sketch a boundary around the sample. During warming, energy raises its internal energy and temperature. During a phase transition, the relative amounts of two phases change at the transition temperature. q = mcΔT assumes no phase transition and an approximately constant specific heat. Adding warming and transition terms gives a piecewise energy budget. The ideal plateau describes a pure substance at fixed pressure; a real experiment may show heat loss and a tilted plateau.''',
'Why can steam burn more severely than the same mass of water at 100 °C? Condensation can release additional energy before the resulting water cools.'),
lesson('Pure substances, mixtures & separation methods',79,
'''A pure substance has a characteristic composition: an element contains one kind of atom, and a compound contains elements chemically combined in a fixed ratio. A mixture has variable composition. A homogeneous mixture has uniform composition at the scale of observation; a heterogeneous mixture has distinguishable regions. A solution is homogeneous; a suspension can settle; a colloid has dispersed particles that can scatter light without readily settling.

Separation exploits a difference in physical properties. Filter an insoluble solid from liquid; use a separatory funnel for immiscible liquids; evaporate solvent or crystallize solute; distil using volatility differences; separate chromatographically using different attractions to stationary and mobile phases. Sieving separates solids by particle size. Magnetic separation, centrifugation, and sublimation are useful when the relevant property differs. Recovering both water and salt calls for distillation rather than simply boiling away the water.''',
'R_f = distance travelled by solute / distance travelled by solvent front',
'A filter does not normally remove dissolved salt from water. Separation of a mixture differs from chemical decomposition of a compound.',
'''In chromatography a component repeatedly partitions between the stationary and moving phases. Greater affinity for the moving phase generally carries it farther. Measure both distances from the same baseline and mark the solvent front promptly. R_f has no units and is comparable only under matching conditions. In fractional distillation, repeated condensation and vaporization improve separation of liquids with relatively close boiling points; one simple boiling-point rule cannot resolve every mixture.''',
'A spot moves 3.2 cm while the solvent front moves 8.0 cm. R_f = 0.40, with no unit.'),
lesson('Ionic & molecular naming: the November 22 chart',103,
'''First classify the formula. For an ionic compound, name the cation and then the anion. A monatomic anion ends in -ide. If the metal can have different charges, infer its charge from the formula and give a Roman numeral: FeCl₃ is iron(III) chloride. A Roman numeral gives the metal’s oxidation state in the compound, not the number of metal atoms.

For a binary molecular compound of nonmetals, use prefixes to show atom counts: mono, di, tri, tetra, penta, hexa, hepta, octa, nona, deca. Usually omit mono- from the first element and end the second in -ide: CO is carbon monoxide, N₂O₄ is dinitrogen tetroxide. For ionic formulas, balance charges in the smallest whole-number ratio. Keep a polyatomic ion’s internal subscripts and use parentheses if more than one is needed.''',
'Ca²⁺ + 2NO₃⁻ → Ca(NO₃)₂ | Fe₂O₃: 2x + 3(−2) = 0, so x = +3',
'Prefixes count atoms in molecular names; ionic names use charge balance. Ca(NO₃)₂ is not CaNO₆.',
'''The scanned November 22 flowchart separates binary ionic, multivalent ionic, polyatomic ionic, and molecular naming. Rebuild the decision from particles: an ionic formula records the neutral ratio of charged species in a lattice; a molecular formula counts atoms in a molecule. NH₄Cl shows why “metal plus nonmetal” is a useful first clue but not a complete definition: ammonium is a polyatomic cation. In Cu₃N₂, two N³⁻ require +6 total, so each Cu is +2 and the name is copper(II) nitride.''',
'Name Ni₂O₃. Oxygen contributes −6 in total, so each Ni is +3: nickel(III) oxide.'),
lesson('Polyatomic ions, acids & hydrates',103,
'''Recognize common ions as units: NH₄⁺ ammonium, OH⁻ hydroxide, NO₃⁻ nitrate, NO₂⁻ nitrite, SO₄²⁻ sulfate, SO₃²⁻ sulfite, CO₃²⁻ carbonate, PO₄³⁻ phosphate, and CH₃COO⁻ acetate. Their names and internal formulas remain when they form salts. For example, (NH₄)₂SO₄ is ammonium sulfate.

Binary aqueous acids commonly use hydro- + root + -ic acid: HCl(aq) is hydrochloric acid, while HCl(g) is hydrogen chloride. For oxyacids, -ate becomes -ic and -ite becomes -ous: HNO₃ is nitric acid; HNO₂ is nitrous acid. Retain per- and hypo- where relevant. A hydrate contains a specified ratio of water in its crystal: CuSO₄·5H₂O is copper(II) sulfate pentahydrate. Include those waters when calculating its molar mass.''',
'Fe³⁺ + SO₄²⁻ → Fe₂(SO₄)₃ | M(CuSO₄·5H₂O) = M(CuSO₄) + 5M(H₂O)',
'Acid naming depends on the formula and aqueous context. “-ate” is an ion name, not a prefix counting oxygen atoms universally.',
'''Oxyanion names compare related ions with the same central element; nitrate has one more oxygen than nitrite, but sulfate and nitrate do not have the same oxygen count. Charge balance applies to acids too: two H⁺ balance SO₄²⁻ to form H₂SO₄. The hydrate dot indicates composition of a crystalline substance, not multiplication of every preceding subscript. Heating some hydrates removes water; gravimetry can determine the mole ratio by comparing lost water with remaining anhydrous salt.''',
'Write aluminum sulfate. Two Al³⁺ balance three SO₄²⁻, giving Al₂(SO₄)₃.')
], [
('Choose the naming route','Name Cu₃N₂, PBr₅, and Ca₃(PO₄)₂.', ['Nitride is N³⁻. Two nitrides total −6, so three copper ions total +6: copper(II) nitride.','P and Br are nonmetals: phosphorus pentabromide.','Calcium has fixed +2 charge and phosphate is PO₄³⁻: calcium phosphate.']),
('Separate a mixture','How could you recover sand, salt, and water from a mixture containing all three?', ['Filter to collect the insoluble sand; rinse and dry it as appropriate.','Distil the filtrate: condense water vapour into a receiver while salt remains.','Recover the remaining salt by controlled evaporation/crystallization. Each step uses a physical-property difference.'])
], [
('Which is homogeneous?',['Salt water with all salt dissolved','Sand in water','Oil and water layers'],0,'A solution has uniform composition at the scale considered.'),
('The III in iron(III) chloride specifies…',['three iron atoms','a +3 oxidation state for iron','three chloride molecules'],1,'In FeCl₃ each chloride is −1, requiring +3 on iron.'),
('The correct formula for calcium nitrate is…',['CaNO₃','Ca₂NO₃','Ca(NO₃)₂'],2,'Two nitrate ions balance one calcium ion; the nitrate group remains intact.')
], ('Build a neutral ionic formula','Let the positive ion have charge +a and the negative ion −b. Choose counts x and y satisfying ax − by = 0. Use the smallest positive integers; group intact polyatomic ions in parentheses when repeated.','Al³⁺ and O²⁻: 3x = 2y gives x = 2, y = 3 → Al₂O₃.','This writes an ionic empirical formula; molecular substances require their own atom counts.','matter-4')),
unit('mole','The mole','Connect particles to measurable amounts.','How can a balance count atoms?','n',[
lesson('Isotopes & relative atomic mass',114,
'''Isotopes are atoms of one element with the same proton number but different neutron numbers. Their masses differ. The periodic table’s atomic mass is a weighted average for a stated isotopic composition; it is not usually the mass number of one atom. A mass number counts protons plus neutrons and is an integer.

Convert each isotope’s percentage abundance into a fraction, multiply each fraction by its isotopic mass, and add. The fractions must total one. The average should lie between the isotope masses and closer to the more abundant one. Relative atomic mass is a dimensionless ratio to one twelfth of a carbon-12 atom’s mass; a single atom’s mass may instead be expressed in u. Use the table’s precision consistently in molar-mass calculations.''',
'Average atomic mass = Σ(fractional abundance × isotopic mass)',
'Use actual isotopic masses when provided. An isotope’s mass number is only an approximate mass in u.',
'''A weighted mean counts every atom’s contribution. Imagine 100 atoms: 75 of mass 35.0 u and 25 of mass 37.0 u. Their total mass is 3550 u; dividing by 100 atoms gives 35.5 u per atom. Algebraically, f m₁ + (1 − f)m₂ = m_average can be solved for an unknown abundance. This equation works because the abundances account for all isotopes included in the model.''',
'Can an element’s average atomic mass be a noninteger? Yes; the weighted average need not equal the mass of any one atom.'),
lesson('Avogadro’s constant, molar mass & particles',121,
'''One mole contains exactly 6.02214076 × 10²³ specified entities. Name the entity: atoms of He, molecules of O₂, ions of Na⁺, or formula units of NaCl. Avogadro’s constant converts between entity count N and amount n. Molar mass M is mass per mole, found by summing atomic contributions in the formula.

Use m/M to convert mass to moles, then nNₐ to count entities. A formula subscript adds another counting step: one mole of CO₂ molecules contains one mole of carbon atoms and two moles of oxygen atoms. Ionic solids contain formula units, not discrete NaCl molecules. For hydrates, include the waters in the formula before summing mass. Using 6.022 × 10²³ in class is a rounded working value, not a redefinition of the constant.''',
'n = m/M; N = nNₐ; Nₐ = 6.02214076 × 10²³ mol⁻¹',
'The molar mass of O₂ is about 32.00 g mol⁻¹. Do not use the atomic molar mass 16.00 g mol⁻¹ for oxygen molecules.',
'''A mole is a counting unit, like a dozen, with a size chosen for atomic-scale entities. Derive n = m/M from the definition M = m/n, then check the units: g divided by g mol⁻¹ gives mol. Next, mol times entities mol⁻¹ gives entities. Keeping each conversion on a separate line makes it harder to confuse the number of molecules with the total number of atoms. Numerical molar masses use the periodic table; the exact mole count does not make those measured masses exact.''',
'One mole of H₂O contains how many moles of atoms in total? Three: two H plus one O per molecule.'),
lesson('Gas volume: STP, molar volume & conditions',138,
'''For an ideal gas, pressure, volume, amount, and absolute temperature satisfy PV = nRT. At fixed temperature and pressure, volume is proportional to moles, so different ideal gases have the same molar volume. The course worksheets use the common school STP convention of 0 °C and 1 atm, giving about 22.4 L mol⁻¹.

State the convention. At 0 °C and 100 kPa the ideal molar volume is about 22.7 L mol⁻¹ instead. At other conditions, calculate RT/P or use the full ideal-gas law. Match R to pressure and volume units: 8.314 kPa L mol⁻¹ K⁻¹ works with kPa and L. Convert Celsius to kelvin. The ideal approximation becomes less reliable at high pressures and near condensation.''',
'PV = nRT; Vₘ = V/n = RT/P; at 273.15 K and 1 atm, Vₘ ≈ 22.4 L mol⁻¹',
'22.4 L mol⁻¹ is a gas-volume conversion at specified conditions. It is not a liquid or solid molar volume.',
'''Dividing PV = nRT by nP yields V/n = RT/P. This shows explicitly why one universal gas molar volume needs fixed T and P. The combined gas law P₁V₁/T₁ = P₂V₂/T₂ follows only when the same gas amount is retained. For a reaction, balance the equation first: gas volume ratios equal coefficient ratios when all compared gas volumes are at the same temperature and pressure.''',
'At the same T and P, does 2 mol of He occupy twice the volume of 1 mol of O₂ in the ideal model? Yes.'),
lesson('Percent composition & empirical formulas',148,
'''Mass percent tells what fraction of the sample’s mass belongs to an element. From a formula, multiply each element’s atomic molar mass by its subscript, divide by the compound’s total molar mass, and multiply by 100%. Percentages should sum to about 100%, allowing rounding.

To determine an empirical formula, convert each element’s mass to moles, divide every mole amount by the smallest, and convert the ratios to small whole numbers. For percent data, choose a convenient 100 g sample. A ratio near 1.5 needs multiplication of every ratio by 2; near 1.333 needs ×3. The empirical formula is the simplest atom ratio; the molecular formula may be a whole-number multiple. Use measured precision to decide whether a ratio is plausibly close to an integer.''',
'% element = (mass of element in 1 mol compound / molar mass compound) × 100%',
'Atom ratios come from moles, not directly from mass percentages. Do not round 1.50 to 2.',
'''Mass is proportional to both atom count and atomic mass. Dividing by each atomic molar mass removes that mass weighting, leaving relative numbers of atoms. Dividing by the smallest mole amount normalizes the ratio without changing it. For 40.0% C, 6.71% H, and 53.3% O, a 100 g model gives approximately 3.33:6.66:3.33 mol, reducing to 1:2:1 and CH₂O. An empirical formula is composition information; it does not determine bonding or molecular shape.''',
'Why can CH₂O and C₆H₁₂O₆ have the same percent composition? The latter is six times the empirical unit, so all mass fractions are unchanged.'),
lesson('Molecular formulas, combustion & hydrates',148,
'''A molecular molar mass fixes the multiple of the empirical formula: divide the molecular molar mass by the empirical-formula molar mass and multiply every subscript by that integer. If the factor is nowhere near an integer within uncertainty, check the composition data and assumptions.

In complete combustion of a compound containing C and H, each mole of CO₂ records one mole of carbon and each mole of H₂O records two moles of hydrogen. If the original compound contains only C, H, and O, find its oxygen mass by subtracting the recovered C and H masses from the original sample mass. For a hydrate, use the loss of water on heating and the moles of remaining anhydrous salt to find the water-to-salt ratio.''',
'k = M_molecular/M_empirical; n(C) = n(CO₂); n(H) = 2n(H₂O)',
'Combustion products contain oxygen from the O₂ supply too. Do not assign all product oxygen to the original sample.',
'''Both methods are conservation arguments. Combustion tracks C and H into products; hydrate heating tracks mass into water vapour and residual salt. For a hydrate, n(H₂O) = mass lost/18.02 g mol⁻¹ and n(salt) = dry mass/M(salt). Their ratio is the hydrate number. The interpretation assumes water is the only lost material, the salt does not decompose, and heating reaches a suitable constant mass without reabsorbing moisture.''',
'An empirical formula is CH₂O, about 30.03 g mol⁻¹, and molecular mass is about 180.18 g mol⁻¹. The multiplier is six: C₆H₁₂O₆.'),
lesson('Molar concentration & preparing solutions',157,
'''Molar concentration c is solute amount divided by final solution volume. With c in mol L⁻¹, use V in litres. To prepare a solution from a solid, calculate n = cV and m = nM; dissolve the measured solute in less than the final volume, transfer quantitatively to a volumetric flask, and dilute to the calibration mark using the assigned procedure. Mix thoroughly.

A 0.100 M CaCl₂ solution has 0.100 mol of CaCl₂ formula units introduced per litre. If fully dissolved and dissociated, it gives 0.100 M Ca²⁺ and 0.200 M Cl⁻. The analytical solute concentration and the concentrations of individual species are related but not identical. Concentration is an intensive ratio; amount in moles depends on how much solution is taken.''',
'c = n/V; n = cV; m = cVM (V in L for c in mol L⁻¹)',
'Final solution volume includes solute and solvent. “Dissolve in 250 mL water” does not guarantee a 250 mL solution.',
'''The formula comes directly from the definition of a ratio: cV restores the total amount. In solution stoichiometry, cV supplies the reactant’s moles just as m/M does for a solid. Both routes meet at the same mole-ratio step. When two solutions mix, both solutes and volumes must be accounted for; one concentration cannot simply be copied into the final mixture.''',
'How many moles are in 25.0 mL of 0.200 M NaCl? 0.200 mol L⁻¹ × 0.0250 L = 0.00500 mol.')
], [
('Count atoms from mass','How many oxygen atoms are in 8.80 g of CO₂? Use M(CO₂) = 44.01 g mol⁻¹.', ['n(CO₂) = 8.80/44.01 = 0.19995 mol.','n(O atoms) = 2 × 0.19995 = 0.39991 mol.','N(O atoms) = 0.39991 × 6.02214076 × 10²³ = 2.41 × 10²³ atoms.']),
('Find a molecular formula','A compound is 40.0% C, 6.71% H, and 53.3% O by mass; its molar mass is 180.2 g mol⁻¹.', ['Take 100 g: n(C) = 40.0/12.01, n(H) = 6.71/1.008, n(O) = 53.3/16.00.','Divide by the smallest: approximately 1:2:1, giving CH₂O.','M(CH₂O) = 30.03 g mol⁻¹; 180.2/30.03 ≈ 6. Molecular formula: C₆H₁₂O₆.'])
], [
('One mole of CO₂ contains…',['one mole of oxygen atoms','two moles of oxygen atoms','three moles of oxygen molecules'],1,'Each CO₂ molecule has two oxygen atoms.'),
('Use 22.4 L mol⁻¹ when…',['any substance is measured','a gas is at the stated school STP conditions','water is at room temperature'],1,'Molar gas volume depends on temperature and pressure.'),
('0.100 mol in a final 500.0 mL solution gives…',['0.200 M','0.0500 M','50.0 M'],0,'Convert 500.0 mL to 0.5000 L, then divide n by V.')
], ('The mole is the conversion hub','Definitions give M = m/n, Nₐ = N/n, c = n/V, and Vₘ = V_gas/n. Rearrange to n = m/M = N/Nₐ = cV = V_gas/Vₘ. Pick the branch matching the known measurement.','5.85 g NaCl ÷ 58.44 g mol⁻¹ ≈ 0.100 mol; dissolving to 0.500 L gives c ≈ 0.200 M.','Specify entities and gas conditions. V in concentration means solution volume; V_gas means gas volume.','mole-2')),
unit('reactions','Chemical changes','Predict products. Balance atoms. Calculate amounts.','Which reactant determines how much product can form?','→',[
lesson('Writing & balancing chemical equations',168,
'''A chemical equation names reactants and products and states their reacting ratio. Write correct formulas first, include physical states when known, and adjust coefficients until every element has equal atom counts on both sides. Use the smallest whole-number coefficients unless a thermochemical convention calls for another basis. Parentheses belong to a formula; coefficients multiply the entire formula.

List the atom counts rather than relying on appearance. Balance elements occurring in fewer places first, and often leave H and O until later for combustion. A polyatomic group that survives intact can be counted as a unit. Molecular and ionic equations must conserve total electric charge as well as atoms. Remember the common diatomic elemental forms H₂, N₂, O₂, F₂, Cl₂, Br₂, and I₂.''',
'2Al(s) + 3Cl₂(g) → 2AlCl₃(s)',
'Never change a formula subscript to balance an equation. That changes the substance.',
'''A coefficient says how many formula units participate together; it does not change their internal composition. Two H₂O molecules have four H atoms and two O atoms; one H₂O₂ molecule has two H and two O and is a different substance. Conservation supplies linear constraints on coefficients. Balancing checks consistency of a proposed reaction, but a balanced equation alone does not prove the reaction occurs under the stated conditions.''',
'Balance propane combustion. C₃H₈ + 5O₂ → 3CO₂ + 4H₂O.'),
lesson('Predicting synthesis, decomposition & combustion',179,
'''Synthesis combines reactants into fewer products, such as Mg + O₂ forming MgO. Decomposition breaks one reactant into multiple products, such as a suitable metal carbonate forming a metal oxide and CO₂ on heating. Learn the specific decomposition patterns assigned in class; formulas and conditions decide which pattern applies.

Complete combustion of a hydrocarbon in sufficient oxygen produces CO₂ and H₂O. Incomplete combustion may produce CO or carbon as well. For synthesis from elements, use ionic charges or known molecular composition to write the product before balancing. Metal oxides and nonmetal oxides can show different acid–base behaviour, but broad classifications have exceptions. Reactions involving peroxides, chlorates, hydroxides, or carbonates require the correct specified product pattern.''',
'CaCO₃(s) → CaO(s) + CO₂(g) | CH₄(g) + 2O₂(g) → CO₂(g) + 2H₂O',
'A reaction category is a pattern, not proof of products. Apply known chemistry and the stated conditions.',
'''The product-prediction handout asks you to combine classification with formula writing. For a metal–oxygen synthesis, first decide the metal’s relevant charge and the oxide ion charge; then neutralize the formula and balance. A carbonate decomposition is conveniently understood as loss of CO₂ from an appropriate carbonate. Hydrocarbon combustion uses conservation of C, then H, then O. Sulfur-containing or nitrogen-containing fuels need additional product information beyond the simple C/H rule.''',
'Is 2KClO₃ → 2KCl + 3O₂ synthesis or decomposition? Decomposition: one reactant substance gives two product substances.'),
lesson('Single replacement, double replacement & net ionic equations',179,
'''In single replacement, one element displaces another from a compound if the activity pattern and conditions support it. Use the class activity series for metals and the halogen trend for halogen displacement. A less reactive metal does not automatically displace a more reactive one. Predict formulas before balancing.

In double replacement, exchange the cation–anion partners, then ask whether there is a driving change: precipitate, gas, or weakly ionized product such as water. Use the assigned solubility table. For a net ionic equation, split soluble strong electrolytes into ions, keep solids, gases, liquids, and weak electrolytes intact, cancel identical spectator ions, then check atoms and charge. Acid plus carbonate commonly produces CO₂ and H₂O because carbonic acid decomposes.''',
'Ag⁺(aq) + Cl⁻(aq) → AgCl(s) | CO₃²⁻(aq) + 2H⁺(aq) → CO₂(g) + H₂O(l)',
'Swapping ions does not guarantee a net reaction. If all species remain unchanged aqueous ions, write no net reaction.',
'''A molecular equation can hide the actual changing species. AgNO₃(aq) + NaCl(aq) forms AgCl(s) while Na⁺ and NO₃⁻ remain dissolved. Removing spectators does not remove the need for charge balance: +1 and −1 combine to a neutral solid. Solubility rules are empirical guides with exceptions; they should be consulted rather than replaced by “all salts dissolve.” In aqueous single replacement, water can compete as a reactant, so classroom prediction patterns need their stated limits.''',
'Why are Na⁺ and NO₃⁻ spectators in the silver chloride example? Their dissolved chemical forms are unchanged on both sides.'),
lesson('Redox: oxidation numbers & electron transfer',193,
'''Oxidation is loss of electrons and reduction is gain. They occur together: one species supplies the electrons another receives. The reducing agent is oxidized; the oxidizing agent is reduced. Oxidation numbers are bookkeeping values that help track electron transfer, including reactions involving covalent compounds.

An element in its free form has oxidation number zero. A monatomic ion’s value equals its charge. Values add to the total charge of the species. Oxygen is usually −2, except in peroxides and other special compounds; hydrogen is usually +1, except in metal hydrides. An increase indicates oxidation; a decrease indicates reduction. Find the changing elements and show the electron counts rather than assuming every reaction is redox.''',
'Zn → Zn²⁺ + 2e⁻ | Cu²⁺ + 2e⁻ → Cu | Zn + Cu²⁺ → Zn²⁺ + Cu',
'Oxidation numbers in a molecule are formal assignments; they are not necessarily actual ionic charges on atoms.',
'''Assign bonding electrons to the more electronegative atom for the formal oxidation-state model. This lets the same conservation logic cover ionic and covalent reactions. In CO₂, O is −2 and C must be +4; in CH₄, H is +1 and C is −4. Complete methane combustion raises carbon from −4 to +4 and lowers oxygen from 0 to −2. Acid–base neutralization can happen with no oxidation-state changes, so it need not be redox.''',
'In Zn + Cu²⁺ → Zn²⁺ + Cu, which is the oxidizing agent? Cu²⁺, because it accepts electrons and is reduced.'),
lesson('Reaction energy, thermochemical equations & calorimetry',204,
'''An exothermic reaction transfers heat to the surroundings; an endothermic reaction absorbs it. At constant pressure under the usual school conditions, these correspond to negative and positive reaction enthalpy changes. Choose the reacting system before interpreting a temperature rise: a warmer surrounding solution usually means the reaction released energy.

Thermochemical equations attach an energy to the equation as written. Reversing the equation reverses the sign; multiplying all coefficients multiplies the energy. For a stated molar enthalpy, name the substance or reaction basis. In a simple insulated calorimeter, estimate heat gained by the solution as mcΔT, then take the opposite sign for the reacting system. Include the calorimeter’s heat capacity when supplied and keep J versus kJ consistent.''',
'q_solution = mcΔT; q_reaction ≈ −q_solution; q = nΔH_molar',
'Breaking bonds absorbs energy; forming bonds releases it. An exothermic reaction releases more in bond formation than it requires overall.',
'''Heat is transfer, while enthalpy is a state property. The shortcut q_reaction = −mcΔT assumes the solution accounts for the energy exchange and losses are negligible. If the cup absorbs energy too, add C_calΔT before changing sign. An energy profile’s endpoint difference describes reaction energy; its peak describes a barrier. A catalyst changes the path and barrier while leaving the same initial and final state enthalpies unchanged.''',
'A solution warms by 5.0 °C during reaction. Is the reaction endothermic? Usually no in an insulated setup: the reaction supplied heat to the solution.'),
lesson('Stoichiometry: mass, gas & solution pathways',213,
'''Start every stoichiometry problem with a balanced equation. Convert the given measurement to moles using mass/molar mass, concentration × solution volume, gas volume/molar gas volume at specified conditions, or PV/RT. Multiply by the required coefficient ratio to obtain moles of the target substance, then convert to the requested mass, volume, or concentration.

For Cu + 2AgNO₃ → Cu(NO₃)₂ + 2Ag, two moles of silver nitrate react with one mole of copper. The coefficients relate moles or particle counts, not gram amounts. Read whether the problem gives an available amount or an amount that actually reacts. In solution reactions use the solute’s moles, not the mass of the whole solution. If multiple reactants have specified amounts, a limiting-reactant check is necessary.''',
'm_A/M_A → n_A → n_A(b/a) = n_B → m_B = n_BM_B',
'A balanced coefficient ratio is not a mass ratio. Convert through moles.',
'''For aA + bB → cC, one reaction advance consumes a mol A for each c mol C formed. Thus n(C) = n(A)c/a if A is fully consumed and enough B is present. This is conservation expressed in batch units. The same middle step connects all the November 8 question types: solids supply m/M, solutions supply cV, and gases supply V/Vₘ. Writing units on each arrow exposes a reversed ratio immediately.''',
'For 2KClO₃ → 2KCl + 3O₂, 4.00 mol KClO₃ can form 6.00 mol O₂ with complete conversion.'),
lesson('Limiting reactants, excess, purity & percentage yield',226,
'''Convert every available reactant to moles, divide each by its coefficient, and compare. The smallest n/coefficient determines the maximum reaction extent and is the limiting reactant. Calculate product from that extent. Find excess remaining by subtracting the amount consumed from the initial amount, using the balanced ratio.

Theoretical yield assumes complete conversion of the limiting reactant into the stated product. Percentage yield compares measured actual product with that theoretical amount. Purity is a different ratio: if only 60.0% of a sample is reactive material, use 0.600 times its mass before doing stoichiometry. In a reverse yield problem, required theoretical production equals desired actual production divided by the fractional yield; then work backward to the needed reactant.''',
'ξ_max = min(nᵢ/νᵢ); % yield = actual/theoretical × 100%; m_pure = fraction_pure × m_sample',
'A yield above 100% usually signals wet or impure product, a measurement issue, or a wrong model. It is not evidence that atoms were created.',
'''The limiting test compares complete “reaction batches,” not raw masses or raw mole amounts. In N₂ + 3H₂ → 2NH₃, 2 mol N₂ permits 2 mol reaction progress but 3 mol H₂ permits only 1 mol. H₂ therefore limits formation to 2 mol NH₃, leaving 1 mol N₂. Purity modifies the initial usable inventory; percentage yield modifies how much product is recovered. Apply them at different stages.''',
'For a reaction needing 1 mol N₂ per 3 mol H₂, do equal initial moles mean neither is limiting? No. H₂ is limiting.')
], [
('A solution stoichiometry chain','What mass of Cu reacts with 100.0 mL of 0.200 M AgNO₃? Use Cu + 2AgNO₃ → Cu(NO₃)₂ + 2Ag and M(Cu) = 63.55 g mol⁻¹.', ['n(AgNO₃) = 0.200 × 0.1000 = 0.0200 mol.','n(Cu) = 0.0200 × 1/2 = 0.0100 mol.','m(Cu) = 0.0100 × 63.55 = 0.636 g, assuming complete reaction.']),
('Limit, then apply yield','2.00 mol N₂ and 3.00 mol H₂ react by N₂ + 3H₂ → 2NH₃. What is the theoretical mass of NH₃, and the actual mass at 80.0% yield? Use 17.03 g mol⁻¹.', ['Compare n/ν: N₂ gives 2.00; H₂ gives 1.00. H₂ limits the reaction.','Theoretical n(NH₃) = 2.00 mol, so theoretical mass = 34.1 g. N₂ remaining = 1.00 mol.','Actual mass = 0.800 × 34.06 = 27.2 g.'])
], [
('To balance an equation, change…',['subscripts','coefficients','element symbols'],1,'Coefficients change amounts while preserving each substance’s identity.'),
('In 2H₂ + O₂ → 2H₂O, 1 mol O₂ can form…',['1 mol H₂O','2 mol H₂O','4 mol H₂O'],1,'The balanced mole ratio H₂O:O₂ is 2:1, provided enough H₂ is present.'),
('A 12.0 g actual yield from a 15.0 g theoretical yield is…',['125%','3.00%','80.0%'],2,'Percentage yield = 12.0/15.0 × 100%.')
], ('One reaction progress connects all amounts','For aA + bB → cC, define ξ so that n(A) consumed = aξ and n(C) formed = cξ. Then ξ = n(A)/a, so n(C) = n(A)c/a. For several available reactants, ξ cannot exceed any nᵢ/νᵢ.','For 2H₂ + O₂ → 2H₂O with 5.00 mol H₂ and 2.00 mol O₂: ξ_max = min(2.50,2.00) = 2.00 mol; water = 4.00 mol and H₂ remaining = 1.00 mol.','Assume the stated reaction goes to completion with no competing consumption; theoretical yield is an upper bound under that model.','reactions-7')),
]
UNITS += [
unit('atoms','Investigating atoms','Use experimental evidence to build a model.','Why does an excited gas emit only certain colours?','e⁻',[
lesson('Atomic models: Dalton to Rutherford',240,
'''Dalton’s atomic theory connected chemical composition with atoms combining in simple ratios. Thomson’s cathode-ray work showed that atoms contain negatively charged electrons, so an atom could not remain an indivisible solid sphere. Rutherford’s scattering experiments showed that most alpha particles passed through thin foil while a small fraction deflected strongly: positive charge and most mass must be concentrated in a very small nucleus.

Later work established protons and neutrons in the nucleus. The modern atom contains a small, dense, positively charged nucleus and an extended electron distribution. Models are judged by the observations they explain and the predictions they make. A model can remain useful for one task after a more complete model replaces it for others.''',
'Atom: nucleus (protons + neutrons) surrounded by an electron probability distribution',
'The gold-foil experiment supports a concentrated nucleus. It does not establish literal planetary electron paths.',
'''A scattered positive alpha particle experiences electric repulsion near concentrated positive charge. If positive charge were spread throughout the atom, large sudden deflections would be much less likely. The fact that most particles passed through constrains how small the scattering region is relative to the atom. Nuclear stability involves the strong nuclear interaction competing with proton–proton electrical repulsion; neutrons do not act as a simple electrostatic glue.''',
'Which finding challenged Thomson’s diffuse-positive-charge model? The rare large-angle deflections of alpha particles.'),
lesson('Subatomic particles, nuclide symbols & ions',240,
'''Atomic number Z counts protons and identifies the element. Mass number A counts protons plus neutrons in a specific isotope, so neutrons = A − Z. A neutral atom has Z electrons. A positive ion has lost electrons; a negative ion has gained electrons. Ion formation normally changes electron number without changing the nucleus.

Write a nuclide using the mass number at upper left, atomic number at lower left, and ion charge at upper right. For ²³Na⁺, Z = 11, A = 23, so there are 11 protons, 12 neutrons, and 10 electrons. Use an explicitly specified isotope to count neutrons. A periodic-table average atomic mass does not uniquely specify the isotope of a particular atom.''',
'p = Z; neutrons = A − Z; electrons = Z − q (q is signed ion charge)',
'Do not round a periodic-table average and present it as a uniquely known mass number unless the problem explicitly asks for that approximation.',
'''Charge in elementary-charge units is q = number of protons − number of electrons. Rearranging gives e = Z − q. This handles both signs: O²⁻ has 8 − (−2) = 10 electrons, while Al³⁺ has 13 − 3 = 10. Species with the same electron count are isoelectronic, but different nuclear charges give different sizes and energies. An element’s identity follows its proton count, so adding a neutron makes an isotope; adding an electron makes an ion.''',
'How many particles are in ³⁵Cl⁻? 17 protons, 18 neutrons, and 18 electrons.'),
lesson('Waves, photons, spectra & the Bohr model',256,
'''Wavelength λ measures the distance between repeating wave positions; frequency ν counts cycles per second; amplitude measures the size of the oscillation. For light in vacuum, c = λν. Shorter wavelength therefore means higher frequency. Photon energy is proportional to frequency, so shorter-wavelength photons carry greater energy.

In the Bohr model of hydrogen, electrons have discrete allowed energies. Absorption raises the atom’s energy by an allowed amount; emission releases a photon whose energy matches a downward energy difference. These discrete differences explain a line spectrum rather than every possible wavelength. White light can show a continuous spectrum, while different elements show characteristic emission patterns. The Bohr model works especially well for one-electron species, and needs replacement for detailed many-electron behaviour.''',
'c = λν; E_photon = hν = hc/λ; |ΔE_atom| = E_photon',
'Amplitude is not frequency. Greater light intensity need not mean greater energy per photon when the frequency stays fixed.',
'''A spectral line is an energy difference, not the energy of a single electron level measured from an arbitrary zero. For emission, ΔE_atom is negative while emitted photon energy is positive. If λ = 500 nm, convert to 5.00 × 10⁻⁷ m: E ≈ 3.97 × 10⁻¹⁹ J per photon. Multiplying by Nₐ gives energy per mole of photons. In a wave-on-a-string activity, changing frequency at fixed wave speed changes wavelength; changing amplitude is a separate control.''',
'Which photon carries more energy, violet or red? Violet, because its wavelength is shorter and frequency higher.'),
lesson('Orbitals, quantum numbers & electron capacity',267,
'''An orbital describes a quantum state and its electron probability distribution, not a track followed by a tiny planet. The principal quantum number n relates to shell and size; the angular quantum number ℓ identifies subshell type; mℓ distinguishes orbitals within a subshell; electron spin has two allowed projections.

For a given n, ℓ can run from 0 to n − 1. The labels s, p, d, and f correspond to ℓ = 0, 1, 2, and 3. A subshell has 2ℓ + 1 orbitals, and each orbital holds at most two electrons with opposite spins. Thus s, p, d, and f hold 2, 6, 10, and 14 electrons. s probability distributions are spherical; p orbitals have two lobes separated by a nodal plane. The sign of a wavefunction lobe is not electric charge.''',
'n = 1,2,…; ℓ = 0,…,n−1; mℓ = −ℓ,…,+ℓ; mₛ = ±½',
'A p subshell contains three orbitals. One p orbital holds two electrons, not six.',
'''Counting states explains capacities: mℓ has 2ℓ + 1 distinct values and each supports two spin states. Summing capacities over all subshells in shell n gives 2n², a maximum shell capacity rather than the neutral-atom filling order. A stylized orbital drawing often shows a boundary enclosing a chosen probability, not a hard wall. Shape alone may identify s/p/d character; the principal number usually requires more information such as radial-node count or a label.''',
'Why is there no 1p subshell? At n = 1, the only allowed ℓ is 0, which is s.'),
lesson('Electron configurations, ions & exceptions',277,
'''Fill lower-energy states first in the usual Aufbau guide: 1s, 2s, 2p, 3s, 3p, 4s, 3d, 4p, 5s, 4d, 5p, 6s, 4f, 5d, 6p. Pauli exclusion permits at most two opposite-spin electrons per orbital. Hund’s rule fills equivalent-energy orbitals singly with parallel spins before pairing. Core notation replaces filled inner shells with the preceding noble-gas symbol.

Check that all superscripts sum to the species’ electron count. For transition-metal cations, remove the highest principal-shell s electrons before the d electrons: Fe is [Ar]3d⁶4s² and Fe²⁺ is [Ar]3d⁶. Cr and Cu are familiar neutral exceptions: [Ar]3d⁵4s¹ and [Ar]3d¹⁰4s¹. More exceptions exist; use a reliable configuration when the question supplies one.''',
'P: [Ne]3s²3p³ | Cu: [Ar]3d¹⁰4s¹ | Cu²⁺: [Ar]3d⁹',
'The filling guide for neutral atoms is not a rule to remove the most recently written electron first. Equal electron counts do not always imply equal configurations for transition ions.',
'''Orbital energies depend on occupation and nuclear charge. “4s fills before 3d” in a neutral-atom building sequence does not mean 4s stays lower for every ion. The November notes also use a course convention for valence electrons: highest-shell s/p plus electrons in incomplete d/f subshells. State that convention for transition metals; main-group valence counts are more straightforward. A diagram showing only d¹⁰ does not uniquely identify the whole species: Zn also has 4s², whereas Zn²⁺ does not.''',
'Write Cr³⁺ from neutral Cr = [Ar]3d⁵4s¹. Remove the 4s electron, then two 3d electrons: [Ar]3d³.')
], [
('Count an ion’s particles','For ⁵⁶Fe³⁺, determine protons, neutrons, electrons, and core electron configuration. Z(Fe) = 26.', ['Protons = 26; neutrons = 56 − 26 = 30.','Electrons = 26 − 3 = 23.','Neutral Fe is [Ar]3d⁶4s². Remove two 4s and one 3d electron: [Ar]3d⁵.']),
('Convert a wavelength to energy','Find the energy per photon of 486 nm light. Use c = 2.998 × 10⁸ m s⁻¹ and h = 6.626 × 10⁻³⁴ J s.', ['λ = 486 × 10⁻⁹ m = 4.86 × 10⁻⁷ m.','ν = c/λ = 6.17 × 10¹⁴ s⁻¹.','E = hc/λ = 4.09 × 10⁻¹⁹ J per photon. A mole of these photons carries about 246 kJ.'])
], [
('In an isotope pair, what remains the same?',['Proton number','Neutron number','Mass number'],0,'Same proton number means the same element; isotopes differ in neutron number.'),
('How many electrons can a d subshell hold?',['2','6','10'],2,'Five d orbitals each hold at most two electrons.'),
('To form Fe²⁺ from Fe, remove…',['two 3d electrons first','two 4s electrons first','two core 3p electrons'],1,'The outer 4s electrons are removed before 3d for this transition-metal cation.')
], ('Photon energy from two definitions','Wave speed gives c = λν, so ν = c/λ. Planck’s relation E = hν then gives E = hc/λ. For emitted light, this positive photon energy equals the magnitude of the atom’s downward energy change.','At λ = 600 nm, E ≈ 3.31 × 10⁻¹⁹ J per photon. Halving λ doubles E.','Use λ in metres with SI constants. The vacuum expression is the school approximation for light measured in air.','atoms-3')),
unit('bonding','Relationships & bonding','Explain periodic patterns and molecular behaviour.','Why is water polar but carbon dioxide nonpolar?','⌁',[
lesson('The periodic table, families & valence patterns',292,
'''Mendeleev organized elements using repeating chemical properties and atomic-mass patterns, leaving gaps that supported predictions. The modern periodic table is arranged by atomic number. Rows are periods; columns are groups. Main-group members in a group have similar outer-electron configurations, helping explain related chemistry.

Group 1 has a common ns¹ valence pattern and commonly forms +1 ions; group 2 has ns² and commonly forms +2. Group 17 has ns²np⁵ and commonly forms −1; group 18 has a filled outer shell, with helium’s 1s² as the first-shell case. The s, p, d, and f blocks correspond to filling subshell types. Metals tend to conduct and are often malleable; nonmetal solids are often brittle; metalloids show mixed behaviour. These are trends with exceptions, not complete definitions.''',
's block: 2 columns | p: 6 | d: 10 | f: 14',
'Groups share recurring valence patterns, not the same principal shell number. Hydrogen’s chemistry is not captured by treating it as an ordinary alkali metal.',
'''The block widths follow orbital capacities, connecting the table’s shape to quantum states. Across a main-group period, the highest-shell s/p occupancy changes in a repeated sequence; down a group, the principal shell number rises while that occupancy pattern recurs. The periodic-table investigation also compares density. Since density depends on both atomic mass and solid packing volume, it has less universal trends than radius or first ionization energy; use the actual data for a density prediction.''',
'Why do Li and Na show related chemistry? Both have a common outer ns¹ pattern, though in different principal shells.'),
lesson('Atomic radius, ion size & ionization-energy exceptions',305,
'''Across a main-group period, atomic radius generally decreases as increasing nuclear charge pulls the electrons in the same main shell inward. Down a group, added shells and shielding generally increase radius. A cation is typically smaller than its parent atom; an anion larger. In an isoelectronic series, greater nuclear charge generally means smaller radius.

First ionization energy is the energy required to remove an electron from a gaseous atom. It generally increases across a period and decreases down a group, but subshell energies and electron pairing create important exceptions. Mg has a higher first ionization energy than Al because Al loses a higher-energy 3p electron. N has a higher first ionization energy than O because removing a paired 2p electron from O reduces pairing repulsion. Electronegativity describes attraction for shared electrons in a bond and generally increases toward the upper right.''',
'X(g) → X⁺(g) + e⁻ | Isoelectronic size: O²⁻ > F⁻ > Na⁺ > Mg²⁺',
'“More protons” alone is incomplete: compare shells, shielding, subshells, and electron pairing too.',
'''Effective nuclear attraction combines actual nuclear charge with electron screening. Across a period, added same-shell electrons do not fully screen each extra proton, so the outer distribution contracts. Down a group, a new principal shell changes the distance scale substantially. Successive ionization energies rise; a large jump after removing the valence electrons signals entry into a core shell. First ionization energy and electronegativity answer different questions: removing an electron versus attracting density in a bond.''',
'Which is smaller, Na⁺ or F⁻? Both have 10 electrons, but Na⁺ has more protons, so it is smaller.'),
lesson('Bond formation, potential energy & bond polarity',317,
'''When two atoms approach, electron–nucleus attractions can lower potential energy; at very short separation, repulsions raise it strongly. The potential-energy minimum marks an equilibrium separation. The force is zero there, although atoms can vibrate around that separation. Separating bonded atoms requires energy; forming a stable bond from separated atoms releases energy overall.

Covalent bonding shares electron density; ionic solids contain oppositely charged ions in an extended structure; metallic bonding involves mobile electrons in a metal structure. Unequal sharing produces a polar covalent bond with partial charges. Use the December handout’s approximate electronegativity-difference boundaries for its questions: below 0.4 nonpolar covalent, 0.4–1.7 polar covalent, above 1.7 ionic. These are course classification conventions within a continuum.''',
'ΔEN = |EN_A − EN_B|; F(r) = −dU/dr; at a stable minimum, dU/dr = 0',
'Ionic and covalent character vary continuously. A numerical cutoff is a classification guide, not an abrupt change in physical behaviour; HF is a molecular polar-covalent example despite exceeding 1.7 on the handout’s scale.',
'''At a separation greater than equilibrium on the attractive side, the force tends to pull atoms together; below equilibrium on the repulsive side, it tends to push them apart. Zero force at the minimum does not require zero speed: an oscillating pair can pass through equilibrium fastest. A well depth describes the energy needed to reach separated atoms from the minimum in that model. For the same atom pair, higher bond order generally means a shorter, stronger bond: compare C–C, C=C, and C≡C. Distinguish this well from a reaction activation barrier; they refer to different physical questions.''',
'At the minimum of a bond-energy curve, are all attractions absent? No. Attractive and repulsive contributions balance.'),
lesson('Lewis structures, formal charge & resonance',330,
'''Count total valence electrons, adding electrons for negative charge and subtracting for positive charge. Choose a plausible skeleton, connect atoms with single bonds, complete terminal octets (H needs two), and place remaining electrons on the centre. Form multiple bonds when needed, then recount every electron and check total charge.

Formal charge helps compare drawings: valence count minus nonbonding electrons minus half of bonding electrons. Resonance contributors have the same atom arrangement but different allowed electron placements. The real electron distribution is not a molecule jumping between drawings. Treat electron-deficient species such as BF₃, odd-electron radicals such as NO, and expanded-octet Lewis representations such as PCl₅ as exceptions to a universal octet recipe. Second-period C, N, O, and F do not expand their octets.''',
'Formal charge = valence electrons − nonbonding electrons − ½(bonding electrons)',
'The shortcut bonds = (octet electrons needed − available electrons)/2 applies only to suitable ordinary octet/duet structures, not every species.',
'''For NO₂⁻ the total is 5 + 2(6) + 1 = 18 electrons. A valid contributor has one N=O, one N–O⁻, and one N lone pair. Exchanging the two O positions gives another contributor; delocalization makes the two N–O bonds equivalent in the isolated ion. For SO₂, zero-formal-charge expanded-octet drawings are useful school bookkeeping. Modern hypervalent bonding is not explained simply by claiming that period-3 atoms use empty d orbitals to make extra bonds.''',
'How many valence electrons are in CO₃²⁻? 4 + 3(6) + 2 = 24.'),
lesson('VSEPR shapes & the molecular dipole',347,
'''Use the Lewis structure to count electron domains around the centre. A single, double, or triple bond each counts as one domain; a lone pair also counts as one. Electron-domain geometry spreads these regions apart. Molecular shape describes the positions of nuclei, so lone pairs affect the shape but are not named as atoms.

Two domains give linear geometry; three give trigonal planar; four give tetrahedral electron geometry. With four domains, CH₄ is tetrahedral, NH₃ is trigonal pyramidal, and H₂O is bent. Five and six domains give trigonal-bipyramidal and octahedral electron geometries. For molecular polarity, combine bond dipoles as vectors using the actual shape and surrounding atoms. Symmetry can cancel equal dipoles: CO₂ is nonpolar, while bent H₂O has a net dipole.''',
'CO₂: AX₂ linear, 180° | CH₄: AX₄, 109.5° | NH₃: AX₃E, ≈107° | H₂O: AX₂E₂, ≈104.5°',
'Polar bonds do not automatically produce a polar molecule. Lone pairs and different terminal atoms can prevent cancellation.',
'''VSEPR is a model for predicting geometry from local electron density. Lone pairs often repel bonding regions more strongly and compress bond angles in simple examples, but ideal angles are reference values rather than universal measured numbers. In CO₂, the two equal C=O dipoles point in opposite directions and sum to zero. In water, the angle prevents the two O–H dipoles from cancelling. A flat Lewis drawing gives connectivity; it is not a reliable three-dimensional geometry diagram.''',
'Why is CO₂ linear despite two double bonds? Each double bond is one domain, so there are two domains around carbon.'),
lesson('Intermolecular forces & water’s behaviour',347,
'''Intramolecular bonds hold atoms together within a molecular substance; intermolecular attractions act between molecules. All atoms and molecules have London dispersion forces arising from fluctuating electron distributions. Greater polarizability and effective surface contact can increase dispersion. Polar molecules also have dipole–dipole attractions.

Hydrogen bonding commonly involves H bonded to N, O, or F interacting with a suitable lone pair on another particle. Ion–dipole attractions connect dissolved ions with polar water molecules. These interactions help explain boiling points, viscosity, surface tension, and solubility. Water’s extensive hydrogen-bond network contributes to its relatively high boiling point and heat capacity; its open ice structure makes ordinary ice less dense than liquid water. Comparisons require molecular size and shape as well as named force types.''',
'Na⁺ attracts water’s Oδ⁻ end; Cl⁻ attracts water’s Hδ⁺ ends',
'Boiling water mainly separates molecules; it does not break each H₂O molecule into hydrogen and oxygen.',
'''A molecule with a hydrogen-bond donor still has dispersion and can have other electrostatic attractions. Do not replace all forces with the strongest named category. A large nonpolar molecule can have a higher boiling point than a smaller polar one because dispersion grows with polarizability. Water can hydrate ions by orienting its partial charges, but hydration must compete with the solid lattice and with water–water interactions, which is why not every ionic solid dissolves readily.''',
'Can ethanol hydrogen-bond with water? Yes: its O–H group can donate and its oxygen lone pairs can accept hydrogen bonds.')
], [
('Explain a periodic exception','Why is the first ionization energy of Al lower than Mg even though Al lies to the right?', ['Mg ends 3s²; Al ends 3s²3p¹.','Al’s removed electron is in 3p, which is higher in energy and less penetrating than 3s in this comparison.','This subshell effect overrides the simple across-period trend.']),
('From electron count to polarity','Predict the shape and polarity of NH₃.', ['Valence electrons: 5 + 3(1) = 8. Three N–H bonds use six; one lone pair remains on N.','Four electron domains give tetrahedral electron geometry, but the atom positions are trigonal pyramidal.','The N–H bond dipoles do not cancel: NH₃ is polar; its angle is about 107°.'])
], [
('Across a typical main-group period, radius generally…',['increases','decreases','has no relationship to nuclear attraction'],1,'Increasing effective nuclear attraction generally contracts the same-shell electron distribution.'),
('A double bond counts as how many VSEPR domains?',['One','Two','Four'],0,'A multiple bond is one region of electron density for domain counting.'),
('Which molecule has polar bonds but no net molecular dipole?',['H₂O','NH₃','CO₂'],2,'Equal C=O bond dipoles cancel in linear, symmetric CO₂.')
], ('Lewis structure → domains → shape → polarity','Conserve valence electrons to draw a Lewis structure. Count bonding regions plus lone pairs to predict electron geometry. Name the atomic arrangement, then add the bond-dipole vectors to decide molecular polarity.','H₂O: 8 electrons → two bonds plus two lone pairs on O → tetrahedral domains → bent atoms → nonzero dipole.','VSEPR is a geometry model, not a complete bonding theory. Use the actual terminal atoms and acknowledge resonance and exceptions.','bonding-5')),
]
UNITS += [
unit('solutions','Solution chemistry','Track dissolved particles and solution volumes.','What is conserved when a solution is diluted?','c',[
lesson('Solubility, saturation & temperature',370,
'''A solution is a homogeneous mixture of solute and solvent. Solubility states the maximum amount that dissolves in a specified amount of solvent or solution at a stated temperature under stated conditions. Read whether the units are g per 100 g water, g per litre solution, or mol per litre: these denominators are different.

An unsaturated solution can dissolve more under those conditions; a saturated solution is at the solubility limit; a supersaturated solution contains more dissolved solute than the stable equilibrium amount and can crystallize when disturbed or seeded. For a saturated solution in contact with solid, dissolving and crystallizing continue with equal rates. Many solids become more soluble as temperature rises, but exceptions exist. Gas solubility commonly decreases on warming and increases with the gas’s partial pressure in the simple dilute model.''',
'Solubility in mol L⁻¹ = solubility in g L⁻¹ / molar mass in g mol⁻¹',
'Saturated does not necessarily mean concentrated. A sparingly soluble compound can form a very dilute saturated solution.',
'''A solubility curve is a capacity map at different temperatures. If a salt dissolves to 40 g per 100 g water at one temperature but 25 g at a lower one, cooling that saturated sample can crystallize 15 g per 100 g water, assuming no solvent loss and the same solid form. Solubility and dissolution rate are different: stirring can accelerate reaching the limit without changing the equilibrium limit itself.''',
'Does grinding a salt necessarily raise its equilibrium solubility? No. It typically increases the rate of dissolving by exposing more area.'),
lesson('Like dissolves like: competing attractions',378,
'''Dissolving requires separating some solute–solute and solvent–solvent contacts while forming solute–solvent contacts. Polar solvents can interact favourably with polar molecules and ions; nonpolar solvents often dissolve nonpolar molecular substances. “Like dissolves like” summarizes common patterns, while the full outcome also depends on crystal stability, mixing effects, temperature, and composition.

Water hydrates Na⁺ with oxygen ends pointing toward the ion and Cl⁻ with hydrogen ends toward it. Ethanol can hydrogen-bond with water through its hydroxyl group; a longer hydrocarbon region can reduce water compatibility in related molecules. Oil and water form separate phases because their interaction balance does not favour extensive mixing. Immiscible liquids can still have small mutual solubilities.''',
'Dissolution: replace some solute–solute and solvent–solvent interactions with solute–solvent interactions',
'Water is not a universal solvent. Being ionic does not guarantee high water solubility.',
'''Use a particle sketch to test the phrase. Draw the solvent’s positive and negative regions, orient them around the solute, and ask what interactions must be overcome. A stable ionic lattice can resist dissolution even though water strongly attracts its ions. Dissolving a molecular solute such as sucrose can preserve molecules, whereas an ionic salt dissociates. This distinction explains why some concentrated solutions conduct poorly and others conduct well.''',
'Why does a hydroxyl group help an alcohol mix with water? It supports favourable hydrogen bonding with the surrounding water.'),
lesson('Dissociation, electrolytes & ion concentrations',389,
'''A dissolved electrolyte supplies mobile ions that carry current. A soluble ionic salt typically dissociates into its component ions; some molecular acids ionize by reacting with water. A nonelectrolyte such as sucrose can dissolve as neutral molecules without supplying many ions. Strong versus weak electrolyte describes the extent of ion production under specified conditions, not simply whether a solution is concentrated.

Write a balanced dissociation equation and use its coefficients to convert formal solute concentration to ion concentrations when dissociation is complete. For Al₂(SO₄)₃ at 0.0200 M, [Al³⁺] = 0.0400 M and [SO₄²⁻] = 0.0600 M. For conductivity, consider concentration, ion charges, mobility, and dissociation; counting ions alone cannot compare every real solution.''',
'CaCl₂(aq) → Ca²⁺(aq) + 2Cl⁻(aq); [Cl⁻] = 2c(CaCl₂)',
'An insoluble ionic solid supplies few ions to water. “Ionic” alone does not establish high solution conductivity.',
'''Charge conservation is an independent check. In 0.100 M CaCl₂, positive charge concentration is 2 × 0.100 and negative charge magnitude is 1 × 0.200, so they balance. The formal concentration tracks how much salt was introduced; brackets identify an actual dissolved species. At this level, assume complete dissociation for the specified soluble salts and ignore complex formation unless supplied by the problem.''',
'For 0.0300 M Na₃PO₄ with complete dissociation, [Na⁺] = 0.0900 M and [PO₄³⁻] = 0.0300 M.'),
lesson('Dilution, mixing & solution stoichiometry',389,
'''Diluting a solution adds solvent while conserving solute amount, provided no reaction or loss occurs. Equate n_before and n_after to obtain c₁V₁ = c₂V₂. Volumes can share any consistent unit in this equation because only their ratio matters. Use final solution volume, not just solvent volume added.

When combining solutions of the same nonreacting solute, add their moles and divide by the final volume. If a reaction occurs, calculate the initial moles of each reacting species, apply the balanced ratio and limiting-reactant logic, and divide remaining or produced moles by the final volume as required. For simple school problems, volumes are often assumed additive. An aliquot transfers only the fraction of total solute corresponding to the volume taken.''',
'c₁V₁ = c₂V₂; c_mix = (c₁V₁ + c₂V₂)/(V₁ + V₂) for additive, nonreacting solutions',
'Diluting to 100.0 mL is different from adding 100.0 mL of water. Averaging concentrations works only for equal mixed volumes without reaction.',
'''Derive rather than memorize: n = cV, and dilution leaves n unchanged, so c₁V₁ = c₂V₂. Mixing adds two inventories instead, giving n_total = c₁V₁ + c₂V₂. Precipitation changes the dissolved inventories; for Ag⁺ + Cl⁻ → AgCl(s), first remove the reacting amounts. The final concentration of any excess ion is its leftover moles divided by total solution volume, not its original concentration minus the other solution’s concentration.''',
'If 25.0 mL of 0.200 M stock is diluted to 100.0 mL, the final concentration is 0.0500 M.'),
lesson('Titrations & experimental technique',399,
'''A titration uses a known-concentration titrant to determine an unknown amount or concentration. The equivalence point is the stoichiometric match given by the balanced equation. The endpoint is the observed signal, such as an indicator colour change; good technique aims to make it close to equivalence. A standard solution has a reliably known concentration; standardization determines that concentration experimentally.

For aA + bB → products, at equivalence n(A)/a = n(B)/b. Use cV for each amount and solve. The common c_acidV_acid = c_baseV_base shortcut needs a 1:1 reaction ratio. Read the burette consistently, remove tip bubbles, swirl, and add slowly near the endpoint. Use concordant titres according to the class criterion and follow the assigned safety and waste procedure.''',
'At equivalence: c_AV_A/a = c_BV_B/b; titre = final burette reading − initial reading',
'Neutralization does not always use a 1:1 ratio. H₂SO₄ requires two moles of NaOH per mole for full neutralization.',
'''Suppose a monoprotic acid sample is titrated with NaOH. An overshot endpoint records too much NaOH and therefore overestimates acid moles if that extra delivery is treated as reaction demand. Water accidentally added to the titration flask changes concentration but not the acid moles already pipetted, so the ideal required titrant moles remain the same. A pipette diluted by residual water before taking the sample is a different error: it can reduce transferred acid moles.''',
'Why does adding a little pure water to the receiving flask not change the ideal titre? It changes volume but conserves the analyte amount.')
], [
('Dilute, then count ions','25.0 mL of 0.400 M CaCl₂ is diluted to 200.0 mL. Find final [Ca²⁺] and [Cl⁻].', ['Formal final c = 0.400 × 25.0/200.0 = 0.0500 M.','CaCl₂ → Ca²⁺ + 2Cl⁻, assuming complete dissociation.','[Ca²⁺] = 0.0500 M and [Cl⁻] = 0.100 M.']),
('Use the titration ratio','25.00 mL of H₂SO₄ requires 30.00 mL of 0.1000 M NaOH for full neutralization. Find the acid concentration.', ['H₂SO₄ + 2NaOH → Na₂SO₄ + 2H₂O.','n(NaOH) = 0.1000 × 0.03000 = 0.003000 mol; n(H₂SO₄) = 0.001500 mol.','c(H₂SO₄) = 0.001500/0.02500 = 0.06000 M.'])
], [
('During dilution without loss or reaction, what is conserved?',['Concentration','Solute amount','Solution volume'],1,'Solvent changes volume; the initial solute inventory is retained.'),
('0.100 M CaCl₂ gives [Cl⁻] of…',['0.0500 M','0.100 M','0.200 M'],2,'Each formula unit supplies two chloride ions under complete dissociation.'),
('At equivalence in H₂SO₄ + 2NaOH, n(NaOH)/n(H₂SO₄) is…',['1','2','0.5'],1,'The full-neutralization equation requires two base moles per acid mole.')
], ('Dilution is conservation of solute','Start with c = n/V. The same retained solute before and after gives n₁ = n₂. Substitute c₁V₁ = c₂V₂ and rearrange: c₂ = c₁V₁/V₂.','20.0 mL of 0.500 M stock diluted to 100.0 mL gives 0.100 M. Solute remains 0.0100 mol.','No solute loss or reaction. For mixing, add inventories first; for titration, include the coefficient ratio.','solutions-4')),
unit('organic','Organic chemistry','Read carbon structures and predict simple reactions.','How can the same formula describe different compounds?','C',[
lesson('Carbon bonding, hydrocarbons & structural formulas',408,
'''Carbon commonly makes four bonds, allowing chains, branches, rings, and multiple bonds. Hydrocarbons contain only C and H. Alkanes have only single C–C bonds; alkenes have C=C; alkynes have C≡C. Saturated acyclic hydrocarbons are alkanes; unsaturation can involve rings or multiple bonds, so inspect structure as well as formula.

A structural formula shows connectivity, a condensed formula groups atoms, and a skeletal formula omits carbon labels and most carbon-bound hydrogen labels. Every unlabeled line end or vertex represents carbon; add enough implicit H to complete the usual carbon valence. The acyclic alkane formula CₙH₂ₙ₊₂ applies to a neutral saturated open chain. One ring or one C=C reduces H by two relative to that formula; a triple bond reduces it by four.''',
'Acyclic alkane: CₙH₂ₙ₊₂ | one acyclic C=C: CₙH₂ₙ | one acyclic C≡C: CₙH₂ₙ₋₂',
'The formula CₙH₂ₙ does not uniquely identify an alkene; a saturated cycloalkane can share it.',
'''Count carbon valence at every position. In CH₃CH=CH₂, the middle carbon has one single bond to C, one double bond to C, and one bond to H: four bond units total. Skeletons encode the same count economically. Benzene’s aromatic bonding is delocalized and should not be treated as an ordinary isolated alkene for every reaction. Many carbon compounds are organic, but familiar carbon oxides and carbonates are conventionally treated as inorganic.''',
'How many carbons are in an unbranched zigzag with four line segments? Five: three interior vertices plus two ends.'),
lesson('Naming hydrocarbons & recognizing isomers',408,
'''Choose a suitable longest parent chain containing the relevant multiple bond or priority functional group. Number to give the important features the lowest appropriate locants, then name substituents and their positions. For a simple branched alkane, use the first point of difference between locant sets. List different substituent names alphabetically; ignore di-, tri-, and tetra- for this alphabetizing step.

Learn the first ten carbon roots: meth, eth, prop, but, pent, hex, hept, oct, non, dec. Use -ane, -ene, or -yne for the hydrocarbon bond type and give multiple-bond positions where necessary. Structural isomers share a molecular formula but have different connectivity: butane and 2-methylpropane both have C₄H₁₀. Rotation about an ordinary single bond changes conformation, not connectivity.''',
'CH₃CH(CH₃)CH₂CH₃ = 2-methylbutane | CH₂=CHCH₂CH₃ = but-1-ene',
'An apparent bend in a chain is not automatically a branch. Find the longest connected path before naming.',
'''Generate isomers systematically by changing the carbon skeleton, then check for duplicates using connectivity rather than the drawing’s orientation. C₅H₁₂ has pentane, 2-methylbutane, and 2,2-dimethylpropane. Reversing the page drawing of pentane does not create a fourth isomer. Restricted rotation at a C=C can also allow geometric isomers when each double-bond carbon has two different substituents; that is a different kind of isomerism from changing connectivity.''',
'Are butane and 2-methylpropane different formulas? Their molecular formula is the same, but their connectivity differs.'),
lesson('Functional groups: recognize, name & compare',423,
'''A functional group is a recurring atom arrangement associated with characteristic chemistry. Recognize alkyl halides (C–X), alcohols (R–OH), ethers (R–O–R), aldehydes (R–CHO), ketones (R–CO–R), carboxylic acids (R–COOH), esters (R–COO–R), amines, and amides. Here R represents a carbon-containing group; an aldehyde may have H in place of that group in methanal.

Alcohol names use -ol, aldehydes -al, ketones -one, and carboxylic acids -oic acid. Esters are named with the alcohol-derived alkyl group followed by the acid-derived -oate. Functional groups influence polarity and hydrogen bonding. An alcohol’s covalent hydroxyl group is not a free hydroxide ion. A molecule may contain more than one functional group; simple naming rules need expansion for multifunctional compounds.''',
'CH₃CH₂OH: ethanol | CH₃COCH₃: propanone | CH₃COOH: ethanoic acid | CH₃COOCH₃: methyl ethanoate',
'An ether has C–O–C; a ketone has C–C(=O)–C. They are not the same functional group.',
'''A carbonyl is C=O. Its location distinguishes aldehydes from ketones; attaching OH to the carbonyl carbon creates a carboxyl group. In an ester, the second oxygen connects the carbonyl group to a carbon group instead of to H. These local structures influence intermolecular attractions. Compare molecular size as well as functional group when predicting boiling point or water solubility; a long nonpolar chain can dominate the behaviour of a molecule with one polar group.''',
'Which class contains R–C(=O)–O–R′? An ester. R–O–R′ without the carbonyl is an ether.'),
lesson('Organic reactions, esterification & polymers',436,
'''Complete combustion of many C/H/O organic compounds produces CO₂ and H₂O in sufficient oxygen. Substitution replaces an atom or group, as in halogenation of an alkane under suitable initiation. Addition converts a multiple bond into more single bonds to incoming atoms; hydrogenation adds H₂ across C=C. Elimination removes a small molecule and forms a multiple bond under suitable conditions.

Esterification combines a carboxylic acid and alcohol to form an ester and water, usually with acid catalysis and appropriate heating; the reverse process is hydrolysis. Addition polymerization links alkene monomers by opening their C=C bonds into a chain. Condensation polymers connect functional monomers while eliminating small molecules in suitable reactions. Identify the changed bond or group and preserve atom balance. Conditions determine which of several possible reactions actually occurs.''',
'CH₂=CH₂ + H₂ → CH₃CH₃ | CH₃COOH + CH₃OH ⇌ CH₃COOCH₃ + H₂O | nCH₂=CH₂ → [–CH₂–CH₂–]ₙ',
'The repeat unit of an addition polymer contains the monomer’s atoms, but the C=C becomes C–C connections along the chain.',
'''Track the carbon skeleton before balancing H and O. Ethene addition retains its two-carbon framework; esterification joins an acid-derived acyl region to an alcohol-derived alkoxy region. A polymer’s properties depend on chain length, branching, and intermolecular packing as well as repeat-unit identity. More linear polyethylene chains can pack more efficiently than strongly branched ones, helping explain different densities. General organic reaction families describe patterns; catalysts, light, solvent, and temperature still matter.''',
'What type of reaction converts ethene to ethane using H₂ and a catalyst? Addition, specifically hydrogenation.')
], [
('Name and count a branched alkane','Name CH₃CH(CH₃)CH₂CH₃ and determine its molecular formula.', ['The longest chain has four carbon atoms: butane.','Number from the nearer branch; a methyl is at carbon 2: 2-methylbutane.','There are five C atoms and twelve H atoms: C₅H₁₂.']),
('Write an esterification','Write the reaction of ethanoic acid with ethanol and name the ester.', ['Identify CH₃COOH as the acid and CH₃CH₂OH as the alcohol.','CH₃COOH + CH₃CH₂OH ⇌ CH₃COOCH₂CH₃ + H₂O under suitable acid-catalysed conditions.','The ester is ethyl ethanoate: ethyl from ethanol, ethanoate from ethanoic acid.'])
], [
('The open-chain saturated hydrocarbon formula is…',['CₙH₂ₙ','CₙH₂ₙ₊₂','CₙHₙ'],1,'A neutral acyclic alkane has two more H than twice its carbon count.'),
('CH₃COCH₃ is a(n)…',['ether','alcohol','ketone'],2,'Its carbonyl carbon is attached to two carbon groups.'),
('Hydrogenation of an alkene is…',['addition','substitution','combustion'],0,'Hydrogen adds across C=C, giving more saturated bonding.')
], ('Derive the acyclic alkane formula','For n carbons in a connected open single-bonded chain, n − 1 C–C bonds consume 2(n − 1) of the 4n carbon bond positions. The remaining positions are filled by H: 4n − 2(n − 1) = 2n + 2.','For n = 5, H = 12: C₅H₁₂. Closing one ring uses two of those H positions, giving C₅H₁₀ for a saturated five-carbon ring.','Assume neutral carbon valence four, hydrogen valence one, and no heteroatoms, rings, or multiple bonds for the alkane result.','organic-1'))
]
# Every local course-note PDF is indexed, including worked-answer companions.
SOURCES = [
 ('Chem 11.pdf','Course outline · 2025/26',2,'Eight-unit course sequence; practical and reporting skills.',['skills','matter','mole','reactions','atoms','bonding','solutions','organic']),
 ('chem 9:19.pdf','September 19 · Foundations',13,'Scientific method (pp. 1–2, 4), chromatography (3), units and significant figures (5–7), matter and energy (8–11), acid/hydrate naming (12), separation (13).',['skills-2','skills-3','skills-4','matter-2','matter-3','matter-4','matter-5']),
 ('Chem11 11:8.pdf','November 8 · Chemical changes',4,'Reaction classification, redox, thermochemistry, limiting reactants, yield/purity (pp. 1–2), solution stoichiometry (3–4).',['reactions-2','reactions-4','reactions-5','reactions-6','reactions-7','solutions-5']),
 ('Chem11 11:14.pdf','November 14 · Investigating atoms',18,'Atomic history and particles (pp. 1–4), photons and models (5–6), configurations and ions (7–10), atomic-model and wave/spectra lab (11–16), reaction classification/stoichiometry lab (17–18).',['atoms-1','atoms-2','atoms-3','atoms-4','atoms-5','reactions-5','reactions-6']),
 ('chem11 11:22.pdf','November 22 · Naming flowchart',1,'Binary ionic, multivalent ionic, polyatomic ionic, and molecular naming, with valence diagrams.',['matter-4','matter-5','bonding-4']),
 ('chem11 11:29.pdf','November 29 · Configurations & patterns',8,'Configuration practice (pp. 1–2); periodic-table investigation, density, radii, ion size, and ionization energy (3–8).',['atoms-4','atoms-5','bonding-1','bonding-2']),
 ('Chem11-29.pdf','November 29 · Worked companion',21,'Worked configuration questions (pp. 1–8), periodic-table investigation and trend explanations (9–21).',['atoms-5','bonding-1','bonding-2']),
 ('chem11 12:5.pdf','December 5 · Trends & metal reactivity',4,'Atomic radius and ionization-energy exceptions (pp. 1–2), metal displacement and reactions with acids investigation (3–4).',['bonding-2','reactions-3','reactions-4']),
 ('12-12/Chem11 12:12.pdf','December 12 · Atomic review',2,'Isotope averages and abundances, model history, quantum numbers, orbital shapes, configurations, ions and valence electrons.',['mole-1','atoms-1','atoms-2','atoms-3','atoms-4','atoms-5']),
 ('12-12/chem1112:12.pdf','December 12 · Chemical bonding notes',14,'Bond energy and electronegativity (pp. 1–4), Lewis structures and exceptions (5–8), resonance and shapes (9–11), intermolecular forces (12), potential-energy investigation (13–14).',['bonding-3','bonding-4','bonding-5','bonding-6','solutions-2']),
 ('12-12/1212answer.pdf','December 12 · Bonding worked companion',41,'Worked bonding/Lewis examples (pp. 1–26), VSEPR and polarity (27–31), intermolecular forces and hydration (32–35), potential-energy investigation (36–41).',['bonding-3','bonding-4','bonding-5','bonding-6','solutions-2']),
 ('12-12/1212answer2.pdf','December 12 · Atomic worked companion',12,'Worked isotope, model, quantum-number, orbital, configuration, and valence review.',['mole-1','atoms-1','atoms-3','atoms-4','atoms-5']),
 ('ProductsPrediction.pdf','Product prediction · Practice & explanations',17,'Reaction patterns and activity series (pp. 1–12), oxidation states, exceptions, and agents (13–17).',['reactions-2','reactions-3','reactions-4']),
 ('labReportGuides.pdf','Laboratory report format',2,'Required report sections, observations, sample calculations, results, discussion, and conclusion.',['skills-1','skills-2']),
 ('SampleLabReport.pdf','Sample laboratory report',3,'Example of reporting the effect of temperature on the magnesium–acid reaction.',['skills-2','reactions-5'])
]
FORMULAS = [
 ('Density','ρ = m/V; m = ρV; V = m/ρ','Keep mass and volume units consistent.','skills-4'),
 ('Weighted atomic mass','m̄ = Σ fᵢmᵢ; Σ fᵢ = 1','Abundances are fractions, not percentages.','mole-1'),
 ('Mass, moles & particles','n = m/M; N = nNₐ','Name the counted entity; Nₐ = 6.02214076 × 10²³ mol⁻¹.','mole-2'),
 ('Gas quantities','PV = nRT; Vₘ = RT/P','Kelvin; R = 8.314 kPa L mol⁻¹ K⁻¹ for kPa and L.','mole-3'),
 ('Composition & molecular formula','% element = element mass/total mass × 100%; k = M_molecular/M_empirical','Convert element masses to moles before finding atom ratios.','mole-4'),
 ('Solution amount','c = n/V; n = cV; m = cVM','V in L when c is in mol L⁻¹; M here means molar mass.','mole-6'),
 ('Reaction mole ratio','n_B = n_A × ν_B/ν_A','Use coefficients from the balanced equation.','reactions-6'),
 ('Limiting reactant','ξ_max = min(nᵢ/νᵢ); n_product = ν_product ξ_max','Compare normalized mole amounts, not raw masses.','reactions-7'),
 ('Yield & purity','% yield = actual/theoretical × 100%; m_pure = f_pure m_sample','Apply purity to the usable reactant, yield to product recovery.','reactions-7'),
 ('Energy accounting','q = mcΔT; q_reaction ≈ −q_solution; q = nΔH_molar','No phase change for mcΔT; check losses and calorimeter heat capacity.','reactions-5'),
 ('Particles in an ion','p = Z; neutrons = A − Z; electrons = Z − q','A is isotope mass number; q is signed ion charge.','atoms-2'),
 ('Light & energy','c_light = λν; E = hν = hc_light/λ','h = 6.62607015 × 10⁻³⁴ J s; c_light = 299792458 m s⁻¹.','atoms-3'),
 ('Quantum-state capacities','Subshell orbitals = 2ℓ + 1; electron capacity = 2(2ℓ + 1)','s/p/d/f: ℓ = 0/1/2/3 → capacities 2/6/10/14.','atoms-4'),
 ('Formal charge','FC = valence − nonbonding − ½(bonding electrons)','Sum all formal charges to recover the species charge.','bonding-4'),
 ('Dilution & nonreacting mixing','c₁V₁ = c₂V₂; c_mix = Σ(cᵢVᵢ)/V_total','Dilution conserves solute; mixing adds inventories.','solutions-4'),
 ('Titration equivalence','c_AV_A/ν_A = c_BV_B/ν_B','Use the actual neutralization ratio; titre is final minus initial.','solutions-5'),
 ('Hydrocarbon patterns','Acyclic alkane CₙH₂ₙ₊₂; one alkene CₙH₂ₙ; one alkyne CₙH₂ₙ₋₂','The latter patterns assume open chains and exactly one indicated multiple bond.','organic-1'),
 ('Chromatography','R_f = solute distance/solvent-front distance','Same baseline; comparable only under matching conditions.','matter-3')
]
