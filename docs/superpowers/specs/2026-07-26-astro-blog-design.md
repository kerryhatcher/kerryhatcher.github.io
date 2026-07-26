# Astro Personal Blog — Design

Date: 2026-07-26
Repo: `kerryhatcher/kerryhatcher.github.io`

## Context

This repo hosts Kerry's personal GitHub Pages site. It previously ran a full
Jekyll blog (posts on Python logging, Linux gaming, encrypted messaging,
CDNs, email providers, etc.), which was deliberately wiped clean in the
"fresh new site" commit. The repo is currently empty except for `.gitignore`.
This spec covers rebuilding it from scratch as an Astro site.

## Goals

- Personal-brand homepage (hero/bio) with a blog as one section of the site,
  not the whole site.
- Start with no migrated content — new posts going forward. Old Jekyll posts
  are not being ported.
- Deploy to GitHub Pages via GitHub Actions, since this is a
  `<username>.github.io` repo.
- Every piece of placeholder content ships with a tracked GitHub issue so it
  doesn't get forgotten.

## Non-goals

- Migrating old Jekyll posts/content.
- A working contact form (GitHub Pages has no backend — see Contact page
  below).
- CMS integration, comments, newsletter, analytics — none requested.

## Stack

- **Astro 5**, static output (`output: 'static'`, the default) — no SSR
  adapter, since GitHub Pages only serves static files.
- **Tailwind CSS 4**, installed via `astro add tailwind` (the Vite plugin
  path, not the legacy `@astrojs/tailwind` integration), plus
  `@tailwindcss/typography` for prose styling of rendered markdown.
- **Package manager**: npm.
- `astro.config.mjs`: `site: 'https://kerryhatcher.github.io'`. No `base` is
  needed because the repo name matches the `<username>.github.io` pattern.

## Content model

Defined in `src/content.config.ts` using the built-in `glob()` loader
(Astro 5's content-layer API):

- **`blog` collection** — `src/content/blog/*.md`
  - schema: `title: string`, `description: string`, `pubDate: date`,
    `updatedDate: date (optional)`, `tags: string[]`, `draft: boolean
    (optional, default false)`
- **`projects` collection** — `src/content/projects/*.md`
  - schema: `title: string`, `description: string`, `url: string
    (optional)`, `tags: string[]`, `image: string (optional)`

Using a content collection for projects (instead of hardcoding cards in a
page) keeps the two content types architecturally consistent and makes it
trivial to add/remove projects later.

## Routes

| Route | Purpose |
|---|---|
| `/` | Hero (photo placeholder, name, tagline, short bio), recent-posts preview, links to About/Projects/Contact |
| `/about` | Fuller bio |
| `/projects` | Grid of project cards from the `projects` collection |
| `/contact` | Email (`mailto:`) + social links. No backend form — see below |
| `/blog` | Paginated post list |
| `/blog/[slug]` | Individual post, rendered through `PostLayout` |
| `/blog/tags/[tag]` | Tag archive page |
| `/rss.xml` | RSS feed via `@astrojs/rss`, built from the `blog` collection |
| `/search` | Pagefind-powered client-side search UI |
| `404.astro` | Custom not-found page |

### Contact page caveat

GitHub Pages serves static files only — there is no server to receive form
submissions. `/contact` will use a plain `mailto:` link and social links for
v1. A real contact form would require a third-party form handler (e.g.
Formspree, Web3Forms) and is out of scope unless requested later.

## Components & layouts

- `BaseLayout.astro` — `<head>`/meta tags, nav, footer, and an inline
  dark-mode-init script (must run before paint to avoid a flash of the wrong
  theme).
- `PostLayout.astro` — wraps rendered markdown in the Tailwind Typography
  `prose` styling.
- `Header.astro`, `Footer.astro`, `ThemeToggle.astro`, `PostCard.astro`,
  `TagPill.astro`, `SocialLinks.astro`.

## Dark/light mode

Tailwind's `class`-strategy dark mode. A toggle button persists the user's
explicit choice to `localStorage`; absent a stored choice, the site follows
`prefers-color-scheme`. The init script lives in `<head>` (not deferred) so
theme is correct on first paint.

## Search

[Pagefind](https://pagefind.app/) indexes the built `dist/` output as a
postbuild step (`astro build && pagefind --site dist`). The `/search` page
mounts Pagefind's UI. This only works after a production build — during
`astro dev` the search page will show no results, which is expected and will
be noted in the page itself or dev docs.

## Deployment

`.github/workflows/deploy.yml` using the official `withastro/action` +
`actions/deploy-pages`, triggered on push to **`master`** (this repo's actual
default branch — not `main`, which is what most Astro deploy docs assume).
Repository Settings → Pages → Source must be set to "GitHub Actions".

## Placeholder content & issue tracking

This build ships with placeholder content in place of real copy/photos, so
the site is fully functional and demonstrable immediately. For every page or
section with placeholder content, a GitHub issue will be opened on this repo
(via `gh issue create`) describing exactly what needs to be replaced:

1. About page bio + photo
2. Projects — each placeholder project card (2–3 issues, one per project, or
   one issue covering all placeholder projects — decided at implementation
   time based on how distinct the placeholder projects are)
3. Contact page — email/social links to verify or replace
4. Starter blog post — placeholder post to replace or delete before the site
   is considered "real"

## Testing / verification

No unit test suite is warranted for a static content site. Verification is:

- `npm run build` succeeds with no errors.
- `npm run dev` — manually check home, about, projects, contact, a blog
  post, tag archive, RSS feed, search (after a build), and dark-mode toggle.
- Confirm the GitHub Actions workflow runs and deploys successfully once
  pushed.

## Open questions

None outstanding — all resolved during brainstorming.
