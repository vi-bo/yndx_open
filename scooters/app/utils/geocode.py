#vibo: файл геокодирования

import typing as tp

import aiohttp

from app import dto

#vibo: класс, которому мы даем ключ (надо сделать https://yandex.ru/dev/maps/geocoder/)
class GeocoderClient:
    def __init__(
        self,
        api_key: str,
        base_url: str = 'https://geocode-maps.yandex.ru',
    ) -> None:
        #vibo: api-ключ
        self.api_key = api_key
        self.base_url = base_url

    #vibo: класс имеет один метод get_address, принимает созданную локацию
    async def get_address(self, location: dto.Location) -> tp.Optional[str]:
        #vibo: делаем сессию с aiohttp клиентом
        async with aiohttp.ClientSession(self.base_url) as session: 
            #vibo: делаем get
            async with session.get(
                '/1.x/',
                params={
                    #vibo: фомат на входе json
                    'format': 'json',
                    #vibo: геоданные
                    'geocode': f'{location.lat},{location.lon}',
                    #vibo: api ключ
                    'apikey': self.api_key,
                },
            ) as response:
                
                #vibo: если наш запрос закончился 200 ответом, то обрабатываем, если нет - выходим
                #vibo: данный подход называется "ранний выход", помогает не писать вложенные конструкции
                #vibo: нужно стараться выйти раньше
                #vibo: этот же код можно написать с тройной вложенностью и это будет плохо
                if response.status != 200:
                    return None

                data = await response.json()

                #vibo: дебажим null
                #print(data)

                member = data['response']['GeoObjectCollection'][
                    'featureMember'
                ]

                if not member:
                    return None

                return member[0]['GeoObject']['metaDataProperty'][
                    'GeocoderMetaData'
                ]['text']
