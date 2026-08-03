# Buhane.com.tr

Static bilingual company website for Buhane Information Technologies. The site presents Buhane's services, live product portfolio, company story, and contact channels in English and Turkish.

## Snapshot

| Metric | Value |
|--------|-------|
| Founded | 2018 |
| Products launched | 10 |
| Platforms | 3 |
| Apps | 4 |
| Games | 3 |
| Service areas | 6 |
| Languages | English, Turkish |

## Live Products

### Platforms

| Product | URL | Summary |
|---------|-----|---------|
| THECOSMICMETA.com | https://thecosmicmeta.com/ | AI-powered technology content platform. |
| U2M.io | https://u2m.io | Smart URL shortener for clean, trackable links. |
| HiveDue | https://hivedue.com/ | Community finance management platform. |

### Apps

| Product | URL | Summary |
|---------|-----|---------|
| Vynix | https://vynix.app | AI video and art studio with access to premium AI models. |
| MoodJot | https://moodjot.app | Mood tracking journal with AI-powered emotional insights. |
| AstralPost | https://astralpost.app/ | Ritual journaling app for cosmic reflections and anonymous connection. |
| Lastimo | https://lastimo.app/ | Private factual tracker for remembering the last time something happened. |

### Games

| Product | URL | Summary |
|---------|-----|---------|
| Gridzle | https://gridzle.app/ | Counts-first puzzle strategy game with offline levels. |
| Glow Spin | https://glowspin.app/ | Rhythm reflex game with spinning ring color-matching mechanics. |
| Swipe Slip | https://swipeslip.app/ | Fast-paced tunnel runner focused on precision and timing. |

## Services

- Software design and development
- Consultancy
- E-commerce solutions
- AI services
- Digital marketing
- Digital content

## Project Structure

```text
.
|-- index.html                   # English landing page
|-- tr/index.html                # Turkish landing page
|-- styles.css                   # Shared visual system
|-- script.js                    # Shared browser interactions
|-- images/                      # Logos, service images, icons, and product assets
|-- app-ads.txt                  # App advertising declaration
|-- yandex_abc334285efd6c2e.html # Domain verification
`-- .planning/                  # GSD project planning artifacts
```

## Local Preview

Serve the project from the repository root so Turkish root-relative paths resolve correctly:

```bash
python3 -m http.server 8000
```

Then open:

- English: http://localhost:8000/
- Turkish: http://localhost:8000/tr/

## Maintenance Notes

- Update both `index.html` and `tr/index.html` for shared content changes.
- Keep product names, links, stats, and footer entries synchronized across languages.
- Prefer stable local assets in `images/` for product icons.
- Preserve `app-ads.txt` and `yandex_abc334285efd6c2e.html` in deployments.

## Repository

Canonical remote:

```text
https://github.com/abutun/buhane.com.tr.git
```
