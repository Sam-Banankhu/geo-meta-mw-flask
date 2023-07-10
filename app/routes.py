from flask import render_template, jsonify
from app import app
from app.models import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/regions', methods=['GET'])
def get_regions():
    regions = Region.query.all()
    result = [{'id': d.id, 'name': d.name, 'code': d.code} for d in regions]
    return jsonify(result)

@app.route('/api/districts', methods=['GET'])
def get_districts():
    districts = District.query.all()
    result = [{'id': d.id, 'name': d.name, 'code': d.code, 'region': d.region.name} for d in districts]
    return jsonify(result)

@app.route('/api/districts/<code>', methods=['GET'])
def get_district_by_code(code):
    district = District.query.filter_by(code=code.upper()).first()
    if not district:
        abort(404, 'Districts not found')  # Return a 404 Not Found error if district with the provided code does not exist

    district_data = {
        'id': district.id,
        'name': district.name,
        'code': district.code,
        'region': district.region.name
    }
    return jsonify(district_data)


@app.route('/api/cities', methods=['GET'])
def get_cities():
    cities = City.query.all()
    result = [{'id': c.id, 'name': f"{c.name} City", 'district': c.district.name, 'region': c.district.region.name} for c in cities]
    return jsonify(result)

# code to download csv of cities
@app.route('/api/cities/download', methods=['GET'])
def download_cities_csv():
    cities = City.query.all()
    data = 'id,name,district_id\n'  # CSV header
    for city in cities:
        data += f'{city.id},{city.name},{city.district_id}\n'  # CSV data rows

    response = Response(data, mimetype='text/csv')
    response.headers.set('Content-Disposition', 'attachment', filename='cities.csv')
    return response


@app.route('/api/city/<city_name>', methods=['GET'])
def get_city_by_name(city_name):
    city = City.query.filter_by(name=city_name.title()).first()
    if not city:
        abort(404, 'Districts not found')  # Return a 404 Not Found error if district with the provided code does not exist

    city_data = {
        'id': city.id,
        'name': city.name,
        'region': city.district.region.name
    }
    return jsonify(city_data)

@app.route('/api/districts/<code>/cities', methods=['GET'])
def get_cities_in_district(code):
    district = District.query.filter_by(code=code.upper()).first()
    if not district:
        abort(404)  # Return a 404 Not Found error if district with the provided code does not exist

    cities = City.query.filter_by(district_id=district.id).all()
    city_data = [{'id': city.id, 'name': city.name, 'district_name': district.name} for city in cities]
    return jsonify(city_data)


@app.route('/api/cities/<city_name>/zip-codes', methods=['GET'])
def get_zip_codes(city_name):
    city = City.query.filter_by(name=city_name).first()
    if not city:
        return jsonify({'error': 'City not found'}), 404

    zip_codes = []
    for ward in city.wards:
        zip_codes.extend([v.zip_code for v in ward.villages])

    return jsonify({'city': city_name, 'zip_codes': zip_codes})



@app.route('/api/residential_areas', methods=['GET'])
def get_residential_areas():
    residential_areas = ResidentialArea.query.all()
    result = [{'id': r.id, 'name': r.name,  'district_name': r.district.name} for r in residential_areas]
    return jsonify(result)

@app.route('/api/traditional_authorities', methods=['GET'])
def get_traditional_authorities():
    traditional_authorities = TraditionalAuthority.query.all()
    result = [{'id': t.id, 'name': t.name, 'district_name': t.district.name} for t in traditional_authorities]
    return jsonify(result)

@app.route('/api/villages', methods=['GET'])
def get_villages():
    villages = Village.query.all()
    result = [{'id': v.id, 'village_name': v.village_name, 'district_name': v.district.name} for v in villages]
    return jsonify(result)

@app.route('/api/constituencies', methods=['GET'])
def get_constituencies():
    constituencies = Constituency.query.all()
    result = [{'id': c.id, 'name': c.name, 'district_name': c.district.name} for c in constituencies]
    return jsonify(result)

@app.route('/api/wards', methods=['GET'])
def get_wards():
    wards = Ward.query.all()
    result = [{'id': w.id, 'name': w.name, 'constituency_name': w.constituency.name} for w in wards]
    return jsonify(result)

# TO-DO add code to get schools by city, district, region etc