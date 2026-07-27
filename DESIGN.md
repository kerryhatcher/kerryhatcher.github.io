# Design

<!-- impeccable:design-schema 1 -->

## Source of truth

This design is **inherited, not invented**: after three rounds of new-direction
exploration (minimalist concepts → instrument-panel concepts → calm-personality
concepts), Kerry rejected all of them and asked to keep the look of his
existing live site, kerryhatcher.com. The tokens below were extracted directly
from that site's rendered computed styles (via browser inspection on
2026-07-26), not guessed from a screenshot.

## Palette

Light theme (the site's only theme today — dark is a net-new addition for
this rebuild, derived from the same hue family rather than invented fresh):

- `--bg`: `oklch(0.975 0.008 252)` — page background. A cool, barely-blue
  near-white. Notably NOT the warm cream/sand band (hue 40-100) that reads as
  an AI-design cliché — this already avoids that trap.
- `--ink`: `oklch(0.22 0.04 252)` — body text and headings. Near-black with
  the same slight blue tint as the background, not a pure neutral gray.
- Accent: no distinct accent color was found in computed styles (header/
  footer/sections are all transparent over the same flat background — this
  is a genuinely single-toned site). `meta[name="theme-color"]` is `#161f30`
  (dark navy) but nothing on-page actually renders in that color — treat it
  as an unused artifact of the current site's template, not a confirmed brand
  color, unless Kerry confirms he wants it used.

Dark theme (new, derived): invert lightness while preserving the hue-252
tint family — e.g. `--bg` around `oklch(0.19 0.02 252)`, `--ink` around
`oklch(0.93 0.015 252)` — same family, not a different color scheme.

## Typography

- Font: **"Noto Sans"**, falling back to
  `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif`.
  One family for everything — body and headings — no serif/mono pairing on
  the current site.
- Base size: `18px` / line-height `28.8px` (1.6 ratio).
- H1: ~`73.6px`, weight `700`, same ink color as body (headings aren't a
  separate accent color).
- The homepage H1 is a first-person voice statement — "I write about
  whatever I'm digging into." — not a name/tagline. Worth preserving that
  personality-through-copy move rather than defaulting to "Kerry Hatcher —
  Software Engineer" as the headline.

## Layout & content patterns (from the live site)

- Header: a "K·H" logo mark + wordmark, nav links **Home** / **About** only.
- Hero: big first-person H1, then a location line ("Macon-Bibb County,
  Georgia"), then a short bio paragraph, then a count line ("43 pieces ·
  Newest first").
- Real bio (current, for reference — not necessarily final copy): "I'm a
  software engineer and a Macon-Bibb County resident. Most pieces here
  started as a question I wanted answered. The recurring subjects are civic
  data, local government, education, digital privacy, [...]"
- Real hero photo exists: `kerry-hero.jpg` — "Kerry Hatcher, smiling, in a
  checkered shirt, standing on a curb in front of a brick public school
  building."
- Post list: each entry shows a category tag (e.g. `bibb-schools`, `macon`,
  `BCSD`), title, one-line excerpt, date, and read time (e.g. "27 May 2026 ·
  7 min read"). Real recent post titles span both civic and technical
  subjects (see PRODUCT.md Evidence on Hand).
- Footer: email, GitHub, Atom feed link.
- No visible card borders/shadows, no accent color, no imagery beyond the
  hero photo and (per earlier survey) some post thumbnails — a genuinely
  quiet, text-forward layout.

## What changes in the rebuild vs. the live site

- Add a real dark/light toggle (feature already scoped in the project spec) —
  derived from the same palette family, not a new look.
- Astro + Tailwind implementation instead of the current platform, with tags/
  RSS/search per the original spec — visual look stays the same, technical
  foundation changes.
- "A little more flare than the current site" (Kerry's words) — within this
  same quiet, single-accent-free system, this likely means: more confident
  typographic scale/rhythm, maybe one deliberate accent used sparingly, and
  polish in spacing/motion — NOT a new visual world. Any such addition should
  be proposed narrowly and confirmed, not assumed.

## Open questions

- Whether the unused `#161f30` navy theme-color should become a real accent,
  or stay unused — undecided, ask before introducing it as a visible color.
- Exact "little more flare" additions — undecided, propose specific small
  moves (e.g. one accent color, refined type scale) rather than a broad
  reinterpretation.
