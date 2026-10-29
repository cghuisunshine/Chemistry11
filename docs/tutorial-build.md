# Chemistry 11 study companion

Open `../tutorial.html` directly in a browser. The page is a standalone HTML file with inline CSS, JavaScript, SVG diagrams, and all lesson content. Internet access is not required for the study tools. Keep the original PDF paths alongside the page for the reading links.

## Rebuild

From the workspace root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/generate_tutorial.py
```

- `scripts/tutorial_content.py`: original lesson text, examples, quizzes, formula derivations, and the source map.
- `scripts/tutorial_models.py`: accessible model markup.
- `scripts/tutorial_university.py`: 42 university extensions, ten foundations, 21 worked derivations, and exact source-page references.
- `scripts/tutorial_university_render.py`: definition tables, connected foundation links, worked reasoning, source maps, and original SVG diagrams.
- `scripts/tutorial.css` and `scripts/tutorial.js`: page design and interactions, embedded during generation.
- `docs/tutorial-outline.md`: generated readable teaching outline.

The generator uses only the Python standard library. There is no installation or build dependency for reading the finished page.

## Coverage

The main reading sequence is the eight chapters of *BC Science Chemistry 11* (Edvantage Interactive, 2011). The complete textbook is `chem11.pdf`; all lesson references use the PDF viewer's one-based page number. The source index lists 15 course, lecture, practice, answer, and lab-report PDFs totaling 162 pages, including all dated root and December 12 notes. Page-level duplicate exports in `11-14/` and `12-12/1/` and `/2/` are represented by their complete parent PDFs. Textbook chapter splits and alternate textbook copies are not counted as additional lecture sources.

Scanned notes were OCR-processed and their topics matched with the textbook. The tutorial gives original explanations, examples, and concept checks; it does not transcribe or solve every worksheet question. Worked-answer companions were cross-checked conceptually rather than treated as definitive. The university tutor layer uses the supplied Chemistry: The Central Science (15th Global edition), Principles of Modern Chemistry (8th edition), and selected definitions from Physical Chemistry (8th edition). The last source was copied unchanged from the sibling Chemistry12 folder to Physical_Chemistry.pdf so all local textbook links work beside the tutorial. The page contains original explanations and deductions rather than reproduced textbook passages. The university layer does not expand the assigned student-level course to every topic in those books.

## Verification

Checked in Chrome at desktop width and a 390 px phone viewport:

- All 42 lessons, 42 university tutor notes and definition tables, ten shared foundations, 21 worked derivations, eight formula trees, eight interactive models, and 16 example solutions render.
- All eight quizzes produce 3/3 for the correct selections; unanswered questions receive feedback.
- Search opens matching lessons, reports no matches, and restores the prior expanded state when cleared.
- Ionic formula construction, density validation, dilution constraints, hydrocarbon formula counting, photon energy, and molecular shapes were checked against known cases.
- Copy buttons, deep links into collapsed lessons, expand/collapse controls, mobile navigation, and progress persistence work.
- No console errors during the interaction checks. No duplicate element IDs or broken local/fragment links in the generated page.
- Mobile document width stays within the viewport. Resource tables scroll within their containers.

Printing expands lesson details and restores the previous state afterward; the print stylesheet is included. A physical printer and Safari/Firefox were not tested.

## University extension verification

Checked the added foundation and derivation fragment links, advanced-topic search, open/close controls for all 42 notes, formula copying, and a 390 px mobile viewport. Wide diagrams scroll inside their own containers. All 317 local PDF links resolve to existing files; there are no duplicate IDs or broken internal targets. Recalculated representative uncertainty, gas-density, heating, mixing, hydrogen-spectrum, dipole-vector, calorimetry, titration, and solubility examples independently. Student lesson text, quizzes, and model data were retained.

## Lesson illustrations

The page embeds 28 original SVG teaching diagrams from `scripts/tutorial_figures.py`, spanning all eight chapters and all five atomic lessons. Captions identify particle keys, model limits, omitted details, and wavefunction phase conventions. Figures are placed in the student lesson before its formula and remain available offline. At phone widths, each diagram scrolls within a keyboard-focusable frame to keep labels readable. Print styles fit figures to the page.
