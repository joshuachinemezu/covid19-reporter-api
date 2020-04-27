from flask import Blueprint
from flask_restful import Api
from resources.Stats import Stats, CurrentGlobalStats

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(Stats, '/stats')
api.add_resource(CurrentGlobalStats, '/global-stats')