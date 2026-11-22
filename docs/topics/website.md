# website

**The public site for OccupySaaS** -- "Reclaiming the software ecosystem, one
open-source project at a time." Plain static HTML/CSS/JS with no build step.

- Repository: <https://github.com/occupysaas/website>
- Pinned here: `projects/website`
- Licence: Apache-2.0
- Live at: <https://occupysaas.com>

## What it is

A single static page served from GitHub Pages, with CSS and a small script for
mobile navigation, GitHub star counts and scroll reveal. There is no build step:
open it with any static server, or push and let Pages serve it.

```
index.html            the page
assets/css/site.css   styles (black / white / protest red)
assets/js/site.js     mobile nav, GitHub star counts, scroll reveal
assets/img/           logo, crowd silhouette, favicon, social card
```

## Working on it

```bash
python3 -m http.server 8000   # then open http://localhost:8000
```

Publishing is GitHub Pages on the `main` branch, with the custom domain set by
the repository's `CNAME` file.

## Clean room

The website carries no third-party vendor source and needs no clean-room
boundary beyond its licence. See the umbrella's note,
[clean-room/website](../clean-room/website.md).
