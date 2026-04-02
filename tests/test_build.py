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
