from flask import render_template, jsonify
from app import app
from app.models import *

@app.route('/')
def index():
    return '<h1 style = "color:red">Hello, World!</h1>'

@app.route('/api/districts', methods=['GET'])
def get_districts():
    districts = District.query.all()
    result = [{'id': d.id, 'name': d.name, 'code': d.code, 'region': d.region} for d in districts]
    return jsonify(result)

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
