from service_1 import db

# classes of db model


class Codes(db.Model):
    code_id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.Text, nullable=False)

# make sur ethat the code is in string format


def __repr__(self):
    return f"Code('{self.code_id}','{self.code}')"
