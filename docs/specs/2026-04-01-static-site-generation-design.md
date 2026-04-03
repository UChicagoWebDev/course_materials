# Static Site Generation Migration

## Overview

Migrate the course materials site from client-side remarkjs rendering to a Python-based static site generator that produces one HTML page per slide. The generator uses Jinja2 for templates and python-markdown for Markdown rendering. Output is static HTML suitable for GitHub Pages or any static host.

## Markdown Processing Pipeline

The build script reads each `lecture_notes/week_N.md` (excluding `week_8_old.md`) and processes it through:

1. **Split on `---`** — split the file into individual slide strings. The `---` must appear on its own line to count as a slide boundary.

2. **Strip remark syntax** from each slide — a preprocessor that:
   - Removes `class: ...` directives at the top of slides. These classes (e.g., `center`, `middle`, `agenda`, `split`) are applied as CSS classes on the slide's container `<div>` in the output HTML, so their visual effect can be preserved via the stylesheet.
   - Converts `.classname[content]` wrappers to `<span class="classname">content</span>` (or `<div>` for block-level content). This preserves classes like `.big`, `.half`, `.credit`, `.gallery` so they can be styled via CSS.
   - Removes `???` presenter note blocks — everything from a line containing only `???` (outside of fenced code blocks) to the end of the slide.
   - Removes `--` incremental reveal markers — only when `--` appears as the sole content on a line, outside of fenced code blocks.

3. **Render Markdown to HTML** — each slide's markdown is run through python-markdown with extensions for fenced code blocks, syntax highlighting (codehilite/Pygments), and tables.

4. **Render into Jinja2 template** — the slide HTML is injected into a `slide.html` template with navigation data, prev/next links, and site CSS.

## Images and Asset Paths

- `lecture_notes/images/` is copied to `_site/lecture_notes/images/`.
- Image references in slide markdown use relative paths like `images/foo.png`. Since slides output to `_site/lecture_notes/week_N/1/index.html`, these relative paths will not resolve correctly. The build script rewrites image `src` attributes in generated slide HTML to use absolute paths (e.g., `/lecture_notes/images/foo.png`).
- Absolute links in the markdown (e.g., `/examples/week_2/columns.html`) are left as-is — they resolve correctly from the site root.
- External image URLs (e.g., xkcd, imgflip) are left as-is.

## Output Structure

```
_site/
├── index.html                     # Course homepage
├── syllabus/
│   └── index.html                 # Rendered syllabus
├── lecture_notes/
│   ├── index.html                 # Week listing page
│   ├── images/                    # Copied from lecture_notes/images/
│   └── week_1/
│       ├── 1/index.html           # Slide 1
│       ├── 2/index.html           # Slide 2
│       └── ...
│   └── week_2/
│       └── ...
├── examples/                      # Copied as-is (including examples/images/)
│   ├── week_1/
│   └── ...
├── css/
│   └── style.css                  # Site stylesheet
└── js/
    └── navigation.js              # Keyboard nav
```

- Clean URLs via `index.html` inside directories (e.g., `/lecture_notes/week_1/3/`)
- Examples directory copied verbatim, including `examples/images/`
- CSS and JS are shared across all pages
- `trevor.html` and `yourname.html` from the repo root are not included in the output (student exercise artifacts)

## Navigation

A vanilla JS file (`navigation.js`) handles keyboard navigation:

- **Left/Up arrow** — previous slide
- **Right/Down arrow** — next slide
- **Home** — first slide of the current week

Each slide's HTML includes data attributes with prev/next URLs and slide count. The JS reads these and navigates via `window.location`.

Each slide page also has a visible nav bar:
- Week title and slide number (e.g., "Week 3 — 12 / 34")
- Clickable prev/next arrows
- Link back to course homepage

## Templates

Four Jinja2 templates:

1. **`base.html`** — shared shell: `<head>`, CSS link, nav bar, JS link, `{% block content %}`
2. **`slide.html`** — extends base. Renders a single slide's HTML content with navigation data (prev/next URLs, slide number, total count, week number).
3. **`page.html`** — extends base. For non-slide pages (syllabus). No slide navigation, just content.
4. **`lecture_index.html`** — extends base. Lists all weeks with links to their first slide. Generated at `/lecture_notes/index.html`.

The homepage is a Jinja2 template rendered directly (`templates/index.html`), not generated from markdown, since it has custom layout.

## Stylesheet

The new `css/style.css` is written from scratch but ports relevant visual rules from the existing `lecture_notes/styles/style.css`:
- Slide container classes preserved from `class:` directives (`center`, `middle`, `split`, `agenda`, `gallery`, etc.)
- Inline content classes preserved from `.classname[]` syntax (`big`, `half`, `credit`, `animate`, etc.)
- Typography (existing Google Fonts: Yanone Kaffeesatz, Droid Serif, Ubuntu Mono)
- Code block styling (Pygments theme)

## Build Script

**`build.py`** — single entry point. `python build.py`:

1. Cleans and recreates `_site/`
2. Walks `lecture_notes/week_*.md` (skipping `*_old.md`), runs each through the split/preprocess/render pipeline
3. Generates the lecture notes index page
4. Renders the homepage and syllabus (from `syllabus.md` at the repo root, using the `page.html` template)
5. Copies `examples/`, `lecture_notes/images/`, and static assets (CSS, JS) into `_site/`

**Local preview:** `python -m http.server -d _site`

## Dependencies

In `requirements.txt`:
- `Jinja2` — templating
- `Markdown` — python-markdown for rendering
- `Pygments` — syntax highlighting for code blocks

## Deployment

- Output is a static `_site/` directory deployable anywhere
- Primary target: GitHub Pages via GitHub Actions (build on push, deploy to Pages)
- Alternative: rsync or any static file host
- The existing `deploy.sh` (rsync to uchicagowebdev.com) is superseded but can be kept for backwards compatibility during transition

## Cleanup

After migration is complete, the following files become unused and can be removed:
- `lecture_notes/scripts/` (remark-v0.15.0.min.js, require.js, slides.js)
- `lecture_notes/styles/` (replaced by `css/style.css`)
- `lecture_notes/index.html` (replaced by generated output)

## Markdown File Organization

Markdown files stay as one file per week (`week_N.md`). The build system splits on `---` to produce individual slide pages. This keeps authoring simple and the files human-readable.
