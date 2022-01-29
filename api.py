import requests


class GuessifyApi(object):

    def __init__(self):
        self.endpoints = {
            "genderize": "https://api.genderize.io",
            "agify": "https://api.agify.io",
            "nationalize": "https://api.nationalize.io"
        }

    def get_predictions(self, name):
        response = list()
        params = {
            "name": name
        }
        for endpoint in self.endpoints:
            predictions = requests.request(url=self.endpoints[endpoint], params=params, method='GET')
            response.append(predictions.json())
        return response
