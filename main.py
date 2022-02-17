import logging
from flask import Flask
from waitress import serve
import settings
from routes import error_blueprint, health_blueprint, main_blueprint

logging.basicConfig(
    format="[%(asctime)s][%(levelname)s][%(name)s]: %(message)s",
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger('main')

def bootstrap():
    logger.info("Starting application")
    app = Flask(__name__)
    logger.info("Registering blueprints")
    app.register_blueprint(error_blueprint)
    app.register_blueprint(health_blueprint, url_prefix="/api")
    app.register_blueprint(main_blueprint, url_prefix="/api")
    serve(app, host=settings.HOST, port=settings.PORT)

bootstrap()
