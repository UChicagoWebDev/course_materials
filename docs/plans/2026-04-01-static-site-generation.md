# Static Site Generation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a Python static site generator that converts remarkjs-flavored markdown into individual HTML slide pages with keyboard navigation.

**Architecture:** A single `build.py` script that splits weekly markdown files into slides, strips remark syntax, renders markdown to HTML via python-markdown, and injects the result into Jinja2 templates. Output is a `_site/` directory of static HTML.

**Tech Stack:** Python 3, Jinja2, python-markdown, Pygments

**Spec:** `docs/specs/2026-04-01-static-site-generation-design.md`

---

## File Structure

```
build.py                          # Main build script
requirements.txt                  # Python dependencies
preprocessor.py                   # Remark syntax stripping and slide splitting
templates/
  base.html                       # Shared HTML shell
  slide.html                      # Single slide page
  page.html                       # Generic content page (syllabus)
  index.html                      # Course homepage
  lecture_index.html              # Week listing page
static/
  css/style.css                   # Site stylesheet (ported from remark CSS)
  js/navigation.js                # Keyboard slide navigation
tests/
  test_preprocessor.py            # Tests for remark syntax stripping
  test_build.py                   # Integration tests for build output
```

---

### Task 1: Project Scaffolding

**Files:**
- Create: `requirements.txt`
- Create: `tests/__init__.py`
- Create: `tests/test_preprocessor.py` (empty initially)

- [ ] **Step 1: Create `requirements.txt`**

```
Jinja2>=3.1
Markdown>=3.5
Pygments>=2.17
```

- [ ] **Step 2: Create empty test package**

```bash
mkdir -p tests
touch tests/__init__.py
```

- [ ] **Step 3: Install dependencies**

Run: `pip install -r requirements.txt`
Expected: Successfully installs Jinja2, Markdown, Pygments and their dependencies.

- [ ] **Step 4: Commit**

```bash
git add requirements.txt tests/__init__.py
git commit -m "add project scaffolding for static site generator"
```

---

### Task 2: Slide Splitting

**Files:**
- Create: `preprocessor.py`
- Create: `tests/test_preprocessor.py`

- [ ] **Step 1: Write failing test for basic slide splitting**

`tests/test_preprocessor.py`:
```python
from preprocessor import split_slides


def test_split_slides_basic():
    md = "# Slide 1\nContent\n---\n# Slide 2\nMore content"
    slides = split_slides(md)
    assert len(slides) == 2
    assert "# Slide 1" in slides[0]
    assert "# Slide 2" in slides[1]


def test_split_slides_ignores_hr_in_code_block():
    md = "# Slide 1\n```\n---\n```\n---\n# Slide 2"
    slides = split_slides(md)
    assert len(slides) == 2
    assert "---" in slides[0]  # The --- inside the code block stays


def test_split_slides_trims_whitespace():
    md = "# Slide 1\n\n---\n\n# Slide 2\n"
    slides = split_slides(md)
    assert slides[0].strip() == "# Slide 1"
    assert slides[1].strip() == "# Slide 2"
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_preprocessor.py -v`
Expected: FAIL — `ImportError: cannot import name 'split_slides'`

- [ ] **Step 3: Implement `split_slides`**

`preprocessor.py`:
```python
import re


def split_slides(markdown: str) -> list[str]:
    """Split markdown on --- slide boundaries, ignoring --- inside fenced code blocks."""
    slides = []
    current_slide = []
    in_code_block = False

    for line in markdown.split("\n"):
        stripped = line.strip()

        # Track fenced code blocks
        if stripped.startswith("```"):
            in_code_block = not in_code_block

        # A line containing only --- outside a code block is a slide boundary
        if stripped == "---" and not in_code_block:
            slides.append("\n".join(current_slide))
            current_slide = []
        else:
            current_slide.append(line)

    # Don't forget the last slide
    if current_slide:
        slides.append("\n".join(current_slide))

    # Strip leading/trailing whitespace from each slide, drop empty slides
    return [s.strip() for s in slides if s.strip()]
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_preprocessor.py -v`
Expected: All 3 tests PASS.

- [ ] **Step 5: Commit**

```bash
git add preprocessor.py tests/test_preprocessor.py
git commit -m "add slide splitting with fenced code block awareness"
```

---

### Task 3: Strip Class Directives

**Files:**
- Modify: `preprocessor.py`
- Modify: `tests/test_preprocessor.py`

- [ ] **Step 1: Write failing tests**

Append to `tests/test_preprocessor.py`:
```python
from preprocessor import strip_class_directive


def test_strip_class_directive_basic():
    slide = "class: center, middle\n# Title"
    content, classes = strip_class_directive(slide)
    assert content.strip() == "# Title"
    assert classes == ["center", "middle"]


def test_strip_class_directive_none():
    slide = "# No class here"
    content, classes = strip_class_directive(slide)
    assert content.strip() == "# No class here"
    assert classes == []


def test_strip_class_directive_single():
    slide = "class: agenda\n# Agenda Items"
    content, classes = strip_class_directive(slide)
    assert content.strip() == "# Agenda Items"
    assert classes == ["agenda"]
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_preprocessor.py::test_strip_class_directive_basic -v`
Expected: FAIL — `ImportError`

- [ ] **Step 3: Implement `strip_class_directive`**

Add to `preprocessor.py`:
```python
def strip_class_directive(slide: str) -> tuple[str, list[str]]:
    """Remove 'class: ...' directive from top of slide. Returns (content, class_list)."""
    lines = slide.split("\n")
    if lines and lines[0].strip().startswith("class:"):
        class_line = lines[0].strip()
        class_str = class_line[len("class:"):].strip()
        classes = [c.strip() for c in class_str.split(",")]
        return "\n".join(lines[1:]), classes
    return slide, []
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_preprocessor.py -v -k "class_directive"`
Expected: All 3 tests PASS.

- [ ] **Step 5: Commit**

```bash
git add preprocessor.py tests/test_preprocessor.py
git commit -m "add class directive stripping from slides"
```

---

### Task 4: Strip Presenter Notes and Incremental Reveals

**Files:**
- Modify: `preprocessor.py`
- Modify: `tests/test_preprocessor.py`

- [ ] **Step 1: Write failing tests**

Append to `tests/test_preprocessor.py`:
```python
from preprocessor import strip_presenter_notes, strip_incremental_reveals


def test_strip_presenter_notes_basic():
    slide = "# Slide\nContent\n\n???\n\nThese are notes"
    result = strip_presenter_notes(slide)
    assert "Content" in result
    assert "notes" not in result
    assert "???" not in result


def test_strip_presenter_notes_no_notes():
    slide = "# Slide\nContent"
    result = strip_presenter_notes(slide)
    assert result == slide


def test_strip_presenter_notes_ignores_code_block():
    slide = "# Slide\n```\n???\n```\nMore content"
    result = strip_presenter_notes(slide)
    assert "???" in result
    assert "More content" in result


def test_strip_incremental_reveals():
    slide = "# Slide\nFirst point\n\n--\n\nSecond point"
    result = strip_incremental_reveals(slide)
    assert "First point" in result
    assert "Second point" in result
    assert "\n--\n" not in result


def test_strip_incremental_reveals_ignores_code_block():
    slide = "```\n--\n```"
    result = strip_incremental_reveals(slide)
    assert "--" in result
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_preprocessor.py -v -k "presenter or incremental"`
Expected: FAIL — `ImportError`

- [ ] **Step 3: Implement both functions**

Add to `preprocessor.py`:
```python
def strip_presenter_notes(slide: str) -> str:
    """Remove everything from a standalone ??? line to end of slide, outside code blocks."""
    lines = slide.split("\n")
    result = []
    in_code_block = False

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("```"):
            in_code_block = not in_code_block

        if stripped == "???" and not in_code_block:
            break  # Drop everything from here to end of slide

        result.append(line)

    return "\n".join(result).rstrip()


def strip_incremental_reveals(slide: str) -> str:
    """Remove standalone -- lines (incremental reveal markers) outside code blocks."""
    lines = slide.split("\n")
    result = []
    in_code_block = False

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("```"):
            in_code_block = not in_code_block

        if stripped == "--" and not in_code_block:
            continue  # Skip this line

        result.append(line)

    return "\n".join(result)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_preprocessor.py -v -k "presenter or incremental"`
Expected: All 5 tests PASS.

- [ ] **Step 5: Commit**

```bash
git add preprocessor.py tests/test_preprocessor.py
git commit -m "add presenter notes and incremental reveal stripping"
```

---

### Task 5: Convert `.classname[content]` Wrappers

**Files:**
- Modify: `preprocessor.py`
- Modify: `tests/test_preprocessor.py`

- [ ] **Step 1: Write failing tests**

Append to `tests/test_preprocessor.py`:
```python
from preprocessor import convert_class_wrappers


def test_convert_class_wrappers_inline():
    text = "Some .big[**bold text**] here"
    result = convert_class_wrappers(text)
    assert result == 'Some <span class="big">**bold text**</span> here'


def test_convert_class_wrappers_line_start_with_trailing_text():
    """A .classname[] at line start with trailing text is inline, not block."""
    text = ".big[**0.1 second**] is about the limit for the user"
    result = convert_class_wrappers(text)
    assert result == '<span class="big">**0.1 second**</span> is about the limit for the user'


def test_convert_class_wrappers_block_whole_line():
    text = ".half[![Image](foo.png)]"
    result = convert_class_wrappers(text)
    assert result == '<div class="half" markdown="1">\n\n![Image](foo.png)\n\n</div>'


def test_convert_class_wrappers_credit():
    text = ".credit[https://xkcd.com/327/]"
    result = convert_class_wrappers(text)
    assert result == '<div class="credit" markdown="1">\n\nhttps://xkcd.com/327/\n\n</div>'


def test_convert_class_wrappers_multiline():
    text = ".animate[\n![Phil](images/phil.jpeg)\n]"
    result = convert_class_wrappers(text)
    assert '<div class="animate">' in result
    assert "![Phil](images/phil.jpeg)" in result


def test_convert_class_wrappers_nested_brackets():
    text = ".big[text with [link](url)]"
    result = convert_class_wrappers(text)
    assert "[link](url)" in result


def test_no_class_wrappers():
    text = "Just normal markdown"
    result = convert_class_wrappers(text)
    assert result == "Just normal markdown"
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_preprocessor.py -v -k "class_wrappers"`
Expected: FAIL — `ImportError`

- [ ] **Step 3: Implement `convert_class_wrappers`**

Add to `preprocessor.py`:
```python
def convert_class_wrappers(text: str) -> str:
    """Convert .classname[content] remark syntax to HTML elements.

    Block-level usage (line starts with .classname[) becomes <div class="...">.
    Inline usage becomes <span class="...">.
    Handles nested brackets (e.g., markdown links inside wrappers).
    Handles multiline blocks where ] is on a subsequent line.
    """
    result = _convert_multiline_wrappers(text)
    result = _convert_inline_wrappers(result)
    return result


def _convert_multiline_wrappers(text: str) -> str:
    """Handle .classname[...] that spans multiple lines."""
    lines = text.split("\n")
    result = []
    i = 0

    while i < len(lines):
        match = re.match(r"^\.(\w[\w-]*)\[\s*$", lines[i].strip())
        if match:
            classname = match.group(1)
            # Collect lines until we find a closing ]
            inner_lines = []
            i += 1
            while i < len(lines) and lines[i].strip() != "]":
                inner_lines.append(lines[i])
                i += 1
            inner = "\n".join(inner_lines).strip()
            result.append(f'<div class="{classname}" markdown="1">\n\n{inner}\n\n</div>')
            i += 1  # Skip the closing ]
        else:
            result.append(lines[i])
            i += 1

    return "\n".join(result)


def _convert_inline_wrappers(text: str) -> str:
    """Handle .classname[...] on a single line."""
    # Pattern: .classname[ at start of line (block) or inline
    def replace_match(match):
        classname = match.group(1)
        content = match.group(2)
        line_before = match.string[:match.start()]
        line_after = match.string[match.end():]

        # Block-level only if .classname[...] is the entire line content:
        # nothing before it (on this line) and nothing after it (on this line)
        last_newline = line_before.rfind("\n")
        line_start = line_before[last_newline + 1:] if last_newline >= 0 else line_before

        next_newline = line_after.find("\n")
        line_end = line_after[:next_newline] if next_newline >= 0 else line_after

        if line_start.strip() == "" and line_end.strip() == "":
            # Block-level: use markdown="1" so python-markdown renders inner content
            return f'<div class="{classname}" markdown="1">\n\n{content}\n\n</div>'
        else:
            return f'<span class="{classname}">{content}</span>'

    # Match .classname[content] handling nested brackets
    pattern = r"\.(\w[\w-]*)\[((?:[^\[\]]*|\[(?:[^\[\]]*|\[[^\[\]]*\])*\])*)\]"
    return re.sub(pattern, replace_match, text)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_preprocessor.py -v -k "class_wrappers"`
Expected: All 7 tests PASS.

- [ ] **Step 5: Commit**

```bash
git add preprocessor.py tests/test_preprocessor.py
git commit -m "add .classname[content] wrapper conversion"
```

---

### Task 6: Full Preprocessing Pipeline

**Files:**
- Modify: `preprocessor.py`
- Modify: `tests/test_preprocessor.py`

- [ ] **Step 1: Write failing test for the combined pipeline**

Append to `tests/test_preprocessor.py`:
```python
from preprocessor import process_slide


def test_process_slide_full():
    slide = """class: center, middle
# Title
.big[**Important**]

--

More content

???

Speaker notes here"""
    html_content, classes = process_slide(slide)
    assert classes == ["center", "middle"]
    assert "Speaker notes" not in html_content
    assert "Important" in html_content
    assert "More content" in html_content
    assert "???" not in html_content
    assert '<span class="big">' in html_content or '<div class="big">' in html_content
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_preprocessor.py::test_process_slide_full -v`
Expected: FAIL — `ImportError`

- [ ] **Step 3: Implement `process_slide`**

Add to `preprocessor.py`:
```python
import markdown


def process_slide(slide_md: str) -> tuple[str, list[str]]:
    """Full preprocessing pipeline for a single slide.

    Returns (rendered_html, css_classes).
    """
    # 1. Extract class directive
    content, classes = strip_class_directive(slide_md)

    # 2. Strip presenter notes
    content = strip_presenter_notes(content)

    # 3. Strip incremental reveals
    content = strip_incremental_reveals(content)

    # 4. Convert .classname[] wrappers
    content = convert_class_wrappers(content)

    # 5. Render markdown to HTML
    # md_in_html extension allows markdown inside <div markdown="1"> blocks
    # produced by convert_class_wrappers for block-level .classname[] usage
    md = markdown.Markdown(
        extensions=["fenced_code", "codehilite", "tables", "md_in_html"],
        extension_configs={
            "codehilite": {"css_class": "highlight", "guess_lang": False}
        },
    )
    html = md.convert(content)

    return html, classes
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_preprocessor.py -v`
Expected: All tests PASS.

- [ ] **Step 5: Commit**

```bash
git add preprocessor.py tests/test_preprocessor.py
git commit -m "add full slide preprocessing pipeline"
```

---

### Task 7: Image Path Rewriting

**Files:**
- Modify: `preprocessor.py`
- Modify: `tests/test_preprocessor.py`

- [ ] **Step 1: Write failing tests**

Append to `tests/test_preprocessor.py`:
```python
from preprocessor import rewrite_image_paths


def test_rewrite_relative_image_paths():
    html = '<img alt="Photo" src="images/photo.png" />'
    result = rewrite_image_paths(html)
    assert 'src="/lecture_notes/images/photo.png"' in result


def test_rewrite_leaves_absolute_paths():
    html = '<img alt="Photo" src="/examples/week_1/image.png" />'
    result = rewrite_image_paths(html)
    assert 'src="/examples/week_1/image.png"' in result


def test_rewrite_leaves_external_urls():
    html = '<img alt="Comic" src="https://imgs.xkcd.com/comics/exploits.png" />'
    result = rewrite_image_paths(html)
    assert 'src="https://imgs.xkcd.com/comics/exploits.png"' in result


def test_rewrite_does_not_touch_script_src():
    html = '<script src="navigation.js"></script>'
    result = rewrite_image_paths(html)
    assert result == html
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_preprocessor.py -v -k "rewrite"`
Expected: FAIL — `ImportError`

- [ ] **Step 3: Implement `rewrite_image_paths`**

Add to `preprocessor.py`:
```python
def rewrite_image_paths(html: str) -> str:
    """Rewrite relative image src paths to absolute /lecture_notes/ paths.
    Only affects <img> tags, not <script> or other elements.
    """
    def replace_img_src(match):
        prefix = match.group(1)
        src = match.group(2)
        if src.startswith(("http://", "https://", "/")):
            return match.group(0)
        return f'<img{prefix}src="/lecture_notes/{src}"'

    return re.sub(r'<img([^>]*)src="([^"]*)"', replace_img_src, html)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_preprocessor.py -v -k "rewrite"`
Expected: All 4 tests PASS.

- [ ] **Step 5: Commit**

```bash
git add preprocessor.py tests/test_preprocessor.py
git commit -m "add image path rewriting for slide output"
```

---

### Task 8: Jinja2 Templates

**Files:**
- Create: `templates/base.html`
- Create: `templates/slide.html`
- Create: `templates/page.html`
- Create: `templates/index.html`
- Create: `templates/lecture_index.html`

- [ ] **Step 1: Create `templates/base.html`**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{% block title %}Web Development{% endblock %}</title>
    <link rel="stylesheet" href="/css/style.css">
</head>
<body>
    <nav id="header">
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/lecture_notes/">Lectures</a></li>
            <li><a href="/syllabus/">Syllabus</a></li>
            <li><a href="/examples/">Examples</a></li>
        </ul>
    </nav>
    <main>
        {% block content %}{% endblock %}
    </main>
    {% block scripts %}{% endblock %}
</body>
</html>
```

- [ ] **Step 2: Create `templates/slide.html`**

```html
{% extends "base.html" %}

{% block title %}Week {{ week }} — Slide {{ slide_num }} | Web Development{% endblock %}

{% block content %}
<div class="slide-container {{ classes|join(' ') }}"
     data-prev="{{ prev_url }}"
     data-next="{{ next_url }}"
     data-first="{{ first_url }}"
     data-slide-num="{{ slide_num }}"
     data-total-slides="{{ total_slides }}"
     data-week="{{ week }}">

    <div class="slide-nav">
        {% if prev_url %}
        <a href="{{ prev_url }}" class="nav-prev" aria-label="Previous slide">&larr;</a>
        {% else %}
        <span class="nav-prev disabled">&larr;</span>
        {% endif %}

        <span class="slide-info">Week {{ week }} &mdash; {{ slide_num }} / {{ total_slides }}</span>

        {% if next_url %}
        <a href="{{ next_url }}" class="nav-next" aria-label="Next slide">&rarr;</a>
        {% else %}
        <span class="nav-next disabled">&rarr;</span>
        {% endif %}
    </div>

    <div class="slide-content">
        {{ content }}
    </div>
</div>
{% endblock %}

{% block scripts %}
<script src="/js/navigation.js"></script>
{% endblock %}
```

- [ ] **Step 3: Create `templates/page.html`**

```html
{% extends "base.html" %}

{% block title %}{{ title }} | Web Development{% endblock %}

{% block content %}
<div class="page-content">
    {{ content }}
</div>
{% endblock %}
```

- [ ] **Step 4: Create `templates/index.html`**

```html
{% extends "base.html" %}

{% block title %}Web Development — MPCS 52553{% endblock %}

{% block content %}
<div class="homepage">
    <h1>Web Development</h1>
    <h3>MPCS 52553 — Spring 2026</h3>
    <ul>
        <li><a href="/syllabus/">Syllabus</a></li>
        <li><a href="/lecture_notes/">Lecture Notes</a></li>
        <li><a href="/examples/">Examples &amp; Labs</a></li>
    </ul>
    <p>
        Course materials are on
        <a href="https://github.com/UChicagoWebDev">GitHub</a>.
        Join <strong>#web-development</strong> on
        <a href="https://cs-uchicago.slack.com/">UChicago CS Slack</a>.
    </p>
</div>
{% endblock %}
```

- [ ] **Step 5: Create `templates/lecture_index.html`**

```html
{% extends "base.html" %}

{% block title %}Lecture Notes | Web Development{% endblock %}

{% block content %}
<div class="lecture-index">
    <h1>Lecture Notes</h1>
    <p>
        Lecture notes are written in
        <a href="https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax">Markdown</a>
        and can also be found
        <a href="https://github.com/UChicagoWebDev/course_materials/tree/main/lecture_notes">in the Course Materials repo on GitHub</a>.
    </p>
    <ul>
        {% for week in weeks %}
        <li><a href="/lecture_notes/week_{{ week }}/1/">Week {{ week }}</a></li>
        {% endfor %}
    </ul>
</div>
{% endblock %}
```

- [ ] **Step 6: Commit**

```bash
git add templates/
git commit -m "add Jinja2 templates for slides, pages, and indexes"
```

---

### Task 9: CSS Stylesheet

**Files:**
- Create: `static/css/style.css`

- [ ] **Step 1: Create `static/css/style.css`**

Port relevant rules from `lecture_notes/styles/style.css`, replacing `.remark-*` selectors with new structure. Key sections:

```css
/* Fonts */
@import url(https://fonts.googleapis.com/css?family=Yanone+Kaffeesatz);
@import url(https://fonts.googleapis.com/css?family=Droid+Serif:400,700,400italic);
@import url(https://fonts.googleapis.com/css?family=Droid+Sans:400,700,400italic);
@import url(https://fonts.googleapis.com/css?family=Ubuntu+Mono:400,700,400italic);

/* Base */
body {
    font-family: "Droid Serif", serif;
    background-color: white;
    margin: 0;
    min-width: 15em;
}

/* Navigation header */
#header {
    background-color: #333;
    font-family: "Droid Sans", sans-serif;
    padding: 0;
}
#header ul {
    display: flex;
    margin: 0;
    padding: 0;
    list-style: none;
}
#header li {
    padding: 0.25em 0.75em;
}
#header a, #header a:visited {
    color: white;
    text-decoration: none;
}
#header a:hover {
    color: #ccc;
}

/* Slide navigation bar */
.slide-nav {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0.5em;
    gap: 1em;
    font-family: "Droid Sans", sans-serif;
    border-bottom: 1px solid #eee;
}
.slide-nav a {
    text-decoration: none;
    color: #333;
    font-size: 1.5em;
}
.slide-nav .disabled {
    color: #ccc;
}
.slide-info {
    font-size: 0.9em;
    color: #666;
}

/* Slide content area */
.slide-container {
    max-width: 960px;
    margin: 0 auto;
    padding: 1em 2em;
}
.slide-content {
    padding: 1em 0;
}

/* Page content (syllabus, etc.) */
.page-content {
    max-width: 960px;
    margin: 0 auto;
    padding: 1em 2em;
}

/* Homepage */
.homepage {
    max-width: 960px;
    margin: 0 auto;
    padding: 2em;
}

/* Lecture index */
.lecture-index {
    max-width: 960px;
    margin: 0 auto;
    padding: 1em 2em;
}

/* Typography */
h1, h2, h3 {
    font-family: "Yanone Kaffeesatz", sans-serif;
    font-weight: normal;
}

/* Remark class ports */
.center { text-align: center; }
.middle { display: flex; flex-direction: column; justify-content: center; min-height: 60vh; }

.big { font-size: xx-large; font-family: "Yanone Kaffeesatz", sans-serif; }
.fancyStrong strong { font-size: xx-large; font-family: "Yanone Kaffeesatz", sans-serif; }

.credit {
    display: block;
    color: #aaa;
    text-decoration: none;
    font-size: 0.75em;
    text-align: center;
    padding: 0.25em;
}
.credit a { color: #aaa; }

.half img { max-width: 40%; max-height: 40%; }

.split ul {
    list-style-type: none;
    display: flex;
    padding: 0;
}
.split ul li {
    width: auto;
    max-width: 70%;
}
.split ul li img { max-width: 100%; }

.agenda h1 { margin-bottom: 0; }
.agenda ul { margin-block-start: 0; color: #666; }

.overlay p { position: relative; z-index: 1; padding: 1em; background: rgba(255,255,255,0.8); }
.overlay p:has(img) { z-index: 0; width: 100%; float: right; margin-bottom: -100%; }

.gallery p:has(img) { display: flex; flex-wrap: wrap; justify-content: center; }
.gallery p:has(img) img { height: 8em; margin: 1em; }

.gallery-big p:has(img) { display: flex; flex-wrap: wrap; justify-content: center; }
.gallery-big p:has(img) img { height: 16em; margin: 1em; }

.animate img {
    width: 210px;
    animation-duration: 3s;
    animation-name: rise;
}
@keyframes rise {
    from { margin-top: 60%; margin-left: 100%; }
    to { margin-top: 0%; }
}

.highlight-third-code-line .highlight pre code .line:nth-child(3) {
    font-weight: bold;
}

/* Images */
img {
    display: block;
    max-width: 80%;
    max-height: 80%;
}

/* Blockquotes */
blockquote p {
    border-left: 0.5em solid lightgray;
    padding-left: 0.5em;
}
blockquote footer {
    font-size: small;
    color: gray;
}

/* Code blocks */
code, pre {
    font-family: "Ubuntu Mono", monospace;
}
code {
    background-color: lightblue;
    padding: 2px 5px;
}
pre code {
    display: block;
    padding: 1em;
    overflow-x: auto;
}
```

- [ ] **Step 2: Commit**

```bash
mkdir -p static/css
git add static/css/style.css
git commit -m "add site stylesheet ported from remark CSS"
```

---

### Task 10: Navigation JavaScript

**Files:**
- Create: `static/js/navigation.js`

- [ ] **Step 1: Create `static/js/navigation.js`**

```javascript
document.addEventListener("DOMContentLoaded", function () {
    const container = document.querySelector(".slide-container");
    if (!container) return;

    const prevUrl = container.dataset.prev;
    const nextUrl = container.dataset.next;
    const firstUrl = container.dataset.first;

    document.addEventListener("keydown", function (e) {
        // Don't navigate if user is typing in an input
        if (e.target.tagName === "INPUT" || e.target.tagName === "TEXTAREA") return;

        switch (e.key) {
            case "ArrowRight":
            case "ArrowDown":
                if (nextUrl) window.location.href = nextUrl;
                break;
            case "ArrowLeft":
            case "ArrowUp":
                if (prevUrl) window.location.href = prevUrl;
                break;
            case "Home":
                if (firstUrl) window.location.href = firstUrl;
                e.preventDefault();
                break;
        }
    });
});
```

- [ ] **Step 2: Commit**

```bash
mkdir -p static/js
git add static/js/navigation.js
git commit -m "add keyboard navigation for slides"
```

---

### Task 11: Build Script

**Files:**
- Create: `build.py`
- Create: `tests/test_build.py`

- [ ] **Step 1: Write integration test**

`tests/test_build.py`:
```python
import os
import shutil
from pathlib import Path
from build import build_site


def test_build_produces_output(tmp_path, monkeypatch):
    """Smoke test: build produces _site/ with expected structure."""
    monkeypatch.chdir(Path(__file__).parent.parent)
    build_site(output_dir=str(tmp_path / "_site"))
    site = tmp_path / "_site"

    assert (site / "index.html").exists()
    assert (site / "syllabus" / "index.html").exists()
    assert (site / "lecture_notes" / "index.html").exists()
    assert (site / "lecture_notes" / "week_1" / "1" / "index.html").exists()
    assert (site / "css" / "style.css").exists()
    assert (site / "js" / "navigation.js").exists()
    assert (site / "examples").is_dir()
    assert (site / "lecture_notes" / "images").is_dir()


def test_build_slide_has_navigation(tmp_path, monkeypatch):
    """Slide pages include navigation data attributes."""
    monkeypatch.chdir(Path(__file__).parent.parent)
    build_site(output_dir=str(tmp_path / "_site"))

    slide = (tmp_path / "_site" / "lecture_notes" / "week_1" / "2" / "index.html").read_text()
    assert 'data-prev=' in slide
    assert 'data-next=' in slide
    assert 'data-slide-num="2"' in slide


def test_build_no_week_8_old(tmp_path, monkeypatch):
    """week_8_old.md should not produce output."""
    monkeypatch.chdir(Path(__file__).parent.parent)
    build_site(output_dir=str(tmp_path / "_site"))

    assert not (tmp_path / "_site" / "lecture_notes" / "week_8_old").exists()
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_build.py -v`
Expected: FAIL — `ImportError: cannot import name 'build_site'`

- [ ] **Step 3: Implement `build.py`**

```python
import glob
import os
import re
import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader
import markdown

from preprocessor import split_slides, process_slide, rewrite_image_paths


def build_site(output_dir: str = "_site"):
    """Build the entire static site."""
    root = Path(__file__).parent
    out = Path(output_dir)

    # Clean output
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    # Set up Jinja2
    env = Environment(loader=FileSystemLoader(root / "templates"))

    # Copy static assets
    shutil.copytree(root / "static" / "css", out / "css")
    shutil.copytree(root / "static" / "js", out / "js")
    shutil.copytree(root / "examples", out / "examples")
    shutil.copytree(root / "lecture_notes" / "images", out / "lecture_notes" / "images")

    # Find week files (exclude _old files)
    week_files = sorted(glob.glob(str(root / "lecture_notes" / "week_*.md")))
    week_files = [f for f in week_files if "_old" not in f]

    weeks = []

    for week_file in week_files:
        week_num = int(re.search(r"week_(\d+)", week_file).group(1))
        weeks.append(week_num)

        md_content = Path(week_file).read_text()
        slide_strings = split_slides(md_content)

        total_slides = len(slide_strings)
        week_dir = out / "lecture_notes" / f"week_{week_num}"

        for i, slide_md in enumerate(slide_strings, 1):
            html_content, classes = process_slide(slide_md)
            html_content = rewrite_image_paths(html_content)

            prev_url = f"/lecture_notes/week_{week_num}/{i - 1}/" if i > 1 else ""
            next_url = f"/lecture_notes/week_{week_num}/{i + 1}/" if i < total_slides else ""
            first_url = f"/lecture_notes/week_{week_num}/1/"

            slide_html = env.get_template("slide.html").render(
                content=html_content,
                classes=classes,
                week=week_num,
                slide_num=i,
                total_slides=total_slides,
                prev_url=prev_url,
                next_url=next_url,
                first_url=first_url,
            )

            slide_dir = week_dir / str(i)
            slide_dir.mkdir(parents=True, exist_ok=True)
            (slide_dir / "index.html").write_text(slide_html)

    # Lecture notes index
    lecture_index_html = env.get_template("lecture_index.html").render(weeks=weeks)
    lectures_dir = out / "lecture_notes"
    lectures_dir.mkdir(parents=True, exist_ok=True)
    (lectures_dir / "index.html").write_text(lecture_index_html)

    # Syllabus
    syllabus_md = (root / "syllabus.md").read_text()
    md_renderer = markdown.Markdown(
        extensions=["fenced_code", "codehilite", "tables"],
        extension_configs={
            "codehilite": {"css_class": "highlight", "guess_lang": False}
        },
    )
    syllabus_html = md_renderer.convert(syllabus_md)
    page_html = env.get_template("page.html").render(
        title="Syllabus", content=syllabus_html
    )
    syllabus_dir = out / "syllabus"
    syllabus_dir.mkdir(parents=True, exist_ok=True)
    (syllabus_dir / "index.html").write_text(page_html)

    # Homepage
    homepage_html = env.get_template("index.html").render()
    (out / "index.html").write_text(homepage_html)


if __name__ == "__main__":
    build_site()
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_build.py -v`
Expected: All 3 tests PASS.

- [ ] **Step 5: Run full build and check output**

Run: `python build.py && python -m http.server -d _site 8080 &`

Manually verify:
- `http://localhost:8080/` — homepage loads
- `http://localhost:8080/lecture_notes/` — week listing
- `http://localhost:8080/lecture_notes/week_1/1/` — first slide, arrow keys work
- `http://localhost:8080/syllabus/` — syllabus renders
- `http://localhost:8080/examples/` — examples directory listing
- Images display correctly on slides

- [ ] **Step 6: Add `_site/` to `.gitignore`**

Append to `.gitignore`:
```
_site/
```

- [ ] **Step 7: Commit**

```bash
git add build.py tests/test_build.py .gitignore
git commit -m "add build script for static site generation"
```

---

### Task 12: GitHub Actions Workflow

**Files:**
- Create: `.github/workflows/build-and-deploy.yml`

- [ ] **Step 1: Create workflow file**

`.github/workflows/build-and-deploy.yml`:
```yaml
name: Build and Deploy

on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: python build.py
      - uses: actions/upload-pages-artifact@v3
        with:
          path: _site

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
```

- [ ] **Step 2: Commit**

```bash
git add .github/workflows/build-and-deploy.yml
git commit -m "add GitHub Actions workflow for Pages deployment"
```

---

### Task 13: End-to-End Verification

- [ ] **Step 1: Run all tests**

Run: `python -m pytest tests/ -v`
Expected: All tests pass.

- [ ] **Step 2: Build the site**

Run: `python build.py`
Expected: `_site/` directory created with all expected files.

- [ ] **Step 3: Manual browser check**

Run: `python -m http.server -d _site 8080`

Check:
- Homepage renders and links work
- Lecture notes index lists all weeks
- Slides render with correct content (no remark syntax visible)
- Keyboard navigation works (arrow keys, Home)
- Images display correctly
- Code blocks have syntax highlighting
- Syllabus page renders
- Examples directory is browsable
- CSS classes from remark (`.big`, `.half`, `.credit`, `.split`, etc.) render correctly

- [ ] **Step 4: Stop server, final commit if any fixes needed**
