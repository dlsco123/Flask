from flask import Flask

def create_app():
    app = Flask(__name__)

    from .views import main_views, classification_views, chat_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(classification_views.bp)
    app.register_blueprint(chat_views.bp)

    return app