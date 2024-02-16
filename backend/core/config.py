import os


class Config:
    def __init__(self):
        self.BASEDIR = os.path.abspath(os.path.dirname(__file__))
        self.SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///")


