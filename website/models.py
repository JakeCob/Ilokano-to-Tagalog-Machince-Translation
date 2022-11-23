from . import db

class TL_IL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tl = db.Column(db.String(300))
    il = db.Column(db.String(300))

    def __repr__(self):
        return f"TL_IL('{self.tl}', '{self.il}')"
