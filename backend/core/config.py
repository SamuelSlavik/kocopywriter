import os


class Config():
    def __init__(self):
        self.BASEDIR = os.path.abspath(os.path.dirname(__file__))
        self.TOKEN_EXPIRATION = 120 # minutes
        self.SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/postgres")
        self.FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")
        self.IMAGES_DIR = os.path.join("images", "")
        self.BRANDS_IMAGES_DIR = os.path.join("images", "brands")
        self.REFERENCES_IMAGES_DIR = os.path.join("images", "references")
        self.POST_IMAGES_DIR = os.path.join("images", "posts")


config = Config()
