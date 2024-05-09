import requests
from config import API_KEY
from pprint import pprint
from dataclasses import dataclass


@dataclass
class GeoModel:
    adress: str 
    lat: float
    lng: float 
    

class Geocoder:
    BASE_URL = 'https://geocode.search.hereapi.com/v1/geocode'
    API_KEY = API_KEY
    
    def get_adress_lat_lng(self, adress: str) -> GeoModel:
        params = {'q': adress, 'limit': 4, 'apiKey': self.API_KEY}

        with requests.get(self.BASE_URL, params=params) as response:
            result = response.json()
            return result
    
    def response_mapping(self, response: dict) -> GeoModel:
        try:
            data = response['items'][0]
        except (KeyError, IndexError):
            print('no data')
            return

        result = GeoModel(adress=data['title'], lat=data['position']['lat'], lng=data['position']['lng'])
        return result 

def main():
    # Тестим на 3 данных
    adress_list=[
        'Москва, Кронштадтский бульвар, 8к1',
        'Москва, Рябиновая , 3к3',
        'Москва, Трехгорный Вал, 1'
    ]
    coder = Geocoder()
    
    pprint(coder.get_adress_lat_lng(adress=adress_list[0]))


if __name__ == "__main__":
    main()
