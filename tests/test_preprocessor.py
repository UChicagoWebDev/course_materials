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
    assert "---" in slides[0]


def test_split_slides_trims_whitespace():
    md = "# Slide 1\n\n---\n\n# Slide 2\n"
    slides = split_slides(md)
    assert slides[0].strip() == "# Slide 1"
    assert slides[1].strip() == "# Slide 2"
