from flask_restful import Resource
import requests

covid_stats = requests.get('https://pomber.github.io/covid19/timeseries.json')

class Stats(Resource):
    def get(self):
        return {'status': 'success', 'data': covid_stats.json()}, 200


class CurrentGlobalStats(Resource):
    def get(self):
        date = '';
        confirmed = deaths = recovered = active = 0;
        data = covid_stats.json()
        countries = data.keys() 
        for country in countries:
            current = data[country][len(data[country]) - 1]
            date = current['date']
            confirmed = confirmed + current['confirmed']
            deaths = deaths + current['deaths']
            recovered = recovered + current['recovered']
            active = active + current['confirmed'] - current['deaths'] - current['recovered']

        response = {'date': date, 'confirmed': confirmed, 'deaths': deaths, 'recovered':recovered, 'active':active, 'number_of_countries': len(countries)}
	
        return {'status': 'success', 'data': response}, 200
