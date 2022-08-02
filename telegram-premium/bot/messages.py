# vibo: как и в файле handlers.py воспользуемся классами и наслевдованием
# vibo: идея - сделать разные типы сообщений для разных типов пользователей, соответственно два класса
# vibo: первый класс - для обычных, второй для премиальных

# vibo:  В питоне нет настоящих интерфейсов, но есть модуль abc, в котором можно реализовать абстрактный класс
# vibo: и он будет вести себя как интерфейс
import abc

# from cgitb import text
# from lib2to3.pytree import Base

# vibo: добавляем импорт телеграм с элиасом tg
import telegram as tg

# import telegram.ext as tg_ext

# vibo: делаем класс абстрактным (наследуемся от специального класса ABC)
# vibo: используя этот метод будем получать сообщания для команды старт
class BaseMessages(abc.ABC):
    # vibo: делаем метод абстрактным
    @abc.abstractmethod
    # vibo: функция будет ассинхронная
    # vibo: создаем базовый метод старт
    def start(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def help(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def echo(self, text: str) -> str:
        raise NotImplemented


# vibo: реализуем класс дял обычного пользователя, отнаследуем его от BaseMesseges
class RegularUser(BaseMessages):
    def start(self) -> str:
        return 'Привет!'

    def help(self) -> str:
        return 'Вам нужно приобрести подписку'

    # vibo: меняем логику, класс должен возвращать само сообщение
    # async def echo(self, update: tg.Update) -> str:
    def echo(self, text: str) -> str:
        ##vibo: возвращаем сообщение пользователя
        # await update.message.reply_text(update.message.text)
        return f'{text}'


# vibo: имплементируем сообщения для премиального пользователя, отнаследуем от RegularUser
class PremiumUser(RegularUser):
    def start(self) -> str:
        return 'Здравствуйте!'

    def help(self) -> str:
        return 'Наш менеджер скоро свяжется с вами!'


def get_messages(user: tg.User) -> BaseMessages:
    # vibo: у нас нет премиального доступа)))
    # vibo: инвертируем логику для проверки кода
    if user.is_premium:
        # if not user.is_premium:
        return PremiumUser()
    return RegularUser()


# vibo: после запуска бот упал, удалили ассинхронный вызов функций
