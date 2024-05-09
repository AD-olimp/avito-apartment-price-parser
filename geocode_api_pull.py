import asyncio
import aiohttp
from config import API_KEY
from pprint import pprint


class Geocoder:
    BASE_URL = 'https://geocode.search.hereapi.com/v1/geocode'
    API_KEY = API_KEY

    def __init__(self, adress_list):
        self.adress_list = adress_list 
            
    async def __get_adress_lat_lng(self, adress: str):
         async with aiohttp.ClientSession() as session:
            params = {'q': adress, 'limit': 4, 'apiKey': self.API_KEY}

            async with session.get(self.BASE_URL, params=params) as response:
                result = await response.json()
                return await self.__get_nessesary_data(result)
    
    async def __get_nessesary_data(self, response: dict) -> dict:
        return response['items'][0]['access']    
    
    async def convert_adresses(self):
        return await asyncio.gather(*[self.__get_adress_lat_lng(adress) for adress in self.adress_list])
        

async def main():
    # Тестим на 3 данных
    
    coder = Geocoder(
        adress_list=[
            'Москва, Кронштадтский бульвар, 8к1',
            'Москва, Рябиновая , 3к3',
            'Москва, Трехгорный Вал, 1'
        ]
    )
    
    pprint(await coder.convert_adresses())


if __name__ == "__main__":
    asyncio.run(main())
