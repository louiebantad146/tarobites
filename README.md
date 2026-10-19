# Taro Bites

A responsive Taro Bites storefront powered by PyScript in the browser. The page
and shopping-bag interactions are implemented in Python in `public/app.py`;
Vite serves the static assets and styles during development and builds the
production site.

## Run locally

Install the JavaScript development dependencies and start Vite:

```sh
npm install
npm run dev
```

Open the local URL printed by Vite. PyScript is loaded from its CDN, so the
browser needs network access to run the Python application.

## Build

```sh
npm run build
npm run preview
```

The production site is written to `dist/`. The PyScript source and other files
in `public/` are copied into the build output.
