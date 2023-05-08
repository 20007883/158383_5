from http.server import HTTPServer, SimpleHTTPRequestHandler


class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

from flask import Flask, jsonify, make_response
import psycopg2
import json

app = Flask(__name__)


# 定义一个 API 接口，返回一些数据
@app.route('/data/coedschool', methods=['GET'])
def get_data_coed():

    conn = psycopg2.connect(host='localhost', dbname='map_data', user='postgres', password='1234567')
    cur = conn.cursor()
    cur.execute('SELECT * FROM school_coed')
    rows = cur.fetchall()
    cur.execute("SELECT ST_AsGeoJSON(geom) FROM school_coed")
    g = cur.fetchall()
    conn.close()
    geojson = {
        'type': 'FeatureCollection',
        'name': 'school_coed',
        'features': []
    }

    # data = jsonify(data)
    # print(type(data))
    for row in range(len(rows)):
        geo = json.loads(g[row][0])

        feature = {
            'type': 'Feature',
            'properties': {
                'full_id': rows[row][1],
                'osm_id': rows[row][2],
                'osm_type': rows[row][3],
                'amenity': rows[row][4],
                'name_ar': rows[row][5],
                'school_gen': rows[row][6],
                'operator_t': rows[row][7],
                'not_name': rows[row][8],
                'contact_fa': rows[row][9],
                'capacity': rows[row][10],
                'natural': rows[row][11],
                'opening_da': rows[row][12],
                'pedagogy': rows[row][13],
                'ref': rows[row][14],
                'descriptio': rows[row][15],
                'building_l': rows[row][16],
                'addr_hamle': rows[row][17],
                'email': rows[row][18],
                'name_etymo': rows[row][19],
                'name_ety_1': rows[row][20],
                'barrier': rows[row][21],
                'landuse': rows[row][22],
                'wheelchair': rows[row][23],
                'owner': rows[row][24],
                'operator': rows[row][25],
                'building_f': rows[row][26],
                'grades': rows[row][27],
                'campus': rows[row][28],
                'start_date': rows[row][29],
                'name_mk': rows[row][30],
                'ref_linz_a': rows[row][31],
                'addr_subur': rows[row][32],
                'old_name': rows[row][33],
                'name_mi': rows[row][34],
                'building': rows[row][35],
                'religion': rows[row][36],
                'denominati': rows[row][37],
                'wikipedia': rows[row][38],
                'alt_name': rows[row][39],
                'addr_city': rows[row][40],
                'wikidata': rows[row][41],
                'website': rows[row][42],
                'type': rows[row][43],
                'phone': rows[row][44],
                'name': rows[row][45],
                'addr_stree': rows[row][46],
                'addr_postc': rows[row][47],
                'addr_house': rows[row][48],
                'moe_years': rows[row][49],
                'moe_id': rows[row][50],
                'moe_gender': rows[row][51],
                'moe_author': rows[row][52],
                'note': rows[row][53]
            }
            ,
            'geometry': {
                'type': 'MultiPolygon',
                'coordinates': geo['coordinates']
            }

        }
        geojson['features'].append(feature)
        json_data = json.dumps(geojson)

    response = make_response(json_data)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route('/data/girlschool', methods=['GET'])
def get_data_girl():

    conn = psycopg2.connect(host='localhost', dbname='map_data', user='postgres', password='1234567')
    cur = conn.cursor()
    cur.execute('SELECT * FROM school_girls')
    rows = cur.fetchall()
    cur.execute("SELECT ST_AsGeoJSON(geom) FROM school_girls")
    g = cur.fetchall()
    conn.close()
    geojson = {
        'type': 'FeatureCollection',
        'name': 'school_girls',
        'features': []
    }

    for row in range(len(rows)):
        geo = json.loads(g[row][0])

        feature = {
            'type': 'Feature',
            'properties': {
                'full_id': rows[row][1],
                'osm_id': rows[row][2],
                'osm_type': rows[row][3],
                'amenity': rows[row][4],
                'name_ar': rows[row][5],
                'school_gen': rows[row][6],
                'operator_t': rows[row][7],
                'not_name': rows[row][8],
                'contact_fa': rows[row][9],
                'capacity': rows[row][10],
                'natural': rows[row][11],
                'opening_da': rows[row][12],
                'pedagogy': rows[row][13],
                'ref': rows[row][14],
                'descriptio': rows[row][15],
                'building_l': rows[row][16],
                'addr_hamle': rows[row][17],
                'email': rows[row][18],
                'name_etymo': rows[row][19],
                'name_ety_1': rows[row][20],
                'barrier': rows[row][21],
                'landuse': rows[row][22],
                'wheelchair': rows[row][23],
                'owner': rows[row][24],
                'operator': rows[row][25],
                'building_f': rows[row][26],
                'grades': rows[row][27],
                'campus': rows[row][28],
                'start_date': rows[row][29],
                'name_mk': rows[row][30],
                'ref_linz_a': rows[row][31],
                'addr_subur': rows[row][32],
                'old_name': rows[row][33],
                'name_mi': rows[row][34],
                'building': rows[row][35],
                'religion': rows[row][36],
                'denominati': rows[row][37],
                'wikipedia': rows[row][38],
                'alt_name': rows[row][39],
                'addr_city': rows[row][40],
                'wikidata': rows[row][41],
                'website': rows[row][42],
                'type': rows[row][43],
                'phone': rows[row][44],
                'name': rows[row][45],
                'addr_stree': rows[row][46],
                'addr_postc': rows[row][47],
                'addr_house': rows[row][48],
                'moe_years': rows[row][49],
                'moe_id': rows[row][50],
                'moe_gender': rows[row][51],
                'moe_author': rows[row][52]

            }
            ,
            'geometry': {
                'type': 'MultiPolygon',
                'coordinates': geo['coordinates']
            }

        }
        geojson['features'].append(feature)
        json_data = json.dumps(geojson)

    response = make_response(json_data)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/data/boyschool', methods=['GET'])
def get_data_boy():

    conn = psycopg2.connect(host='localhost', dbname='map_data', user='postgres', password='1234567')
    cur = conn.cursor()
    cur.execute('SELECT * FROM school_boys')
    rows = cur.fetchall()
    cur.execute("SELECT ST_AsGeoJSON(geom) FROM school_boys")
    g = cur.fetchall()
    conn.close()
    geojson = {
        'type': 'FeatureCollection',
        'name': 'school_boys',
        'features': []
    }

    for row in range(len(rows)):
        geo = json.loads(g[row][0])

        feature = {
            'type': 'Feature',
            'properties': {
                'full_id': rows[row][1],
                'osm_id': rows[row][2],
                'osm_type': rows[row][3],
                'amenity': rows[row][4],
                'name_ar': rows[row][5],
                'school_gen': rows[row][6],
                'operator_t': rows[row][7],
                'not_name': rows[row][8],
                'contact_fa': rows[row][9],
                'capacity': rows[row][10],
                'natural': rows[row][11],
                'opening_da': rows[row][12],
                'pedagogy': rows[row][13],
                'ref': rows[row][14],
                'descriptio': rows[row][15],
                'building_l': rows[row][16],
                'addr_hamle': rows[row][17],
                'email': rows[row][18],
                'name_etymo': rows[row][19],
                'name_ety_1': rows[row][20],
                'barrier': rows[row][21],
                'landuse': rows[row][22],
                'wheelchair': rows[row][23],
                'owner': rows[row][24],
                'operator': rows[row][25],
                'building_f': rows[row][26],
                'grades': rows[row][27],
                'campus': rows[row][28],
                'start_date': rows[row][29],
                'name_mk': rows[row][30],
                'ref_linz_a': rows[row][31],
                'addr_subur': rows[row][32],
                'old_name': rows[row][33],
                'name_mi': rows[row][34],
                'building': rows[row][35],
                'religion': rows[row][36],
                'denominati': rows[row][37],
                'wikipedia': rows[row][38],
                'alt_name': rows[row][39],
                'addr_city': rows[row][40],
                'wikidata': rows[row][41],
                'website': rows[row][42],
                'type': rows[row][43],
                'phone': rows[row][44],
                'name': rows[row][45],
                'addr_stree': rows[row][46],
                'addr_postc': rows[row][47],
                'addr_house': rows[row][48],
                'moe_years': rows[row][49],
                'moe_id': rows[row][50],
                'moe_gender': rows[row][51],
                'moe_author': rows[row][52]

            }
            ,
            'geometry': {
                'type': 'MultiPolygon',
                'coordinates': geo['coordinates']
            }

        }
        geojson['features'].append(feature)
        json_data = json.dumps(geojson)

    response = make_response(json_data)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/data/park', methods=['GET'])
def get_data_park():
    conn = psycopg2.connect(host='localhost', dbname='map_data', user='postgres', password='1234567')
    cur = conn.cursor()
    cur.execute('SELECT * FROM park')
    rows = cur.fetchall()
    cur.execute("SELECT ST_AsGeoJSON(geom) FROM park")
    g = cur.fetchall()
    conn.close()
    geojson = {
        'type': 'FeatureCollection',
        'name': 'park',
        'features': []
    }

    for row in range(len(rows)):
        geo = json.loads(g[row][0])

        feature = {
            'type': 'Feature',
            'properties': {
        #         'full_id': rows[row][1],
        #         'osm_id': rows[row][2],
        #         'osm_type': rows[row][3],
        #         'leisure': rows[row][4],
        #
        #         # 'sorting_na': rows[row][60],
        #         # 'website': rows[row][61],
        #         # 'protection': rows[row][62],
        #         # 'protect_cl': rows[row][63],
        #         # 'natural': rows[row][64],
        #         # 'boundary': rows[row][65],
        #         # 'alt_name': rows[row][66],
        #         # 'wikipedia': rows[row][67],
        #         # 'wikidate': rows[row][68],
        #         # 'start_date': rows[row][69],
        #         # 'name_mk': rows[row][70],
        #         # 'name_ja': rows[row][71],
        #         # 'name_ety_1': rows[row][72],
        #         # 'name_ety_2': rows[row][73],
        #         # 'name_cs': rows[row][74],
        #         # 'operator_w': rows[row][75],
        #         # 'operator_1': rows[row][76],
        #         # 'operator_t': rows[row][77],
        #         # 'operator': rows[row][78],
        #         # 'name_mi': rows[row][79],
        #         # 'name_en': rows[row][80],
        #         # 'type': rows[row][81],
        #         # 'name': rows[row][82],
        #         # 'dog': rows[row][83],
        #
        #
        #
            }
            ,
            'geometry': {
                'type': 'MultiPolygon',
                'coordinates': geo['coordinates']
            }

        }
        geojson['features'].append(feature)
        json_data = json.dumps(geojson)

    response = make_response(json_data)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, CORSRequestHandler)
    app.run()
    httpd.serve_forever()

