import logging
import os

logging.basicConfig(
        level=logging.INFO,
        format='%(name)s %(levelname)s %(asctime)s      '
                '%(message)s',
        datefmt='%I:%M:%S'
)

log = logging.getLogger()

log.info('Worker with PID %s has been started',
        os.getpid())
