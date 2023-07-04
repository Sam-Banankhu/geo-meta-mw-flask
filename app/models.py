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


class City(db.Model):
 class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    district_id = db.Column(db.Integer, db.ForeignKey('district.id'))
    district = db.relationship('District', backref=db.backref('cities', lazy=True))

    def __repr__(self):
        return f'<City {self.name}>'


class ResidentialArea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    district_id = db.Column(db.Integer, db.ForeignKey('district.id'))
    name = db.Column(db.String(255))
    district = db.relationship('District', backref=db.backref('residential_areas'))

    def __repr__(self):
        return f'<ResidentialArea {self.name}>'

    def populate_from_csv(self, row):
        self.district_id = int(row[0])
        self.name = row[1]


class TraditionalAuthority(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    district_id = db.Column(db.Integer, db.ForeignKey('district.id'))
    district = db.relationship('District', backref=db.backref('traditional_authorities'))

    def __repr__(self):
        return f'<TraditionalAuthority {self.name}>'

    def populate_from_csv(self, row):
        self.name = row[0]
        self.district_id = int(row[1])


class Village(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    village_name = db.Column(db.String(255))
    district_id = db.Column(db.Integer, db.ForeignKey('district.id'))
    district = db.relationship('District', backref=db.backref('villages'))

    def __repr__(self):
        return f'<Village {self.village_name}>'

    def populate_from_csv(self, row):
        self.village_name = row[0]
        self.district_id = int(row[1])


class Constituency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    district_id = db.Column(db.Integer, db.ForeignKey('district.id'))
    district = db.relationship('District', backref=db.backref('constituencies'))

    def __repr__(self):
        return f'<Constituency {self.name}>'

    def populate_from_csv(self, row):
        self.name = row[0]
        self.district_id = int(row[1])


class Ward(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    constituency_id = db.Column(db.Integer, db.ForeignKey('constituency.id'))
    constituency = db.relationship('Constituency', backref=db.backref('wards'))

    def __repr__(self):
        return f'<Ward {self.name}>'

    def populate_from_csv(self, row):
        self.name = row[0]
        self.constituency_id = int(row[1])
