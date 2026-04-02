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

    # Set up Jinja2 — autoescape=False since templates use {{ content }}
    # with pre-rendered HTML and this is a static site generator, not a web app
    env = Environment(loader=FileSystemLoader(root / "templates"), autoescape=False)

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
