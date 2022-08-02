# vibo: сейчас хендлеры оформлены как обычные функции, заменим их на функциональные объекты (aka фунтеры)
# vibo: заведем специальные классы, в кторых будет метод и эти классы будут вести себя как функции
# vibo: когда мы будем их вызывать - будет вызываться специальный метод __call__
# vibo: объявляем базовый класс хэндлера, это будет интерфейс хэндлера, чтобы все обработчики наших команд дальше
# vibo: будут это интерфейс имплементиовать.
# vibo:  В питоне нет настоящих интерфейсов, но есть модуль abc, в котором можно реализовать абстрактный класс
# vibo: и он будет вести себя как интерфейс
import abc
import typing as tp

# vibo: добавляем импорт телеграм с элиасом tg
import telegram as tg
import telegram.ext as tg_ext

# vibo: новый импорт
from bot import messages

# vibo: делаем класс абстрактным (наследуемся от специального класса ABC)
class BaseHandler(abc.ABC):
    # vibo: добавляем пользователя
    def __init__(self) -> None:
        self.user: tp.Optional[tg.User] = None

    async def __call__(
        self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE
    ) -> None:
        # vibo: индентифицируем пользователя
        self.user = update.effective_user
        self.messages = messages.get_messages(self.user)
        await self.handle(update, context)

    # vibo: делаем метод абстрактным
    @abc.abstractmethod
    # vibo: функция будет ассинхронная
    async def handle(
        self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE
    ) -> None:
        raise NotImplemented


# vibo: заимплементируем другие наши методы обработчики
# vibo: класс занимающийся обработкой команды старт
class StartHandler(BaseHandler):
    async def handle(
        self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE
    ) -> None:
        # await update.message.reply_html(
        #     #vibo: вынесем все сообщания в отдельный модуль
        #     #rf"Hi {user.mention_html()}!",
        #     rf"Hi {self.user.mention_html()}!",
        #     #vibo: добавили
        #     reply_markup=tg_ext.ForceReply(selective=True),
        # )
        await update.message.reply_text(self.messages.start())
        # #vibo: вводим условие выбор пользователя
        # if self.user.is_premium:
        #     await update.message.reply_text(messages.PremiumUser().start)
        # else:
        #     await update.message.reply_text(messages.RegularUser().start)


# vibo: класс занимающийся обработкой
class HelpHandler(BaseHandler):
    async def handle(
        self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE
    ) -> None:
        # await update.message.reply_text("Help!")
        await update.message.reply_text(self.messages.help())


# vibo: класс занимающийся обработкой
class EchoHandler(BaseHandler):
    async def handle(
        self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE
    ) -> None:
        # await update.message.reply_text(update.message.text)
        await update.message.reply_text(
            self.messages.echo(update.message.text)
        )


##vibo: функия приветствия, возвращает имя пользователя
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#    user = update.effective_user
#    await update.message.reply_html(
#        rf"Hi {user.mention_html()}!",
#        reply_markup=ForceReply(selective=True),
#    )

##vibo: функция, возвращает Help!
# async def help_command(
#    update: Update, context: ContextTypes.DEFAULT_TYPE
# ) -> None:
#    await update.message.reply_text("Help!")

##vibo: функция, собственно 'эхо'
# async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#    await update.message.reply_text(update.message.text)

# vibo: пишем функцию setup_handlers
def setup_handlers(application: tg_ext.Application) -> None:
    # vibo: настраиваем всех обработчиков
    # application.add_handler(CommandHandler("start", start))
    application.add_handler(tg_ext.CommandHandler('start', StartHandler()))
    # application.add_handler(CommandHandler("help", help_command))
    application.add_handler(tg_ext.CommandHandler('help', HelpHandler()))
    # application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.add_handler(
        tg_ext.MessageHandler(
            tg_ext.filters.TEXT & ~tg_ext.filters.COMMAND, EchoHandler()
        )
    )


# vibo: ЗАЧЕМ ВЕЗДЕ tg_ext?
# vibo: это хорошая практика, т.к. может такое случиться, что мы можем импортировать метод из двух различных
# vibo: модулей и какой-то из них вызовется, а какой-то нет. Причем питон не скажет какой именно и будет проблема.
# vibo:  чтобы понимать откуда объект пришел, нужно использовать элиасы.
