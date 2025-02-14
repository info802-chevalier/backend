def create_app():
    """
    Crée et configure une instance de l'application Flask.

    Cette fonction initialise une application Flask et configure CORS (Cross-Origin Resource Sharing)
    pour permettre aux requêtes provenant de n'importe quelle origine d'accéder aux ressources
    sous le préfixe '/api/*'.

    :return: Une instance de l'application Flask configurée.
    """
    from flask import Flask
    from flask_cors import CORS
    app = Flask(__name__)
    ## CORS
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    return app

def create_api(app):
    """
    Crée et configure une instance de l'API Flask-Restful.

    Cette fonction configure une instance de l'API Flask-Restful avec les ressources
    définies dans les modules importés ci-dessous.

    :param app: Une instance de l'application Flask.
    :return: Une instance de l'API Flask-Restful configurée.
    """
    from flask import render_template
    from flask_restful import Api
    from flask_restful_swagger import swagger
    api = swagger.docs(Api(app, prefix="/api"), apiVersion='1', api_spec_url="/documentation")
    ## Classes importées
    from api.resources.ORS.OrsRoute import OrsRoute
    from api.resources.ORS.OrsRouteCoordinates import OrsRouteCoordinates
    from api.resources.ORS.OrsRouteSummary import OrsRouteSummary
    from api.resources.ORS.OrsGeocodeSearch import OrsGeocodeSearch
    from api.resources.ORS.OrsRouteDetailed import OrsRouteDetailed

    from api.resources.ChargeTrip.CtVehicleList import ChargeTripVehicles
    from api.resources.ChargeTrip.CtNearestStation import ChargeTripNearestStation

    ## Routes
    # -- Base --
    @app.route('/api')
    def home():
        return render_template('documentation.html')
    # -- ORS --
    api.add_resource(OrsRoute, '/ors/route/<string:start>/<string:end>')
    api.add_resource(OrsRouteCoordinates, '/ors/route/coordinates/<string:start>/<string:end>')
    api.add_resource(OrsRouteSummary, '/ors/route/summary/<string:start>/<string:end>')
    api.add_resource(OrsGeocodeSearch, '/ors/geocode/search/<string:text>')
    api.add_resource(OrsRouteDetailed, '/ors/route/detailed')
    # -- ChargeTrip --
    api.add_resource(ChargeTripVehicles, '/ct/vehicles')
    api.add_resource(ChargeTripNearestStation, '/ct/stations/nearest/<string:longitude>/<string:latitude>')
    return api
