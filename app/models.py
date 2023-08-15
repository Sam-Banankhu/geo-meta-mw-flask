from app import db

class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    code = db.Column(db.String(255))
   

    def populate_from_csv(self, row):
        self.name = row[0]
        self.code = row[1]
        

class District(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    code = db.Column(db.String(255))
    region_id = db.Column(db.Integer, db.ForeignKey('region.id', onupdate='CASCADE', ondelete='CASCADE'))
    region = db.relationship('Region', backref=db.backref('districts'))

    def __repr__(self):
        return f'<District {self.name}>'
    
    def populate_from_csv(self, row):
        self.name = row[0]
        self.code = row[1]
        self.region_id = int(row[2])



class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    district_id = db.Column(db.Integer, db.ForeignKey('district.id', onupdate='CASCADE', ondelete='CASCADE'))
    district = db.relationship('District', backref=db.backref('cities'))

    def __repr__(self):
        return f'<City {self.name}>'

    def populate_from_csv(self, row):
        self.name = row[0]
        self.district_id = int(row[1])


class ResidentialArea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    district_id = db.Column(db.Integer, db.ForeignKey('district.id', onupdate='CASCADE', ondelete='CASCADE'))
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
    district_id = db.Column(db.Integer, db.ForeignKey('district.id', onupdate='CASCADE', ondelete='CASCADE'))
    district = db.relationship('District', backref=db.backref('traditional_authorities'))

    def __repr__(self):
        return f'<TraditionalAuthority {self.name}>'

    def populate_from_csv(self, row):
        self.name = row[0]
        self.district_id = int(row[1])


class Village(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    village_name = db.Column(db.String(255))
    district_id = db.Column(db.Integer, db.ForeignKey('district.id', onupdate='CASCADE', ondelete='CASCADE'))
    district = db.relationship('District', backref=db.backref('villages'))

    def __repr__(self):
        return f'<Village {self.village_name}>'

    def populate_from_csv(self, row):
        self.village_name = row[0]
        self.district_id = int(row[1])


class Constituency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    district_id = db.Column(db.Integer, db.ForeignKey('district.id', onupdate='CASCADE', ondelete='CASCADE'))
    district = db.relationship('District', backref=db.backref('constituencies'))

    def __repr__(self):
        return f'<Constituency {self.name}>'

    def populate_from_csv(self, row):
        self.name = row[0]
        self.district_id = int(row[1])


class Ward(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    constituency_id = db.Column(db.Integer, db.ForeignKey('constituency.id', onupdate='CASCADE', ondelete='CASCADE'))
    constituency = db.relationship('Constituency', backref=db.backref('wards'))

    def __repr__(self):
        return f'<Ward {self.name}>'

    def populate_from_csv(self, row):
        self.name = row[0]
        self.constituency_id = int(row[1])


class School(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(255))
    address = db.Column(db.String(255))
    district_id = db.Column(db.Integer, db.ForeignKey('district.id', onupdate='CASCADE', ondelete='CASCADE'))
    district = db.relationship('District', backref=db.backref('schools'))

    def __repr__(self):
        return f'<School {self.school_name}>'

    def populate_from_csv(self, row):
        self.school_name = row[0]
        self.address = row[1]
        self.district_id = int(row[2])

