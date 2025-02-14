import os
from flask_restful import Resource
from flask_restful_swagger import swagger
from api.resources.ApiHandler import ApiHandler

# Récupérer les variables d'environnement
CHARGE_TRIP_API_URL = os.getenv("CHARGE_TRIP_API_URL")
CHARGE_TRIP_X_CLIENT_ID = os.getenv("CHARGE_TRIP_X_CLIENT_ID_1")
CHARGE_TRIP_X_APP_ID = os.getenv("CHARGE_TRIP_X_APP_ID_1")

# Configurer les en-têtes pour l'API Charge Trip
headers = {
    "Content-Type": "application/json",
    "x-client-id": CHARGE_TRIP_X_CLIENT_ID,
    "x-app-id": CHARGE_TRIP_X_APP_ID,
}

api_handler = ApiHandler(url=CHARGE_TRIP_API_URL, token=None, headers=headers)

# Définir une classe pour obtenir la liste des véhicules électriques
class ChargeTripVehicles(Resource):
    @swagger.operation()
    def get(self):
        # Définir la requête GraphQL
        """
        Requête GET pour obtenir la liste des véhicules électriques supportés par Charge Trip.

        La requête GraphQL est définie pour extraire les informations suivantes :
        - id
        - make, model, version, edition, chargetrip_version
        - type de transmission (moteur, batterie, etc.)
        - types de connecteurs (standard, power, max_electric_power, time, speed)
        - types d'adaptateurs (standard, power, max_electric_power, time, speed)
        - capacité de la batterie (usable_kwh, full_kwh)
        - nombre de places
        - disponibilité (status)
        - autonomie (best, worst)
        - images et vidéos associées
        - support de la recharge rapide
        - fournisseurs de recharge

        La réponse est un objet JSON contenant la liste des véhicules, ou un objet d'erreur
        si la requête a échoué.

        :return: Une liste de véhicules ou un objet d'erreur
        :rtype: list | dict
        """
        query = """
        {
          vehicleList {
            id
            naming {
              make
              model
              version
              edition
              chargetrip_version
            }
            drivetrain {
              type
            }
            connectors {
              standard
              power
              max_electric_power
              time
              speed
            }
            adapters {
              standard
              power
              max_electric_power
              time
              speed
            }
            battery {
              usable_kwh
              full_kwh
            }
            body {
              seats
            }
            availability {
              status
            }
            range {
              chargetrip_range {
                best
                worst
              }
            }
            media {
              image {
                id
                type
                url
                height
                width
                thumbnail_url
                thumbnail_height
                thumbnail_width
              }
              brand {
                id
                type
                url
                height
                width
                thumbnail_url
                thumbnail_height
                thumbnail_width
              }
              video {
                id
                url
              }
            }
            routing {
              fast_charging_support
            }
            connect {
              providers
            }
          }
        }
        """


        response = api_handler.post("", {"query" : query})

        # Vérifier le statut de la réponse et renvoyer les données ou une erreur
        if response.status_code == 200:
            return response.json()["data"]["vehicleList"]
        return {
            "error": f"Failed to fetch vehicles. Status code: {response.status_code}",
            "details": response.text,
        }

