from datetime import date
from django.core.management.base import BaseCommand
from books.models import Book


class Command(BaseCommand):
    help = 'Seed the database with sample books'

    def handle(self, *args, **options):
        books = [
            {
                'title': 'Django for Beginners',
                'author': 'William S. Vincent',
                'pages': 294,
                'pub_date': date(2022, 5, 1),
            },
            {
                'title': 'Two Scoops of Django',
                'author': 'Daniel & Audrey Feldroy',
                'pages': 530,
                'pub_date': date(2022, 1, 15),
            },
            {
                'title': 'Fluent Python',
                'author': 'Luciano Ramalho',
                'pages': 792,
                'pub_date': date(2022, 4, 1),
            },
            {
                'title': 'Clean Code',
                'author': 'Robert C. Martin',
                'pages': 464,
                'pub_date': date(2008, 8, 1),
            },
            {
                'title': 'The Pragmatic Programmer',
                'author': 'David Thomas & Andrew Hunt',
                'pages': 352,
                'pub_date': date(2019, 9, 23),
            },
            {
                'title': 'Design Patterns',
                'author': 'Gang of Four',
                'pages': 395,
                'pub_date': date(1994, 10, 31),
            },
        ]

        created_count = 0
        for book_data in books:
            _, created = Book.objects.get_or_create(
                title=book_data['title'],
                defaults=book_data,
            )
            if created:
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f'Done! Created {created_count} new book(s). '
                f'{len(books) - created_count} already existed.'
            )
        )
