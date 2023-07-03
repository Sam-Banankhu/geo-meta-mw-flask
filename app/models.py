from app import db

class District(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    code = db.Column(db.String(255))
    region = db.Column(db.String(255))

    def populate_from_csv(self, row):
        self.name = row[0]
        self.code = row[1]
        self.region = row[2]


class ResidentialArea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    district_id = db.Column(db.Integer, db.ForeignKey('district.id'))
    name = db.Column(db.String(255))

    def populate_from_csv(self, row):
        self.district_id = int(row[0])
        self.name = row[1]


class TraditionalAuthority(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    district_id = db.Column(db.Integer, db.ForeignKey('district.id'))

    def populate_from_csv(self, row):
        self.name = row[0]
        self.district_id = int(row[1])


class Village(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    village_name = db.Column(db.String(255))
    district_id = db.Column(db.Integer, db.ForeignKey('district.id'))

    def populate_from_csv(self, row):
        self.village_name = row[0]
        self.district_id = int(row[1])


class Constituency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    district_id = db.Column(db.Integer, db.ForeignKey('district.id'))

    def populate_from_csv(self, row):
        self.name = row[0]
        self.district_id = int(row[1])


class Ward(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    constituency_id = db.Column(db.Integer, db.ForeignKey('constituency.id'))

    def populate_from_csv(self, row):
        self.name = row[0]
        self.constituency_id = int(row[1])
