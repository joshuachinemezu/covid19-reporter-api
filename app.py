from flask import Blueprint
from flask_restful import Api
from resources.Stats import Stats, GlobalStatsCount, AffectedCountriesDetailed

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(Stats, '/global/stats')
api.add_resource(GlobalStatsCount, '/global/count')
api.add_resource(AffectedCountriesDetailed, '/global/affected/stats')