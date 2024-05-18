import os


class Config():
    def __init__(self):
        self.BASEDIR = os.path.abspath(os.path.dirname(__file__))
        self.TOKEN_EXPIRATION = 120 # minutes
        self.SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://default:Qshx82gMEYNJ@ep-young-hill-a2xr36fw-pooler.eu-central-1.aws.neon.tech:5432/verceldb") # Change tou your db
        self.FRONTEND_URL = os.getenv("FRONTEND_URL", "https://kocopywriter-frontend.vercel.app/") # Change to your localhost
        self.IMAGES_DIR = os.path.join("images", "")
        self.BRANDS_IMAGES_DIR = os.path.join("images", "brands")
        self.REFERENCES_IMAGES_DIR = os.path.join("images", "references")
        self.POST_IMAGES_DIR = os.path.join("images", "posts")


config = Config()
