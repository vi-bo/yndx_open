from cgitb import handler
import logging

log = logging.getLogger()
log.setLevel(logging.DEBUG)

handler = logging.FileHandler('myapp.log')
handler.setFormatter(logging.Formatter(
        '%(levelname)s:%(name)s         %(message)s'
))
handler.setLevel(logging.INFO)

log.addHandler(handler)
log.addHandler(logging.StreamHandler())

log.debug('Debag message')
log.info('Info message')
log.warning('Warning message')