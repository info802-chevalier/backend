import os
from flask import request
from flask_restful import Resource
from flask_restful_swagger import swagger
from flask_cors import cross_origin
from app.resources.ApiHandler import ApiHandler


## Get from .env file
OPEN_ROUTE_SERVICE_API_URL = os.getenv('OPEN_ROUTE_SERVICE_API_URL')
OPEN_ROUTE_SERVICE_API_KEY = os.getenv('OPEN_ROUTE_SERVICE_API_KEY_1') 

headers = {
    "Authorization" : OPEN_ROUTE_SERVICE_API_KEY,
    "Content-Type": "application/json; charset=utf-8",
    "Accept" : "application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8"
}

api_handler = ApiHandler(url=OPEN_ROUTE_SERVICE_API_URL, token=OPEN_ROUTE_SERVICE_API_KEY, headers=headers)

class OrsRouteDetailed(Resource):
    @swagger.operation()
    @cross_origin()
    def post(self):
        """
        Retourne un itinéraire routier (driving-car) détailé en format GeoJSON entre deux points de départ et d'arrivée .
        
        :param coordinates: Liste de coordonnées GPS (format : [[lon1, lat1], [lon2, lat2], ...])
        :return: itinéraire routier en format GeoJSON, ou le JSON de la reponse en cas d'erreur
        """
        data = request.get_json()
        coordinates = data.get("coordinates", [])
        payload = {
            "coordinates": coordinates
        }
        response = api_handler.post('/v2/directions/driving-car', payload)
        if response.status_code == 200:
            return response.json()["features"][0]
        return response.json()