from app.api.v1.routes import v1_urls
from app.templating.routes import urls

from archus import Archus
from archus.middleware import SecurityHeadersMiddleware, CORSMiddleware, LoggingMiddleware, GlobalExceptionHandlerMiddleware

from config import BASE_DIR


application = Archus(BASE_DIR=BASE_DIR)

application.add_middleware(SecurityHeadersMiddleware)
application.add_middleware(CORSMiddleware)
application.add_middleware(LoggingMiddleware)
application.add_middleware(GlobalExceptionHandlerMiddleware)

application.register_blueprint("/", urls)
application.register_blueprint("/api/v1", v1_urls)