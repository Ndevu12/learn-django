# Learn Django With Ndevu

Interactive learning resources for the **Django & Python Rwanda BootCamp** — covering Django concepts, patterns, and best practices through hands-on projects and rich documentation.

[![Deploy to GitHub Pages](https://github.com/Ndevu12/learn-django/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/Ndevu12/learn-django/actions/workflows/deploy-pages.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**Live Site:** [https://ndevu12.github.io/learn-django](https://ndevu12.github.io/learn-django)

---

## Table of Contents

- [Overview](#overview)
- [Modules](#modules)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Running the Django Project](#running-the-django-project)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

This repository is a growing collection of interactive learning modules built for the Django & Python Rwanda BootCamp. Each module includes:

- A **polished, interactive documentation page** hosted on GitHub Pages (dark-themed, mobile-responsive)
- A **fully working Django project** you can run locally to experiment with the concepts
- **Quizzes** to test your understanding

---

## Modules

### 1. CRUD with Class-Based Views

> Models, Views, Templates, URLs — FBV vs CBV comparison, deep-dive, and quiz

| Topic | What You'll Learn |
|---|---|
| **Overview** | CRUD operations map, request → response flow, the `Book` model |
| **Setup** | Creating a Django project from scratch (venv, startproject, migrations) |
| **FBV → CBV** | Side-by-side comparison of Function-Based Views vs Class-Based Views |
| **CBV Deep-Dive** | `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView` with overridable methods |
| **Templates** | Auto template naming, `csrf_token`, template inheritance |
| **URLs** | URL patterns, `reverse_lazy` vs `reverse`, `LoginRequiredMixin` |
| **Quiz** | 5 interactive multiple-choice questions with instant feedback |

**Django project:** A Book Manager app (`CBV/cbv_project/`) demonstrating all five CRUD CBVs with a `Book` model, custom admin configuration, seed data command, and four templates extending a base layout.

---

## Project Structure

```
learn-django/
├── index.html                  # GitHub Pages landing page
├── Pipfile                     # Python dependencies
├── LICENSE                     # MIT License
│
├── CBV/                        # Module: CRUD with Class-Based Views
│   ├── django-crud-cbv.html    # Interactive documentation page
│   ├── styles/index.css        # Dark-theme design system
│   ├── scripts/index.js        # Sidebar, section toggling, quiz logic
│   │
│   └── cbv_project/            # Working Django 6.0 project
│       ├── manage.py
│       ├── cbv_project/        # Project settings & root URL config
│       │   ├── settings.py
│       │   └── urls.py
│       │
│       └── books/              # Books app
│           ├── models.py       # Book model (title, author, pages, pub_date)
│           ├── views.py        # All 5 CRUD CBVs
│           ├── urls.py         # URL patterns for CRUD operations
│           ├── forms.py        # BookForm (ModelForm)
│           ├── admin.py        # Admin with list_display, filters, search
│           ├── management/
│           │   └── commands/
│           │       └── seed_books.py  # Seeds 6 sample books
│           └── templates/
│               └── books/      # Templates (base, list, detail, form, delete)
│
└── .github/
    └── workflows/
        └── deploy-pages.yml    # Auto-deploy to GitHub Pages on push
```

---

## Getting Started

### Prerequisites

- **Python 3.12+**
- **pip** and **pipenv** (or use `pip install django` directly)

### Installation

```bash
# Clone the repository
git clone https://github.com/Ndevu12/learn-django.git
cd learn-django

# Install dependencies with pipenv
pipenv install
pipenv shell
```

Or with pip:

```bash
pip install django
```

---

## Running the Django Project

Each module contains a standalone Django project you can run locally.

### CRUD with Class-Based Views

```bash
cd CBV/cbv_project

# Apply migrations
python manage.py migrate

# Seed sample data (6 books)
python manage.py seed_books

# Start the development server
python manage.py runserver
```

Then visit:

| URL | Description |
|---|---|
| `http://127.0.0.1:8000/books/` | Book list |
| `http://127.0.0.1:8000/books/new/` | Add a new book |
| `http://127.0.0.1:8000/books/1/` | Book detail |
| `http://127.0.0.1:8000/books/1/edit/` | Edit a book |
| `http://127.0.0.1:8000/books/1/delete/` | Delete a book |
| `http://127.0.0.1:8000/admin/` | Django admin panel |

To access the admin panel, create a superuser:

```bash
python manage.py createsuperuser
```

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

Made for the **Django & Python Rwanda BootCamp 2026** by [Ndevu](https://github.com/Ndevu12)
