---
name: van-gogh-emotional-diptych
description: "Turn one photo into an editorial Van Gogh diptych by rebuilding its felt meaning as a new painting, then borrowing one board only for brushwork and colour behaviour."
---

# Van Gogh Emotional Diptych

Create an editorial diptych: the untouched photograph records what was seen; the painting independently constructs what that encounter felt like. This is not image-to-image stylisation. The source photo is **semantic evidence**, never a staging, camera, or layout template.

## Non-negotiable principle

Do not paint the things in the photograph. Paint the image's inner relation—its tension, emotion, metaphor, pressure, colour condition, or contradiction—using a newly constructed pictorial event.

The painting may retain only the few source cues needed for recognition. It must not retain the camera crop, viewpoint, figure pose, subject scale, background geometry, object positions, or attention path merely because they appear in the photograph. A result that can be described as “the original photo with painterly brushwork” is a failed generation, regardless of technical quality.

## Delivery

Show one finished composed diptych per source photo. Save each composed PNG with its exact English micro-title as the filename, for example `White Weight, Light Veil.png`, rather than a numbered name. On the same output line, place the exact English micro-title and one short Chinese phrase directly after each inline image, separated by ` —— ` and `，`—for example, `![White Weight, Light Veil](/absolute/path/White Weight, Light Veil.png) —— White Weight, Light Veil，暗室中被凝视托住的温暖人脸。` The Chinese phrase distills the completed reconstruction into its felt visual relation; it is a concise viewer-facing essence, not a record of reasoning, a prompt, or a process explanation. Keep detailed analysis, treatments, boards, raw paintings, and repairs private. For multiple inputs, pair each image with its matching title-and-phrase on the same line; never merge inputs into one image or return a contact sheet.

## Required sequence

`source reading → felt-world reading → independent reconstruction → board selection → painting → layout → review`

The board is unknown during the first three stages. Do not open, inspect, name, or borrow from any board until the independent reconstruction has been completed in words.

### 1. Read the source, not a style reference

Look at the source photo alone. Record internally:

- observable signals: gesture, distance, pressure, absence, repeated rhythm, light, and colour relation;
- the relation those signals enact;
- the emotional kernel or implicit metaphor: what the image makes the viewer feel before they name its objects;
- one to three semantic anchors that must remain for the new image to still belong to this source.

Then read [references/perceptual-translation.md](references/perceptual-translation.md) to select one governing felt world. Use it only to sharpen the reading, never as a mood preset, visual template, or source of objects.

### 2. Write an independent reconstruction, then discard the camera map

Before seeing a board, write a 4–7 sentence internal **new-scene treatment**. It is a scene to paint, not an edit list for the photograph. It must state:

- the felt proposition: “make ___ visible as ___”;
- the new dominant mass or force, its counterweight, and the first place the eye lands;
- a newly organised spatial relation that makes the kernel larger than the literal things;
- how light, colour, intensity, direction, density, contour, and quiet make the pressure visible;
- what is omitted, merged, displaced, enlarged, or reduced;
- the source-traceable visual consequence that makes the latent relation suddenly legible.

Use [references/visual-grammar.md](references/visual-grammar.md) here. It should help invent the most expressive formal behaviour for this particular source, not supply a style.

The treatment must explicitly abandon the source's camera map. Name the original crop, scale, placement, depth relation, or background arrangement that will no longer survive. Construct a new one instead. Preserve semantic anchors, not photographed coordinates.

The treatment passes only if it describes a visual order that could not be overlaid onto the source. “Keep the portrait/scene and alter its colours or marks” fails. Do not create a separate decorative surprise; the surprise must be the consequence of making the hidden relation visible.

### 3. Borrow the hand only after the new scene exists

Now select exactly one board from [references/boards/index.md](references/boards/index.md). Its only job is to guide exposed brushwork, chromatic construction, mark direction, rhythm, density, and atmosphere.

The board cannot introduce a subject, motif, layout, local coordinate, or Van Gogh quotation. If it changes the new-scene treatment, reject it. The treatment decides **what the painting is**; the board helps decide **how the paint behaves**.

### 4. Generate a painting from the new scene

Generate only the painterly interpretation at the source aspect ratio. It must contain no photo panel, ivory ground, caption, frame, split screen, logo, or watermark.

Make the generation prompt lead with the new scene's dominant relation and spatial construction—not a request to transform, repaint, preserve, or stylise the source photograph. Mention only the source anchors needed to carry the meaning. Do not reintroduce camera-level facts the treatment discarded.

Reject smooth academic modelling, brown glazing, sepia ageing, preset filters, uniform swirls, polished photorealism, copied Van Gogh compositions, and cosmetic treatment of faces, clothing, or backgrounds.

### 5. Compose and review

Use [references/layout-and-caption.md](references/layout-and-caption.md) only after the painting succeeds. Assemble the untouched source and the final painting with `scripts/compose_diptych.py`; the script output, not an image-model collage, is the user-facing deliverable.

Review at ordinary display size with [references/evaluation.md](references/evaluation.md). If the painting repeats the original camera view, do not repair it with more texture or colour: return to the new-scene treatment and regenerate. For a specific failure, read [references/failure-modes.md](references/failure-modes.md) and repair only that layer.
