# vibo: первоисточник https://www.youtube.com/watch?v=Qw-Wj6NZelQ

# vibo: запускаем бота из терминала
# vibo: python main.py --token $(cat secrets/token)

# vibo: исходный пример кода с гитхаба, эхобот (принимает сообщание и отправляет его в ответ)

import logging

# vibo: добавляем библиотеку (нужна для создания функции парсера аргументов)
import argparse

# vibo: добавили для Application
import telegram.ext as tg_ext

# vibo: перед эти через терминал pip install -r requirements.txt

# vibo: закоментим лишнее
# from telegram import ForceReply, Update

# vibo: закоментим лишнее
# from telegram.ext import (
#    Application,
#    CommandHandler,
#    ContextTypes,
#    MessageHandler,
#    filters,
# )

# vibo: ИМПОРТИРУЕМ СОЗДАННЫЙ НАМИ МЕТОД
from bot import handlers

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# vibo: перенесли три функwии в handlers.py

# vibo: деалем функцию, которая создает парсер аргументов питона
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--token', type=str, required=True)
    return parser.parse_args()


# vibo: начинаем с функции main
def main() -> None:
    # vibo: идем в BotFather, получаем токен
    # vibo: хотим спрятать токен
    # vibo: возвращаем аргументы функции, написанной выше
    args = parse_args()
    # application = Application.builder().token("TOKEN").build()
    # application = Application.builder().token(args.token).build()
    # vibo: делаем Application
    application = tg_ext.Application.builder().token(args.token).build()

    # vibo: вынесли application start, help и эхо в отдельный файл
    # vibo: вызываем созданный нами метод и передаем application
    handlers.setup_handlers(application)
    # vibo: запускаем код в работу
    application.run_polling()


if __name__ == "__main__":
    main()

# vibo: бот простой, для развития вынесем ряд функций в отдельный файл
