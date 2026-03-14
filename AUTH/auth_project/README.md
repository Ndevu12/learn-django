# Auth & Security — Practical Project

A Django REST API demonstrating **JWT authentication**, **role-based access control (RBAC)**, and **protected CRUD endpoints** — the practical companion to the [Auth & Security Guide](../auth-security-guide.html).

Built on the same Book domain as the CBV module, extended with a custom User model, ownership, and per-action permissions.

---

## Table of Contents

- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
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
| SQLite3 | built-in | Development database |

---

## Project Structure

```
auth_project/
├── manage.py
├── db.sqlite3
├── auth_project/
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
cd AUTH/auth_project

# 3. Apply migrations
pipenv run python manage.py migrate

# 4. Seed test data (3 users + 6 books)
pipenv run python manage.py seed_data

# 5. Start the development server
pipenv run python manage.py runserver 8001
```

The API is now available at `http://localhost:8001/api/`.

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
