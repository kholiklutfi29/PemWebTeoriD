from app import db

class Gambar(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    text = db.Column(db.String(128))
    url = db.Column(db.String(2048), nullable=False)

    def __repr__(self):
        return '<Gambar {}>'.format(self.url)