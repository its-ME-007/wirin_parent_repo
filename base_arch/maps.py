from flask import Flask, render_template, request, jsonify, Blueprint
import requests

global coords
coords = None
mapping_bp = Blueprint('mapping', __name__)

MAPBOX_TOKEN = 'pk.eyJ1Ijoid2lwb2RydmNlIiwiYSI6ImNsdnVzN255YzE5MDYycm55c3hheDhtdTUifQ.lEWdCkssgxZWHlg0eGNkiw'

@mapping_bp.route('/')
def index():
    return render_template('index.html', mapbox_token=MAPBOX_TOKEN)

@mapping_bp.route('/geocode')
def geocode():
    address = request.args.get('address')
    response = requests.get(f'https://api.mapbox.com/geocoding/v5/mapbox.places/{address}.json?access_token={MAPBOX_TOKEN}')
    data = response.json()
    coordinates = data['features'][0]['geometry']['coordinates']
    print(coordinates)
    return jsonify({'coordinates': coordinates})

@mapping_bp.route('/directions')
def directions():
    global coords
    start = request.args.get('start')
    end = request.args.get('end')
    response = requests.get(f'https://api.mapbox.com/directions/v5/mapbox/driving/{start};{end}?geometries=geojson&overview=full&steps=true&access_token={MAPBOX_TOKEN}')
    data = response.json()
    route = data['routes'][0]['geometry']
    print(route)
    print(data)
    return jsonify({'route': route})
    


@mapping_bp.route('/print', methods=['GET'])
def display():
    global coords
    return render_template('coords_display.html', coords=coords)

