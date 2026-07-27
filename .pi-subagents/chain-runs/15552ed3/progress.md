# Progress: Astro Rebuild Implementation Plan

## Task 1: Scaffold the Astro project with Tailwind CSS 4 ✅

- [x] Step 1: Scaffold a minimal Astro project
- [x] Step 2: Verify the scaffold
- [x] Step 3: Add Tailwind CSS 4
- [x] Step 4: Set the `site` config
- [x] Step 5: Install RSS, Typography, and Pagefind packages
- [x] Step 6: Write the design tokens and dark-mode variant
- [x] Step 7: Add postbuild script for Pagefind indexing
- [x] Step 8: Verify the build produces Tailwind output and a Pagefind index
- [x] Step 9: Commit

**Commit:** `88bd8cd` - feat: scaffold Astro project with Tailwind CSS 4 and design tokens

## Task 2: Content collections + placeholder content ✅

- [x] Step 1: Write the content collections config (`src/content.config.ts`)
- [x] Step 2: Write the placeholder blog post (`src/content/blog/hello-world.md`)
- [x] Step 3: Write the three placeholder project entries (`fieldnote.md`, `plumb.md`, `ledger-cli-tools.md`)
- [x] Step 4: Verify the build succeeds with no Zod schema errors
- [x] Step 5: Commit

**Commit:** `76b130a` - feat: add blog and projects content collections with placeholder entries

## Task 3: Site chrome — BaseLayout, Header, Footer, ThemeToggle ✅

- [x] Step 1: Write SocialLinks.astro
- [x] Step 2: Write ThemeToggle.astro
- [x] Step 3: Write Header.astro
- [x] Step 4: Write Footer.astro
- [x] Step 5: Write BaseLayout.astro
- [x] Step 6: Wire index.astro to BaseLayout temporarily
- [x] Step 7: Verify the build and dark mode toggle
- [x] Step 8: Commit

**Commit:** `a807814` - feat: add site chrome with dark-mode toggle

## Task 4: Homepage ✅

- [x] Step 1: Write TagPill.astro
- [x] Step 2: Write PostCard.astro
- [x] Step 3: Replace src/pages/index.astro with the homepage
- [x] Step 4: Verify the build includes the placeholder post
- [x] Step 5: Commit

**Commit:** `0ba8668` - feat: build homepage with recent-posts list

**Notes:**
- Build succeeded. `Hello, world` confirmed in `dist/index.html`.
- Pagefind indexed 1 page (the homepage).
- TagPill and PostCard components created for reuse in Tasks 5 and 6.

## Task 5: Blog list, individual post, and tag archive pages ✅

- [x] Step 1: Write PostLayout.astro
- [x] Step 2: Write blog/index.astro
- [x] Step 3: Write blog/[slug].astro
- [x] Step 4: Write blog/tags/[tag].astro
- [x] Step 5: Verify all three page types build and link correctly
- [x] Step 6: Commit

**Commit:** `02ef925` - feat: add blog list, post, and tag archive pages

**Notes:**
- Build succeeded. All 4 pages generated (blog list, hello-world post, meta tag archive, homepage).
- Pagefind indexed 4 pages.
- PostLayout created with prose styling via `@tailwindcss/typography` (prose dark:prose-invert).

## Task 6: About, Projects, Contact pages ✅

- [x] Step 1: Write the About page (`src/pages/about.astro`)
- [x] Step 2: Write the Projects page (`src/pages/projects.astro`)
- [x] Step 3: Write the Contact page (`src/pages/contact.astro`)
- [x] Step 4: Verify all three pages build
- [x] Step 5: Commit

**Commit:** `96ceb60` - feat: add about, projects, and contact pages

**Notes:**
- Build succeeded. 7 pages total now (homepage, about, projects, contact, blog list, hello-world post, meta tag archive).
- Pagefind indexed 7 pages.
- Projects page renders the 3 placeholder project entries (Fieldnote, plumb, ledger-cli-tools) in a 2-column grid.
- Contact page uses SocialLinks component and mailto: link.

## Task 7: RSS feed ✅

- [x] Step 1: Write the RSS endpoint (`src/pages/rss.xml.js`)
- [x] Step 2: Verify the feed builds and includes the placeholder post
- [x] Step 3: Commit

**Commit:** `7c3978a` - feat: add RSS feed

**Notes:**
- Build succeeded. 8 routes generated (7 pages + rss.xml).
- Pagefind indexed 7 pages (RSS is XML, not HTML, so not indexed).
- `Hello, world` confirmed in `dist/rss.xml`.

## Task 8: Search (Pagefind) and 404 page ✅

- [x] Step 1: Write the search page (`src/pages/search.astro`)
- [x] Step 2: Write the 404 page (`src/pages/404.astro`)
- [x] Step 3: Verify the build produces Pagefind assets
- [x] Step 4: Commit

**Commit:** `f0361f2` - feat: add Pagefind search page and 404 page

**Notes:**
- Build succeeded. 9 pages built (8 HTML pages + rss.xml).
- Pagefind indexed 9 pages.
- `dist/search/index.html` and `dist/404.html` both exist.
- `dist/pagefind/pagefind-ui.js` exists (Pagefind UI assets).

## Task 9: GitHub Actions deploy workflow ✅

- [x] Step 1: Write the deploy workflow (`.github/workflows/deploy.yml`)
- [x] Step 2: Verify the YAML is well-formed
- [x] Step 3: Commit
- [x] Step 4: Push to master

**Commit:** `6828370` - feat: add GitHub Actions workflow to deploy to GitHub Pages

**Notes:**
- YAML validated successfully with `python3 yaml.safe_load`.
- Pushed to `origin/master`. Push bypassed unsigned-commit rules (pre-existing across all chain commits).
- One-time manual step remains: set GitHub repo Settings → Pages → Source to "GitHub Actions".

## Task 10: Placeholder-content GitHub issues ✅

- [x] Step 1: Create `content` label
- [x] Step 2: Open 5 placeholder-content issues
- [x] Step 3: Verify the issues were created

**Issues created:**
- #15 — Replace placeholder homepage bio
- #16 — Replace the placeholder project entries
- #17 — Replace placeholder About page bio and add a photo
- #18 — Replace or delete the placeholder starter blog post
- #19 — Verify or replace placeholder contact details

**Notes:**
- All 5 issues have the `content` label (color: FBCA04, description: "Placeholder content that needs replacing with the real thing").
- No commit needed — this task creates GitHub metadata, not files.
