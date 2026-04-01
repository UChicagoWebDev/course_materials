import re

import markdown


def split_slides(markdown: str) -> list[str]:
    """Split markdown on --- slide boundaries, ignoring --- inside fenced code blocks."""
    slides = []
    current_slide = []
    in_code_block = False

    for line in markdown.split("\n"):
        stripped = line.strip()

        if stripped.startswith("```"):
            in_code_block = not in_code_block

        if stripped == "---" and not in_code_block:
            slides.append("\n".join(current_slide))
            current_slide = []
        else:
            current_slide.append(line)

    if current_slide:
        slides.append("\n".join(current_slide))

    return [s.strip() for s in slides if s.strip()]


def strip_class_directive(slide: str) -> tuple[str, list[str]]:
    """Remove 'class: ...' directive from top of slide. Returns (content, class_list)."""
    lines = slide.split("\n")
    if lines and lines[0].strip().startswith("class:"):
        class_line = lines[0].strip()
        class_str = class_line[len("class:"):].strip()
        classes = [c.strip() for c in class_str.split(",")]
        return "\n".join(lines[1:]), classes
    return slide, []


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
            break

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
            continue

        result.append(line)

    return "\n".join(result)


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
