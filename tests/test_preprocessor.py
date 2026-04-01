from preprocessor import split_slides, strip_class_directive, strip_presenter_notes, strip_incremental_reveals, convert_class_wrappers


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
    assert '<div class="animate"' in result
    assert "![Phil](images/phil.jpeg)" in result


def test_convert_class_wrappers_nested_brackets():
    text = ".big[text with [link](url)]"
    result = convert_class_wrappers(text)
    assert "[link](url)" in result


def test_no_class_wrappers():
    text = "Just normal markdown"
    result = convert_class_wrappers(text)
    assert result == "Just normal markdown"
