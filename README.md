# Van Gogh Emotional Diptych

> Not a “Van Gogh filter.” A Codex skill that learns from Van Gogh’s way of seeing: it paints not what things look like, but what they feel like.

A Codex skill, designed for Codex and adaptable by compatible agents. It turns one source photograph into an editorial diptych: the original photograph remains untouched, while a separately constructed painting makes its underlying emotional relation visible.

This is **not** an image-to-image style-transfer skill. It does not repaint the photograph or preserve its camera view beneath Van Gogh-like brushwork. The painting is a new scene, built from the photograph's felt meaning; it borrows only controlled paint behaviour from one selected board.

## What it produces

For each source photograph, the skill delivers one composed PNG diptych containing:

- the untouched original photograph;
- an independently reconstructed painterly interpretation at the same aspect ratio;
- an English micro-title and a concise Chinese phrase that express the completed visual relation.

The source photograph supplies semantic anchors, not its crop, viewpoint, pose, spatial arrangement, or attention path.

## Use with Codex

1. Place this directory in a Codex-discoverable skills directory, such as `~/.codex/skills/van-gogh-emotional-diptych`.
2. Start a Codex task with a source photo and ask for an editorial Van Gogh diptych, or invoke `$van-gogh-emotional-diptych` explicitly.
3. Codex reads [`SKILL.md`](SKILL.md) for the operating instructions and follows its linked references when needed.

The skill is intentionally opinionated about the artistic outcome. Do not use it when the desired result is a faithful painterly restyle of the original photograph.

## Repository structure

```text
van-gogh-emotional-diptych/
├── .gitignore
├── SKILL.md                         # Runtime instructions for Codex
├── agents/
│   └── openai.yaml                  # Optional interface metadata
├── references/                      # Selectively loaded artistic and review guidance
│   ├── boards/
│   │   ├── index.md                 # Board-selection guidance
│   │   └── {anxiety, hardship, stillness,
│   │       turbulence, vitality}.png
│   ├── evaluation.md                # Review criteria
│   ├── failure-modes.md             # Targeted repair guidance
│   ├── layout-and-caption.md        # Final composition rules
│   ├── perceptual-translation.md    # Felt-world selection
│   └── visual-grammar.md            # New-scene construction
├── scripts/
│   └── compose_diptych.py           # Deterministic composition helper
├── README.md                        # Human-facing project documentation
└── LICENSE.md                       # Human-facing legal terms
```

## Design principles

- Reconstruct the photograph's inner relation rather than its visible arrangement.
- Choose the reference board only after defining the new scene.
- Borrow brushwork, colour behaviour, rhythm, and atmosphere—not subjects, compositions, or quotations.
- Use the supplied composition script for the final diptych rather than asking an image model to fabricate the layout.

## Included materials and rights

Before publishing derivative work or adding new source images, boards, or visual references, make sure you have the necessary rights to share them. The repository license applies to this skill's code and written instructions; it does not grant rights in third-party images or other material that may be added later.

## License

Released under the [PolyForm Noncommercial License 1.0.0](LICENSE.md). Noncommercial use, study, modification, and redistribution are permitted under its terms. Commercial use or sale is not licensed; request a separate commercial license from Briar Shen before proceeding.
