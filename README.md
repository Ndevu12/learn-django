# Learn Django With Ndevu

A hands-on learning repository for the **Django & Python Rwanda BootCamp** — covering Django from CRUD basics through authentication, security, and REST APIs with interactive guides, working projects, and quizzes.

[![Deploy to GitHub Pages](https://github.com/Ndevu12/learn-django/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/Ndevu12/learn-django/actions/workflows/deploy-pages.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**Live Site:** [https://ndevu12.github.io/learn-django](https://ndevu12.github.io/learn-django)

---

## Table of Contents

- [Overview](#overview)
- [Learning Roadmap](#learning-roadmap)
- [Tech Stack](#tech-stack)
- [Modules](#modules)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Running the Projects](#running-the-projects)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

This repository is a growing collection of interactive learning modules built for the Django & Python Rwanda BootCamp. Each module follows the same structure:

- A **polished, interactive documentation page** hosted on GitHub Pages (dark-themed, mobile-responsive)
- A **fully working Django project** you can run locally to experiment with the concepts
- A **knowledge quiz** to test your understanding
- A **detailed project README** with setup instructions, architecture, and code walkthroughs

Modules build on each other — the same **Book** domain model is used throughout, evolving from a simple template-based app to a secured REST API with JWT and role-based access control.

---

## Learning Roadmap

```
 Module 1                          Module 2                         Coming Soon
┌─────────────────────┐     ┌──────────────────────────┐     ┌─────────────────────┐
│  CRUD with CBVs     │     │  Auth & Security         │     │  Testing & Deploy   │
│                     │     │                          │     │                     │
│  • Django basics    │ ──▶ │  • Django REST Framework │ ──▶ │  • Unit & API tests │
│  • Models & forms   │     │  • JWT authentication    │     │  • CI/CD pipelines  │
│  • Class-Based Views│     │  • Role-based access     │     │  • Deployment       │
│  • Templates & URLs │     │  • Permission classes    │     │  • Docker           │
└─────────────────────┘     └──────────────────────────┘     └─────────────────────┘
```

---

## Tech Stack

| Package | Purpose |
|---------|----------|
| **Django 6.0** | Web framework — models, views, templates, admin |
| **Django REST Framework** | API toolkit — serializers, viewsets, routers |
| **djangorestframework-simplejwt** | JWT authentication — access/refresh tokens, blacklisting |
| **SQLite** | Development database (built-in) |
| **Pipenv** | Dependency management & virtual environments |
| **GitHub Pages** | Hosting for interactive documentation |

---

## Modules

### 1. CRUD with Class-Based Views

> Build a full Create · Read · Update · Delete workflow using Django's generic CBVs

| Section | What You'll Learn |
|---|---|
| Overview | CRUD operations map, request → response flow, the `Book` model |
| Setup | Creating a Django project from scratch — venv, startproject, migrations |
| FBV → CBV | Side-by-side migration from Function-Based to Class-Based Views |
| CBV Deep-Dive | `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView` |
| Templates | Auto template naming, `{% csrf_token %}`, template inheritance |
| URLs | `path()`, `reverse_lazy`, named routes, `LoginRequiredMixin` |
| Quiz | Interactive multiple-choice questions with instant feedback |

**Project:** [`CBV/cbv_project/`](CBV/cbv_project/) — Book Manager web app with 5 CBVs, ModelForm, 4 templates, admin config, and seed data.  
**Guide:** [CRUD with CBV](https://ndevu12.github.io/learn-django/CBV/django-crud-cbv.html) &nbsp;|&nbsp; **Folder README:** [CBV/](CBV/README.md) &nbsp;|&nbsp; **Project README:** [CBV/cbv_project/](CBV/cbv_project/README.md)

---

### 2. Auth & Security

> Secure a REST API with JWT authentication, role-based access control, and protected endpoints

| Section | What You'll Learn |
|---|---|
| Overview | Authentication vs authorization, session-based vs token-based auth |
| How JWT Works | Header · Payload · Signature anatomy, access vs refresh tokens |
| Django + JWT | Installing `simplejwt`, settings, wiring token endpoints |
| Role-Based Access | Custom User model with roles, writing permission classes |
| Protecting Endpoints | Per-action permissions, object-level ownership checks |
| Common Threats | XSS, CSRF, token theft, brute-force — mitigations |
| Quiz | Interactive multiple-choice questions with instant feedback |

**Project:** [`AUTH/auth_project/`](AUTH/auth_project/) — Book REST API with JWT auth, 3 roles (admin/editor/viewer), per-action permissions, and throttling.  
**Guide:** [Auth & Security](https://ndevu12.github.io/learn-django/AUTH/auth-security-guide.html) &nbsp;|&nbsp; **Folder README:** [AUTH/](AUTH/README.md) &nbsp;|&nbsp; **Project README:** [AUTH/auth_project/](AUTH/auth_project/README.md)

---

## Project Structure

```
learn-django/
├── index.html                  # GitHub Pages landing page
├── Pipfile                     # Python dependencies
├── LICENSE                     # MIT License
│
├── CBV/                        # Module 1: CRUD with Class-Based Views
│   ├── README.md               # Module overview & quick start
│   ├── django-crud-cbv.html    # Interactive documentation page
│   ├── styles/index.css        # Dark-theme design system
│   │
│   └── cbv_project/            # Working Django 6.0 project
│       ├── manage.py
│       ├── cbv_project/        # Project settings & root URL config
│       │   ├── settings.py
│       │   └── urls.py
│       └── books/              # Books app
│           ├── models.py       # Book model (title, author, pages, pub_date)
│           ├── views.py        # All 5 CRUD CBVs
│           ├── urls.py         # URL patterns for CRUD operations
│           ├── forms.py        # BookForm (ModelForm)
│           ├── admin.py        # Admin with list_display, filters, search
│           ├── management/     # seed_books command (6 sample books)
│           └── templates/      # base, list, detail, form, delete templates
│
├── AUTH/                       # Module 2: Auth & Security
│   ├── README.md               # Module overview & quick start
│   ├── auth-security-guide.html # Interactive documentation page
│   ├── styles/index.css        # Module-specific styles
│   │
│   └── auth_project/           # Working Django 6.0 + DRF REST API
│       ├── manage.py
│       ├── auth_project/       # Project settings (JWT, throttle, DRF config)
│       │   ├── settings.py
│       │   └── urls.py         # JWT token endpoints + app include
│       └── books/              # Books app
│           ├── models.py       # Custom User (roles) + Book (ownership)
│           ├── serializers.py  # JWT token, Book, User serializers
│           ├── permissions.py  # IsAdminRole, IsEditorOrAdmin, IsOwnerOrAdmin
│           ├── views.py        # BookViewSet, MyTokenView, UserListView
│           ├── urls.py         # DRF Router + admin user list
│           ├── admin.py        # User + Book admin with role fieldsets
│           └── management/     # seed_data command (3 users + 6 books)
│
└── .github/
    └── workflows/
        └── deploy-pages.yml    # Auto-deploy to GitHub Pages on push
```

---

## Getting Started

### Prerequisites

- **Python 3.12+**
- **pipenv** (`pip install pipenv`)

### Installation

```bash
# Clone the repository
git clone https://github.com/Ndevu12/learn-django.git
cd learn-django

# Install all dependencies (Django, DRF, simplejwt)
pipenv install
```

> **Pipenv note:** The shared `Pipfile` at the repo root manages dependencies for all modules.
> - `pipenv shell` activates the environment but **resets your cwd** to the repo root — `cd` into the project folder afterwards.
> - `pipenv run <cmd>` runs a one-off command without activating (respects your current directory).
> - `exit` deactivates the shell.

---

## Running the Projects

Each module has its own Django project on a different port. You can run them simultaneously.

| Module | Directory | Port | Seed Command | Server Command |
|--------|-----------|:----:|--------------|----------------|
| CBV | `CBV/cbv_project/` | 8000 | `python manage.py seed_books` | `python manage.py runserver` |
| Auth | `AUTH/auth_project/` | 8001 | `python manage.py seed_data` | `python manage.py runserver 8001` |

### Quick Start (any module)

```bash
# Activate the environment (from repo root)
pipenv shell

# Navigate to the module's project
cd <MODULE>/

# Migrate, seed, and run
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

### Module 2 — Auth & Security (port 8001)

```bash
cd AUTH/auth_project
python manage.py migrate && python manage.py seed_data
python manage.py runserver 8001
```

| URL | Method | Description |
|-----|--------|-------------|
| `http://127.0.0.1:8001/api/books/` | GET | List all books (public) |
| `http://127.0.0.1:8001/api/books/` | POST | Create a book (editor/admin) |
| `http://127.0.0.1:8001/api/token/` | POST | Login — returns JWT tokens |
| `http://127.0.0.1:8001/api/token/refresh/` | POST | Refresh access token |
| `http://127.0.0.1:8001/api/admin/users/` | GET | List users (admin only) |

**Test users:** `admin_anna`, `editor_bob`, `viewer_cara` — password: `pass1234!`

```bash
# Quick login test
curl -s -X POST http://localhost:8001/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username":"editor_bob","password":"pass1234!"}' | python3 -m json.tool
```

See each module's README for full documentation:
- [CBV/cbv_project/README.md](CBV/cbv_project/README.md) — views, forms, templates, admin
- [AUTH/auth_project/README.md](AUTH/auth_project/README.md) — cURL guide, RBAC matrix, JWT config, permission classes

---

## Contributing

Contributions are welcome! If you'd like to add a new module, fix a bug, or improve the documentation:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-module`)
3. Commit your changes (`git commit -m 'Add new module'`)
4. Push to the branch (`git push origin feature/new-module`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Made for the <strong>Django & Python Rwanda BootCamp 2026</strong> by <a href="https://github.com/Ndevu12">Ndevu</a>
</p>
