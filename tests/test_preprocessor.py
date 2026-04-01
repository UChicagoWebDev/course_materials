from preprocessor import split_slides, strip_class_directive, strip_presenter_notes, strip_incremental_reveals


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
    assert "---" in slides[0]


def test_split_slides_trims_whitespace():
    md = "# Slide 1\n\n---\n\n# Slide 2\n"
    slides = split_slides(md)
    assert slides[0].strip() == "# Slide 1"
    assert slides[1].strip() == "# Slide 2"


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
