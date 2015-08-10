try:
    from django.db.backends.base.operations import BaseDatabaseOperations
except ImportError:
    from django.db.backends import BaseDatabaseOperations

class DatabaseOperations(BaseDatabaseOperations):
    def quote_name(self, name):
        return name # Netezza doesn't seem to like quoted names
