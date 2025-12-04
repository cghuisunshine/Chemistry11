# Repository Guidelines

## Project Structure & Module Organization
- This repo is a static study site for Chemistry 11 with standalone HTML pages: `index.html` (table of contents with copy-on-double-click), `matter.html`, `organic.html`, `pattern.html`, and `solution.html`.
- All styling and scripting live inline in each page; there is no external build pipeline or asset folder. Keep related CSS/JS close to the sections they affect.
- When adding a new topic, mirror existing page patterns: a `<div class="wrap">` or `.page` container, clearly labeled headings, and compact helper text blocks for quick scanning.

## Build, Test, and Development Commands
- Serve locally to validate layout and copy interactions: `python3 -m http.server 8000` then open `http://localhost:8000/index.html`.
- For ad-hoc linting of HTML/CSS, use a browser’s devtools or a validator of your choice; there is no repo-managed lint step.

## Coding Style & Naming Conventions
- Use 2-space indentation for HTML, CSS, and inline JavaScript to match the existing files.
- Prefer semantic HTML (`<section>`, `<h4>`, `<ul>`) and concise class names that describe layout or color intent (e.g., `.wrap`, `.section-panel`).
- Keep CSS variables in the `:root` block organized by purpose (colors, typography, spacing). Reuse existing palette tokens like `--accent` and `--muted` before adding new ones.
- Keep JavaScript minimal and self-contained at the bottom of the page; use clear function names (e.g., `renderTOC`, `attachCopyHandlers`) instead of abbreviations.

## Testing Guidelines
- There are no automated tests; rely on manual verification in at least one Chromium-based browser and Safari/Firefox when possible.
- Confirm copy-to-clipboard behavior on elements marked `data-copyable`, toggle/expand controls, and responsive layout at mobile widths (≤480px).
- For new sections, scan for console errors and validate that keyboard navigation and focus outlines remain visible.

## Content Updates & Interactivity
- Keep instructional text concise and action-oriented; aim for scannable bullet lists and short `<pre>` blocks for hints.
- When adding interactive affordances (copy buttons, expanders), ensure `aria` labels and keyboard triggers are present, and avoid inline event attributes when unobtrusive listeners suffice.
- Maintain consistent emoji and icon usage with the existing tone (e.g., 📘 in the main title).

## Commit & Pull Request Guidelines
- Follow an imperative, short subject line for commits (e.g., "Refine redox tips"), with optional body describing rationale and scope.
- Group related visual and content changes together; avoid large unrelated edits in one commit.
- For pull requests, include a brief summary of changes, steps to review (which page and section), and screenshots or short clips for UI/interaction tweaks. Link related issues when available.
