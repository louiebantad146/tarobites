# Taro Bites

A responsive storefront whose page rendering and interactions run in Python
with PyScript in the browser.

## Run locally

From the project folder, start Python's built-in static file server:

```sh
python -m http.server 8000
```

Open <http://localhost:8000>. The PyScript runtime is loaded from its CDN, so
the browser needs network access. Python's HTTP server only serves the files;
the storefront logic runs as Python in the browser.

The source files are `public/app.py` (application), `src/App.css` (styles),
and `index.html` (the small page shell that loads PyScript).
