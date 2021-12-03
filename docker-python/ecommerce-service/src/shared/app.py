from src.shared.infrastructure.framewrok.flask import create_flask_app
from src.shared.infrastructure.database.sqlalchemy import Client as sql_client

def create_app():
    app = App()
    return app.flask

class App:
    def __init__(self):
        self.databases = {
            "sql": sql_client
        }

        self.flask = create_flask_app(self)
    
    def run(self):
        return self.flask.run(host='127.0.0.1', port=8000)

