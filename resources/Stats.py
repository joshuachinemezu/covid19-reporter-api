from flask_restful import Resource


class Stats(Resource):
    def get(self):
        return {'status': 'success', 'data': 'Hello'}, 200
