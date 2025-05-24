from django.apps import AppConfig
from django.db import connections
from django.db.utils import OperationalError
import sys

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        # Only run this when using the runserver command
        if 'runserver' not in sys.argv:
            return

        db_conn = connections['default']
        try:
            db_conn.cursor()
        except OperationalError:
            print("Database not connected.")
        else:
            print("Successfully connected to the database.")
