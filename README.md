# HTML & CSS Lab

**Sixteen static page exercises, with a browsable gallery.**

By [Nikita Kozchenko](https://github.com/Nk0shey) · HTML · CSS · No build step

[Gallery](index.html) · [Run locally](#run-locally) · [Checks](#checks) · [Review](docs/REVIEW.md)

A coursework collection covering text formatting, lists, layout, menus, tables and forms. The gallery groups the original exercises into cards so a visitor can find and open each page.

## Run locally

From the repository root:

```sh
python3 -m http.server 8000
```

Open `http://localhost:8000/` in a browser. On Windows, the interpreter may be named `python`. Python is only a convenient local file server; the pages themselves are HTML/CSS and need no Python runtime. Opening `index.html` directly also works for these local pages.

The original module directories contain colons, which are supported on Linux/macOS but not normal Windows checkout paths. Windows users need to rename those directories and update the gallery links, or use a Linux filesystem. This review preserves the historical folder names.

## Exercises

- Module 01: Romeo and Juliet typography, card-game display and HTML tutorial.
- Module 02: fruit list, to-do list and tag definition.
- Module 03: product cards, vertical menu, page structure and footer.
- Module 04: table layout, dropdown menu and subscription cards.
- Module 06: credit-card, library and registration forms.

The forms and links are interface exercises. They do not provide account creation, payment processing or a persistent application backend. Use fictional values in demonstrations.

## Checks

Requires Python 3 for the optional repository check:

```sh
python3 scripts/check_assets.py
```

The check examines HTML/CSS local references and basic page metadata. It currently verifies **17 pages** (16 exercises plus the gallery), **76 local references**, page titles, language attributes and viewport metadata with zero issues.

These are structural checks, not browser screenshot comparisons, accessibility certification or a responsive-layout audit. The review added a missing page title and viewport declaration; it did not redesign the individual exercises. See [review notes](docs/REVIEW.md).
