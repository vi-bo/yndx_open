#vibo: это надежный вариант хранения секретов, нежели, чем в коде

import os
import typing as tp

#vibo: класс, умеющий читать из файла
class SecretsReader:
    secrets_dir: str

    def __init__(self, secrets_dir: str):
        #vibo: указываем путь до секретов
        self.secrets_dir = secrets_dir

    #vibo: метод get, который принимает имя секрета
    #def get(self, name: str) -> tp.Optional[str]:
    def get(self, name: str) -> str:
        #vibo: ищем секрет с нужным имененм в нужной дирректории 
        filename = os.path.join(self.secrets_dir, name.lower())
        if os.path.exists(filename):
            #vibo: читаем найденный файл
            with open(filename) as file:
                return file.read().strip()
        #return None
        #vibo: делаем исключение
        raise ValueError(f'Secret: "{name}" not found')

#vibo: как доставляются секреты до секретной дирректории отдельный вопрос, есть варианты,
#vibo: например, docker-secrets (как самая базовая), или другие open-sourses продукты
