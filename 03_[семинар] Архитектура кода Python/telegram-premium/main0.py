# vibo: запускаем бота из терминала
# vibo: python main.py --token $(cat secrets/token)

# vibo: исходный пример кода с гитхаба, эхобот (принимает сообщание и отправляет его в ответ)

import logging

# vibo: добавляем библиотеку (нужна для создания функции парсера аргументов)
import argparse

# vibo: перед эти через терминал pip install -r requirements.txt
from telegram import ForceReply, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# vibo: функия приветствия, возвращает имя пользователя
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


# vibo: функция, возвращает Help!
async def help_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    await update.message.reply_text("Help!")


# vibo: функция, собственно 'эхо'
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)


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
    application = Application.builder().token(args.token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    )

    application.run_polling()


if __name__ == "__main__":
    main()

# vibo: бот простой, для развития вынесем ряд функций в отдельный файл
