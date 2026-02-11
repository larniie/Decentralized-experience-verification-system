# Configuration settings for DEVS
class Config:
    DEBUG = True
    SECRET_KEY = 'your-secret-key-here'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///devs.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Add other configuration options as needed
