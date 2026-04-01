import re


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
