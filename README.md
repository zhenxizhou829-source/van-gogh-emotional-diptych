# Van Gogh Emotional Diptych

> Not a “Van Gogh filter.” This Codex skill learns from Van Gogh’s way of seeing: it paints not what things look like, but what they feel like.

**Van Gogh Emotional Diptych** turns one photograph into an editorial diptych. The original photograph stays intact; alongside it sits a separately constructed painting that makes the photograph’s underlying relation visible.

It is a Codex skill, designed for Codex and adaptable by compatible agents.

## Not style transfer

Most photo-to-Van-Gogh workflows preserve the scene and add a painterly surface. This skill takes the opposite route. It treats the photograph as **semantic evidence**, rather than a template for its crop, viewpoint, pose, object placement, or attention path.

The painting preserves only one to three anchors needed for the new image to remain recognisably connected to the source. It then rebuilds the source’s central relation as an independent scene. A person beside a rock, for example, may become an image about the tension between weight and lightness—not an oil-painted version of the same pose.

The governing order is deliberate:

```text
read the source → identify its felt world → construct a new scene → select one board → paint → compose → review
```

The reference board is unavailable until the new scene has been decided. This prevents familiar Van Gogh motifs from taking over a photograph that should remain specific to its own meaning.

## How it works

### 1. Read relations, not just objects

The skill reads visible evidence such as distance, pressure, repeated forms, light, wear, colour contrast, and gesture. It turns those signals into formal decisions: direction, scale, negative space, density, colour temperature, rhythm, resistance, or release.

Words such as “dreamlike” or “emotional” are not enough. The reconstruction must describe visible actions: compress, suspend, radiate, fracture, surround, fold, or open.

### 2. Choose one felt world

Every photograph is read through one governing relation—not a subject category or a generic mood preset. A flower may carry anxiety; a person may carry vitality. The right choice is the relation whose removal would damage the image’s meaning.

| Felt world | Core relation | Typical painterly action |
| --- | --- | --- |
| Turbulence | Force moves through the whole field. | Organise dispersed elements into a directional field and introduce resistance. |
| Anxiety | A relationship cannot settle. | Compress or interrupt space; make colour or direction collide locally. |
| Stillness | Calm remains alive. | Establish a stable centre with restrained contrast and continuous marks. |
| Hardship | Weight interrupts movement. | Make support, wear, enclosure, folds, or stagnation tangible. |
| Vitality | Life presses outward. | Build an expanding rhythm through ascent, branching, clustering, or growth. |

### 3. Construct the image before choosing the hand

Before any visual board is opened, the skill writes a new-scene treatment: the dominant force and counterforce, a changed spatial logic, what will be enlarged or removed, and which camera decisions will be discarded.

Only then does it select exactly one of the five curated boards. A board may guide brushwork, chromatic behaviour, mark direction, rhythm, density, and atmosphere. It may never supply a subject, layout, local coordinate, or recognisable Van Gogh quotation. The treatment decides **what** the painting is; the board helps decide **how the paint behaves**.

## What you receive

For each source photograph, the skill delivers one final PNG diptych:

- an untouched, edge-to-edge original photograph;
- a same-ratio painterly interpretation, independently constructed from the source;
- a short English micro-title and a concise viewer-facing phrase.

The two outer cells are equal in size. Portrait sources are normally arranged left to right, with the source on the left; landscape and square sources are normally arranged top to bottom. The painting sits on a warm ivory interpretation cell with its title. It is never asked to generate the split layout itself.

Final composition is deterministic rather than image-model generated. It preserves the normalized source pixels, rejects interpretations whose aspect ratio differs by more than 1%, and confines scaling and captioning to the interpretation cell.

## Use with Codex

1. Place this directory in a Codex-discoverable skills directory, such as `~/.codex/skills/van-gogh-emotional-diptych`.
2. Start a Codex task with a source photo and ask for an editorial Van Gogh diptych, or invoke `$van-gogh-emotional-diptych` explicitly.
3. Codex reads [`SKILL.md`](SKILL.md), then loads the linked guidance only when the relevant stage needs it.

Use this skill when you want an original interpretation of a photograph’s felt meaning. Do not use it when you need the original scene faithfully redrawn with an oil-paint surface.

## Review and repair

The question is not “Does it look like Van Gogh?” A successful result must show that:

- the output is a scripted diptych and the source remains intact;
- reconstruction happened before board selection;
- at least one decisive spatial property changed, together with scale, direction, density, colour, or intensity;
- the source-derived relation is visible before object recognition at normal display size;
- any Van Gogh association arises from the source’s relation, rather than inserted stock motifs.

Repairs are intentionally narrow: rerun the composition script for a packaging failure; regenerate only the painting for a semantic, construction, focus, or painterliness failure. A successful layer is not changed merely because another layer failed.

## Repository structure

```text
van-gogh-emotional-diptych/
├── .gitignore
├── SKILL.md                         # Runtime instructions and workflow gates
├── agents/
│   └── openai.yaml                  # Optional interface metadata
├── references/
│   ├── perceptual-translation.md    # Five felt worlds and their selection
│   ├── visual-grammar.md            # Visual evidence → painterly action
│   ├── boards/
│   │   ├── index.md                 # Delayed board-selection guidance
│   │   └── {anxiety, hardship, stillness,
│   │       turbulence, vitality}.png
│   ├── layout-and-caption.md        # Diptych and micro-title contract
│   ├── evaluation.md                # Final review criteria
│   └── failure-modes.md             # One-layer-at-a-time repairs
├── scripts/
│   └── compose_diptych.py           # Deterministic final composition
├── README.md                        # Human-facing project documentation
└── LICENSE.md                       # Human-facing legal terms
```

## Included materials and rights

Before publishing derivative work or adding source images, boards, or visual references, make sure you have the rights to share them. The repository license applies to this skill’s code and written instructions; it does not grant rights in third-party images or other material added to the project.

## License

Released under the [PolyForm Noncommercial License 1.0.0](LICENSE.md). Noncommercial use, study, modification, and redistribution are permitted under its terms. Commercial use or sale is not licensed; request a separate commercial license from Briar Shen before proceeding.
