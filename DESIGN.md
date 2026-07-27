# Design

<!-- impeccable:design-schema 1 -->

## Source of truth

This design is a **replacement visual world** chosen through the Impeccable shape process (2026-07-26). After four rounds of exploration — three previous from-scratch attempts that were rejected, then a fourth that landed — Kerry chose the **Zine / DIY Punk** direction in a **dark mode, gold accent** iteration. The incumbent design (inherited from kerryhatcher.com) is replaced; this document records the new system.

## World

A hand-assembled zine — cut-and-paste, photocopied, stapled. Raw, authentic, independent publishing energy. Not polished, not institutional — real. The site reads like Issue #001 of a personal zine published from Macon, GA.

## Palette

### Dark mode (primary — the default scene is a reader at night, on a phone or laptop, in low ambient light)

- `--bg`: `#0d1117` — page background. Deep, near-black navy.
- `--card`: `#111622` — card/surface background. Slightly lighter than page.
- `--ink`: `#e6edf3` — headings and primary text. Bright, high contrast.
- `--body`: `#c9d1d9` — body text. Slightly softer than headings.
- `--line`: `#30363d` — borders and rules. Subtle, structural.
- `--accent`: `#d4a843` — gold. The complementary accent (blue's complement is amber/gold). Used for K·H logo, tag labels, highlight blocks, hover states, and interactive elements. Like foil stamping on a dark press.
- `--muted`: `#8b949e` — secondary text, metadata, dates.

### Light mode (derived — same zine system, inverted)

- `--bg`: `#e8ecf0` — cool silver-gray page.
- `--card`: `#f4f6f8` — card surface.
- `--ink`: `#1a2a4a` — deep navy headings.
- `--body`: `#2a3a5a` — body text.
- `--line`: `#c4cbd4` — borders.
- `--accent`: `#d4a843` — gold carries over, same value.
- `--muted`: `#6a7a8a` — secondary text.

## Typography

- **Primary face:** `"Courier New", "IBM Plex Mono", "JetBrains Mono", "Cascadia Code", ui-monospace, monospace` — monospace throughout. The zine voice: typewriter, cut-and-paste, DIY.
- **Headings:** All-caps, monospace, bold weight. Letter-spacing: `0.02em` to `0.05em` depending on size.
- **Body:** Sentence case, monospace. Size: `14px`–`16px` depending on surface. Line-height: `1.6`–`1.7`.
- **Display max:** `2rem` (32px) for hero headlines. The zine format is intimate, not monumental.
- **Measure:** Body text constrained to `65ch` max-width for readability.

## Layout & Composition

- **Borders:** Chunky `2px` or `3px` solid borders on cards, nav buttons, and containers. No border-radius (or minimal `2px` where needed).
- **Rotation:** Post cards and some containers have slight rotation (`-0.5deg` to `0.5deg`) — the hand-cut paste-up feel. Applied sparingly, not to every element.
- **Staple marks:** Small circles at top-center and bottom-center of the main zine container.
- **Dashed borders:** Used for the bio box and other "handwritten" annotation areas.
- **Tag pills:** Rendered as `[tag]` in gold, no background fill, just brackets.
- **Highlight blocks:** Gold background behind key text (e.g., "DIGGING INTO" in the hero).
- **Nav buttons:** Chunky bordered rectangles with gold hover (invert: gold bg, dark text).

## Components

### Header
- K·H logo in gold, monospace, bold, letter-spaced
- Nav items as bordered buttons: `border: 2px solid var(--line)`, gold hover inverts
- Theme toggle styled as a bordered button matching nav

### Hero (homepage)
- "Issue #001 · Macon, GA" tag in gold, small, tracked
- Headline: all-caps monospace, bold, with one key phrase in a gold highlight block
- Location + piece count: bordered pill tags
- Bio: dashed border box with gold `►` prefix

### Post Card
- Chunky `2px` solid border
- Slight rotation (alternating directions)
- `[tag]` label in gold at top
- Title in bold monospace
- Date + read time in muted text
- Hover: border color shifts to gold

### Footer
- Top border in `var(--line)`
- Links in muted monospace, gold hover
- Email, GitHub, RSS

## Motion

One authored moment: **paper settling** — on page load, the main zine container has a subtle settle animation (slight vertical bounce + rotation settle, ~400ms, ease-out). All other transitions are simple hover state inversions (border color, background color swaps, ~150ms).

## States

- **Hover:** Gold border or gold background inversion on interactive elements
- **Focus:** Gold outline (`2px solid var(--accent)`) with slight offset
- **Active:** Slight scale-down (`transform: scale(0.97)`) on buttons
- **Dark/light:** Toggle switches between the two palette sets above. Default respects `prefers-color-scheme`.

## What changed from the incumbent design

- Complete visual replacement: from quiet, text-forward, single-toned Noto Sans system → bold, dark, monospace zine with gold accent
- Added: dark mode as primary, gold accent, chunky borders, rotation, staple marks, DIY cut-and-paste feel
- Removed: Noto Sans, cool near-white bg, no-accent-color restraint, inherited kerryhatcher.com look
- Preserved: content, function, static site constraints, dark/light toggle, Astro + Tailwind foundation
