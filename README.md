# Learn Django With Ndevu

A hands-on **learning journey** for the **Django & Python Rwanda BootCamp** — from **CRUD with class-based views**, through **authentication, security, and REST APIs**, to **deployment and production practices**. The repository is a growing collection of **interactive documentation** (dark-themed, mobile-responsive, hosted on GitHub Pages), **runnable Django projects** where each topic needs them, **knowledge quizzes**, and **per-module READMEs** with setup and walkthroughs.

[![Deploy to GitHub Pages](https://github.com/Ndevu12/learn-django/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/Ndevu12/learn-django/actions/workflows/deploy-pages.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**Live site:** [https://ndevu12.github.io/learn-django](https://ndevu12.github.io/learn-django)

---

## Table of contents

- [Overview](#overview)
- [How this journey fits together](#how-this-journey-fits-together)
- [Learning roadmap](#learning-roadmap)
- [Modules](#modules)
- [Tech stack](#tech-stack)
- [Project structure](#project-structure)
- [Getting started](#getting-started)
- [Running the projects](#running-the-projects)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

This repository is built so you **read the guides, then run the code** (or apply deployment patterns to your own project). In general, each track includes:

- A **polished, interactive documentation page** with section navigation, diagrams, compare views, and a **quiz**
- A **fully working Django project** *when the topic needs one* (CRUD and Auth modules)
- A **module README** (`CBV/README.md`, `AUTH/README.md`, `DEPLOYMENT/README.md`) plus **project READMEs** inside `cbv_project/` and `auth_project/`

The same **Book** domain is used in **CBV** and **AUTH** so you see one idea evolve from server-rendered CRUD to a **secured REST API** with JWT and roles. The **deployment** module is documentation-first: you wire **python-decouple**, **Docker**, **Compose**, and **CI/CD** into the apps you already have (or any Django project).

---

## How this journey fits together

| Layer | What it is |
|--------|------------|
| **Landing page** | [`index.html`](index.html) — links to every module |
| **Interactive guides** | HTML guides under `CBV/`, `AUTH/`, `DEPLOYMENT/` — shared [`styles/`](styles/) + [`scripts/header.js`](scripts/header.js), optional `MODULE/styles/index.css` |
| **Django projects** | [`CBV/cbv_project/`](CBV/cbv_project/), [`AUTH/auth_project/`](AUTH/auth_project/) — migrate, seed, run locally |
| **Deployment track** | Guide + checklist + quiz — see [`DEPLOYMENT/README.md`](DEPLOYMENT/README.md) |

**Viewing guides locally:** open `index.html` from disk or run a static server from the repo root so relative paths resolve:

```bash
python -m http.server 8080
# http://127.0.0.1:8080/
```

---

## Learning roadmap

```
 Module 1                    Module 2                      Module 3
┌─────────────────────┐     ┌──────────────────────────┐     ┌──────────────────────────┐
│  CRUD with CBVs     │     │  Auth & Security         │     │  Deployment & practices  │
│                     │ ──▶ │                          │ ──▶ │                          │
│  • Django basics    │     │  • Django REST Framework │     │  • python-decouple / .env│
│  • Models & forms   │     │  • JWT authentication    │     │  • Docker & Compose      │
│  • Class-based views│     │  • Role-based access     │     │  • CI/CD (e.g. Actions)  │
│  • Templates & URLs │     │  • Permission classes    │     │  • Checklist & quiz      │
└─────────────────────┘     └──────────────────────────┘     └──────────────────────────┘
     runnable project            runnable project              guide + README (apply to your app)
```

*Possible next expansions:* deeper **testing** (unit/API), more **ops** topics — same patterns as existing modules.

---

## Modules

### 1. CRUD with class-based views

> Build a full **Create · Read · Update · Delete** workflow using Django’s generic CBVs.

| Section | What you'll learn |
|---------|-------------------|
| Overview | CRUD map, request → response flow, the `Book` model |
| Setup | Creating a Django project — venv, `startproject`, migrations |
| FBV → CBV | Side-by-side migration from function-based to class-based views |
| CBV deep-dive | `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView` |
| Templates | Auto template naming, `{% csrf_token %}`, template inheritance |
| URLs | `path()`, `reverse_lazy`, named routes, `LoginRequiredMixin` |
| Quiz | Multiple-choice questions with instant feedback |

**Project:** [`CBV/cbv_project/`](CBV/cbv_project/) — Book manager web app with five CBVs, `ModelForm`, templates, admin, and seed data.  
**Guide:** [CRUD with CBV (Pages)](https://ndevu12.github.io/learn-django/CBV/django-crud-cbv.html) · [CBV/README.md](CBV/README.md) · [CBV/cbv_project/README.md](CBV/cbv_project/README.md)

---

### 2. Auth & security

> Secure a **REST API** with **JWT**, **role-based access control**, and **protected endpoints**.

| Section | What you'll learn |
|---------|-------------------|
| Overview | Authentication vs authorization, session-based vs token-based auth |
| How JWT works | Header · payload · signature; access vs refresh tokens |
| Django + JWT | Installing `simplejwt`, settings, token endpoints |
| Role-based access | Custom `User` model with roles, permission classes |
| Protecting endpoints | Per-action permissions, object-level ownership checks |
| Common threats | XSS, CSRF, token theft, brute-force — mitigations |
| Quiz | Multiple-choice questions with instant feedback |

**Project:** [`AUTH/auth_project/`](AUTH/auth_project/) — Book REST API with JWT, roles (admin/editor/viewer), per-action permissions, and throttling.  
**Guide:** [Auth & security (Pages)](https://ndevu12.github.io/learn-django/AUTH/auth-security-guide.html) · [AUTH/README.md](AUTH/README.md) · [AUTH/auth_project/README.md](AUTH/auth_project/README.md)

---

### 3. Deployment & best practices

> **Secrets**, **containers**, **Compose**, and a concise **CI/CD** path from git push to production — with a **deploy checklist** and **quiz**.

| Section | What you'll learn |
|---------|-------------------|
| Overview | Production stack (decouple, Gunicorn, Nginx, Docker, Actions) |
| Environment variables | `python-decouple`, `.env`, `settings.py` patterns |
| Docker | Dockerfile layers, `.dockerignore`, build and run |
| Compose | Dev vs prod `docker-compose.yml`, networking, volumes |
| CI/CD | GitHub Actions-style workflow: test → build → deploy |
| Checklist | Config, database, containers, TLS, monitoring |
| Quiz | Env vars, Docker caching, Compose networking, pipelines |

**Project:** There is **no** separate `manage.py` tree under `DEPLOYMENT/`. Apply the guide to [`CBV/cbv_project/`](CBV/cbv_project/), [`AUTH/auth_project/`](AUTH/auth_project/), or your own Django app.  
**Guide:** [Deployment & best practices (Pages)](https://ndevu12.github.io/learn-django/DEPLOYMENT/deployment-best-practices.html) · **[DEPLOYMENT/README.md](DEPLOYMENT/README.md)**

---

## Tech stack

| Package | Purpose |
|---------|---------|
| **Django 6.0** | Web framework — models, views, templates, admin |
| **Django REST Framework** | API toolkit — serializers, viewsets, routers (Auth module) |
| **djangorestframework-simplejwt** | JWT — access/refresh tokens, blacklisting (Auth module) |
| **SQLite** | Development database (built-in) |
| **Pipenv** | Dependency management and virtual environments (repo root) |
| **GitHub Pages** | Hosting for the interactive documentation |
| **Deployment guide (concepts)** | `python-decouple`, Docker, Docker Compose, Gunicorn/Nginx, CI/CD |

---

## Project structure

```
learn-django/
├── index.html                  # GitHub Pages landing page
├── Pipfile                     # Python dependencies (shared)
├── Pipfile.lock
├── LICENSE
│
├── styles/                     # Shared design system (tokens, components, responsive)
├── styles/index.css            # Landing page
├── scripts/header.js           # Header, nav, showSection, quiz helpers
├── assets/                     # Static assets (e.g. instructors)
│
├── CBV/                        # Module 1: CRUD with class-based views
│   ├── README.md
│   ├── django-crud-cbv.html    # Interactive documentation
│   ├── styles/index.css        # Module-specific styles
│   │
│   └── cbv_project/            # Django 6.0 project
│       ├── manage.py
│       ├── cbv_project/        # Settings & root URL config
│       │   ├── settings.py
│       │   └── urls.py
│       └── books/
│           ├── models.py       # Book (title, author, pages, pub_date)
│           ├── views.py        # Five CRUD CBVs
│           ├── urls.py
│           ├── forms.py        # BookForm (ModelForm)
│           ├── admin.py
│           ├── management/commands/seed_books.py
│           └── templates/books/
│
├── AUTH/                       # Module 2: Auth & security
│   ├── README.md
│   ├── auth-security-guide.html
│   ├── styles/index.css
│   │
│   └── auth_project/           # Django 6.0 + DRF
│       ├── manage.py
│       ├── auth_project/
│       │   ├── settings.py     # JWT, throttle, DRF
│       │   └── urls.py
│       └── books/
│           ├── models.py       # Custom User (roles) + Book
│           ├── serializers.py
│           ├── permissions.py
│           ├── views.py
│           ├── urls.py
│           ├── admin.py
│           └── management/commands/seed_data.py
│
├── DEPLOYMENT/                 # Module 3: Deployment (guides; apply to your app)
│   ├── README.md               # Module overview & how to use the guide
│   ├── deployment-best-practices.html
│   └── styles/index.css
│
└── .github/workflows/
    └── deploy-pages.yml        # Deploy to GitHub Pages on push
```

---

## Getting started

### Prerequisites

- **Python 3.12+**
- **pipenv** (`pip install pipenv`)

### Installation

```bash
git clone https://github.com/Ndevu12/learn-django.git
cd learn-django
pipenv install
```

> **Pipenv note:** The shared `Pipfile` at the repo root manages dependencies for all modules.
>
> - `pipenv shell` activates the environment but **may reset your cwd** to the repo root — `cd` into the project folder afterwards.
> - `pipenv run <cmd>` runs a one-off command without activating (keeps your current directory).
> - `exit` deactivates the shell.

---

## Running the projects

Each runnable module has its own Django project. Use **different ports** if you run both at once.

| Module | Directory | Port | Seed command | Server command |
|--------|-----------|:----:|--------------|----------------|
| CBV | `CBV/cbv_project/` | 8000 | `python manage.py seed_books` | `python manage.py runserver` |
| Auth | `AUTH/auth_project/` | 8001 | `python manage.py seed_data` | `python manage.py runserver 8001` |

### Quick start (any runnable module)

```bash
pipenv shell
cd <MODULE_PATH>/          # e.g. CBV/cbv_project or AUTH/auth_project

python manage.py migrate
python manage.py <seed_command>
python manage.py runserver <port>
```

### Module 1 — CBV (port 8000)

```bash
cd CBV/cbv_project
python manage.py migrate && python manage.py seed_books
python manage.py runserver
```

| URL | Description |
|-----|-------------|
| `http://127.0.0.1:8000/books/` | Book list |
| `http://127.0.0.1:8000/books/new/` | Create a book |
| `http://127.0.0.1:8000/books/1/` | Book detail |
| `http://127.0.0.1:8000/books/1/edit/` | Edit a book |
| `http://127.0.0.1:8000/books/1/delete/` | Delete a book |
| `http://127.0.0.1:8000/admin/` | Django admin |

### Module 2 — Auth & security (port 8001)

```bash
cd AUTH/auth_project
python manage.py migrate && python manage.py seed_data
python manage.py runserver 8001
```

| URL | Method | Description |
|-----|--------|-------------|
| `http://127.0.0.1:8001/api/books/` | GET | List books (public) |
| `http://127.0.0.1:8001/api/books/` | POST | Create a book (editor/admin) |
| `http://127.0.0.1:8001/api/token/` | POST | Login — JWT access + refresh |
| `http://127.0.0.1:8001/api/token/refresh/` | POST | Refresh access token |
| `http://127.0.0.1:8001/api/admin/users/` | GET | List users (admin only) |

**Test users:** `admin_anna`, `editor_bob`, `viewer_cara` — password: `pass1234!`

```bash
curl -s -X POST http://localhost:8001/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username":"editor_bob","password":"pass1234!"}' | python3 -m json.tool
```

### Module 3 — Deployment

No server command in `DEPLOYMENT/` — follow **[DEPLOYMENT/README.md](DEPLOYMENT/README.md)** and the [interactive guide](https://ndevu12.github.io/learn-django/DEPLOYMENT/deployment-best-practices.html) to containerize and deploy **CBV** or **AUTH** (or your own project).

---

### Deeper documentation

- [CBV/cbv_project/README.md](CBV/cbv_project/README.md) — views, forms, templates, admin
- [AUTH/auth_project/README.md](AUTH/auth_project/README.md) — cURL guide, RBAC matrix, JWT config, permission classes
- [DEPLOYMENT/README.md](DEPLOYMENT/README.md) — deployment module overview and how to apply it

---

## Contributing

Contributions are welcome: guides, quizzes, styles, sample projects, or new modules.

1. Fork the repository  
2. Create a feature branch (`git checkout -b feature/your-topic`)  
3. Commit your changes with clear messages  
4. Push and open a Pull Request  

New modules should mirror existing ones: interactive HTML using shared `styles/` + `scripts/header.js`, optional `MODULE/styles/index.css`, and a **README** (plus a `manage.py` project if the topic needs runnable code).

---

## License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE).

---

<p align="center">
  Made for the <strong>Django & Python Rwanda BootCamp 2026</strong> by <a href="https://github.com/Ndevu12">Ndevu</a>
</p>
