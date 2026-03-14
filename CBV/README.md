# Module: CRUD with Class-Based Views

> **Models, Views, Templates, URLs** — FBV vs CBV comparison, deep-dive, and quiz

This module teaches Django's **Class-Based Views (CBVs)** for CRUD operations through an interactive guide and a fully working Django project.

---

## What's Inside

```
CBV/
├── django-crud-cbv.html       # Interactive documentation page (GitHub Pages)
├── styles/index.css            # Module-specific dark-theme styles
│
└── cbv_project/                # Working Django 6.0 project
    ├── manage.py
    ├── cbv_project/            # Project config (settings, root URLs)
    └── books/                  # Books app — models, views, forms, templates
```

---

## Learning Path

| Section | Description |
|---------|-------------|
| **Overview** | CRUD operations map, request → response flow, FBV vs CBV comparison |
| **Setup** | Creating a Django project from scratch (venv, startproject, migrations) |
| **FBV → CBV** | Side-by-side migration from Function-Based Views to Class-Based Views |
| **CBV Deep-Dive** | `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView` with overridable methods |
| **Templates** | Auto template naming, `{% csrf_token %}`, template inheritance |
| **URLs** | URL patterns, `reverse_lazy` vs `reverse`, `LoginRequiredMixin` |
| **Quiz** | Interactive multiple-choice questions with instant feedback |

---

## Key Concepts Covered

- **Django Generic Views** — `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`
- **ModelForm** — form generation from models with custom widgets
- **Template Inheritance** — base layout with `{% block %}` overrides
- **URL Routing** — `path()`, `.as_view()`, named routes, `<int:pk>` captures
- **Admin Customization** — `list_display`, `list_filter`, `search_fields`
- **Management Commands** — custom `seed_books` command for sample data

---

## Quick Start

```bash
# From the repository root
pipenv install && pipenv shell
cd CBV/cbv_project

python manage.py migrate
python manage.py seed_books
python manage.py runserver
```

Visit `http://localhost:8000/books/` to see the app.

---

## URL Endpoints

| URL | Description |
|-----|-------------|
| `/books/` | List all books |
| `/books/<id>/` | Book detail |
| `/books/new/` | Create a book |
| `/books/<id>/edit/` | Edit a book |
| `/books/<id>/delete/` | Delete a book |
| `/admin/` | Django admin panel |

---

## Resources

- **Interactive Guide:** [django-crud-cbv.html](django-crud-cbv.html) (or view on [GitHub Pages](https://ndevu12.github.io/learn-django/CBV/django-crud-cbv.html))
- **Project README:** [cbv_project/README.md](cbv_project/README.md) — detailed setup, model, views, forms, templates, and admin documentation
- **Django Docs:** [Class-Based Views](https://docs.djangoproject.com/en/5.0/topics/class-based-views/)
