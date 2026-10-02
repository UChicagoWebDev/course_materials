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


def test_build_base_url(tmp_path, monkeypatch):
    """base_url is prefixed on all internal links."""
    monkeypatch.chdir(Path(__file__).parent.parent)
    build_site(output_dir=str(tmp_path / "_site"), base_url="/course_materials")
    site = tmp_path / "_site"

    # Homepage links use base_url
    homepage = (site / "index.html").read_text()
    assert 'href="/course_materials/syllabus/"' in homepage

    # Slide navigation uses base_url
    slide = (site / "lecture_notes" / "week_1" / "2" / "index.html").read_text()
    assert 'data-prev="/course_materials/lecture_notes/week_1/1/"' in slide
    assert "/course_materials/js/navigation.js" in slide
    assert "/course_materials/css/style.css" in slide

    # Lecture index uses base_url
    lecture_index = (site / "lecture_notes" / "index.html").read_text()
    assert "/course_materials/lecture_notes/week_1/1/" in lecture_index


def test_fill_template_vars(monkeypatch):
    """{{ NAME }} placeholders use site_config values; other braces are untouched."""
    import site_config
    from build import fill_template_vars

    monkeypatch.setattr(site_config, "CANVAS_COURSE_ID", "12345")
    text = (
        "https://canvas.uchicago.edu/courses/{{CANVAS_COURSE_ID}}/ "
        "{{ QUARTER }} {{ UNKNOWN_NAME }} {{ message }}"
    )
    assert fill_template_vars(text) == (
        f"https://canvas.uchicago.edu/courses/12345/ "
        f"{site_config.QUARTER} {{{{ UNKNOWN_NAME }}}} {{{{ message }}}}"
    )


def test_build_fills_markdown_template_vars(tmp_path, monkeypatch):
    """Built slides contain site_config values, not raw placeholders."""
    import site_config

    monkeypatch.chdir(Path(__file__).parent.parent)
    build_site(output_dir=str(tmp_path / "_site"))

    week_dir = tmp_path / "_site" / "lecture_notes" / "week_1"
    slides = "".join(p.read_text() for p in week_dir.glob("*/index.html"))
    assert "{{CANVAS_COURSE_ID}}" not in slides
    assert f"canvas.uchicago.edu/courses/{site_config.CANVAS_COURSE_ID}" in slides
