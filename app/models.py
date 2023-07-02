from app import db

class District(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    code = db.Column(db.String(255))
    region = db.Column(db.String(255))

class ResidentialArea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    district_id = db.Column(db.Integer, db.ForeignKey('district.id'))
    name = db.Column(db.String(255))

class TraditionalAuthority(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    district_id = db.Column(db.Integer, db.ForeignKey('district.id'))

class Village(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    village_name = db.Column(db.String(255))
    district_id = db.Column(db.Integer, db.ForeignKey('district.id'))

class Constituency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    district_id = db.Column(db.Integer, db.ForeignKey('district.id'))

class Ward(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    constituency_id = db.Column(db.Integer, db.ForeignKey('constituency.id'))
