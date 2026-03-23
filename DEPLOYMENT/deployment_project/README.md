# Auth & Security — Practical Project

A Django REST API demonstrating **JWT authentication**, **role-based access control (RBAC)**, and **protected CRUD endpoints** — the practical companion to the [Auth & Security Guide](../auth-security-guide.html).

Built on the same Book domain as the CBV module, extended with a custom User model, ownership, and per-action permissions.

---

## Table of Contents

- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
- [Environment variables](#environment-variables)
- [Docker](#docker)
- [CI/CD (GitHub Actions)](#cicd-github-actions)
- [Seeded Data](#seeded-data)
- [API Endpoints](#api-endpoints)
- [Authentication Flow](#authentication-flow)
- [Role-Based Access Control](#role-based-access-control)
- [Permission Classes](#permission-classes)
- [JWT Configuration](#jwt-configuration)
- [Throttling](#throttling)
- [Testing with cURL](#testing-with-curl)
- [Guide Mapping](#guide-mapping)

---

## Tech Stack

| Package | Version | Purpose |
|---------|---------|---------|
| Django | 6.0.3 | Web framework |
| Django REST Framework | latest | API toolkit |
| djangorestframework-simplejwt | latest | JWT authentication |
| python-decouple | latest | Config from `.env` / environment |
| Gunicorn | latest | WSGI server (container default CMD) |
| WhiteNoise | latest | Static files for production-style runs |
| psycopg | latest | PostgreSQL driver (Docker / optional local) |
| SQLite3 | built-in | Default DB when `DB_NAME` is unset |

---

## Project Structure

```
deployment_project/
├── manage.py
├── requirements.txt       # Docker + pip installs
├── Dockerfile
├── docker-compose.yml
├── .env.example            # Local SQLite–oriented template
├── .env.compose.example    # Template for Docker Compose + Postgres
├── db.sqlite3              # Created when using SQLite
├── deployment_project/
│   ├── __init__.py
│   ├── settings.py          # DRF, JWT, throttle config
│   ├── urls.py              # JWT endpoints + app include
│   ├── wsgi.py
│   └── asgi.py
└── books/
    ├── __init__.py
    ├── models.py            # Custom User (with roles) + Book (with owner)
    ├── serializers.py       # MyTokenSerializer, BookSerializer, UserSerializer
    ├── permissions.py       # IsAdminRole, IsEditorOrAdmin, IsOwnerOrAdmin
    ├── views.py             # MyTokenView, BookViewSet, UserListView
    ├── urls.py              # DRF Router + admin user list
    ├── admin.py             # User (with role fieldsets) + Book admin
    ├── apps.py
    ├── tests.py
    └── management/
        └── commands/
            └── seed_data.py # Seeds users + books
```

---

## Quick Start

From the **repository root**:

```bash
# 1. Install dependencies (if not already done)
pipenv install

# 2. Navigate to the project
cd DEPLOYMENT/deployment_project

# 3. Apply migrations
pipenv run python manage.py migrate

# 4. Seed test data (3 users + 6 books)
pipenv run python manage.py seed_data

# 5. Start the development server
pipenv run python manage.py runserver 8001
```

The API is now available at `http://localhost:8001/api/`.

---

## Environment variables

Configuration is loaded with **python-decouple** (see the [Deployment guide](../deployment-best-practices.html#envvars)): real environment variables override values from a `.env` file in this directory.

| Variable | Role |
|----------|------|
| `SECRET_KEY` | Django signing; set a strong value in any shared or production environment |
| `DEBUG` | `True` / `False` |
| `ALLOWED_HOSTS` | Comma-separated hostnames |
| `DB_NAME` | If set (non-empty), Django uses **PostgreSQL** with the `DB_*` variables below; if unset, **SQLite** (`db.sqlite3`) is used |

Copy `.env.example` for local SQLite use. For Docker Compose, copy `.env.compose.example` to `.env` so Postgres and the web service get matching credentials.

---

## Docker

- **Image** (`Dockerfile`): installs dependencies, runs `collectstatic`, starts **Gunicorn** on port 8000 (suitable for a single-container demo or behind a reverse proxy).
- **Compose** (`docker-compose.yml`): **Postgres 16** + **Django `runserver`** with the project bind-mounted for a simple dev loop (aligned with the guide’s Compose section).

```bash
cd DEPLOYMENT/deployment_project
cp .env.compose.example .env   # edit secrets if needed
docker compose up --build

# In another terminal (once containers are up):
docker compose exec web python manage.py migrate
docker compose exec web python manage.py seed_data   # optional
```

API: `http://localhost:8000/api/` (Compose maps port **8000**).

To build and run the Gunicorn image without Compose:

```bash
docker build -t deployment-books:latest .
docker run --rm -p 8000:8000 \
  -e SECRET_KEY=your-secret \
  -e DEBUG=False \
  -e ALLOWED_HOSTS=localhost,127.0.0.1 \
  deployment-books:latest
```

(That run example uses defaults that expect SQLite inside the container; for Postgres, pass the same `DB_*` variables as in `.env.compose.example` and use `--network` to reach the database.)

---

## CI/CD (GitHub Actions)

Workflow [`.github/workflows/deployment-project-ci.yml`](../../.github/workflows/deployment-project-ci.yml) runs on pushes and pull requests that touch this project. It installs `requirements.txt`, runs `manage.py check`, migrates against **SQLite**, and runs `manage.py test`.

### Repository configuration (secrets and variables)

Do **not** put real `SECRET_KEY` values in the YAML. Configure them in the GitHub UI: **Settings → Secrets and variables → Actions**.

| Name | Type | Required | Purpose |
|------|------|----------|---------|
| `DJANGO_SECRET_KEY` | **Secret** | Yes | Django signing key for CI (use a long random string; can differ from production) |
| `DJANGO_CI_DEBUG` | Variable | No | `True` or `False` for `DEBUG` in CI (default: `True`) |
| `DJANGO_CI_ALLOWED_HOSTS` | Variable | No | Comma-separated hosts (default: `localhost,127.0.0.1`) |

**Fork pull requests:** GitHub does not inject repository secrets into workflows triggered from forks, so `DJANGO_SECRET_KEY` will be empty and the verify step will fail until a maintainer runs checks from a branch on this repo or the contributor adds the same secret on their fork for local parity. That matches common practice of not exposing secrets to untrusted code.

Use the workflow as a starting point for Docker image builds or deploy jobs that read registry credentials from **Secrets** (for example `CONTAINER_REGISTRY_TOKEN`) rather than hardcoding them.

---

## Seeded Data

### Users

| Username | Role | Password | Can Create | Can Edit Own | Can Delete |
|----------|------|----------|:----------:|:------------:|:----------:|
| `admin_anna` | admin | `pass1234!` | Yes | Yes | Yes |
| `editor_bob` | editor | `pass1234!` | Yes | Yes | No |
| `viewer_cara` | viewer | `pass1234!` | No | No | No |

### Books

| Title | Author | Owner |
|-------|--------|-------|
| Django for Beginners | William S. Vincent | admin_anna |
| Two Scoops of Django | Daniel & Audrey Feldroy | admin_anna |
| The Pragmatic Programmer | David Thomas & Andrew Hunt | admin_anna |
| Fluent Python | Luciano Ramalho | editor_bob |
| Clean Code | Robert C. Martin | editor_bob |
| Design Patterns | Gang of Four | editor_bob |

---

## API Endpoints

### Authentication

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| `POST` | `/api/token/` | None | Login — returns access + refresh tokens with `username` and `role` claims |
| `POST` | `/api/token/refresh/` | None | Refresh — exchange refresh token for new access token |
| `POST` | `/api/token/blacklist/` | Bearer | Logout — blacklist a refresh token |

### Books CRUD

| Method | Endpoint | Permission | Description |
|--------|----------|------------|-------------|
| `GET` | `/api/books/` | AllowAny | List all books |
| `GET` | `/api/books/:id/` | AllowAny | Retrieve a single book |
| `POST` | `/api/books/` | IsEditorOrAdmin | Create a book (owner auto-set) |
| `PUT` | `/api/books/:id/` | IsOwnerOrAdmin | Full update |
| `PATCH` | `/api/books/:id/` | IsOwnerOrAdmin | Partial update |
| `DELETE` | `/api/books/:id/` | IsAdminRole | Delete a book |

### Admin

| Method | Endpoint | Permission | Description |
|--------|----------|------------|-------------|
| `GET` | `/api/admin/users/` | IsAdminRole | List all users and their roles |

---

## Authentication Flow

```
┌─────────┐         POST /api/token/          ┌──────────┐
│  Client  │ ──── { username, password } ────▶ │  Server  │
│          │ ◀─── { access, refresh }   ────── │          │
└─────────┘                                    └──────────┘
     │
     │  Subsequent requests:
     │  Authorization: Bearer <access_token>
     │
     │  When access expires (15 min):
     │  POST /api/token/refresh/
     │  { "refresh": "<refresh_token>" }
     │  → New access token returned
     │  → Old refresh token rotated + blacklisted
     │
     │  To logout:
     │  POST /api/token/blacklist/
     │  { "refresh": "<refresh_token>" }
     │  → Refresh token blacklisted
```

### Custom JWT Claims

The access token payload includes:

```json
{
  "token_type": "access",
  "exp": 1773500855,
  "iat": 1773499955,
  "jti": "d166a799964b4400910d58452be1b24f",
  "user_id": "2",
  "username": "editor_bob",
  "role": "editor"
}
```

---

## Role-Based Access Control

### User Model

```python
class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN  = 'admin',  'Admin'
        EDITOR = 'editor', 'Editor'
        VIEWER = 'viewer', 'Viewer'

    role = models.CharField(max_length=10, choices=Role.choices, default=Role.VIEWER)
```

### RBAC Matrix

| Action | Admin | Editor | Viewer | Anonymous |
|--------|:-----:|:------:|:------:|:---------:|
| List books | Yes | Yes | Yes | Yes |
| View book detail | Yes | Yes | Yes | Yes |
| Create book | Yes | Yes | No | No |
| Update own book | Yes | Yes | No | No |
| Update any book | Yes | No | No | No |
| Delete book | Yes | No | No | No |
| List users | Yes | No | No | No |

---

## Permission Classes

Defined in `books/permissions.py`:

### `IsAdminRole`
Grants access only to users with `role='admin'`. Used for destructive operations (delete) and admin-only views (user list).

### `IsEditorOrAdmin`
- **Safe methods** (GET, HEAD, OPTIONS): any authenticated user
- **Write methods** (POST, PUT, PATCH, DELETE): only editors and admins

Used for the `create` action.

### `IsOwnerOrAdmin`
Object-level permission:
- **Safe methods**: allow all
- **Write methods**: only the book's `owner` or an admin

Used for `update` and `partial_update` actions.

### Per-Action Permission Mapping

```python
def get_permissions(self):
    if self.action in ('list', 'retrieve'):
        return [AllowAny()]
    if self.action == 'create':
        return [IsEditorOrAdmin()]
    if self.action == 'destroy':
        return [IsAdminRole()]
    return [IsOwnerOrAdmin()]  # update / partial_update
```

---

## JWT Configuration

Configured in `settings.py`:

| Setting | Value | Purpose |
|---------|-------|---------|
| `ACCESS_TOKEN_LIFETIME` | 15 minutes | Short-lived for security |
| `REFRESH_TOKEN_LIFETIME` | 7 days | Longer session persistence |
| `ROTATE_REFRESH_TOKENS` | True | New refresh token on each refresh |
| `BLACKLIST_AFTER_ROTATION` | True | Old refresh tokens invalidated |
| `ALGORITHM` | HS256 | HMAC-SHA256 signing |
| `AUTH_HEADER_TYPES` | Bearer | `Authorization: Bearer <token>` |

Global defaults:
- **Authentication**: `JWTAuthentication` (all endpoints require JWT unless overridden)
- **Permission**: `IsAuthenticated` (all endpoints require auth unless overridden)

---

## Throttling

| Scope | Rate | Description |
|-------|------|-------------|
| `anon` | 30/minute | Unauthenticated requests (e.g. login attempts) |
| `user` | 200/minute | Authenticated user requests |

---

## Testing with cURL

### Login (get tokens)

```bash
curl -s -X POST http://localhost:8001/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username":"editor_bob","password":"pass1234!"}' | python3 -m json.tool
```

### List books (no auth needed)

```bash
curl -s http://localhost:8001/api/books/ | python3 -m json.tool
```

### Create a book (editor or admin)

```bash
TOKEN="<access_token_from_login>"

curl -s -X POST http://localhost:8001/api/books/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title":"New Book","author":"Author Name","pages":200,"pub_date":"2026-01-01"}' \
  | python3 -m json.tool
```

### Update a book (owner or admin)

```bash
curl -s -X PATCH http://localhost:8001/api/books/1/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"pages":350}' | python3 -m json.tool
```

### Delete a book (admin only)

```bash
curl -s -X DELETE http://localhost:8001/api/books/1/ \
  -H "Authorization: Bearer $TOKEN" -w "\nHTTP %{http_code}\n"
```

### Refresh token

```bash
curl -s -X POST http://localhost:8001/api/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh":"<refresh_token>"}' | python3 -m json.tool
```

### Logout (blacklist refresh token)

```bash
curl -s -X POST http://localhost:8001/api/token/blacklist/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"refresh":"<refresh_token>"}'
```

### List users (admin only)

```bash
curl -s http://localhost:8001/api/admin/users/ \
  -H "Authorization: Bearer $TOKEN" | python3 -m json.tool
```

---

## Guide Mapping

Each file in this project maps to a section in the [Auth & Security Guide](../auth-security-guide.html):

| File | Guide Section | Concepts |
|------|--------------|----------|
| `models.py` | RBAC — Step 1 | Custom User with `Role` TextChoices, `is_admin`/`is_editor` properties |
| `permissions.py` | RBAC — Step 2 | `has_permission` vs `has_object_permission`, `SAFE_METHODS` |
| `serializers.py` | Django + JWT — Step 6 | Custom `TokenObtainPairSerializer` with extra claims |
| `views.py` | Protecting Endpoints — Level 2 | `get_permissions()` per-action, `perform_create()` auto-owner |
| `urls.py` (project) | Django + JWT — Step 4 | Token obtain, refresh, blacklist URL wiring |
| `settings.py` | Django + JWT — Steps 2-3, Endpoints — Level 1 | `REST_FRAMEWORK`, `SIMPLE_JWT`, `AUTH_USER_MODEL`, throttle config |
| `admin.py` | — | Django admin with role fieldsets |
| `seed_data.py` | — | Test data for all three roles |
