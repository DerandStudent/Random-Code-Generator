from service_1 import db

# classes of db model
class Codes(db.Model):
    code_id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.Text, nullable=False)