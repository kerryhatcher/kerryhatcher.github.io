# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Two audiences, both real: the tech community / peers (other software
engineers reading technical posts and project work), and a civic/local
audience — Macon-Bibb County constituents and anyone following Kerry's local
government, education, and civic-data writing. Kerry Hatcher is also the
site's author/owner, publishing his own writing and project history.

## Product Purpose

kerryhatcher.github.io is becoming the real, unified home for Kerry's
writing — both software engineering content and civic/local-government
writing currently living at kerryhatcher.com — replacing a previous Jekyll
site that was deliberately wiped clean. Content migration scope and timing
is undecided (see Evidence on Hand); the visual/structural rebuild is not
blocked on it.

## Positioning

Broader than a pure engineering blog: Kerry is a software engineer AND a
civically-engaged Macon-Bibb County resident. His real writing (at
kerryhatcher.com) spans both — tech posts (tooling, AI-assisted coding,
email privacy) alongside civic material (a Bibb County School District
budget analysis, a school board candidacy announcement, voter registration
verification, literacy initiatives). Voice is analytical yet accessible —
"thoughtful engineer-turned-advocate," not a narrow infra/security
specialist and not a generic templated portfolio. The mechanism is that it's
a genuine personal record (real posts, real projects, over time), now
carrying real civic weight, not just a hobby blog.

## Operating Context

- Hosted on GitHub Pages (`kerryhatcher.github.io`), static output only.
- Deployed via GitHub Actions (`withastro/action` + `actions/deploy-pages`)
  triggered on push to `master` — this repo's actual default branch.
- Content authored as Markdown in Astro content collections (`blog`,
  `projects`).
- Historical context: the repo previously ran a Jekyll blog with posts on
  Python logging, Linux gaming, encrypted messaging, CDNs, and email
  providers, plus a projects section (e.g. a Fire TV review). That content
  was removed in the "fresh new site" commit and is not being migrated.

## Capabilities and Constraints

- Fully static site — no backend/server. Every feature must work without one.
- No working contact form for v1; GitHub Pages can't receive form
  submissions. `/contact` uses a `mailto:` link and social links. A real form
  would require a third-party handler (e.g. Formspree) — undecided, deferred
  until requested.
- No CMS, comments, newsletter, or analytics — none requested.

## Brand Commitments

Name: Kerry Hatcher. No separate logo/wordmark beyond the current site's
"K·H" mark. Confirmed: the rebuild inherits kerryhatcher.com's real visual
system rather than adopting a new one — see DESIGN.md for the extracted
palette, typography, and layout tokens (light theme: cool near-white bg
`oklch(0.975 0.008 252)`, near-black ink `oklch(0.22 0.04 252)`, "Noto Sans"
throughout, no accent color, quiet text-forward layout).

## Evidence on Hand

kerryhatcher.github.io itself has no current real content (the old Jekyll
posts were wiped and are not being carried over as reference material). But
a real, currently-live site exists at kerryhatcher.com: ~43 posts, a real
bio ("a software engineer and a Macon-Bibb County resident... civic data,
local government, education, digital privacy"), a real hero photo, and a
light/minimal/grayscale, text-forward visual style with post thumbnails
(some custom imagery, some stock). Nav is just Home/About; footer has
email, GitHub, and an Atom feed. Whether and how much of that content
migrates here is explicitly undecided ("not sure if all of it will come
anyway") — placeholder content in this build is still placeholder and each
instance gets a tracked GitHub issue rather than being treated as final.

## Product Principles

- This site is becoming the real, unified home for Kerry's writing — civic
  and technical — not a tech-only side project; content migration scope is
  a separate, later decision from the structural/visual rebuild.
- Fully static: no feature may assume a server exists.
- Personal-brand home with the blog as one section, not a blog-only site.
- Every placeholder ships with a tracked GitHub issue — nothing silently
  passes as real content.
- Visual direction: inherit kerryhatcher.com's real look (see DESIGN.md),
  not a new design. After three rejected rounds of from-scratch direction
  exploration (too minimalist, then too busy, then still not right), Kerry
  chose to keep the current site's look rather than replace it. "A little
  more flare" than today should be pursued as small, specific, confirmed
  additions within that same system — not a broad reinterpretation.
