import os
from flask_restful import Resource
from flask_restful_swagger import swagger
from app.resources.ApiHandler import ApiHandler


## Get from .env file
OPEN_ROUTE_SERVICE_API_URL = os.getenv('OPEN_ROUTE_SERVICE_API_URL')
OPEN_ROUTE_SERVICE_API_KEY = os.getenv('OPEN_ROUTE_SERVICE_API_KEY_2') 

headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Accept" : "application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8"
}

api_handler = ApiHandler(url=OPEN_ROUTE_SERVICE_API_URL, token=OPEN_ROUTE_SERVICE_API_KEY, headers=headers)

class OrsGeocodeSearch(Resource):
    @swagger.operation()
    def get(self, text):
        """
        Effectue une requête GET vers l'endpoint de recherche de géocodage avec le texte fourni.

        :param text: Le texte de recherche à utiliser pour le géocodage.
        :return: Une liste de fonctionnalités provenant de la réponse de recherche de géocodage en cas de succès, 
                sinon retourne le JSON de la réponse.
        """
        response = api_handler.get(f'/geocode/search?api_key={OPEN_ROUTE_SERVICE_API_KEY}&text={text}')
        if response.status_code == 200:
            return response.json()["features"]
        return response.json()