# Module: Deployment & best practices

> **Environment variables**, **Docker**, **Docker Compose**, and a concise **CI/CD** overview — plus a **production checklist** and **quiz**

This module teaches how to move a Django app from **local development** toward **production**: keeping secrets out of git (**python-decouple** / `.env`), **containerizing** the app, orchestrating **web + database + reverse proxy** with Compose, and automating **test → build → deploy** with a pipeline (e.g. **GitHub Actions**).

You can apply the patterns to **`[deployment_project](deployment_project/)`** (JWT + Books API, same stack as Auth, under this module), or to **[CBV](../CBV/cbv_project/)**, **[AUTH](../AUTH/auth_project/)**, or any Django project you already have.

---

## What's inside

```
DEPLOYMENT/
├── README.md                        # This file
├── deployment_project/              # Sample Django project: JWT + books API, .env, Docker, requirements.txt
├── deployment-best-practices.html   # Interactive guide (GitHub Pages)
└── styles/index.css                 # Module-specific layout (pipeline, env cards, checklist, …)
```

CI for that sample app: `.github/workflows/deployment-project-ci.yml` (check, migrate SQLite, tests).

Shared chrome (header, nav, typography, code blocks, quizzes) comes from the repo root: [`styles/`](../styles/), [`scripts/header.js`](../scripts/header.js).

---

## Learning path (guide sections)

| Section | Description |
|---------|-------------|
| **Overview** | Production-oriented stack: config, WSGI, reverse proxy, containers, automation |
| **Environment variables** | `python-decouple`, `.env`, `.gitignore`, wiring `settings.py` (e.g. `DEBUG`, `SECRET_KEY`, database) |
| **Docker** | Sample `Dockerfile`, layer caching (`requirements.txt` before app code), `.dockerignore` |
| **Compose** | Dev vs production `docker-compose.yml` (volumes, networking, `depends_on`, Nginx) |
| **CI/CD** | Example workflow: tests, build image, push registry, deploy; `needs:` between jobs |
| **Checklist** | Interactive checklist — config, DB, containers, TLS, CI/CD, monitoring |
| **Quiz** | Multiple-choice questions on decouple, Docker layers, Compose networking, pipelines |

---

## Key concepts covered

- **Twelve-factor style config** — secrets and environment-specific values in the environment, not in source control  
- **python-decouple** — `config()`, casts (`bool`, `Csv`), priority: OS env → `.env` → defaults  
- **Docker images** — multi-stage patterns, cache-friendly layer order, non-root user where appropriate  
- **Docker Compose** — services, networks, volumes; internal DNS (`db` as hostname); dev vs prod differences  
- **Reverse proxy** — Nginx terminating TLS, serving static files, proxying to Gunicorn  
- **CI/CD** — failing tests block deploy; secrets in CI (e.g. GitHub Secrets), not in workflow YAML  

---

## View the guide

- **On GitHub Pages:** [Deployment & best practices](https://ndevu12.github.io/learn-django/DEPLOYMENT/deployment-best-practices.html)  
- **Locally:** from the repository root, open `DEPLOYMENT/deployment-best-practices.html` in a browser **or** run `python -m http.server` from the repo root and open the same path in the URL (so `../styles/` and `../scripts/` resolve correctly).

---

## Applying this module to a project

1. Use `DEPLOYMENT/deployment_project`, or another sample app (e.g. `CBV/cbv_project` or `AUTH/auth_project`).  
2. Walk through the guide section by section: add `.env`, adjust `settings.py`, then introduce a `Dockerfile` and `docker-compose.yml` as shown.  
3. Use the **checklist** before calling an environment “production ready.”  
4. Adapt the sample **GitHub Actions** YAML to your repo name, registry, and host.

The guide references a **Books**-style API for continuity with other modules; the same steps apply to other apps.

---

## Related documentation

- **Root README:** [../README.md](../README.md) — full learning journey, repo layout, running CBV/Auth projects  
- **Interactive guide:** [deployment-best-practices.html](deployment-best-practices.html)  
- **Django deployment checklist:** [Deployment checklist (Django docs)](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/)  
- **Gunicorn:** [https://docs.gunicorn.org/](https://docs.gunicorn.org/)  
- **Docker Compose:** [https://docs.docker.com/compose/](https://docs.docker.com/compose/)  

---

## Contributing

Improvements to the HTML guide, checklist items, or this README are welcome via the main repository [Contributing](../README.md#contributing) process. Keep styling consistent with other modules (shared `styles/` + `header.js`, module-specific rules only in `DEPLOYMENT/styles/index.css`).
