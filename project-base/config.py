import os

basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    HOST = str(os.environ.get("DB_HOST"))
    DATABASE = str(os.environ.get("DB_DATABASE"))
    USERNAME = str(os.environ.get("DB_USERNAME"))
    PASSWORD = str(os.environ.get("DB_PASSWORD"))
        # Untuk JWT Token
    JWT_SECRET_KEY = str(os.environ.get("JWT_SECRET"))

    # Koneksi ke SQLALCHEMY untuk mengkoneksi
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DATABASE
    # Mengatur track modifikasi apakah true/false
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # untuk ke record ke query
    SQLALCHEMY_RECORD_QUERIES = True

    UPLOAD_FOLDER = str(os.environ.get("UPLOAD_FOLDER"))
    # Membuat ukuran apa yang akan diupload
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024