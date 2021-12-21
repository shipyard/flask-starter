import os


class Parse:
    """Class of utility functions to parse environment variables"""

    @staticmethod
    def bool(field):
        """Parse booleans (defaults to False)"""
        return os.getenv(field, '').lower() in ['true', '1']

    @staticmethod
    def string(field, default=None):
        """
        Parse strings - defaults to the default value provided even if the environment variable is
        set to a blank string.
        """
        return os.getenv(field) or default


class Settings:

    # General
    DEV = Parse.bool('DEV')
    DOOM_URL = Parse.string('DOOM_URL', 'http://localhost:8000')
    REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
    REDIS_URL = f'redis://{REDIS_HOST}:6379'

    # Database
    AES_SECRET_KEY = os.getenv('AES_SECRET_KEY', 'fake-aes-key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

    # Celery
    CELERY_BROKER_URL = REDIS_URL
    CELERY_RESULT_BACKEND = REDIS_URL
    CELERY_CONFIG = {
        'beat_schedule': {
            'do_something': {
                'task': 'src.tasks.do_something',
                'args': (10,),
                'schedule': 5.0,
            },
        }
    }
