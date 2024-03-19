# Django 가 DB 연결에 실패했을 시, 재시도를 하도록 만드는 로직을 추가\
from django.core.management.base import BaseCommand
from django.db import connections
import time

# Operation Error & Psycopg2 Operation Error
# from django.db.untils import OperationalError
# from psycopg2 import OperationalError asPsycopg2Error

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Wating for DB connection')

        is_db_connected = None
        while not is_db_connected:
            try:
                is_db_connected = connections['default']
            except:
                self.stdout.write("Retrying DB connection ...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("PostgreSQL DB Connection Success!!"))