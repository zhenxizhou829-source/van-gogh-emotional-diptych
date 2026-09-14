#!/usr/bin/env python3
"""Compose two equal editorial cells: source plus inset interpretation."""

from __future__ import annotations

import argparse
import math
from pathlib import Path
import sys

from PIL import Image, ImageDraw, ImageFont, ImageOps


IVORY = "#F3EFE5"
INK = "#26231E"
RATIO_TOLERANCE = 0.01


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Place a source photo and smaller same-ratio interpretation in equal cells."
    )
    parser.add_argument("source", type=Path)
    parser.add_argument("interpretation", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--title", required=True)
    parser.add_argument(
        "--layout",
        choices=("auto", "top-bottom", "left-right"),
        default="auto",
    )
    parser.add_argument("--font", type=Path)
    parser.add_argument("--background", default=IVORY)
    parser.add_argument("--quality", type=int, default=95)
    return parser.parse_args()


def load_rgb(path: Path) -> Image.Image:
    with Image.open(path) as image:
        return ImageOps.exif_transpose(image).convert("RGB")


def choose_layout(width: int, height: int, requested: str) -> str:
    if requested != "auto":
        return requested
    return "left-right" if height / width >= 1.18 else "top-bottom"


def clamp(value: float, lower: float, upper: float) -> float:
    return max(lower, min(value, upper))


def aspect_pressure(ratio: float, reference: float) -> float:
    """Return a continuous 0–1 measure of distance from an editorial baseline."""
    return clamp(abs(math.log(ratio / reference)) / math.log(2), 0.0, 1.0)


def validate(source: Image.Image, interpretation: Image.Image, title: str) -> None:
    source_ratio = source.width / source.height
    interpretation_ratio = interpretation.width / interpretation.height
    error = abs(source_ratio - interpretation_ratio) / source_ratio
    if error > RATIO_TOLERANCE:
        raise ValueError(
            f"Interpretation aspect ratio differs from source by {error:.1%}; "
            "regenerate it at the source ratio instead of cropping."
        )
    words = title.split()
    if not 2 <= len(words) <= 6:
        raise ValueError("Title must contain two to six English words.")
    if any(char in title for char in "\n\r"):
        raise ValueError("Title must be one line.")


def font_candidates(explicit: Path | None) -> list[Path]:
    candidates = []
    if explicit:
        candidates.append(explicit)
    candidates.extend(
        [
            Path("/System/Library/Fonts/Supplemental/Baskerville.ttc"),
            Path("/System/Library/Fonts/Supplemental/Georgia.ttf"),
            Path("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"),
        ]
    )
    return candidates


def load_font(explicit: Path | None, size: int) -> ImageFont.ImageFont:
    for path in font_candidates(explicit):
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def fit_title_font(
    draw: ImageDraw.ImageDraw,
    title: str,
    explicit: Path | None,
    initial_size: int,
    max_width: int,
) -> ImageFont.ImageFont:
    size = initial_size
    while size >= 12:
        font = load_font(explicit, size)
        box = draw.textbbox((0, 0), title, font=font)
        if box[2] - box[0] <= max_width:
            return font
        size -= 2
    return load_font(explicit, 12)


def resize_interpretation(image: Image.Image, width: int) -> Image.Image:
    height = round(width * image.height / image.width)
    return image.resize((width, height), Image.Resampling.LANCZOS)


def vertical_title_image(title: str, font: ImageFont.ImageFont) -> Image.Image:
    measure = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    box = measure.textbbox((0, 0), title, font=font)
    title_image = Image.new("RGBA", (box[2] - box[0], box[3] - box[1]))
    ImageDraw.Draw(title_image).text(
        (-box[0], -box[1]), title, fill=INK, font=font
    )
    return title_image.transpose(Image.Transpose.ROTATE_270)


def compose_top_bottom(
    source: Image.Image,
    interpretation: Image.Image,
    title: str,
    font_path: Path | None,
    background: str,
) -> Image.Image:
    width, cell_height = source.size
    ratio = width / cell_height
    pressure = aspect_pressure(ratio, 1.5)
    short_edge = min(width, cell_height)
    side_clearance = max(24, round(short_edge * (0.075 + 0.015 * pressure)))
    title_gap = max(16, round(short_edge * (0.05 + 0.015 * pressure)))
    title_size = max(18, round(short_edge * (0.038 + 0.004 * pressure)))
    target_scale = 0.75 - 0.05 * pressure
    measure = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    font = fit_title_font(
        measure, title, font_path, title_size, round(cell_height * target_scale)
    )
    vertical_title = vertical_title_image(title, font)
    target_width = round(width * target_scale)
    available_width = width - 2 * side_clearance - title_gap - vertical_title.width
    height_limited_width = round(
        cell_height * target_scale * interpretation.width / interpretation.height
    )
    inset_width = max(1, min(target_width, available_width, height_limited_width))
    inset = resize_interpretation(interpretation, inset_width)
    canvas = Image.new("RGB", (width, cell_height * 2), background)
    canvas.paste(source, (0, 0))
    group_width = inset.width + title_gap + vertical_title.width
    inset_x = (width - group_width) // 2
    inset_y = cell_height + (cell_height - inset.height) // 2
    canvas.paste(inset, (inset_x, inset_y))
    title_x = inset_x + inset.width + title_gap
    title_y = inset_y
    canvas.paste(
        vertical_title, (title_x, title_y), vertical_title
    )
    return canvas


def compose_left_right(
    source: Image.Image,
    interpretation: Image.Image,
    title: str,
    font_path: Path | None,
    background: str,
) -> Image.Image:
    source_width, height = source.size
    ratio = source_width / height
    pressure = aspect_pressure(ratio, 2 / 3)
    short_edge = min(source_width, height)
    top_margin = max(24, round(height * (0.065 + 0.015 * pressure)))
    footer = max(30, round(height * (0.085 + 0.02 * pressure)))
    title_gap = max(16, round(short_edge * (0.03 + 0.01 * pressure)))
    title_size = max(22, round(short_edge * (0.039 + 0.004 * pressure)))
    target_width = round(source_width * (0.76 - 0.04 * pressure))
    measure = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    initial_font = fit_title_font(measure, title, font_path, title_size, source_width)
    title_box = measure.textbbox((0, 0), title, font=initial_font)
    title_height = title_box[3] - title_box[1]
    available_height = height - top_margin - title_gap - title_height - footer
    height_limited_width = round(
        available_height * interpretation.width / interpretation.height
    )
    inset_width = max(1, min(target_width, height_limited_width))
    inset = resize_interpretation(interpretation, inset_width)
    canvas = Image.new("RGB", (source_width * 2, height), background)
    canvas.paste(source, (0, 0))
    inset_x = source_width + (source_width - inset.width) // 2
    inset_y = top_margin
    canvas.paste(inset, (inset_x, inset_y))
    draw = ImageDraw.Draw(canvas)
    max_title_width = source_width - (inset_x - source_width) - max(24, short_edge // 14)
    font = fit_title_font(draw, title, font_path, title_size, max_title_width)
    draw.text((inset_x, inset_y + inset.height + title_gap), title, fill=INK, font=font)
    return canvas


def main() -> int:
    args = parse_args()
    try:
        source = load_rgb(args.source)
        interpretation = load_rgb(args.interpretation)
        validate(source, interpretation, args.title)
        layout = choose_layout(source.width, source.height, args.layout)
        if layout == "top-bottom":
            result = compose_top_bottom(
                source, interpretation, args.title, args.font, args.background
            )
        else:
            result = compose_left_right(
                source, interpretation, args.title, args.font, args.background
            )
        args.output.parent.mkdir(parents=True, exist_ok=True)
        save_kwargs = {}
        if args.output.suffix.lower() in {".jpg", ".jpeg"}:
            save_kwargs = {"quality": args.quality, "subsampling": 0}
        result.save(args.output, **save_kwargs)
        print(f"Wrote {args.output} ({result.width}x{result.height}, {layout})")
        return 0
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
