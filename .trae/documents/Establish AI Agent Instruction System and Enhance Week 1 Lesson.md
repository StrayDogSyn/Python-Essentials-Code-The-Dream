## Overview
- Implement a full AI agent instruction workflow for Python Essentials and enhance Week 1 content to meet the specified pedagogical and technical standards.
- Use the professional multi‑agent documentation (the `.agents/` system) referenced by project guides, and apply the 15‑step enhancement template.
- Target lesson file: use `lesson-plans/lesson_week1_intro_python.html` (present in repository) as the working equivalent of `lessons/week1.html`. Maintain consistency with the existing lesson architecture and index navigation.

## Research & Familiarization
- System guides found: `AGENTS_SYSTEM_GUIDE.md`, `AGENT_SYSTEM_ENHANCED.md`, `START_HERE.md`, `INTEGRATION_COMPLETE.md`, `SETUP_COMPLETE.md`.
- Action:
  - Review `.agents/README.md`, `.agents/CONTEXT.md`, `.agents/STYLE_GUIDE.md`, role files under `.agents/roles/content-enhancer/`, and `.agents/templates/lesson-enhancement.md` once available (the guides indicate they exist). If the `.agents/` folder is not yet present, use the master guides above for standards until the folder is materialized.

## Role Activation (Content Enhancer)
- Activate the Content Enhancer role using the role docs (`AGENT.md`, `PROMPTS.md`) and quality criteria (`CHECKLIST.md`).
- Adopt voice, formatting, accessibility, and career‑focused tone per the style guide.

## Target & Scope
- Target file: `lesson-plans/lesson_week1_intro_python.html` (Week 1 HTML lesson already implemented with sections: Intro, Setup, Basics, Control Flow, Functions, Debugging, Cheat Sheet).
- Maintain retro‑terminal aesthetic, CSS variables, and existing layout/navigation.

## 15‑Step Execution (from `.agents/templates/lesson-enhancement.md`)
1. Read style/context docs; confirm learner persona and success metrics.
2. Audit current Week 1 HTML structure and flow.
3. Identify gaps vs. spec (word count, analogies, code examples, interactivity, notebook integration).
4. Draft a structured outline with new subsections and exercises.
5. Expand content to ~1500+ words while preserving clarity and reading level.
6. Add at least 5 relatable analogies (gaming, cooking, finance, movies, everyday life).
7. Add 10+ progressive code examples: beginner → intermediate → applied.
8. Add 2+ interactive components: run‑simulation buttons, mini quiz.
9. Add Jupyter integration markers and explicit references to `notebook-sessions/week1/session1_intro_to_python.ipynb`.
10. Strengthen career connections and real company examples.
11. Insert accessibility features: ARIA labels, keyboard nav notes, contrast checks.
12. Validate code examples for Python 3.8+.
13. Mobile responsiveness check at 375px (update CSS only if needed; keep existing variables).
14. Document changes with timestamps in `.agents/archive/week1-work.md`.
15. Final QA against `CHECKLIST.md`; mark Week 1 complete.

## Initial Audit Summary (current file)
- Present content:
  - Intro with career context, cooking analogy, objectives, vocabulary, multiple code examples, Try‑It exercises (Budget, Tip Calculator), Control Flow basics (if/elif/else; loops), Functions basics, Debugging (try/except, print debugging), Cheat Sheet.
- Gaps vs. spec:
  - Control Flow: add gaming dialogue tree analogy; more applied examples (age verification, grade calculator, tiered discounts); Try‑It temp converter/grade calculator.
  - Functions: expand recipe analogy; add progressive series (greeting → calculator → validation); Try‑It tax calculator.
  - Debugging: add detective/doctor analogy; add common error types table (SyntaxError, TypeError, NameError, ZeroDivisionError, ValueError) with fixes; pro tips (read errors bottom‑up).
  - Interactivity: add at least one mini quiz and simulated run output to key blocks; ensure keyboard navigation hints.
  - Notebook integration: explicit “Practice in `session1_intro_to_python.ipynb`” callouts; flag 5‑7 concepts for notebook developer.
  - Metadata: add enhancement tags, aria‑labels where appropriate.

## Content Enhancements (concrete items)
- Control Flow:
  - Analogy: “Gaming dialogue tree” mapping to `if/elif/else`.
  - Examples: age verification (16/18/21 thresholds); grade calculator (A/B/C/D/F); tiered discount logic (memberships + purchase thresholds).
  - Try‑It: temperature converter (C↔F) or grade calculator; starter code + requirements.
- Functions:
  - Analogy: recipe → ingredients=parameters, dish=return value, kitchen=scope.
  - Progressive examples: `greet()`, `add()/subtract()/calc_tax()`, `validate_email()` with `return` vs `print`, default args and simple input sanitation.
  - Try‑It: reusable tax calculator (progressive rates, rounding to two decimals).
- Debugging:
  - Analogy: detective (clues→hypothesis→test) / doctor (symptoms→diagnosis→treatment).
  - Table: common errors with causes, example code line, and fix.
  - Pro tips: print debugging patterns, reading stack traces bottom‑up, isolating minimal repro.
- Interactivity:
  - Add a 5‑question mini quiz (MCQ) embedded in HTML for control flow and functions.
  - Add run‑simulation buttons with expected outputs for 4–6 key examples.
- Notebook callouts:
  - Inline markers: “Practice in `notebook-sessions/week1/session1_intro_to_python.ipynb`.”
  - Flag these concepts for notebook developer: variables/types, `if/elif/else`, boolean logic patterns, loops (`for`, `while`), `return` vs `print`, basic error handling.

## Technical Best Practices
- Semantic HTML sections (`<section>`, `<nav>`, `<main>`, `<header>`); add ARIA labels to interactive controls.
- Mobile‑first: verify 375px breakpoint; adjust spacing if needed.
- Progressive enhancement: interactivity works but content remains readable without JS.
- Accessible contrast: keep existing palette; ensure new elements meet WCAG contrast.
- Client‑side storage (optional): reuse existing completion tracking for topics; avoid adding heavy frameworks.

## QA
- Validate all Python examples in a Python 3.8+ REPL.
- Verify keyboard navigation and tab order for interactive elements.
- Confirm all internal hyperlinks (index cards, navigation buttons) work.
- Run an accessibility pass (labels, contrast, focus states).
- Re‑check page at 375px and desktop widths.

## Documentation & Version Control
- Change log: create/update `.agents/archive/week1-work.md` with dated entries, sections changed, lines impacted, and rationale.
- Metadata: tag new blocks with data‑attributes (e.g., `data-analogy="gaming"`, `data-tryit="grade-calculator"`) for future auditing.
- Checklist: mark items completed in `CHECKLIST.md` under content‑enhancer.

## Delivery
- Output: professionally formatted HTML in `lesson-plans/lesson_week1_intro_python.html` following site conventions.
- QA summary: attach to change log.
- Confirm mobile compliance and code validity.

## Open Questions / Assumptions
- `.agents/` directory: project guides indicate it exists; if not present, we will materialize it or follow master guides until enabled.
- Target path: Using `lesson-plans/lesson_week1_intro_python.html` as Week 1 HTML; if `lessons/week1.html` is required for a separate site, we can mirror the changes to that path after confirmation.

## Next Step
- Upon approval, I will perform the audit, apply the enhancements described, validate, and produce the change log in `.agents/archive/week1-work.md`, ensuring all QA checks and delivery requirements are met.