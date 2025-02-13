import os
from flask_restful import Resource
from flask_restful_swagger import swagger
from    app.resources.ApiHandler import ApiHandler


## Get from .env file
OPEN_ROUTE_SERVICE_API_URL = os.getenv('OPEN_ROUTE_SERVICE_API_URL')
OPEN_ROUTE_SERVICE_API_KEY = os.getenv('OPEN_ROUTE_SERVICE_API_KEY_1') 

headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Accept" : "application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8"
}

api_handler = ApiHandler(url=OPEN_ROUTE_SERVICE_API_URL, token=OPEN_ROUTE_SERVICE_API_KEY, headers=headers)

class OrsRouteSummary(Resource):
    @swagger.operation()
    def get(self, start, end):
        """
        Retourne un résumé  d'itinéraire routier (driving-car) en format JSON entre deux points de départ et d'arrivée .
        
        :param start: Coordonnées gps de départ (format : "lon,lat")
        :param end: Coordonnées gps d'arrivée (format : "lon,lat")
        :return: Un dictionnaire contenant le résumé  de l'itinéraire routier (temps de trajet, en minutes, et longueur du trajet en mètres)
        """
        response = api_handler.get(f'/v2/directions/driving-car?api_key={OPEN_ROUTE_SERVICE_API_KEY}&start={start}&end={end}')
        if response.status_code == 200:
            return response.json()["features"][0]["properties"]["summary"]
        return response.json()