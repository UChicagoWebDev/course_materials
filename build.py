import argparse
import glob
import re
import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader
import markdown

from preprocessor import split_slides, process_slide, rewrite_image_paths
import site_config

QUARTER_PATTERN = re.compile(
    r"(Winter|Spring|Fall|Autumn|Summer)(\s+Quarter)?\s+\d{4}"
)
CANVAS_COURSE_PATTERN = re.compile(r"canvas\.uchicago\.edu/courses/\d+")

EXAMPLES_EXCLUDE_DIRS = {"__pycache__", "images"}
EXAMPLES_EXCLUDE_SUFFIXES = {".pyc"}


def build_examples_indexes(examples_root: Path, env, base_url: str):
    """Generate index.html pages for the examples tree.

    Walks examples/ recursively. For any directory without an existing
    index.html, renders one that lists its subdirectories and files.
    The top-level page lists each week; deeper pages list their contents.
    """
    template = env.get_template("examples_index.html")

    def is_hidden(p: Path) -> bool:
        return any(part.startswith(".") for part in p.relative_to(examples_root).parts)

    def is_excluded(p: Path) -> bool:
        return any(part in EXAMPLES_EXCLUDE_DIRS for part in p.relative_to(examples_root).parts)

    all_dirs = [examples_root, *sorted(p for p in examples_root.rglob("*") if p.is_dir())]
    for dirpath in all_dirs:
        if is_hidden(dirpath) or is_excluded(dirpath):
            continue
        if (dirpath / "index.html").exists():
            continue

        rel = dirpath.relative_to(examples_root)
        url_prefix = f"{base_url}/examples"
        if rel != Path("."):
            url_prefix += "/" + "/".join(rel.parts)

        entries = sorted(dirpath.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))
        dirs = [
            {"name": p.name, "url": f"{url_prefix}/{p.name}/"}
            for p in entries
            if p.is_dir()
            and p.name not in EXAMPLES_EXCLUDE_DIRS
            and not p.name.startswith(".")
        ]
        files = [
            {"name": p.name, "url": f"{url_prefix}/{p.name}"}
            for p in entries
            if p.is_file()
            and p.name != "index.html"
            and p.suffix not in EXAMPLES_EXCLUDE_SUFFIXES
            and not p.name.startswith(".")
        ]

        if rel == Path("."):
            title = "Examples"
            crumbs = []
            parent_url = ""
        else:
            title = "Examples — " + " / ".join(part.replace("_", " ") for part in rel.parts)
            crumbs = [{"name": "Examples", "url": f"{base_url}/examples/"}]
            accum = f"{base_url}/examples"
            for part in rel.parts[:-1]:
                accum += f"/{part}"
                crumbs.append({"name": part, "url": f"{accum}/"})
            crumbs.append({"name": rel.parts[-1], "url": ""})
            parent_parts = rel.parts[:-1]
            parent_url = f"{base_url}/examples/" + (
                "/".join(parent_parts) + "/" if parent_parts else ""
            )

        html = template.render(
            title=title, crumbs=crumbs, parent_url=parent_url, dirs=dirs, files=files
        )
        (dirpath / "index.html").write_text(html)


def apply_config(text: str) -> str:
    """Replace quarter and Canvas course ID references with current config values."""
    season, year = site_config.QUARTER.split()

    def replace_quarter(match):
        quarter_word = match.group(2) or ""
        return f"{season}{quarter_word} {year}"

    text = QUARTER_PATTERN.sub(replace_quarter, text)
    text = CANVAS_COURSE_PATTERN.sub(
        f"canvas.uchicago.edu/courses/{site_config.CANVAS_COURSE_ID}", text
    )
    return text


def update_source_files(root: Path):
    """Update source files in place with current config values."""
    files = [root / "README.md", root / "syllabus.md"]
    files.extend(sorted((root / "lecture_notes").glob("week_*.md")))

    for filepath in files:
        if not filepath.exists():
            continue
        content = filepath.read_text()
        updated = apply_config(content)
        if updated != content:
            filepath.write_text(updated)


def build_site(output_dir: str = "_site", base_url: str = ""):
    """Build the entire static site.

    base_url: path prefix for project sites (e.g., "/course_materials").
              Empty string for sites served at the domain root.
    """
    root = Path(__file__).parent
    out = Path(output_dir)

    # Update source files with current config values
    update_source_files(root)

    # Clean output
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    # Set up Jinja2 — autoescape=False since templates use {{ content }}
    # with pre-rendered HTML and this is a static site generator, not a web app
    env = Environment(loader=FileSystemLoader(root / "templates"), autoescape=False)
    env.globals["base_url"] = base_url
    env.globals["quarter"] = site_config.QUARTER
    env.globals["canvas_url"] = f"https://canvas.uchicago.edu/courses/{site_config.CANVAS_COURSE_ID}"

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
            html_content = rewrite_image_paths(html_content, base_url)

            prev_url = f"{base_url}/lecture_notes/week_{week_num}/{i - 1}/" if i > 1 else ""
            next_url = f"{base_url}/lecture_notes/week_{week_num}/{i + 1}/" if i < total_slides else ""
            first_url = f"{base_url}/lecture_notes/week_{week_num}/1/"

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

    # Examples index pages (top-level + per-week + per-subdir)
    build_examples_indexes(out / "examples", env, base_url)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build the static site.")
    parser.add_argument(
        "--base-url",
        default="",
        help="URL path prefix for project sites (e.g., /course_materials)",
    )
    args = parser.parse_args()
    build_site(base_url=args.base_url.rstrip("/"))
