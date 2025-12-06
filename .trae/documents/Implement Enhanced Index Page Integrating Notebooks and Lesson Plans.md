## Goal
Create/upgrade the main `index.html` landing page to integrate Jupyter notebooks and lesson plans for Weeks 1–11, matching your enhanced index spec (quick customization, three notebook access methods, progress tracking, achievements, setup tabs), and add two docs: `index-setup-guide.md` and `index-quick-reference.md`.

## Repository Reality Check (Read‑only results)
- Lessons exist under `lesson-plans/` (e.g., Week 1, Week 2, Week 3, Week 4–11 files already present).
- Notebooks found under `notebook-sessions/weekX/` (e.g., `week6/session1_...ipynb`, `week7/session1_intro_to_data_visualization.ipynb`, `week8/session1_intro_to_web_scraping.ipynb`, `week11` sessions). There is no `/notebooks` folder.
- No existing `index.html` detected; we will create it at repo root unless you have another location.

## Integration Strategy
### 1) Index Cards per Week (11 cards)
Each card includes:
- Title and short description
- Buttons:
  - Download ⬇️ → direct link to the `.ipynb` in `notebook-sessions/weekN/...` (exact file names configurable)
  - Colab 🚀 → `https://colab.research.google.com/github/<yourusername>/CTD/blob/main/<path-to-ipynb>`
  - View 👁️ → `https://nbviewer.org/github/<yourusername>/CTD/blob/main/<path-to-ipynb>`
  - Start Lesson → points to `lesson-plans/lesson_weekN_*.html` (current repo structure)
- Mark Complete ✓ button → localStorage progress + card checkmark

### 2) Notebook Path Mapping
- Default pattern: `notebook-sessions/weekN/session1_<topic>.ipynb` (and session2 for group work where applicable)
- We will:
  - Add data attributes per card to store notebook path(s) (`data-nb-path`, `data-nb-path2`)
  - Provide a small config JS object where you can override file names for each week if they differ
  - If a file is missing, the button disables and shows a tooltip “Notebook not found”

### 3) Lessons Path Mapping
- Use existing lesson files:
  - Week 1: `lesson-plans/lesson_week1_intro_python.html`
  - Week 2: `lesson-plans/lesson_week2_data_structures.html`
  - Week 3: `lesson-plans/lesson_week3_python_skills.html`
  - Week 4: `lesson-plans/lesson_week4_data_engineering.html`
  - Week 5: `lesson-plans/lesson_week5_data_visualization.html`
  - Week 6: `lesson-plans/lesson_week6_sql_databases.html`
  - Week 7: `lesson-plans/lesson_week7_apis_scraping.html`
  - Week 8: `lesson-plans/lesson_week8_advanced_pandas.html`
  - Week 9: `lesson-plans/lesson_week9_intro_ml.html`
  - Week 10: `lesson-plans/lesson_week10_flask_web.html`
  - Week 11: `lesson-plans/lesson_week11_deployment.html`

### 4) Quick Customization Reference (inline on index)
- Include your “FASTEST SETUP (5 Minutes)” section with:
  - Find/Replace `yourusername` (34 places) — We’ll centralize in a JS `const GITHUB_USER = 'yourusername'` and propagate links to reduce manual edits; still include manual instructions in case users prefer editor replace
  - Email in footer
  - Course title, tagline, description, theme color variables
- Provide exact line anchors/comments for quick edits (approximate indices noted, but emphasize commenting markers rather than absolute line numbers to keep resilient to future edits)

### 5) Setup Tabs (Colab / Local / VS Code)
- A top “Setup” section with tabbed instructions consistent across weeks:
  - Colab: How to open and run; Google account requirement
  - Local Jupyter: pip install, run `jupyter lab/notebook`, open files
  - VS Code: Python extension, Jupyter extension, open `.ipynb`

### 6) Progress Tracking & Achievements
- LocalStorage keys: `pe_progress` for week completion states (array of week numbers)
- Progress bar at top; achievement popups at milestones (e.g., 3, 6, 9, 11 weeks completed)

### 7) Accessibility & Mobile
- ARIA labels for quiz buttons and interactive controls
- Keyboard navigation across week cards and tabs
- Mobile-first CSS using existing retro-terminal theme; verify at 375px

### 8) Testing & Publishing Checklist (inline section)
- Local test: ensure each button renders, lesson links open, notebooks found
- GitHub Pages: confirm Colab and nbviewer links work when repo is public
- Progress persists on reload; achievements trigger

### 9) Docs to Produce
- `index-setup-guide.md` (full instructions per your “Setup Guide” content)
- `index-quick-reference.md` (copy-paste quick customization and exact edit markers)

### 10) Coordination
- Notebook Developer: confirm notebook file names per week; create missing placeholders; align with card config
- Assessment Creator: add mini-quizzes on index (optional) linking to lesson quizzes; ensure alignment with weekly learning objectives

## Implementation Steps
1. Create `index.html` at repo root using your retro-terminal design; add cards for Weeks 1–11.
2. Add a JS config section:
   ```js
   const GITHUB_USER = 'yourusername';
   const WEEK_CONFIG = {
     1: { title:'Intro to Python', nb:'notebook-sessions/week1/session1_intro_to_python.ipynb' },
     2: { title:'Data Structures', nb:'notebook-sessions/week2/session1_data_structures.ipynb' },
     // ... override with actual paths found; leave missing disabled
   };
   ```
3. Generate notebook button `href`s from `GITHUB_USER` + `WEEK_CONFIG` and attach to buttons; add disabled state if path not found.
4. Insert Quick Customization block and Setup Tabs.
5. Implement localStorage progress; progress bar; achievements.
6. Integrate your Testing Checklist and Publishing steps.
7. Produce `index-setup-guide.md` and `index-quick-reference.md` with your provided content adapted to current repo structure (`lesson-plans/` and `notebook-sessions/`).

## Verification
- Validate all links:
  - Download: raw file path existing in repo
  - Colab: correct GitHub path formatting
  - nbviewer: correct path formatting
  - Lesson links: `lesson-plans` pages load
- Test localStorage progress, achievements
- Mobile check at 375px and desktop
- Accessibility: labels, focus, ARIA

## Notes & Assumptions
- If any week’s notebooks differ in name/location, we’ll override in `WEEK_CONFIG` rather than changing the HTML structure.
- If an existing `index.html` is discovered, we’ll merge enhancements into it instead of replacing.

## Deliverables
- `index.html` landing page integrated with notebooks and lesson plans
- `index-setup-guide.md` and `index-quick-reference.md`
- Inline quick customization block
- Configurable username and per-week notebook mapping
- Testing checklist embedded and docs
