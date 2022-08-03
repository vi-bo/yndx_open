# vibo: пишем функцию, которая ходит в базу данных

from asyncio import futures
from ctypes import addressof
import dataclasses
import typing as tp
import time
import asyncio

from app.context import AppContext
from app import storage
from app import dto
from app.utils import geocode

# vibo: название функции - это супер-важно
# vibo: дообогащение данными
# vibo: из личного опыта - идем в переводчик и подбираем нужное слово
async def _enrich_address(
    scooters: tp.List[dto.Scooter], client: geocode.GeocoderClient
) -> None:
    futures = [client.get_address(scooter.location) for scooter in scooters]

    result = await asyncio.gather(*futures)

    for scooter, address in zip(scooters, result):

        # vibo: мы используем ассинхронный фреймворк
        # vibo: в этом месте мы идем циклом, медленно
        # address = await client.get_address(scooter.location)
        # vibo: дебажим null
        # print(address)
        scooter.address = address


@dataclasses.dataclass
class GetScootersParams:
    fetch_address: bool = False


async def get_scooters(
    context: AppContext, params: GetScootersParams
) -> tp.List[dto.Scooter]:
    scooters = [
        dto.Scooter.from_model(scooter)
        for scooter in await storage.get_scooters(context)
    ]

    # vibo: обогащать параметрами будем если только стоит флаг, что нужно фетчить
    if params.fetch_address:
        # vibo: замерим время выполнения обращения к геокодеру
        start = time.time()
        # vibo: нижняя черта скрывает метод от внешнего импортирования
        await _enrich_address(scooters, context.geocoder)
        finish = time.time()
        print(f'Elapsed time: {finish - start}')
        # vibo: у меня получилось Elapsed time: 3.0557057857513428
        # vibo: и это для 10 самокатов, очень медленно, используем преимущество
        # vibo: ассинхронного бэкенда - будем ходит в геокодер параллельно

        # vibo: улучшение за счет ассинхронности до Elapsed time: 0.8750975131988525

    return scooters
