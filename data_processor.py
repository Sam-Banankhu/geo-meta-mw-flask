import csv
from app import app, db
from app.models import District, ResidentialArea, TraditionalAuthority, Village, Constituency, Ward

# Function to read and insert data from CSV file
def insert_data_from_csv(csv_file, model):
    with app.app_context():
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                # Create an instance of the model and populate its attributes
                instance = model()
                instance.populate_from_csv(row)
                # Add the instance to the database session
                db.session.add(instance)
        # Commit the changes to the database
        db.session.commit()

# insert_data_from_csv('data/districts.csv', District)
# insert_data_from_csv('data/residential_areas.csv', ResidentialArea)
# insert_data_from_csv('data/traditional_authorities.csv', TraditionalAuthority)
# insert_data_from_csv('data/villages.csv', Village)
# insert_data_from_csv('data/constituencies.csv', Constituency)
# insert_data_from_csv('data/wards.csv', Ward)
