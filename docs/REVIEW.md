# Repository review — 2026-11-02

The structural check reports 17 pages (16 exercises plus the new gallery), 76 existing local references, and zero missing assets or basic metadata issues. It verifies linked HTML/CSS files and images, page title, html language and viewport declarations.

Added an index gallery and English root README with module navigation. Added the missing credit-card page title and tag-definition viewport declaration. Existing exercise styles and local image assets remain unchanged. A standard-library scripts/check_assets.py makes the structural checks repeatable.

The review did not claim browser screenshot comparisons, accessibility certification or cross-device layout verification. Existing module-directory colons prevent ordinary Windows checkouts; the README documents that limitation rather than silently renaming all historical paths. Form examples are static and have no backend. No hosting or GitHub Pages configuration was changed.
