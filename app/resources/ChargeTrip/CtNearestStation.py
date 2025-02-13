import os
from flask_restful import Resource
from flask_restful_swagger import swagger
from app.resources.ApiHandler import ApiHandler

# Récupérer les variables d'environnement
CHARGE_TRIP_API_URL = os.getenv("CHARGE_TRIP_API_URL")
CHARGE_TRIP_X_CLIENT_ID = os.getenv("CHARGE_TRIP_X_CLIENT_ID_2")
CHARGE_TRIP_X_APP_ID = os.getenv("CHARGE_TRIP_X_APP_ID_2")

# Configurer les en-têtes pour l'API Charge Trip
headers = {
    "Content-Type": "application/json",
    "x-client-id": CHARGE_TRIP_X_CLIENT_ID,
    "x-app-id": CHARGE_TRIP_X_APP_ID,
}

api_handler = ApiHandler(url=CHARGE_TRIP_API_URL, token=None, headers=headers)

# Définir une classe pour obtenir la liste des véhicules électriques
class ChargeTripNearestStation(Resource):
    @swagger.operation()
    def get(self, longitude, latitude):
        """
        Requête GET pour obtenir la station de recharge la plus proche des coordonnées fournies.

        Cette méthode envoie une requête GraphQL pour récupérer des informations sur la station
        de recharge la plus proche dans un rayon de 10 km autour des coordonnées GPS fournies.

        :param longitude: Longitude du point de départ
        :param latitude: Latitude du point de départ
        :return: Un dictionnaire contenant les détails de la station de recharge la plus proche ou un objet d'erreur
        :rtype: dict
        """
        query = """
        {
          stationAround(
            filter: {
            location: { type: Point, coordinates: [ """ + str(longitude) + """,""" + str(latitude) + """ ] }
            distance: 10000
            powers: [50, 22]
            amenities: []
            }
            size: 1
            page: 0
        ) {
            id
            external_id
            name
            location {
            type
            coordinates
            }
            elevation
            physical_address {
            continent
            country
            county
            city
            street
            number
            postalCode
            what3Words
            formattedAddress
            }
            amenities
            power
            # add more fields here
        }
        }
        """
        response = api_handler.post("", {"query" : query})

        # Vérifier le statut de la réponse et renvoyer les données ou une erreur
        if response.status_code == 200:
            return response.json()["data"]["stationAround"]
        return {
            "error": f"Failed to fetch charging stations. Status code: {response.status_code}",
            "details": response.text,
        }

