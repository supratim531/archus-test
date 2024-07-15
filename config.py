from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

# Server Key
# Secret key (use your random key for security)"
KEY = "928635e70a014b41bfd38a66cf6a1939"

# SMTP
# SMTP_USE_TLS = True  # will automatically detect port 587
# SMTP_USE_TLS = True  # will automatically detect port 465
SMTP_SERVER = ''
SMTP_USERNAME = ''
SMTP_PASSWORD = ''
SMTP_USE_TLS = True
SMTP_USE_SSL = False

# CORS
ALLOWED_ORIGINS = ['*']
ALLOWED_HEADERS = ['Content-Type']
ALLOWED_METHODS = ['OPTIONS', 'POST', 'PUT', 'PATCH', 'DELETE']

# Throttling
MAX_REQUESTS = 10
PERIOD = 60  # Seconds

# Dirs
LOG_DIR = "log"
MEDIA_DIR = "media"
STATIC_DIR = "static"
TEMPLATE_DIR = "templates"