import os

from sqlalchemy import create_engine
from sqlalchemy.orm import close_all_sessions, sessionmaker, registry, clear_mappers
from sqlalchemy.engine import url

class Client():
    def __init__(self):

        driver = os.environ["DB_DRIVER"]
        username = os.environ["DB_USER"]
        password = os.environ["DB_PASSWORD"]
        database = os.environ["DB_NAME"]
        host = os.environ.get("ECOMMERCE_DABASE_NAME", None)

        db_url = url.URL.create(
            drivername = driver,
            username = username,
            password = password,
            database = database,
            host = host,
            query = None,
        )
        
        self.engine = create_engine(db_url, echo = False)
        self.session_factory = sessionmaker(bind = self.engine, expire_on_commit = False)
        self.mapper_registry = registry()
