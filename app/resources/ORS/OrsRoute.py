import os
from flask_restful import Resource
from flask_restful_swagger import swagger
from app.resources.ApiHandler import ApiHandler


## Get from .env file
OPEN_ROUTE_SERVICE_API_URL = os.getenv('OPEN_ROUTE_SERVICE_API_URL')
OPEN_ROUTE_SERVICE_API_KEY = os.getenv('OPEN_ROUTE_SERVICE_API_KEY_1') 

headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Accept" : "application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8"
}

api_handler = ApiHandler(url=OPEN_ROUTE_SERVICE_API_URL, token=OPEN_ROUTE_SERVICE_API_KEY, headers=headers)

class OrsRoute(Resource):
    @swagger.operation()
    def get(self, start, end):
        """
        Retourne un itineraire routier (driving-car) en format GeoJSON entre deux points de depart et d'arrivée .
        
        :param start: Coordonnees gps de d part (format : "lon,lat")
        :param end: Coordonnees gps d'arrivee (format : "lon,lat")
        :return: itineraire routier en format GeoJSON, ou le JSON de la reponse en cas d'erreur
        """
        response = api_handler.get(f'/v2/directions/driving-car?api_key={OPEN_ROUTE_SERVICE_API_KEY}&start={start}&end={end}')
        if response.status_code == 200:
            return response.json()["features"][0]
        return response.json()