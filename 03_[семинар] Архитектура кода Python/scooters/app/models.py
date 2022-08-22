from __future__ import annotations

import typing as tp
import dataclasses

import asyncpg

from app import dto

# vibo: делаем модели (данные из БД)
@dataclasses.dataclass
class User:
    id: str

    @classmethod
    def from_db(cls, user_id: tp.Optional[str]) -> User:
        if user_id:
            return User(id=user_id)
        return None


'''
#vibo: использование tuple, как и dict - антипаттерн,
обращение в квадратных скобках по индексу и т.д. Делаем класс.
Читать код приходится гораздо больше, чем писать!
'''

# @dataclasses.dataclass
# class Location:
#     lat: float #vibo: широта
#     lon: float #vibo: долгота


@dataclasses.dataclass
class Scooter:
    id: str
    location: dto.Location
    user: tp.Optional[User] = None

    # #vibo: не лучшее решение
    # def get_address() -> str:
    #     pass

    @classmethod
    # vibo: пытаемся вернуть в тайпинге объект, который только что объявился,
    # vibo: добавляем выше import annotations
    def from_db(cls, row: asyncpg.Record) -> Scooter:
        # vibo: одно метсо, где можно обратиться через индексы, остальное только по имени
        return cls(
            id=row['id'],
            location=dto.Location(
                lat=row['location'][0], lon=row['location'][1]
            ),
            user=User.from_db(row['user']),
        )
