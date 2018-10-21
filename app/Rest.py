from flask import Blueprint
from flask import Response
from flask import request
from app import app
from json import dumps

rest_api = Blueprint('rest_api', __name__)

@rest_api.route("/")
def helloRest():
    return "Hello Rest"

#Here I want to add some endpoint that returns fake data

@rest_api.route("/cars_agg", methods=["GET"])
def carsAgg():
    #Dummy parameters, won't be used
    start_date = request.args.get('start')
    end_date   = request.args.get('end')
    #Location makes this more generic than country/city
    location   = request.args.get('location')
    #Insurance and fuel options should use ids, but for simplicity I'll use strings
    aggregatedData = [
            {
                "company"           : "Hertz",
                "car"               : "audi_a4_2017",
                "fuel_options"      : ["full-to-full", "return-empty"],
                "insurance_options" : ["basic", "full-with-deductible", "full-without-deductibe"],
                "base_price_eur"    : 123.10,
                "insurance_prices"  : [0, 20, 30.5],
                "fuel_prices"       : [0,20]
            },
            {
                "company"           : "Hertz",
                "car"               : "audi_a3_2017",
                "fuel_options"      : ["full-to-full", "return-empty"],
                "insurance_options" : ["basic", "full-with-deductible", "full-without-deductibe"],
                "base_price_eur"    : 100.90,
                "insurance_prices"  : [0, 15, 20.5],
                "fuel_prices"       : [0,17]
            },
            {
                "company"           : "Alamo",
                "car"               : "audi_a4_2017",
                "fuel_options"      : ["return-empty"],
                "insurance_options" : ["full-with-deductible", "full-without-deductibe"],
                "base_price_eur"    : 121.10,
                "insurance_prices"  : [0, 30.5],
                "fuel_prices"       : [0]
            },
            {
                "company"           : "Avis",
                "car"               : "bmw_z3_2015",
                "fuel_options"      : ["return-empty"],
                "insurance_options" : ["full-with-deductible", "full-without-deductibe"],
                "base_price_eur"    : 143,
                "insurance_prices"  : [0, 30.5],
                "fuel_prices"       : [0]
            }
    ]
    return Response(dumps({'data': aggregatedData}), status=200)
