# ensure package/conf is importable

DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "db_test"}
}

DEBUG = True

INSTALLED_APPS = (
    "djbookshelf",
    "tests",
    "bootstrap5",
)
MIDDLEWARE = []

ROOT_URLCONF = "tests.urls"

USE_TZ = True

TIME_ZONE = "UTC"

SECRET_KEY = "foobar"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
    }
]

STATIC_URL = "/static/"

# XMLTestRunner output
TEST_OUTPUT_DIR = ".xmlcoverage"
