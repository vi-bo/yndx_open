import logging

# получаем логгер
log = logging.getLogger(__name__)

# устанавливаем уровень
log.setLevel(logging.INFO)

#добавляем фильтры
log.addFilter(PingFilter())

# добавляем хэндлеры
log.addHandler(logging.StreamHandler())

# используем
log.info('..')
log.debug('..')