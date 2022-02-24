from os import environ


TOKEN = environ.get("TOKEN")

POSTGRES_HOST = environ.get("POSTGRES_HOST", default="db")
POSTGRES_PORT = environ.get("POSTGRES_PORT", default=5432)
POSTGRES_PASSWORD = environ.get("POSTGRES_PASSWORD", default="postgres")
POSTGRES_USER = environ.get("POSTGRES_USER", default="postgres")
POSTGRES_DB = environ.get("POSTGRES_DB", default="postgres")
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
