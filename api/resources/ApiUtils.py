from flask import render_template
from flask_restful import Resource
from flask_restful_swagger import swagger
from api.resources.ApiHandler import ApiHandler


class ApiUtils(Resource):
    @swagger.operation()
    def get(self):
        """
        Affiche la documentation de l'API

        Renvoie un template HTML qui affiche la documentation de l'API.
        """
        return render_template("documentation.html")