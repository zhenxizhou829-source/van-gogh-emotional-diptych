# Layout and Caption

Use this reference only after the painting is complete. It governs the editorial wrapper and caption, never the meaning or composition of the generated painting. Do not feed the ivory ground, outer cells, caption, or diptych layout into the image-generation prompt.

## Equal-cell layout contract

The finished work contains exactly two equal-sized outer cells. Think of them as two pages of one editorial spread:

- the source cell contains the unchanged photograph edge-to-edge;
- the interpretation cell is warm ivory and contains a smaller same-ratio painting plus one caption;
- both cells have exactly the source photo's width and height;
- no gutter, decorative rule, frame, shadow, or third region is inserted between them.

The painting's breathing room belongs to the interpretation cell, not inside the generated image. Never letterbox, pillarbox, crop, extend, or pad either image to reconcile aspect ratios.

### Left–right

Default for strongly portrait photos. Place the source cell on the left and the equal-sized interpretation cell on the right.

- Measure the caption first, then set the painting's scale from the source ratio, short edge, and remaining height. More unusual portrait ratios receive proportionally more breathing room.
- Center the painting horizontally and place it in the upper portion of the cell.
- Reserve clear space below for the caption; align the caption to the painting's left edge, allowing it to use the remaining cell width when a narrow image would otherwise force unreadably small type.

### Top–bottom

Default for landscape and square photos. Place the source cell above and the equal-sized interpretation cell below.

- Measure the clockwise caption first, then set painting scale, margins, and title gap from the source ratio, short edge, and remaining width. More unusual landscape ratios receive proportionally more breathing room.
- At the common 3:2 baseline, the painting uses about 75% of the cell width, with balanced 12.5% upper and lower margins. The painting-plus-caption group is centered horizontally, while retaining at least 7.5% side clearance; other ratios vary continuously from that relationship.
- Set the caption clockwise immediately to the right of the painting, with its first letter aligned to the painting's upper edge. Use a measured breathing gap rather than anchoring it to the cell's outer edge.

The values are visual baselines, not fixed templates: the solver measures the actual caption and adapts each inset without changing the equal-cell structure, source pixels, or painting aspect ratio.

## Caption contract

Write one original English micro-title:

- two to six words;
- grounded in visible content, spatial relation, light, weather, posture, time, or material force;
- compressed and concrete rather than ornate;
- able to hold the primary emotion and counter-state when possible;
- when a meaning-bearing revelation is essential to the painting, it must echo the revelation's relation or force rather than name an unrelated object;
- never a quotation, artwork-title imitation, diagnosis, claim about the subject's inner life, date, or location label.

Prefer a concrete noun plus motion, light plus place, or a visible relationship. Avoid generic titles such as *A Beautiful Moment*, *Dreamy Night*, *Golden Memories*, and *Silent Beauty*.

## Composition command

Run:

```bash
python3 scripts/compose_diptych.py SOURCE INTERPRETATION OUTPUT --title "English Title" --layout auto
```

Name `OUTPUT` with the exact title plus `.png`, for example `White Weight, Light Veil.png` for `--title "White Weight, Light Veil"`; do not use numbered names such as `diptych1.png`.

Prefer PNG to avoid JPEG recompression after composition. The script accepts common source modes and normalizes both source and interpretation to RGB; it applies no crop, resize, or tonal adjustment to the source after that normalization. `auto` chooses `left-right` for strongly portrait sources and `top-bottom` otherwise. The finished canvas is exactly `2 × source width` by `source height` for left–right, or `source width` by `2 × source height` for top–bottom.

Use the original photo file for `SOURCE`, never a preview, screenshot, or model output. Use the image model's painting-only file for `INTERPRETATION`. The script output is the only final deliverable.

The script applies no crop, filter, tonal adjustment, resampling, or internal padding to the normalized source. It rejects an interpretation whose aspect ratio differs by more than 1%, scales only the interpretation, and places the caption in the ivory cell. This separation is intentional: generated images may be expressive, but they are not trusted to preserve source geometry.

The script requires Pillow. Use the configured workspace Python when bare `python3` lacks it; do not install a duplicate runtime merely for this script. Use an explicit `--layout` only when the user requests an orientation or readability clearly requires an override.
