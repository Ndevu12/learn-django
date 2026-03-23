from datetime import date

from django.core.management.base import BaseCommand

from books.models import Book, User


class Command(BaseCommand):
    help = 'Seed users with different roles and books with owners'

    def handle(self, *args, **options):
        # ── Users (one per role) ──
        users_data = [
            {'username': 'admin_anna', 'email': 'anna@example.com',
             'password': 'pass1234!', 'role': 'admin'},
            {'username': 'editor_bob', 'email': 'bob@example.com',
             'password': 'pass1234!', 'role': 'editor'},
            {'username': 'viewer_cara', 'email': 'cara@example.com',
             'password': 'pass1234!', 'role': 'viewer'},
        ]

        created_users = {}
        for u in users_data:
            user, created = User.objects.get_or_create(
                username=u['username'],
                defaults={'email': u['email'], 'role': u['role']},
            )
            if created:
                user.set_password(u['password'])
                user.save()
                self.stdout.write(f'  Created user: {user}')
            else:
                self.stdout.write(f'  Already exists: {user}')
            created_users[u['role']] = user

        self.stdout.write(self.style.SUCCESS(
            f"Users ready: {', '.join(u['username'] for u in users_data)}"
        ))

        # ── Books (distributed across owners) ──
        admin_user = created_users['admin']
        editor_user = created_users['editor']

        books = [
            {'title': 'Django for Beginners', 'author': 'William S. Vincent',
             'pages': 294, 'pub_date': date(2022, 5, 1), 'owner': admin_user},
            {'title': 'Two Scoops of Django', 'author': 'Daniel & Audrey Feldroy',
             'pages': 530, 'pub_date': date(2022, 1, 15), 'owner': admin_user},
            {'title': 'Fluent Python', 'author': 'Luciano Ramalho',
             'pages': 792, 'pub_date': date(2022, 4, 1), 'owner': editor_user},
            {'title': 'Clean Code', 'author': 'Robert C. Martin',
             'pages': 464, 'pub_date': date(2008, 8, 1), 'owner': editor_user},
            {'title': 'The Pragmatic Programmer', 'author': 'David Thomas & Andrew Hunt',
             'pages': 352, 'pub_date': date(2019, 9, 23), 'owner': admin_user},
            {'title': 'Design Patterns', 'author': 'Gang of Four',
             'pages': 395, 'pub_date': date(1994, 10, 31), 'owner': editor_user},
        ]

        created_count = 0
        for b in books:
            _, created = Book.objects.get_or_create(
                title=b['title'],
                defaults=b,
            )
            if created:
                created_count += 1

        self.stdout.write(self.style.SUCCESS(
            f'Done! Created {created_count} new book(s). '
            f'{len(books) - created_count} already existed.'
        ))
