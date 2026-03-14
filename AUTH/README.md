# Module: Auth & Security

> **JWT Authentication, Role-Based Access Control, Protected REST API Endpoints** — and quiz

This module teaches Django REST Framework **authentication and authorization** through an interactive guide and a fully working API project.

---

## What's Inside

```
AUTH/
├── auth-security-guide.html    # Interactive documentation page (GitHub Pages)
├── styles/index.css             # Module-specific dark-theme styles
│
└── auth_project/                # Working Django 6.0 + DRF REST API
    ├── manage.py
    ├── auth_project/            # Project config (settings, JWT, throttle config)
    └── books/                   # Books app — models, serializers, permissions, views
```

---

## Learning Path

| Section | Description |
|---------|-------------|
| **Overview** | Authentication vs authorization, session vs token-based auth |
| **How JWT Works** | Header, payload, signature anatomy; access vs refresh tokens |
| **Django + JWT** | Installing `simplejwt`, configuring settings, token endpoints |
| **Role-Based Access** | Custom User model with roles, permission classes |
| **Protecting Endpoints** | Per-action permissions, object-level ownership checks |
| **Common Threats** | XSS, CSRF, token theft, brute-force — mitigations and best practices |
| **Quiz** | Interactive multiple-choice questions with instant feedback |

---

## Key Concepts Covered

- **JWT Authentication** — access/refresh token flow, custom claims, token rotation & blacklisting
- **Custom User Model** — `AbstractUser` with `Role` TextChoices (`admin`, `editor`, `viewer`)
- **Permission Classes** — `IsAdminRole`, `IsEditorOrAdmin`, `IsOwnerOrAdmin`
- **Per-Action Permissions** — `get_permissions()` override on `ModelViewSet`
- **Object-Level Permissions** — `has_object_permission()` for ownership checks
- **DRF ViewSets & Routers** — `ModelViewSet`, `DefaultRouter`, `ListAPIView`
- **Serializers** — `ModelSerializer`, custom `TokenObtainPairSerializer` with extra claims
- **Throttling** — rate limiting for anonymous and authenticated users

---

## RBAC Matrix

| Action | Admin | Editor | Viewer | Anonymous |
|--------|:-----:|:------:|:------:|:---------:|
| List / View books | Yes | Yes | Yes | Yes |
| Create book | Yes | Yes | No | No |
| Update own book | Yes | Yes | No | No |
| Update any book | Yes | No | No | No |
| Delete book | Yes | No | No | No |
| List users | Yes | No | No | No |

---

## Quick Start

```bash
# From the repository root
pipenv install && pipenv shell
cd AUTH/auth_project

python manage.py migrate
python manage.py seed_data       # Creates 3 users + 6 books
python manage.py runserver 8001
```

The API is available at `http://localhost:8001/api/`.

---

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/token/` | Login — returns access + refresh JWT |
| `POST` | `/api/token/refresh/` | Refresh access token |
| `POST` | `/api/token/blacklist/` | Logout — invalidate refresh token |

### Books CRUD

| Method | Endpoint | Permission |
|--------|----------|------------|
| `GET` | `/api/books/` | AllowAny |
| `GET` | `/api/books/:id/` | AllowAny |
| `POST` | `/api/books/` | Editor or Admin |
| `PUT/PATCH` | `/api/books/:id/` | Owner or Admin |
| `DELETE` | `/api/books/:id/` | Admin only |

### Admin

| Method | Endpoint | Permission |
|--------|----------|------------|
| `GET` | `/api/admin/users/` | Admin only |

---

## Test Users

| Username | Role | Password |
|----------|------|----------|
| `admin_anna` | admin | `pass1234!` |
| `editor_bob` | editor | `pass1234!` |
| `viewer_cara` | viewer | `pass1234!` |

---

## Resources

- **Interactive Guide:** [auth-security-guide.html](auth-security-guide.html) (or view on [GitHub Pages](https://ndevu12.github.io/learn-django/AUTH/auth-security-guide.html))
- **Project README:** [auth_project/README.md](auth_project/README.md) — detailed setup, API docs, cURL examples, JWT config, and permission class reference
- **Django REST Framework:** [Authentication](https://www.django-rest-framework.org/api-guide/authentication/)
- **SimpleJWT:** [Documentation](https://django-rest-framework-simplejwt.readthedocs.io/)
