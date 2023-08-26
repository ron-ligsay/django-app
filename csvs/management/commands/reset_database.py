from django.core.management.base import BaseCommand
from django.db import connections

class Command(BaseCommand):
    help = 'Delete all tables from the database'

    def handle(self, *args, **options):
        connection = connections['default']
        with connection.cursor() as cursor:
            cursor.execute('SET FOREIGN_KEY_CHECKS = 0;')
            cursor.execute('SHOW TABLES;')
            tables = cursor.fetchall()
            for table in tables:
                table_name = table[0]
                cursor.execute(f'DROP TABLE IF EXISTS {table_name};')
            cursor.execute('SET FOREIGN_KEY_CHECKS = 1;')

        self.stdout.write(self.style.SUCCESS('All tables deleted successfully'))
