# CRUD with Class-Based Views — Practical Project

A Django web application demonstrating **CRUD operations** using **class-based views (CBVs)** — the practical companion to the [CRUD with CBV Guide](../django-crud-cbv.html).

A simple Book management app that showcases all five generic CBVs: `ListView`, `DetailView`, `CreateView`, `UpdateView`, and `DeleteView`.

---

## Table of Contents

- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
- [Seeded Data](#seeded-data)
- [URL Endpoints](#url-endpoints)
- [Model](#model)
- [Views](#views)
- [Form](#form)
- [Templates](#templates)
- [Admin](#admin)
- [Guide Mapping](#guide-mapping)

---

## Tech Stack

| Package | Version | Purpose |
|---------|---------|---------|
| Django | 6.0.3 | Web framework |
| SQLite3 | built-in | Development database |

---

## Project Structure

```
cbv_project/
├── manage.py
├── db.sqlite3
├── cbv_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py              # Admin + books app include
│   ├── wsgi.py
│   └── asgi.py
└── books/
    ├── __init__.py
    ├── models.py            # Book model
    ├── views.py             # 5 CBVs (List, Detail, Create, Update, Delete)
    ├── urls.py              # 5 URL patterns
    ├── forms.py             # BookForm (ModelForm with date widget)
    ├── admin.py             # BookAdmin with list_display/filter/search
    ├── apps.py
    ├── tests.py
    ├── management/
    │   └── commands/
    │       └── seed_books.py  # Seeds 6 sample books
    ├── migrations/
    │   └── 0001_initial.py
    └── templates/
        └── books/
            ├── base.html                # Base layout with nav
            ├── book_list.html           # Table of all books
            ├── book_detail.html         # Single book details
            ├── book_form.html           # Shared create/edit form
            └── book_confirm_delete.html # Delete confirmation
```

---

## Quick Start

From the **repository root**:

```bash
# 1. Install dependencies (if not already done)
pipenv install

# 2. Activate the virtual environment
pipenv shell

# 3. Navigate to the project (pipenv shell resets to the Pipfile directory)
cd CBV/cbv_project

# 4. Apply migrations
python manage.py migrate

# 5. Seed sample books
python manage.py seed_books

# 6. Start the development server
python manage.py runserver
```

The app is now available at `http://localhost:8000/books/`.

> **Note:** This project uses **pipenv** — there is no local `venv/` folder.
> The virtualenv lives in `~/.local/share/virtualenvs/`.
>
> - `pipenv shell` — activates the env, but **resets your working directory** to where the `Pipfile` is (the repo root). You must `cd` into the project folder again after activating.
> - `pipenv run <cmd>` — runs a single command without activating (respects your current directory).
> - `exit` — deactivates the pipenv shell.
>
> **Alternative** (no shell activation needed):
> ```bash
> cd CBV/cbv_project
> pipenv run python manage.py migrate
> pipenv run python manage.py seed_books
> pipenv run python manage.py runserver
> ```

---

## Seeded Data

The `seed_books` management command creates 6 books using `get_or_create` for idempotency:

| Title | Author | Pages | Published |
|-------|--------|------:|-----------|
| Django for Beginners | William S. Vincent | 294 | 2022-05-01 |
| Two Scoops of Django | Daniel & Audrey Feldroy | 530 | 2022-01-15 |
| Fluent Python | Luciano Ramalho | 792 | 2022-04-01 |
| Clean Code | Robert C. Martin | 464 | 2008-08-01 |
| The Pragmatic Programmer | David Thomas & Andrew Hunt | 352 | 2019-09-23 |
| Design Patterns | Gang of Four | 395 | 1994-10-31 |

---

## URL Endpoints

| URL Pattern | Name | View | HTTP Method | Description |
|-------------|------|------|:-----------:|-------------|
| `/books/` | `book-list` | `BookListView` | GET | List all books (ordered by `-pub_date`) |
| `/books/<int:pk>/` | `book-detail` | `BookDetailView` | GET | Single book details |
| `/books/new/` | `book-create` | `BookCreateView` | GET / POST | Create a new book |
| `/books/<int:pk>/edit/` | `book-update` | `BookUpdateView` | GET / POST | Edit an existing book |
| `/books/<int:pk>/delete/` | `book-delete` | `BookDeleteView` | GET / POST | Delete confirmation + action |
| `/admin/` | — | Django Admin | — | Admin interface |

---

## Model

```python
class Book(models.Model):
    title    = models.CharField(max_length=200)
    author   = models.CharField(max_length=100)
    pages    = models.IntegerField()
    pub_date = models.DateField()
```

- `__str__()` returns the title
- `get_absolute_url()` returns the detail URL — used by `CreateView` and `UpdateView` for redirect after save

---

## Views

Five generic CBVs, each with minimal configuration:

| View | Generic Base | Key Config |
|------|-------------|------------|
| `BookListView` | `ListView` | `ordering = ['-pub_date']`, `context_object_name = 'books'` |
| `BookDetailView` | `DetailView` | `context_object_name = 'book'` |
| `BookCreateView` | `CreateView` | `form_class = BookForm` (redirects via `get_absolute_url`) |
| `BookUpdateView` | `UpdateView` | `form_class = BookForm` (redirects via `get_absolute_url`) |
| `BookDeleteView` | `DeleteView` | `success_url = reverse_lazy('book-list')` |

### CBV → Django Generic View Mapping

```
ListView     → SELECT * FROM books ORDER BY pub_date DESC
DetailView   → SELECT * FROM books WHERE pk = ?
CreateView   → INSERT INTO books (title, author, pages, pub_date) VALUES (...)
UpdateView   → UPDATE books SET ... WHERE pk = ?
DeleteView   → DELETE FROM books WHERE pk = ?
```

---

## Form

```python
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'pages', 'pub_date']
        widgets = {
            'pub_date': forms.DateInput(attrs={'type': 'date'}),
        }
```

- Shared by both `CreateView` and `UpdateView`
- Uses HTML5 `<input type="date">` for the publication date picker

---

## Templates

All templates live in `books/templates/books/` following Django's app-namespaced convention.

| Template | Extends | Purpose |
|----------|---------|---------|
| `base.html` | — | Layout shell: HTML head, header with nav link, content block |
| `book_list.html` | `base.html` | Table with Title / Author / Pages / Published / Actions columns |
| `book_detail.html` | `base.html` | Definition list with book fields + Edit / Delete / Back links |
| `book_form.html` | `base.html` | Shared create/edit form; uses `{% if object %}` to switch heading |
| `book_confirm_delete.html` | `base.html` | Danger-styled confirmation with CSRF-protected POST form |

### Template Inheritance

```
base.html
├── book_list.html
├── book_detail.html
├── book_form.html          (Create + Update)
└── book_confirm_delete.html
```

---

## Admin

```python
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display  = ('title', 'author', 'pages', 'pub_date')
    list_filter   = ('author',)
    search_fields = ('title', 'author')
```

Access at `http://localhost:8000/admin/` — create a superuser first:

```bash
pipenv run python manage.py createsuperuser
```

---

## Guide Mapping

Each file maps to a section in the [CRUD with CBV Guide](../django-crud-cbv.html):

| File | Guide Section | Concepts |
|------|--------------|----------|
| `models.py` | Setup — Models | `CharField`, `IntegerField`, `DateField`, `__str__`, `get_absolute_url` |
| `views.py` | CBV Deep-Dive | `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView` |
| `urls.py` | URLs & Wiring | `path()`, `.as_view()`, named routes, `<int:pk>` captures |
| `forms.py` | FBV → CBV | `ModelForm`, custom widget, shared form for create + update |
| `templates/` | Templates | Template inheritance, `{% block %}`, `{% csrf_token %}`, `{% if object %}` |
| `admin.py` | — | `list_display`, `list_filter`, `search_fields` |
| `seed_books.py` | — | Management commands, `get_or_create` for idempotent seeding |
