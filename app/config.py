class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///structure.db"

class DevelopmentConfig(Config):
    DEBUG = True
    